Name:		lxcfs
Version:	5.0.3
Release:	alt1
Summary:	FUSE filesystem for LXC

Group:		Development/Other
License:	LGPL-2.1-or-later
URL:		https://github.com/lxc/lxcfs

VCS:		https://github.com/lxc/lxcfs.git
Source0:	%name-%version.tar
Source1:	lxcfs.sysvinit
# revert https://github.com/lxc/lxcfs/pull/555
Patch:		lxcfs-5.0.3-fix-service.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 0.61 python3-module-jinja2
BuildRequires: libfuse-devel
BuildRequires: pkgconfig(systemd)
BuildRequires: help2man

%define _check_contents_method relaxed

%description
FUSE filesystem for LXC, offering the following features:
 - a cgroupfs compatible view for unprivileged containers
 - a set of cgroup-aware files:
   - cpuinfo
   - meminfo
   - stat
   - uptime

%prep
%setup
%patch -p1
sed -i 's|/bin/fusermount|/usr/bin/fusermount|' config/init/systemd/lxcfs.service.in

%build
%meson \
    -Dinit-script=systemd

%meson_build

%install
%meson_install

mkdir -p %buildroot%_localstatedir/%name
install -Dm0755 %SOURCE1 %buildroot%_initdir/lxcfs

find %buildroot -name '*.la' -delete

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS COPYING README.md
%_bindir/%name
%_libdir/%name/lib%name.so
%_man1dir/%name.1*
%_initdir/%name
%_unitdir/%name.service
%_datadir/lxc/config/common.conf.d/*
%_datadir/%name
%dir %_localstatedir/%name

%changelog
* Thu Mar 23 2023 Alexey Shabalin <shaba@altlinux.org> 5.0.3-alt1
- Updated to 5.0.3.
- Built against libfuse-2.

* Sat Dec 04 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.11-alt1
- Updated to lxcfs-4.0.11.

* Thu Jul 22 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.9-alt1
- Updated to lxcfs-4.0.9.

* Wed Feb 03 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.7-alt1
- Updated to lxcfs-4.0.7.

* Sun Oct 25 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.6-alt1
- Updated to lxcfs-4.0.6.
- Built against libfuse3.
- Fixed systemd service file.

* Sun Aug 09 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.5-alt1
- Updated to lxcfs-4.0.5.
- Fixed license field.

* Fri May 08 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.3-alt1
- Updated to 4.0.3.

* Wed Apr 15 2020 Alexey Shabalin <shaba@altlinux.org> 4.0.2-alt1
- new version 4.0.2

* Tue Mar 31 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.1-alt1
- Updated to 4.0.1.

* Thu Jul 04 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.4-alt1
- 3.0.4

* Wed Feb 06 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.3-alt1
- 3.0.3

* Sun Sep  9 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Jul 10 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.0.1-alt2
- packaged with SysVinit script

* Sun Jun 24 2018 Denis Pynkin <dans@altlinux.org> 3.0.1-alt1
- Update
- pam moved to lxc package

* Wed Jan 24 2018 Denis Pynkin <dans@altlinux.org> 2.0.8-alt1
- Update

* Wed Jan 24 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.7-alt2
- Fixed localstatedir location.

* Fri Jun 30 2017 Denis Pynkin <dans@altlinux.org> 2.0.7-alt1
- Update

* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 2.0.5-alt1
- Update

* Sun Oct 23 2016 Denis Pynkin <dans@altlinux.org> 2.0.4-alt1
- Update

* Wed Aug 24 2016 Denis Pynkin <dans@altlinux.org> 2.0.3-alt1
- Update

* Mon Apr 11 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt3
- Release 2.0

* Thu Mar 03 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt2.rc2
- Added service restart

* Tue Mar 01 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt1.rc2
- Removed devel package.
  liblxcfs.so is loaded via dlopen.

* Thu Feb 25 2016 Denis Pynkin <dans@altlinux.org> 2.0.0-alt0.rc2
- Version update

* Wed Feb 24 2016 Denis Pynkin <dans@altlinux.ru> 2.0.0-alt0.beta2
- Initial version
