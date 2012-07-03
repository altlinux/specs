# vim: set ft=spec: -*- rpm-spec -*-

Name: wimax-tools
Version: 1.4.4
Release: alt1

Summary: Low level user space tools for the Linux WiMAX stack
Group: System/Kernel and hardware
License: BSD
Url: http://linuxwimax.org/

BuildRequires: libnl-devel kernel-headers-un-def glib2-devel

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
Low level user space tools for the Linux WiMAX stack.

%package -n libwimaxll
Summary: Low level library for the Linux WiMAX stack
Group: System/Kernel and hardware
Conflicts: %name < %version-%release
Conflicts: %name > %version-%release

%description -n libwimaxll
Low level library for the Linux WiMAX stack.

%package devel
Summary: Development files for %name
Group: Development/Kernel
Requires: libwimaxll = %version-%release
Provides: libwimaxll-devel = %version-%release

%description devel
Development files for %name.

%prep
%setup
%patch -p1
touch NEWS AUTHORS ChangeLog COPYING

%build
%autoreconf
%configure \
	--enable-shared \
	--disable-static
%make_build

%install
%makeinstall_std

%files
%doc README
%_bindir/*
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/*.so

%files -n libwimaxll
%_libdir/libwimaxll*.so.*

%files devel
%_includedir/wimaxll*
%_libdir/libwimaxll*.so
%_pkgconfigdir/libwimaxll*.pc
%_pkgconfigdir/wimaxll-cmd*.pc

%changelog
* Mon Oct 25 2010 Alexey I. Froloff <raorn@altlinux.org> 1.4.4-alt1
- [1.4.4]

* Sun Sep 12 2010 Alexey I. Froloff <raorn@altlinux.org> 1.4.3-alt2
- wimaxll-cmd.pc moved to devel subpackage
- Renamed libwimaxll-devel to wimax-tools-devel

* Sun Sep 12 2010 Alexey I. Froloff <raorn@altlinux.org> 1.4.3-alt1
- [1.4.3]

