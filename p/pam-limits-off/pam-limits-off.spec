Name: pam-limits-off
Version: 0.1
Release: alt1
Summary: Configure pam_limits to disable limits
License: GPL-3.0-or-later
Group: System/Configuration/Other

BuildArch: noarch

%define limitsdir %_sysconfdir/security/limits.d

%description
%summary
(Disable limits nproc, nofile).

%prep

%build

%install
mkdir -p %buildroot%limitsdir
cat << EOF >> %buildroot%limitsdir/95-desktop.conf
# better defaults for desktop systems
*		soft	nproc	infinity
*		hard	nproc	infinity
*		soft	nofile	infinity
*		hard	nofile	infinity
*		soft	memlock	infinity
*		hard	memlock	infinity
EOF

%files
%limitsdir/95-desktop.conf

%changelog
* Thu Nov 13 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 0.1-alt1
- Initial build.
