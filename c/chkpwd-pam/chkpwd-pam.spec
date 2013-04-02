%define _libexecdir %_prefix/libexec

Name: chkpwd-pam
Version: 0.1.0
Release: alt1
Summary: PAM user password checker
License: GPLv3
Group: System/Base
Source: %name-%version.tar

BuildRequires: pam_userpass-devel

%description
Tool for check user password through PAM.


%prep
%setup -q


%build
%make_build CFLAGS="%optflags"


%install
install -d -m 0755 %buildroot{%_libexecdir,%_sysconfdir/pam.d}
install -m 0755 %name %buildroot%_libexecdir/
install -m 0644 userpass.pamd %buildroot%_sysconfdir/pam.d/userpass


%files
%attr(2711,root,chkpwd) %_libexecdir/*
%_sysconfdir/pam.d/*


%changelog
* Tue Apr 02 2013 Led <led@altlinux.ru> 0.1.0-alt1
- initial build
