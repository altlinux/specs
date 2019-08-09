%define _unpackaged_files_terminate_build 1
%def_with python3

Name: python-module-lazr.uri
Version: 1.0.3
Release: alt3
Summary: A self-contained, easily reusable library for parsing, manipulating, and generating URIs
Group: Development/Python
License: lgpl3
Url: https://launchpad.net/lazr.restfulclient

Source: %name-%version.tar
Packager: Anatoly Kitaikin <cetus@altlinux.ru>

BuildPreReq: rpm-build-licenses

BuildArch: noarch

BuildRequires: rpm-build-python

%if_with python3
BuildRequires(pre): rpm-build-python3
%endif

%py_provides lazr.uri

%add_python_req_skip lazr

%description
%summary

This project is also part of https://launchpad.net/lazr.

%package tests
Summary: lazr.uri tests
Group: Development/Python
Requires: %name = %version-%release

%description tests
%summary

%if_with python3
%package -n python3-module-lazr.uri
Summary: A self-contained, easily reusable library for parsing, manipulating, and generating URIs
Group: Development/Python3
%py3_provides lazr.uri

%description -n python3-module-lazr.uri
%summary

This project is also part of https://launchpad.net/lazr.

%package -n python3-module-lazr.uri-tests
Summary: lazr.uri tests
Group: Development/Python3

%description -n python3-module-lazr.uri-tests
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
%exclude %python_sitelibdir/lazr/uri/tests
%doc HACKING.txt README.txt

%files tests
%python_sitelibdir/lazr/uri/tests

%if_with python3

%files -n python3-module-lazr.uri
%python3_sitelibdir/*
%exclude %python3_sitelibdir/lazr/uri/tests
%doc HACKING.txt README.txt

%files -n python3-module-lazr.uri-tests
%python3_sitelibdir/lazr/uri/tests

%endif

%changelog
* Fri Aug 09 2019 Anatoly Kitaikin <cetus@altlinux.org> 1.0.3-alt3
- Repack

* Sat Jul 20 2019 Anatoly Kitaikin <cetus@altlinux.org> 1.0.3-alt2
- Python3 support added

* Fri Apr 26 2019 Anatoly Kitaykin <cetus@altlinux.org> 1.0.3-alt1
- initial build
