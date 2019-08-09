%define _unpackaged_files_terminate_build 1
%def_with python3

Name: python-module-wadllib
Version: 1.3.3
Release: alt3
Summary: Python library for navigating WADL files
License: lgpl3
Group: Development/Python
Url: https://launchpad.net/wadllib
Packager: Anatoly Kitaikin <cetus@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

%add_python_req_skip lazr
Requires: python%_python_version(lazr.uri)

BuildPreReq: rpm-build-licenses
%if_with python3
BuildPreReq: rpm-build-python3
%endif

%description
The Web Application Description Language is an XML vocabulary
for describing the capabilities of HTTP resources. wadllib can
be used in conjunction with an HTTP library to navigate and
manipulate those resources.

This project is also part of https://launchpad.net/lazr.

%package tests
Summary: wadllib tests
Group: Development/Python

%description -n python-module-wadllib-tests
%summary

%if_with python3

%package -n python3-module-wadllib
Summary: wadllib tests
Group: Development/Python3

%description -n python3-module-wadllib
%summary

%package -n python3-module-wadllib-tests
Summary: wadllib tests
Group: Development/Python3

%description -n python3-module-wadllib-tests
%summary

%endif

%prep
%setup -q
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/wadllib/tests
%doc HACKING.txt README.txt

%files tests
%python_sitelibdir/wadllib/tests

%if_with python3

%files -n python3-module-wadllib
%python3_sitelibdir/*
%exclude %python3_sitelibdir/wadllib/tests
%doc HACKING.txt README.txt

%files -n python3-module-wadllib-tests
%python3_sitelibdir/wadllib/tests

%endif

%changelog
* Fri Aug 09 2019 Anatoly Kitaikin <cetus@altlinux.org> 1.3.3-alt3
- Repack

* Sun Jul 21 2019 Anatoly Kitaikin <cetus@altlinux.org> 1.3.3-alt2
- Python3 support added

* Fri Apr 26 2019 Anatoly Kitaykin <cetus@altlinux.org> 1.3.3-alt1
- initial build
