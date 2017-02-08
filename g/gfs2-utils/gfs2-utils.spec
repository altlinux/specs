Name: gfs2-utils
Version: 3.1.9
Release: alt1
License: GPLv2+ and LGPLv2+
Group: System/Kernel and hardware
Summary: Utilities for managing the global file system (GFS2)
URL: https://fedorahosted.org/cluster/wiki/HomePage

Source0: https://fedorahosted.org/released/gfs2-utils/gfs2-utils-%version.tar.gz
Patch0: gfs2-utils-3.1.9-alt-dmsetup.patch

BuildRequires: flex libblkid-devel libncurses-devel zlib-devel

%description
The gfs2-utils package contains a number of utilities for creating,
checking, modifying, and correcting any inconsistencies in GFS2
file systems.

%prep
%setup -q
%patch0 -p1

%build
%autoreconf
%configure \
	--with-udevdir=/lib/udev
%make_build

%check
%make check

%install
%make -C gfs2 DESTDIR=%buildroot install

%files
%doc doc/COPYING.* doc/COPYRIGHT doc/*.txt doc/README.contributing doc/README.licence doc/README.tests
%_udevrulesdir/82-gfs2-withdraw.rules
%_sbindir/fsck.gfs2
%_sbindir/gfs2_grow
%_sbindir/gfs2_jadd
%_sbindir/mkfs.gfs2
%_sbindir/gfs2_convert
%_sbindir/gfs2_edit
%_sbindir/tunegfs2
%_sbindir/gfs2_withdraw_helper
%_man8dir/fsck.gfs2.8*
%_man8dir/gfs2_grow.8*
%_man8dir/gfs2_jadd.8*
%_man8dir/mkfs.gfs2.8*
%_man8dir/gfs2_convert.8*
%_man8dir/gfs2_edit.8*
%_man8dir/tunegfs2.8*
%_man5dir/*.5*

%changelog
* Wed Feb 08 2017 Valery Inozemtsev <shrek@altlinux.ru> 3.1.9-alt1
- new upstream release

* Thu Mar 31 2016 Valery Inozemtsev <shrek@altlinux.ru> 3.1.8-alt1
- initial release

