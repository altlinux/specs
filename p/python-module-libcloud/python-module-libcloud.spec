%define oname libcloud

Name: python-module-%oname
Version: 2.3.0
Release: alt1
Summary: Library for interacting with popular cloud service

License: Apache-2.0
Group: Development/Python
Url: http://libcloud.apache.org/
# https://github.com/apache/libcloud
BuildArch: noarch

Source: %oname-%version.tar

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-requests
BuildRequires: python-module-pytest-runner
BuildRequires: python-module-urllib3

# for docs
BuildRequires: python-module-sphinx

# for tests
%py_requires mock requests requests_mock pytest

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-module-requests
BuildPreReq: python3-module-pytest-runner
BuildPreReq: python3-module-urllib3

# for docs
BuildPreReq: python3-module-sphinx


%description
Apache Libcloud is a Python library which hides differences between 
different cloud provider APIs and allows you to manage different 
cloud resources through a unified and easy to use API.

%package -n python3-module-%oname
Summary: Library for interacting with popular cloud service
Group: Development/Python3
# for tests
%py3_requires mock requests requests_mock pytest

%description -n python3-module-%oname
Apache Libcloud is a Python library which hides differences between 
different cloud provider APIs and allows you to manage different 
cloud resources through a unified and easy to use API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Apache Libcloud is a Python library which hides differences between 
different cloud provider APIs and allows you to manage different 
cloud resources through a unified and easy to use API.

This package contains tests for %oname

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: python-module-%oname = %EVR

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
%setup -n %oname-%version
pushd %oname
sed -i 's/requests.packages.//' http.py
pushd test
mv secrets.py-dist secrets.py
popd
pushd compute/drivers
rm -f vsphere.py
popd
popd

rm -rf ../python3
cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

export PYTHONPATH=$PWD
%make -C docs man

%install
%python_build_install

pushd ../python3
%python3_install
popd

%files
%doc *.rst LICENSE example_*.py
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files -n python3-module-%oname
%doc *.rst LICENSE example_*.py
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/libcloud/test/*

%files tests
%python_sitelibdir/libcloud/test/*

%files docs
%doc docs/_build/*


%changelog
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
