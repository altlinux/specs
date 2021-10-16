%define  oname GeoIP2
%define  descr Python code for GeoIP2 webservice client and database reader

Name:    python3-module-%oname
Version: 4.4.0
Release: alt1

Summary: %descr
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/maxmind/GeoIP2-python

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-MaxMindDB
BuildRequires: python3-module-sphinx

BuildArch: noarch

Source:  %oname-%version.tar

%description
%descr

%package doc
Summary: Documentation for %oname
Group: Development/Documentation

%description doc
Documentation for %oname.

%prep
%setup -n %oname-%version

%build
%python3_build
sphinx-build-3 -b html docs html
rm -rf html/.{buildinfo,doctrees}

%install
%python3_install

%files
%python3_sitelibdir/geoip2
%python3_sitelibdir/*.egg-info

%files doc
%doc LICENSE html/

%changelog
* Sat Oct 16 2021 Grigory Ustinov <grenka@altlinux.org> 4.4.0-alt1
- Automatically updated to 4.4.0.

* Mon May 17 2021 Grigory Ustinov <grenka@altlinux.org> 4.2.0-alt1
- Automatically updated to 4.2.0.

* Sun Sep 27 2020 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1
- Automatically updated to 4.1.0.

* Fri Jul 31 2020 Grigory Ustinov <grenka@altlinux.org> 4.0.2-alt1
- Automatically updated to 4.0.2.

* Tue Jun 30 2020 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.
- Fix license.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 2.9.0-alt2
- Build without python2.
- Build with docs.

* Wed Dec 19 2018 Grigory Ustinov <grenka@altlinux.org> 2.9.0-alt1
- Initial build for Sisyphus.
