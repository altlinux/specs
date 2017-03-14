Name: pam-limits-desktop
Version: 0.1
Release: alt2

Summary: Configure pam_limits for desktop use
License: GPL
Group: System/Configuration/Other

Url: http://forum.altlinux.org/index.php?topic=37107.0
BuildArch: noarch

%define limitsdir %_sysconfdir/security/limits.d

%description
%summary
(increase nproc, nofile).

%prep

%build

%install
mkdir -p %buildroot%limitsdir
cat << EOF >> %buildroot%limitsdir/90-desktop.conf
# better defaults for desktop systems
*		soft	nproc	4096
*		hard	nproc	5120
*		soft	nofile	8192
*		hard	nofile	10240
*		soft	memlock	1024
*		hard	memlock	2048
EOF

%files
%limitsdir/90-desktop.conf

%changelog
* Tue Mar 14 2017 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- added memlock limits suggested by shaba@

* Mon Feb 27 2017 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

