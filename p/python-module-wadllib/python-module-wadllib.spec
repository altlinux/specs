Name: python-module-wadllib
Version: 1.3.3
Release: alt1
Summary: Python library for navigating WADL files

Group: Development/Python
License: lgpl3
Url: https://launchpad.net/wadllib

Source: %name-%version.tar
Packager: Anatoly Kitaikin <cetus@altlinux.ru>

BuildPreReq: rpm-build-licenses

BuildArch: noarch
BuildRequires: python-module-setuptools

Requires: python%_python_version(lazr.uri)

%add_python_req_skip lazr

%description
The Web Application Description Language is an XML vocabulary
for describing the capabilities of HTTP resources. wadllib can
be used in conjunction with an HTTP library to navigate and
manipulate those resources.

This project is also part of https://launchpad.net/lazr.

%package -n python-module-wadllib-tests
Summary: wadllib tests
Group: Development/Other
Requires: %name = %version-%release

%description -n python-module-wadllib-tests
%summary

%prep
%setup -q

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/wadllib*
%exclude %python_sitelibdir/wadllib/tests
%doc HACKING.txt README.txt

%files -n python-module-wadllib-tests
%python_sitelibdir/wadllib/tests

%changelog
* Fri Apr 26 2019 Anatoly Kitaykin <cetus@altlinux.org> 1.3.3-alt1
- initial build
