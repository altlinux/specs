%define oname libcloud

Name: python3-module-%oname
Version: 3.7.0
Release: alt1

Summary: Library for interacting with popular cloud service

License: Apache-2.0
Group: Development/Python3
Url: http://libcloud.apache.org/

BuildArch: noarch

# Source-git: https://github.com/apache/libcloud
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-requests
BuildPreReq: python3-module-urllib3

%py3_provides libcloud.compute.drivers.vsphere

# for docs
BuildPreReq: python3-module-sphinx
# for tests
%py3_requires mock requests requests_mock pytest

%description
Apache Libcloud is a Python library which hides differences between 
different cloud provider APIs and allows you to manage different 
cloud resources through a unified and easy to use API.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Apache Libcloud is a Python library which hides differences between 
different cloud provider APIs and allows you to manage different 
cloud resources through a unified and easy to use API.

This package contains tests for %oname

%package docs
Summary: Documentation for %name
Group: Development/Documentation

%description docs
Apache Libcloud is a Python library which hides differences between 
different cloud provider APIs and allows you to manage different 
cloud resources through a unified and easy to use API.

This package contains documentation for %oname

%prep
%setup
sed -i 's/requests.packages.//' %oname/http.py
cp libcloud/test/secrets.py-dist libcloud/test/secrets.py

%build
%python3_build

export PYTHONPATH=$PWD
%make SPHINXBUILD="sphinx-build-3" -C docs man

%install
%python3_install

%files
%doc *.rst LICENSE example_*.py
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files tests
%python3_sitelibdir/libcloud/test/*

%files docs
%doc docs/_build/*


%changelog
* Wed Feb 08 2023 Grigory Ustinov <grenka@altlinux.org> 3.7.0-alt1
- Automatically updated to 3.7.0.

* Wed Oct 12 2022 Grigory Ustinov <grenka@altlinux.org> 3.6.1-alt1
- Automatically updated to 3.6.1.

* Sat May 28 2022 Grigory Ustinov <grenka@altlinux.org> 3.6.0-alt1
- Automatically updated to 3.6.0.

* Wed May 25 2022 Grigory Ustinov <grenka@altlinux.org> 3.5.1-alt1
- Automatically updated to 3.5.1.

* Thu Apr 01 2021 Grigory Ustinov <grenka@altlinux.org> 3.3.1-alt1
- Build new version.
- Drop python2 support.

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 2.5.0-alt1
- new version 2.5.0 (with rpmrb script)

* Tue Mar 03 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.3.0-alt1
- Updated version to 2.3.0

* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.4.0-alt1
- New version

* Thu Jul 28 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.1.0-alt3
- Dropped pysphere for build with python3

* Thu Jul 28 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.1.0-alt2
- Build with python3 (ALT 32321)

* Mon Jul 25 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.1.0-alt1
- New version
- Build with python3

* Mon Feb 29 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.20.1-alt1
- New version

* Mon Aug 31 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.18.0-alt1
- New version

* Wed Feb 25 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.17.0-alt1
- New version

* Mon Nov 17 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.16.0-alt1
- New version
- Dropped py3 module caused dependiences issues

* Wed Oct 29 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.15.1-alt2
- Added module for Python 3

* Fri Jul 11 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.15.1-alt1
- New version

* Sat Jul 05 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.15.0-alt1
- New version

* Tue Jul 01 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.14.1-alt2
- Add %%dir for unit tests, just a little fix

* Fri Jun 20 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.14.1-alt1
- New version
- Add subpackages python-module-libcloud-tests

* Thu Jan 23 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.14-alt1
- Initial build for ALT
