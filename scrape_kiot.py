import urllib.request
import re
import json

def scrape():
    base_url = "https://kiot.ac.in/facilities/transport/"
    req = urllib.request.Request(base_url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
    except Exception as e:
        print(f"Failed to fetch base url: {e}")
        return
        
    # Find links like <a href="https://kiot.ac.in/bus-no-1/">1</a>
    # or similar.
    links = re.findall(r'href="(https://kiot\.ac\.in/bus[^"]+)"', html)
    links = list(set(links))
    print(f"Found {len(links)} route links: {links[:3]}...")
    
    routes_data = []
    
    for link in links:
        try:
            page_html = urllib.request.urlopen(urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
            # Extract table rows
            # The stops are usually in a table. Let's find all <td> elements or similar.
            # Usually format is: <tr><td>S.No</td><td>Boarding Point</td><td>Time</td></tr>
            # We can extract text from td
            tds = re.findall(r'<td[^>]*>(.*?)</td>', page_html, re.IGNORECASE | re.DOTALL)
            
            # Clean up tds
            tds = [re.sub(r'<[^>]+>', '', td).strip() for td in tds]
            # remove html entities like &nbsp;
            tds = [td.replace('&nbsp;', ' ').replace('&#8211;', '-').strip() for td in tds]
            
            # Assuming every 3 columns: S.No, Boarding Point, Time
            # or sometimes 2 or 4. Let's just look for anything that looks like a time and take the previous item as stop.
            
            stops = []
            for i, td in enumerate(tds):
                # if time format e.g., 7.15 AM
                if re.search(r'\d{1,2}[\.\:]\d{2}\s*[AaPp][Mm]?', td):
                    if i > 0:
                        stop_name = tds[i-1]
                        if not stop_name.isdigit() and len(stop_name) > 2:
                            stops.append(stop_name)
                            
            if stops:
                # extract route name from link
                route_name = link.strip('/').split('/')[-1].replace('-', ' ').title()
                routes_data.append({
                    "route_name": route_name,
                    "stops": [{"name": s, "lat": 0, "lng": 0} for s in stops]
                })
                print(f"Scraped {route_name}: {len(stops)} stops")
        except Exception as e:
            print(f"Failed on {link}: {e}")
            
    with open('routes.json', 'w') as f:
        json.dump(routes_data, f, indent=2)
        
    print("Done writing routes.json")
    
if __name__ == "__main__":
    scrape()
