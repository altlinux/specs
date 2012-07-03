Name: installer-feature-samba-usershares
Version: 0.4
Release: alt1

Summary: Installer hooks for Samba usershares
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
This package contains installer hooks for
enabling Samba usershares.

%package stage2
Summary: Installer stage2 hook for Samba usershares
Group: System/Configuration/Other
Requires: samba

%description stage2
This package contains installer stage2 hook for
enabling Samba usershares.

%prep
%setup

%install
%define hookdir %_datadir/install2/preinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files stage2
%hookdir/*

%changelog
* Mon Feb 13 2012 Mikhail Efremov <sem@altlinux.org> 0.4-alt1
- Rename hook: 75-* -> 85-* (closes: #26930).

* Fri May 20 2011 Mikhail Efremov <sem@altlinux.org> 0.3-alt1
- Enable samba service.
- Change group name to sambashare.
- Set UMASK for home dirs to 076.
- smb.conf: Change workgroup MYGROUP -> WORKGROUP.
- Typo in comment.
- Don't add existing users to smbusershare group.
- Stage3 hook -> stage2 hook.

* Thu May 19 2011 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- Create default-groups file for alterator-users.
- Fix users searching.

* Wed May 04 2011 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build
