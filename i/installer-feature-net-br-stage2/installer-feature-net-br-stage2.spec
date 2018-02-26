Name: installer-feature-net-br-stage2
Version: 0.2
Release: alt1

Summary: Enslave interface to bridge
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Source: %name-%version.tar
Requires: installer-common-stage2

%description
This package contains ifaddbr utility to create a bridge for
for each ethernet interface and to enslave interface to that bridge.

%prep
%setup

%install
mkdir -p %buildroot%_sbindir
install -pm755 ifaddbr %buildroot%_sbindir/

%files
%_sbindir/*

%changelog
* Mon Jul 13 2009 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt1
- Build as noarch (closes: #20769).

* Tue Apr 28 2009 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt1
- Reworked for installer-feature-net-br-stage2.

* Thu Apr 23 2009 Anton Protopopov <aspsk@altlinux.org> 0.02-alt1
- Imitate (virtual) ifclone functionality directly in ifaddbr

* Mon Apr 20 2009 Anton Protopopov <aspsk@altlinux.org> 0.01-alt1
- Build for Sisyphus

* Fri Apr 10 2009 Anton Protopopov <aspsk@altlinux.org> 0.01-alt0.1
- Initial build
