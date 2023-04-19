import csv
import time
from selenium import webdriver
from anonymous_techniques import *
from selenium.webdriver.common.by import By

pakistanAirports = [['Islamabad', 'ISB', 'Pakistan'], ['Karachi', 'KHI', 'Pakistan'], ['Lahore', 'LHE', 'Pakistan'],
                    ['Multan', 'MUX', 'Pakistan'], ['Peshawar', 'PEW', 'Pakistan'], ['Quetta', 'UET', 'Pakistan']]

desAirports = [['Toronto', 'YYZ', 'Canada'], ['Vancouver', 'YVR', 'Canada'], ['Montreal', 'YUL', 'Canada'],
               ['Calgary', 'YYC', 'Canada'], ['Edmonton', 'YEG', 'Canada'], ['Ottawa', 'YOW', 'Canada'],
               ['Halifax', 'YHZ', 'Canada'], ['Quebec City', 'YQB', 'Canada'], ['Winnipeg', 'YWG', 'Canada'],
               ['Riyadh', 'RUH', 'Saudi Arabia'], ['Jeddah', 'JED', 'Saudi Arabia'], ['Dammam', 'DMM', 'Saudi Arabia'],
               ['Dubai', 'DXB', 'United Arab Emirates'], ['Abu Dhabi', 'AUH', 'United Arab Emirates'],
               ['London', 'LHR', 'United Kingdom'], ['Manchester', 'MAN', 'United Kingdom'],
               ['New York', 'JFK', 'United States'], ['Los Angeles', 'LAX', 'United States'],
               ['Chicago', 'ORD', 'United States']]

targetCountries = ['United Arab Emirates', 'Saudi Arabia', 'United States', 'United Kingdom', 'Canada']

values = 0
overallData = []
for l in range(11, 20):
        for m in range(14, 20):
            for org in pakistanAirports:
                if m>=l:
                    for des in desAirports:
                        origin = org[0]
                        destination = des[0]
                        originCode = org[1]
                        destinationCode = des[1]
                        arrDate = f'05/{l}/2023'
                        desDate = f'05/{m}/2023'
                        country = f"{org[2]} - {des[2]}"
                        try:
                            obj = Anonymous()
                            driver = obj.setup_webDriver()
                            url = f"https://vacation.hotwire.com/Flights-Search?leg1=from%3A{origin}%20%28{originCode}%20-%20{origin}%20Intl.%29%2Cto%3A{destination}%20%28{destinationCode}%20-%20{destination}%20Intl.%29%2Cdeparture%3A{arrDate.split('/')[0].replace('0', '')}%2F{arrDate.split('/')[1]}%2F{arrDate.split('/')[2]}TANYT&leg2=from%3A{destination}%20%28{destinationCode}%20-%20{destination}%20Intl.%29%2Cto%3A{origin}%20%28{originCode}%20-%20{origin}%20Intl.%29%2Cdeparture%3A{desDate.split('/')[0].replace('0', '')}%2F{desDate.split('/')[1]}%2F2023TANYT&mode=search&options=carrier%3A%2A%2Ccabinclass%3A%2Cmaxhops%3A1%2Cnopenalty%3AN&pageId=0&passengers=adults%3A1%2Cchildren%3A0%2Cinfantinlap%3AN&trip=roundtrip"
                            driver.get(url)
                            try:
                                lis = driver.find_elements(By.XPATH,
                                                           "//main//ul[@class='uitk-typelist uitk-typelist-orientation-stacked uitk-typelist-size-2 uitk-typelist-spacing']//li")
                                val = ""
                                tempdata = []
                                for li in lis:
                                    flightTime = li.find_element(By.XPATH,
                                                                 ".//span[@data-test-id='departure-time']").text
                                    duration = li.find_element(By.XPATH,
                                                               ".//div[@data-test-id='journey-duration']").text
                                    stopDur = li.find_element(By.XPATH, ".//div[@data-test-id='layovers']").text
                                    flightName = li.find_element(By.XPATH,
                                                                 ".//div[@data-test-id='flight-operated']").text
                                    flightImgUrl = li.find_element(By.XPATH,
                                                                   ".//img[@class='uitk-image-media']").get_attribute(
                                        'src')
                                    price = li.find_element(By.XPATH, ".//span[@class='uitk-lockup-price']").text
                                    path = f"{originCode}-{destinationCode}"
                                    gotData = [origin, originCode, destination, destinationCode, country, path,
                                               flightTime, arrDate, desDate, duration, stopDur, flightName,
                                               flightImgUrl, price]
                                    print(gotData)
                                    overallData.append(gotData)
                                    with open("outputFile.txt", "a") as file:
                                        file.write(
                                            f'["{origin}", "{originCode}", "{destination}", "{destinationCode}", "{country}", "{path}", "{flightTime}", "{arrDate}", "{desDate}", "{duration}", "{stopDur}", "{flightName}", "{flightImgUrl}", "{price}"],\n')
                                        file.close()
                            except Exception as e:
                                pass
                            driver.close()
                        except Exception as e:
                            pass
                        values += 1
                        print(f"{values}/200 DONE:")



# with open("outputFile.csv", "a") as file2:
#     writer2 = csv.writer(csvfile)
#     # write the column headers
#     writer2.writerow(['Origin', 'OriginCode', 'Destination', 'DestinationCode', 'Country', 'FLight_Path', 'Flight_Time', 'Departure Date', 'Return Date', 'Duration', 'Stops', 'Flight_Name', 'Img_URL', 'Price'])
#     for row in overallData:
#         writer2.writerow(row)
