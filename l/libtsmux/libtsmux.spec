Name: libtsmux
Version: 0.2.0
Release: alt1.1

Summary: Library for muxing of MPEG Transport Streams
Group: System/Libraries
License: LGPL/GPL/MPL/MIT
URL: http://schrodinger.sourceforge.net

Source0: %name-%version.tar.bz2

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Wed Mar 07 2007
#BuildRequires: gcc-c++ gcc-fortran glib2-devel glibc-devel-static linux-libc-headers packages-info-i18n-common
BuildRequires: gcc-c++ glib2-devel

%description
Library for muxing of MPEG Transport Streams

%package devel
Summary: Libraries and includefiles for libtsmux
Group: Development/C
Requires: %name = %version-%release

%description devel
Header files and libraries for libtsmux

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS COPYING COPYING.GPL COPYING.LGPL COPYING.MIT COPYING.MPL ChangeLog README
%_libdir/libtsmux.so.*

%files devel
%_libdir/libtsmux.so
%dir %_includedir/tsmux/
%_includedir/tsmux/*.h
%_pkgconfigdir/tsmux.pc

%changelog
* Fri Nov 06 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.2.0-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libtsmux
  * postun_ldconfig for libtsmux

* Wed Mar 07 2007 Igor Zubkov <icesik@altlinux.org> 0.2.0-alt1
- build for Sisyphus (spec based on template from source package)

* Mon Nov 13 2006 Christian F.K. Schaller <christian@fluendo.com>
- First attempt at spec
