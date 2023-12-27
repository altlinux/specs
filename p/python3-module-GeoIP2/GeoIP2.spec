%define  oname GeoIP2
%define  descr Python code for GeoIP2 webservice client and database reader

%def_with docs
%def_with check

Name:    python3-module-%oname
Version: 4.8.0
Release: alt1

Summary: %descr

License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/maxmind/GeoIP2-python

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-MaxMindDB
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with docs
BuildRequires: python3-module-sphinx
%endif

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-mocket
BuildRequires: python3-module-decorator
BuildRequires: python3-module-http-parser
BuildRequires: python3-module-aiohttp
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
%descr

%if_with docs
%package doc
Summary: Documentation for %oname
Group: Development/Documentation

%description doc
Documentation for %oname.
%endif

%prep
%setup

%build
%pyproject_build

%if_with docs
sphinx-build-3 -b html docs html
rm -rf html/.{buildinfo,doctrees}
%endif

%install
%pyproject_install

%check
# database_test needs submodule with database
# webservice_test needs internet connection
%pyproject_run_pytest -k 'not database_test and not webservice_test'

%files
%python3_sitelibdir/geoip2
%python3_sitelibdir/geoip2-%version.dist-info

%if_with docs
%files doc
%doc LICENSE html
%endif

%changelog
* Wed Dec 27 2023 Grigory Ustinov <grenka@altlinux.org> 4.8.0-alt1
- Automatically updated to 4.8.0.

* Mon May 15 2023 Grigory Ustinov <grenka@altlinux.org> 4.7.0-alt1
- Automatically updated to 4.7.0.

* Fri Jun 24 2022 Grigory Ustinov <grenka@altlinux.org> 4.6.0-alt1
- Automatically updated to 4.6.0.
- Build with check.

* Mon Nov 29 2021 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt1
- Automatically updated to 4.5.0.

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
