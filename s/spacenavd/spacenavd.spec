Name:    spacenavd
Version: 1.4
Release: alt1

Summary: Free user-space driver for 6-dof space-mice
License: GPL-3.0-or-later
Group:   System/Configuration/Hardware
URL:     https://spacenav.sourceforge.net
VCS:     https://github.com/FreeSpacenav/spacenavd

Source:  %name-%version.tar
Patch: spacenavd-fix-pidfile.patch

BuildRequires: gcc git-core
BuildRequires: libXi-devel libXtst-devel libX11-devel libXext-devel

%description
Spacenavd is a free software replacement user-space driver (daemon) for
3Dconnexion's 6-degree-of-freedoms input devices. It is compatible with
the original 3dxsrv daemon, and works perfectly with any program that
was written for the 3Dconnexion driver.

%prep
%setup
%patch -p1

%build
%configure
%make_build

%install
%makeinstall_std
install -Dm755 %name %buildroot%_sbindir/%name
install -Dm644 contrib/systemd/%name.service %buildroot%_unitdir/%name.service
install -Dm644 doc/example-spnavrc %buildroot%_sysconfdir/spnavrc
mkdir -p %buildroot%_presetdir
echo 'enable %name.service' > %buildroot%_presetdir/90-%name.preset

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%doc AUTHORS COPYING README.md
%_bindir/%name
%_bindir/spnavd_ctl
%_sbindir/%name
%config(noreplace) %_sysconfdir/spnavrc
%dir %_presetdir
%_presetdir/90-%name.preset
%_unitdir/%name.service

%changelog
* Tue Oct 27 2026 Sergey Palcheh <minergenon@altlinux.org> 1.4-alt1
- new version 1.4
- update patch spacenavd-fix-pidfile

* Tue May 19 2026 Sergey Palcheh <minergenon@altlinux.org> 1.3.1-alt2
- spec cleanup

* Fri Mar 21 2025 Sergey Palcheh <minergenon@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus
