Name: 	 zramen
Version: 1.0.1
Release: alt1
Summary: Manage zram swap space
License: Unlicense
Group:   System/Base
URL:     https://github.com/atweiden/zramen
VCS:     https://github.com/atweiden/zramen
Source:  %name-%version.tar
Patch:   %name-%version-%release.patch

BuildArch: noarch

%description
Manage zram swap space.

%prep
%setup
%autopatch -p1

%install
install -D -m 0644 zramen.service %buildroot/%_unitdir/zramen.service
install -D -m 0755 zramen %buildroot/%_sbindir/zramen
install -D -m 0644 zramen.conf %buildroot/%_sysconfdir/zramen.conf

%files
%_unitdir/zramen.service
%config(noreplace) %_sysconfdir/zramen.conf
%_sbindir/zramen
%doc README.md UNLICENSE

%changelog
* Tue Oct 21 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 1.0.1-alt1
- Initial build.
