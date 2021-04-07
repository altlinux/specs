%define _unpackaged_files_terminate_build 1
%def_with check

Name: makesurface
Version: 0.2.14
Release: alt3
Summary: Create vector datasets from raster surfaces
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/makesurface/

# https://github.com/mapbox/make-surface.git
Source0: https://pypi.python.org/packages/7d/a8/d6b3561d36bc45eaa6aba7b05624b9fa351430be7ac4b05cbb5d1c0958af/%{name}-%{version}dev.tar.gz
Patch0: 0001-Fix-imports-of-self.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(click)
BuildRequires: python3(fiona)
BuildRequires: python3(numpy)
BuildRequires: python3(rasterio)
BuildRequires: python3(shapely)
BuildRequires: python3(scipy)
BuildRequires: python3(mercantile)
BuildRequires: python3(pyproj)
BuildRequires: python3(tox)
%endif

%py3_provides %name
%py3_requires click fiona numpy rasterio shapely scipy mercantile pyproj

%description
Raster -> vector surface creation tools in python.

%prep
%setup -q -n %{name}-%{version}dev
%autopatch -p2

%build
%python3_build_debug

%install
%python3_install

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
commands =
    makesurface --help
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr

%files
%doc *.rst
%_bindir/makesurface
%python3_sitelibdir/*

%changelog
* Wed Apr 07 2021 Stanislav Levin <slev@altlinux.org> 0.2.14-alt3
- Fixed imports of self (closes: #39884).

* Thu Oct 24 2019 Grigory Ustinov <grenka@altlinux.org> 0.2.14-alt2
- Transfer on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.14-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.14-alt1
- automated PyPI update

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.9-alt1.git20150218
- Initial build for Sisyphus
