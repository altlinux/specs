Name: x11vnc-service
Version: 0.1
Release: alt3

Summary: Service for x11vnc
License: GPL
Group: Networking/Remote access

Source0: %name-%version.tar.gz
Packager: Korneechev Evgeniy <ekorneechev@altlinux.org>

BuildArch: noarch
BuildRequires: /proc
Requires: x11vnc

%description
This tool adds the systemd service for x11vnc

%prep
%setup

%install
install -pDm644 x11vnc.service %buildroot%_unitdir/x11vnc.service
install -pDm644 %name.1 %buildroot%_mandir/man1/%name.1

%post
%post_service x11vnc

%preun
%preun_service x11vnc

%files
%_unitdir/x11vnc.service
%_mandir/man1/%name.1.xz

%changelog
* Mon Jan 30 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.1-alt3
- Replaced: postun -> preun

* Tue Dec 20 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.1-alt2
- Fixed spec for p8

* Thu Dec 15 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.1-alt1
- Initial build
- Thanks 'rabochyITs' - https://forum.altlinux.org/index.php?topic=32355#msg285275


