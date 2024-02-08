from geopy.geocoders import Nominatim
import folium

def get_coordinates(location_name):
    # Nominatimを使用して位置の名前から座標を取得
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(location_name)
    
    if location is not None:
        return [location.latitude, location.longitude]
    else:
        return None

def create_map(location_name):
    # 地図の中心座標を取得
    coordinates = get_coordinates(location_name)
    
    if coordinates is not None:
        # 地図を作成
        my_map = folium.Map(location=coordinates, zoom_start=15)
        
        # マーカーを追加
        folium.Marker(coordinates, popup=location_name).add_to(my_map)
        
        # 地図をHTMLファイルとして保存
        my_map.save('map.html')
        print(f"地図を作成しました。HTMLファイル: map.html")
    else:
        print("座標を取得できませんでした。")

if __name__ == "__main__":
    # 対象の場所を指定
    location_name = "〇〇"

    # 地図を作成
    create_map(location_name)
