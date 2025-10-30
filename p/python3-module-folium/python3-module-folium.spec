%define _unpackaged_files_terminate_build 1
%define pypi_name folium

%def_with check

Name: python3-module-%pypi_name
Version: 0.20.0
Release: alt1
Summary: Python Data, Leaflet.js Maps
License: MIT
Group: Development/Python3
URL: https://pypi.org/project/folium/
VCS: https://github.com/python-visualization/folium
BuildArch: noarch
Source: %name-%version.tar

%py3_provides %pypi_name

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-requests
BuildRequires: python3-module-numpy
BuildRequires: python3-module-selenium
BuildRequires: python3-module-branca
BuildRequires: python3-module-xyzservices
BuildRequires: python3-module-pandas
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-geopandas
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-geodatasets
%endif

%description
Manipulate your data in Python,
then visualize it in a Leaflet map via folium

%prep
%setup
# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
     git init
     git config user.email author@example.com
     git config user.name author
     git add .
     git commit -m 'release'
     git tag '%version'
fi

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v -m 'not request' -k "\
not test__repr_png_is_bytes \
and not test_valid_png \
and not test_valid_png_size \
and not test_choropleth_geopandas_mixed \
and not test_choropleth_geopandas_str \
and not test_json_request \
and not test_timedynamic_geo_json \
and not test_choropleth_geopandas_numeric" \
--ignore tests/selenium \
--ignore tests/snapshots \

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}


%changelog
* Fri Oct 03 2025 Nikita Panov <nexxy@altlinux.org> 0.20.0-alt1
- Initial build for Sisyphus
