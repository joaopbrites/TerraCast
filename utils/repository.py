from pathlib import Path


class AssetsRepository:
	def __init__(self, root: Path | None = None):
		self.root = Path(root) if root is not None else Path(__file__).resolve().parent.parent

		self.files: list[dict[str, Path | str]] = [
			{
				"name": "IR4AVHRR6.cpt",
				"path": self.root / "assets" / "colortables" / "IR4AVHRR6.cpt",
			},
			{
				"name": "Square Root Visible Enhancement.cpt",
				"path": self.root / "assets" / "colortables" / "Square Root Visible Enhancement.cpt",
			},
			{
				"name": "SVGAIR_TEMP.cpt",
				"path": self.root / "assets" / "colortables" / "SVGAIR_TEMP.cpt",
			},
			{
				"name": "SVGAIR2_TEMP.cpt",
				"path": self.root / "assets" / "colortables" / "SVGAIR2_TEMP.cpt",
			},
			{
				"name": "SVGAWVX_TEMP.cpt",
				"path": self.root / "assets" / "colortables" / "SVGAWVX_TEMP.cpt",
			},
			{
				"name": "test.cpt",
				"path": self.root / "assets" / "colortables" / "test.cpt",
			},
			{
				"name": "WVCOLOR35.cpt",
				"path": self.root / "assets" / "colortables" / "WVCOLOR35.cpt",
			},
			{
				"name": "wx-star.com_GOES-R_ABI_False-Color-LUT_sat20.png",
				"path": self.root / "assets" / "colortables" / "wx-star.com_GOES-R_ABI_False-Color-LUT_sat20.png",
			},
			{
				"name": "land_ocean_ice_8192.jpg",
				"path": self.root / "assets" / "maps" / "land_ocean_ice_8192.jpg",
			},
			{
				"name": "natural-earth-1_large2048px.jpg",
				"path": self.root / "assets" / "maps" / "natural-earth-1_large2048px.jpg",
			},
			{
				"name": "world.topo.bathy.200408.3x5400x2700.jpg",
				"path": self.root / "assets" / "maps" / "world.topo.bathy.200408.3x5400x2700.jpg",
			},
			{
				"name": "BlackMarble_2016_6km_geo.tif",
				"path": self.root / "assets" /"maps" / "BlackMarble_2016_6km_geo.tif",
			},
			{
				"name": "inpe_cptec.jpg",
				"path": self.root / "assets" / "logos" / "inpe_cptec.jpg",
			},
			{
				"name": "my_logo.png",
				"path": self.root / "assets" / "logos" / "my_logo.png",
			},
			{
				"name": "noaa_logo.png",
				"path": self.root / "assets" / "logos" / "noaa_logo.png",
			},
			{
				"name": "24HMICROPHYSICS_legend.png",
				"path": self.root / "assets" / "legends" / "24HMICROPHYSICS_legend.png",
			},
			{
				"name": "AEROSSOL_legend.png",
				"path": self.root / "assets" / "legends" / "AEROSSOL_legend.png",
			},
			{
				"name": "AIRMASS_legend.png",
				"path": self.root / "assets" / "legends" / "AIRMASS_legend.png",
			},
			{
				"name": "ASH_legend.png",
				"path": self.root / "assets" / "legends" / "ASH_legend.png",
			},
			{
				"name": "CLOUDPHASE_legend.png",
				"path": self.root / "assets" / "legends" / "CLOUDPHASE_legend.png",
			},
			{
				"name": "DAYCLOUDCONVECTION_legend.png",
				"path": self.root / "assets" / "legends" / "DAYCLOUDCONVECTION_legend.png",
			},
			{
				"name": "DAYCLOUDPHASE_legend.png",
				"path": self.root / "assets" / "legends" / "DAYCLOUDPHASE_legend.png",
			},
			{
				"name": "DAYCONVECTION_legend.png",
				"path": self.root / "assets" / "legends" / "DAYCONVECTION_legend.png",
			},
			{
				"name": "DAYLANDCLOUDFIRE_legend.png",
				"path": self.root / "assets" / "legends" / "DAYLANDCLOUDFIRE_legend.png",
			},
			{
				"name": "DAYLANDCLOUD_legend.png",
				"path": self.root / "assets" / "legends" / "DAYLANDCLOUD_legend.png",
			},
			{
				"name": "DAYMICROPHYSICS_legend.png",
				"path": self.root / "assets" / "legends" / "DAYMICROPHYSICS_legend.png",
			},
			{
				"name": "DAYSNOWFOG_legend.png",
				"path": self.root / "assets" / "legends" / "DAYSNOWFOG_legend.png",
			},
			{
				"name": "DMWF_legend.png",
				"path": self.root / "assets" / "legends" / "DMWF_legend.png",
			},
			{
				"name": "DUST_legend.png",
				"path": self.root / "assets" / "legends" / "DUST_legend.png",
			},
			{
				"name": "DWV_legend.png",
				"path": self.root / "assets" / "legends" / "DWV_legend.png",
			},
			{
				"name": "FIRETEMPERATURE_legend.png",
				"path": self.root / "assets" / "legends" / "FIRETEMPERATURE_legend.png",
			},
			{
				"name": "FIRE_legend.png",
				"path": self.root / "assets" / "legends" / "FIRE_legend.png",
			},
			{
				"name": "FLOOD_legend.png",
				"path": self.root / "assets" / "legends" / "FLOOD_legend.png",
			},
			{
				"name": "GFS_CLOUDS_legend.png",
				"path": self.root / "assets" / "legends" / "GFS_CLOUDS_legend.png",
			},
			{
				"name": "GLM_TRACK_legend.png",
				"path": self.root / "assets" / "legends" / "GLM_TRACK_legend.png",
			},
			{
				"name": "LANDCOVERTYPE_legend.png",
				"path": self.root / "assets" / "legends" / "LANDCOVERTYPE_legend.png",
			},
			{
				"name": "NATURALTRUECOLOR_legend.png",
				"path": self.root / "assets" / "legends" / "NATURALTRUECOLOR_legend.png",
			},
			{
				"name": "NIGHTMICROPHYSICS_legend.png",
				"path": self.root / "assets" / "legends" / "NIGHTMICROPHYSICS_legend.png",
			},
			{
				"name": "PHASE_legend.png",
				"path": self.root / "assets" / "legends" / "PHASE_legend.png",
			},
			{
				"name": "SAL_legend.png",
				"path": self.root / "assets" / "legends" / "SAL_legend.png",
			},
			{
				"name": "SO2_legend.png",
				"path": self.root / "assets" / "legends" / "SO2_legend.png",
			},
			{
				"name": "SWV_legend.png",
				"path": self.root / "assets" / "legends" / "SWV_legend.png",
			},
			{
				"name": "TRUECOLOR_legend.png",
				"path": self.root / "assets" / "legends" / "TRUECOLOR_legend.png",
			},
			{
				"name": "showcast_fire_legend.png",
				"path": self.root / "assets" / "legends" / "showcast_fire_legend.png",
			},
			{
				"name": "ne_10m_admin_1_states_provinces.dbf",
				"path": self.root / "assets" / "shapefiles" / "ne_10m_admin_1_states_provinces.dbf",
			},
			{
				"name": "ne_10m_admin_1_states_provinces.shp",
				"path": self.root / "assets" / "shapefiles" / "ne_10m_admin_1_states_provinces.shp",
			},
			{
				"name": "ne_10m_admin_1_states_provinces.shx",
				"path": self.root / "assets" / "shapefiles" / "ne_10m_admin_1_states_provinces.shx",
			},
			{
				"name": "ne_10m_coastline.dbf",
				"path": self.root / "assets" / "shapefiles" / "ne_10m_coastline.dbf",
			},
			{
				"name": "ne_10m_coastline.shp",
				"path": self.root / "assets" / "shapefiles" / "ne_10m_coastline.shp",
			},
			{
				"name": "ne_10m_coastline.shx",
				"path": self.root / "assets" / "shapefiles" / "ne_10m_coastline.shx",
			},
			{
				"name": "ne_50m_admin_0_countries.dbf",
				"path": self.root / "assets" / "shapefiles" / "ne_50m_admin_0_countries.dbf",
			},
			{
				"name": "ne_50m_admin_0_countries.shp",
				"path": self.root / "assets" / "shapefiles" / "ne_50m_admin_0_countries.shp",
			},
			{
				"name": "ne_50m_admin_0_countries.shx",
				"path": self.root / "assets" / "shapefiles" / "ne_50m_admin_0_countries.shx",
			},
		]

	def get_path(self, file_name: str) -> Path:
		for item in self.files:
			if item["name"] == file_name:
				return item["path"]

		raise FileNotFoundError(f"Arquivo '{file_name}' não encontrado no repository.")


_repository: AssetsRepository | None = None


def get_repository() -> AssetsRepository:
	global _repository
	if _repository is None:
		_repository = AssetsRepository()
	return _repository


def get_asset_path(file_name: str) -> Path:
	return get_repository().get_path(file_name)
