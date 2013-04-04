%define _group chkpwd
%define _libexecdir %_prefix/libexec

Name: chkpwd-pam
Version: 0.1.1
Release: alt1
Summary: PAM user password checker
License: GPLv3
Group: System/Base
Source: %name-%version.tar
%define _bindir %_libexecdir/%name
%define lockfilesdir %_lockdir/%name

BuildRequires: pam_userpass-devel

%description
Tool for check user password through PAM.


%prep
%setup -q


%build
%make_build CFLAGS="%optflags"


%install
install -d -m 0755 %buildroot{%_bindir,%lockfilesdir,%_tmpfilesdir,%_sysconfdir/pam.d}
install -m 0755 %name %buildroot%_bindir/
install -m 0644 userpass.pamd %buildroot%_sysconfdir/pam.d/userpass

echo 'd %lockfilesdir 1770 root %_group' > %buildroot%_tmpfilesdir/%name.conf


%files
%dir %_bindir
%attr(2711,root,%_group) %_bindir/*
%attr(1770,root,%_group) %dir %lockfilesdir
%_tmpfilesdir/%name.conf
%_sysconfdir/pam.d/*


%changelog
* Thu Apr 04 2013 Led <led@altlinux.ru> 0.1.1-alt1
- 0.1.1:
  + add throttle chkpwd-pam invocations to avoid abusing it for bruteforcing
    the password
- add systemd support

* Wed Apr 03 2013 Led <led@altlinux.ru> 0.1.0-alt2
- moved chkpwd-pam to separate directory

* Tue Apr 02 2013 Led <led@altlinux.ru> 0.1.0-alt1
- initial build
