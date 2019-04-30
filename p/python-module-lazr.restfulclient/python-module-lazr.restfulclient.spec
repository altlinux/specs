Name: python-module-lazr.restfulclient
Version: 0.14.2
Release: alt1
Summary: A programmable lazr.restful client library

Group: Development/Python
License: lgpl3
Url: https://launchpad.net/lazr.restfulclient

Source: %name-%version.tar
Packager: Anatoly Kitaikin <cetus@altlinux.ru>

BuildPreReq: rpm-build-licenses

BuildArch: noarch
BuildRequires: python-module-setuptools

Requires: python%_python_version(lazr.uri)

%add_python_req_skip lazr

%description
A programmable client library that takes advantage of the commonalities
among lazr.restful web services to provide added functionality on top of wadllib.

This project is also part of https://launchpad.net/lazr.

%package -n python-module-lazr.restfulclient-tests
Summary: lazr.restfulclient tests
Group: Development/Other
Requires: %name = %version-%release

%description -n python-module-lazr.restfulclient-tests
%summary


%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%dir %python_sitelibdir/lazr
%python_sitelibdir/lazr/restfulclient*
%exclude %python_sitelibdir/lazr/restfulclient/tests
%python_sitelibdir/lazr.restfulclient*
%doc HACKING.rst README.rst

%files -n python-module-lazr.restfulclient-tests
%python_sitelibdir/lazr/restfulclient/tests

%changelog
* Fri Apr 26 2019 Anatoly Kitaykin <cetus@altlinux.org> 0.14.2-alt1
- initial build
