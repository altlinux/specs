%define _unpackaged_files_terminate_build 1
%define pypi_name libpysal

%def_with check

Name: python3-module-%pypi_name
Version: 4.13.0
Release: alt1
Summary: Core components of Python Spatial Analysis Library
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/libpysal/
VCS: https://github.com/pysal/libpysal
BuildArch: noarch

%py3_provides %pypi_name

Source: %name-%version.tar
Source1: ncovr.zip
Source2: newHaven.zip
Source3: rio_grande_do_sul.zip
Source4: taz.zip

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-geopandas
BuildRequires: python3-module-geodatasets
BuildRequires: python3-module-numpy
BuildRequires: python3-module-numpy-tests
BuildRequires: python3-module-scipy
BuildRequires: python3-module-pandas
BuildRequires: python3-module-scikit-learn
BuildRequires: python3-module-fiona
BuildRequires: python3-module-rtree
BuildRequires: python3-module-networkx
BuildRequires: python3-module-xarray
BuildRequires: python3-module-pyproj
BuildRequires: unzip
BuildRequires: gdal
BuildRequires: proj-data
%endif

%description
Python library for spatial analysis and econometrics.
Provides tools for spatial weights, statistical analysis
of geographic data, and spatial modeling.

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

%if_with check
mkdir -p pysal_data/pysal
unzip %SOURCE1 -d pysal_data/pysal/NCOVR
unzip %SOURCE2 -d pysal_data/pysal/newHaven
unzip %SOURCE3 -d pysal_data/pysal/Rio_Grande_do_Sul
unzip %SOURCE4 -d pysal_data/pysal/taz
%endif


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install	

%check
export PROJ_DATA=%_datadir/proj
export GDAL_DATA=%_datadir/gdal
export XDG_DATA_HOME=$PWD/pysal_data
%pyproject_run_pytest -m 'not network' -k "\
not test_voronoi \
and not test_correctness_voronoi \
and not test_fuzzy_contiguity \
and not test_holes" \
--ignore libpysal/cg/tests/test_voronoi.py \

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Sep 25 2025 Nikita Panov <nexxy@altlinux.org> 4.13.0-alt1
- Initial build for Sisyphus
