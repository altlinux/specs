Name: blockcheck
Version: 0.0.8.2
Release: alt1
Summary: Checks Russian ISP blocking type
License: MIT
Group: Security/Networking
Url: https://github.com/ValdikSS/blockcheck/
Packager: Evgenii Terechkov <evg@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: python3-module-dns

%description
Checks Russian ISP blocking type

%prep
%setup
%build

%install
install -Dp -m 755 %name.py %buildroot%_bindir/%name.py

%files
%_bindir/%name.py
%doc README.md

%changelog
* Mon Jul 25 2016 Terechkov Evgenii <evg@altlinux.org> 0.0.8.2-alt1
- 0.0.8.2

* Mon Apr 25 2016 Terechkov Evgenii <evg@altlinux.org> 0.0.8.1-alt1
- 0.0.8.1

* Sun Mar 13 2016 Terechkov Evgenii <evg@altlinux.org> 0.0.7.4-alt1
- 0.0.7.4

* Wed Feb 10 2016 Terechkov Evgenii <evg@altlinux.org> 0.0.6.4-alt1
- 0.0.6.4

* Sat Nov 21 2015 Terechkov Evgenii <evg@altlinux.org> 0.0.6.3-alt1
- Initial build for ALT Linux Sisyphus
