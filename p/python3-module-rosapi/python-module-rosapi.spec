%define _unpackaged_files_terminate_build 1

Name: python3-module-rosapi
Version: 0.2.4
Release: alt2

Summary: Routerboard API
Group: Development/Python3
License: CCPL
Url: https://github.com/jellonek/rosapi
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Routerboard API for accessing mikrotik routers.

Base of this code is http://wiki.mikrotik.com/index.php?title=Manual:API

%prep
%setup

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%doc README.txt
%python3_sitelibdir/rosapi*


%changelog
* Tue Nov 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.4-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.4-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Oct 25 2015 Terechkov Evgenii <evg@altlinux.org> 0.2.4-alt1
- Initial build for ALT Linux Sisyphus
- 0.2.0-9-g79c18be
