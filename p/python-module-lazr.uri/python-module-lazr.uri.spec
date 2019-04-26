Name: python-module-lazr.uri
Version: 1.0.3
Release: alt1
Summary: A self-contained, easily reusable library for parsing, manipulating, and generating URIs

Group: Development/Python
License: lgpl3
Url: https://launchpad.net/lazr.restfulclient

Source: %name-%version.tar
Packager: Anatoly Kitaikin <cetus@altlinux.ru>

BuildPreReq: rpm-build-licenses

BuildArch: noarch
BuildRequires: python-module-setuptools

%add_python_req_skip lazr

%description
%summary

This project is also part of https://launchpad.net/lazr.

%package -n python-module-lazr.uri-tests
Summary: lazr.uri tests
Group: Development/Other
Requires: %name = %version-%release

%description -n python-module-lazr.uri-tests
%summary

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/lazr/uri/tests
%doc HACKING.txt README.txt

%files -n python-module-lazr.uri-tests
%python_sitelibdir/lazr/uri/tests

%changelog
* Fri Apr 26 2019 Anatoly Kitaykin <cetus@altlinux.org> 1.0.3-alt1
- initial build
