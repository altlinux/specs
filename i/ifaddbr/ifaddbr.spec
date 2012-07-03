Name: ifaddbr
Version: 0.02
Release: alt1
Source: %name-%version.tar
Packager: Anton Protopopov <aspsk@altlinux.org>

Summary: Enslave interface to bridge automatically
License: GPL
Group: System/Configuration/Other

%description
Add udev() rules to create a bridge for each new ethernet interface
and to enslave interface to that bridge.

%prep
%setup -q
%make

%install
%makeinstall destdir=%buildroot

%files
/sbin/*
%_sysconfdir/udev/rules.d/*

%changelog
* Thu Apr 23 2009 Anton Protopopov <aspsk@altlinux.org> 0.02-alt1
- Imitate (virtual) ifclone functionality directly in ifaddbr

* Mon Apr 20 2009 Anton Protopopov <aspsk@altlinux.org> 0.01-alt1
- Build for Sisyphus

* Fri Apr 10 2009 Anton Protopopov <aspsk@altlinux.org> 0.01-alt0.1
- Initial build
