Name: python-module-rosapi
Version: 0.2.4
Release: alt1.1
Summary: Routerboard API

Group: Development/Python
License: CCPL
Url: https://github.com/jellonek/rosapi
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools
BuildArch: noarch

%description
Routerboard API for accessing mikrotik routers.

Base of this code is http://wiki.mikrotik.com/index.php?title=Manual:API

%package -n python3-module-rosapi
Summary: Routerboard API
Group: Development/Python3

%description -n python3-module-rosapi
Routerboard API for accessing mikrotik routers.

Base of this code is http://wiki.mikrotik.com/index.php?title=Manual:API

%prep
%setup

%build
%python_build
%python3_build

%install
%python_install
%python3_install

%files
%python_sitelibdir/rosapi*
%doc README.txt

%files -n python3-module-rosapi
%python3_sitelibdir/rosapi*

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Oct 25 2015 Terechkov Evgenii <evg@altlinux.org> 0.2.4-alt1
- Initial build for ALT Linux Sisyphus
- 0.2.0-9-g79c18be
