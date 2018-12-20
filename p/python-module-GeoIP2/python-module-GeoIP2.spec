%define  oname GeoIP2
%define  descr Python code for GeoIP2 webservice client and database reader

Name:    python-module-%oname
Version: 2.9.0
Release: alt1

Summary: %descr
License: ASLv2.0
Group:   Development/Python
URL:     https://github.com/maxmind/GeoIP2-python

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-MaxMindDB
BuildRequires: python-module-sphinx
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-MaxMindDB

BuildArch: noarch

Source:  %oname-%version.tar

%description
%descr

%package -n python3-module-%oname
Summary: %descr
Group: Development/Python3

%description -n python3-module-%oname
%descr

%prep
%setup -n %oname-%version
cp -a . ../python3

%build
%python_build
pushd ../python3
%python3_build
popd
sphinx-build -b html docs html
rm -rf html/.{buildinfo,doctrees}

%install
%python_install
pushd ../python3
%python3_install
popd

%files
%python_sitelibdir/geoip2
%python_sitelibdir/*.egg-info

%files -n python3-module-%oname
%python3_sitelibdir/geoip2
%python3_sitelibdir/*.egg-info

%changelog
* Wed Dec 19 2018 Grigory Ustinov <grenka@altlinux.org> 2.9.0-alt1
- Initial build for Sisyphus.
