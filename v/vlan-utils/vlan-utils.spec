Name: vlan-utils
Version: 1.9
Release: alt3

Summary: Userspace utilities for controlling VLANs on ethernet devices
License: GPLv2+
Group: System/Kernel and hardware
Url: http://www.candelatech.com/~greear/vlan.html
Packager: Dmitry V. Levin <ldv@altlinux.org>

# http://www.candelatech.com/~greear/vlan/vlan.%version.tar.gz
Source: vlan-%version.tar
Patch: vlan-1.9-deb-alt-fixes.patch

Provides: vlan-utils24 = %version-%release
Obsoletes: vlan-utils24 < %version
Conflicts: vlan-utils22

%description
This package contains the user mode utility required to add and remove
VLAN devices from ethernet devices.

%prep
%setup -q -n vlan-%version
%patch -p1

%build
make clean
%make_build VERSION=%version CCFLAGS='%optflags -D_GNU_SOURCE'
# fix broken refs
sed -i -e 's|<a href="vlan/howto|<a href="howto|' \
	-e 's|<a href="vlan/vlan|<a href="http://www.candelatech.com/~greear/vlan/vlan|' \
	vlan.html

%install
mkdir -p %buildroot{%_bindir,%_man8dir}
install -pm755 vconfig %buildroot%_bindir/
install -pm644 vconfig.8 %buildroot%_man8dir/

%files
%_bindir/*
%_man8dir/*
%doc CHANGELOG README *.html vlan_test.pl

%changelog
* Tue Oct 02 2007 Dmitry V. Levin <ldv@altlinux.org> 1.9-alt3
- Updated debian patch (also fixes #12619).
- Moved vlan_test to %%doc due to contrib quality (also fixes #13009).

* Thu Feb 15 2007 Dmitry V. Levin <ldv@altlinux.org> 1.9-alt2
- Fixed broken references in documentation (#2797).

* Sat Feb 03 2007 Dmitry V. Levin <ldv@altlinux.org> 1.9-alt1
- Updated to 1.9.
- Removed makefile patch.
- Renamed back to vlan-utils.
- Packaged vconfig(8) manpage.

* Wed Oct 01 2003 Dmitry V. Levin <ldv@altlinux.org> 1.8-alt1
- Updated to 1.8, updated makefile patch.

* Thu Apr 10 2003 Stanislav Ievlev <inger@altlinux.ru> 1.6-alt1.1
- remove all alternatives support, this is basesystem.

* Fri Dec 06 2002 Dmitry V. Levin <ldv@altlinux.org> 1.6-alt1
- Updated to 1.6, updated makefile patch.

* Fri Feb 22 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.5-alt2
- Fix build with kernel24-headers.

* Tue Jan 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.5-alt1
- Renamed to vlan-utils24.

* Fri Jan 04 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.5-alt1
- 1.5

* Wed Aug 15 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.3-alt1
- Initial revision.
