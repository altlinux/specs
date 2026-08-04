Name: fontconfig-usr-cache
Version: 0.1
Release: alt1

Summary: Fontconfig config for storing cache in /usr
License: GPL-3.0-or-later
Group: Other
URL: http://git.altlinux.org/people/rirusha/packages/fontconfig-usr-cache
VCS: http://git.altlinux.org/people/rirusha/packages/fontconfig-usr-cache.git

Source: %name-%version.tar

Requires: fontconfig

BuildArch: noarch

%description
%summary.

%prep
%setup

%install
install -pDm0644 conf \
	%buildroot%_sysconfdir/fonts/conf.d/99_%name.conf

%files
%_sysconfdir/fonts/conf.d/99_%name.conf

%changelog
* Tue Aug 04 2026 Vladimir Romanov <rirusha@altlinux.org> 0.1-alt1
- Initial build.
