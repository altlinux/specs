Name: libsexymm
Version: 0.1.9
Release: alt2.1

Summary: collection of additional gtkmm widgets - library
Group: System/Libraries
License: LGPL
Url: http://www.chipx86.com/wiki/Libsexy

Source0: http://releases.chipx86.com/libsexy/%name/%name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

%define gtkmm_ver 2.4.0
%define libsexy_ver 0.1.9

Requires: libgtkmm2 >= %gtkmm_ver
Requires: libsexy >= %libsexy_ver

BuildPreReq: libgtkmm2-devel >= %gtkmm_ver
BuildPreReq: libsexy-devel >= %libsexy_ver

# Automatically added by buildreq on Wed May 07 2008
BuildRequires: gcc-c++ libgtkmm2-devel libsexy-devel

%description
libsexy is a collection of GTK+ widgets that extend the functionality of
such standard widgets as GtkEntry and GtkLabel by subclassing them and
working around the limitations of the widgets.

These are the C++ bindings.

%package devel
Summary: collection of additional gtkmm widgets - header files
Group: Development/C++

Requires: %name = %version-%release

%description devel
libsexy is a collection of GTK+ widgets that extend the functionality of
such standard widgets as GtkEntry and GtkLabel by subclassing them and
working around the limitations of the widgets.

These are the C++ bindings (header files).

%prep
%setup -q

%build
%configure \
	--disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc ChangeLog NEWS
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%dir %_includedir/libsexymm
%dir %_includedir/libsexymm/libsexymm
%dir %_includedir/libsexymm/libsexymm/private
%_includedir/libsexymm/*.h
%_includedir/libsexymm/libsexymm/*.h
%_includedir/libsexymm/libsexymm/private/*.h
%_libdir/libsexymm/include/libsexymmconfig.h
%_libdir/libsexymm/proc/m4/convert.m4
%_libdir/libsexymm/proc/m4/convert_libsexymm.m4
%_pkgconfigdir/libsexymm.pc

%changelog
* Fri Nov 06 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.9-alt2.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libsexymm
  * postun_ldconfig for libsexymm

* Wed May 07 2008 Igor Zubkov <icesik@altlinux.org> 0.1.9-alt2
- fix for fresh sisyphus_check
- buildreq

* Thu Jun 07 2007 Igor Zubkov <icesik@altlinux.org> 0.1.9-alt1
- build for Sisyphus

