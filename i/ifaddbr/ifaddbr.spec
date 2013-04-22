Name: ifaddbr
Version: 0.02
Release: alt1.qa2
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
# sysconf/udev policy - /etc is for user
mkdir -p %buildroot%_udevrulesdir/
mv %buildroot%_sysconfdir/udev/rules.d/* %buildroot%_udevrulesdir/

%files
/sbin/*
%_udevrulesdir/*

%changelog
* Tue Apr 23 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0.02-alt1.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * udev-files-in-etc for ifaddbr

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.02-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Apr 23 2009 Anton Protopopov <aspsk@altlinux.org> 0.02-alt1
- Imitate (virtual) ifclone functionality directly in ifaddbr

* Mon Apr 20 2009 Anton Protopopov <aspsk@altlinux.org> 0.01-alt1
- Build for Sisyphus

* Fri Apr 10 2009 Anton Protopopov <aspsk@altlinux.org> 0.01-alt0.1
- Initial build
