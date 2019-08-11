%define _unpackaged_files_terminate_build 1
%def_with python3

Name: python-module-lazr.restfulclient
Version: 0.14.2
Release: alt4
Summary: A programmable lazr.restful client library
License: lgpl3
Group: Development/Python
Url: https://launchpad.net/lazr.restfulclient
Packager: Anatoly Kitaikin <cetus@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: rpm-build-licenses
%if_with python3
BuildRequires(pre): rpm-build-python3
%endif

%add_python_req_skip lazr
Requires: python%_python_version(lazr.uri)

%py_provides lazr.restfulclient

%description
A programmable client library that takes advantage of the commonalities
among lazr.restful web services to provide added functionality on top of wadllib.

This project is also part of https://launchpad.net/lazr.

%package tests
Summary: lazr.restfulclient tests
Group: Development/Python
Requires: %name = %version-%release

%description tests
%summary

%if_with python3

%package -n python3-module-lazr.restfulclient
Summary: A programmable lazr.restful client library
Group: Development/Python3

%py3_provides lazr.restfulclient

%description -n python3-module-lazr.restfulclient
A programmable client library that takes advantage of the commonalities
among lazr.restful web services to provide added functionality on top of wadllib.

This project is also part of https://launchpad.net/lazr.

%package -n python3-module-lazr.restfulclient-tests
Summary: lazr.restfulclient tests
Group: Development/Python3
Requires: python3-module-lazr.restfulclient = %version-%release

%description -n python3-module-lazr.restfulclient-tests
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
%exclude %python_sitelibdir/lazr/restfulclient/tests
%doc HACKING.rst README.rst

%files tests
%python_sitelibdir/lazr/restfulclient/tests

%if_with python3

%files -n python3-module-lazr.restfulclient
%python3_sitelibdir/*
%exclude %python3_sitelibdir/lazr/restfulclient/tests
%doc HACKING.rst README.rst

%files -n python3-module-lazr.restfulclient-tests
%python3_sitelibdir/lazr/restfulclient/tests

%endif

%changelog
* Sun Aug 11 2019 Anatoly Kitaikin <cetus@altlinux.org> 0.14.2-alt4
- Requirements fix

* Sun Jul 21 2019 Anatoly Kitaikin <cetus@altlinux.org> 0.14.2-alt3
- Repack

* Sun Jul 21 2019 Anatoly Kitaikin <cetus@altlinux.org> 0.14.2-alt2
- Python3 support added

* Fri Apr 26 2019 Anatoly Kitaykin <cetus@altlinux.org> 0.14.2-alt1
- initial build
