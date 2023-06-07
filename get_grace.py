from netCDF4 import Dataset, num2date
from matplotlib.pyplot import axes, pcolormesh, savefig, close, colorbar
from cartopy.crs import PlateCarree
from numpy import logical_or
from numpy import nan



data_path = "data/GRCTellus.JPL.200204_202303.GLO.RL06.1M.MSCNv03CRI.nc"



with Dataset(data_path) as fid:
    data = fid["lwe_thickness"][:]
    scale_factor = fid["scale_factor"][:].filled(1.0)
    data_lat = fid["lat"][:]
    data_lon = fid["lon"][:]
    data_time = fid["time"]
    data_time = num2date(data_time[:], data_time.units)

# data_lon = data_lon - 360.0
# data_lon = data_lon % 360.0

proj = PlateCarree(central_longitude = 180.0)

ax = axes(projection=proj)

min_lon = -20.0
max_lon = 20.0
min_lat = -60.0
max_lat = -20.0

# data[(data > 100.0) | (data < -100.0)] = nan

ax.set_extent([min_lon, max_lon, min_lat, max_lat], crs=proj)

pcolormesh(data_lon, data_lat, data[200, :, :] * scale_factor, vmin=-10.0, vmax=10.0, transform=proj)

colorbar()

ax.coastlines()

savefig("test.png")

close()