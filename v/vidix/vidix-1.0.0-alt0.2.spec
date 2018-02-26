Packager: Repocop Q. A. Robot <repocop@altlinux.org>
%def_disable static

%define svnrev 21861

Name: vidix
%define lname lib%name
Version: 1.0.0
Release: alt0.2.1
Summary: VIDeo Interface for *niX
License: GPL
Group: System/Libraries
URL: http://www.mplayerhq.hu
# svn checkout svn.mplayerhq.hu/mplayer/trunk/libdha
Source: %name-svn-r%svnrev.tar.bz2
Patch0: %name-svn-r21861-configure.patch.gz
Patch1: %name-svn-r21861-include.patch.gz

BuildRequires: libdha-devel >= 1.0-alt0.3

%description
VIDIX - VIDeo Interface for *niX.
This interface was designed and introduced as interface to userspace
drivers to provide DGA everywhere where it's possible (unline X11).
What is it:
  - It's portable successor of mga_vid technology which is located in
    user-space.
  - Unlikely X11 it's provides DGA everywhere where it's possible.
  - Unlikely v4l it provides interface for video playback
  - Unlikely linux's drivers it uses mathematics library.

  
%package -n %lname
Summary: VIDeo Interface for *niX library
Group: System/Libraries

%description -n %lname
VIDIX - VIDeo Interface for *niX.
This interface was designed and introduced as interface to userspace
drivers to provide DGA everywhere where it's possible (unline X11).
What is it:
  - It's portable successor of mga_vid technology which is located in
    user-space.
  - Unlikely X11 it's provides DGA everywhere where it's possible.
  - Unlikely v4l it provides interface for video playback
  - Unlikely linux's drivers it uses mathematics library.

This package contents shared library for VIDIX.


%package -n %lname-devel
Summary: Headers for VIDeo Interface for *niX library
Group: Development/C
Requires: %lname = %version-%release

%description -n %lname-devel
Headers for VIDeo Interface for *niX (VIDIX) library.


%if_enabled static
%package -n %lname-devel-static
Summary: Static library of VIDeo Interface for *niX
Group: Development/C
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
Static library of VIDeo Interface for *niX (VIDIX).
%endif


%package drivers
Summary: Drivers for VIDIX
Group: System/Libraries
Conflicts: MPlayer-vidix-driver

%description drivers
VIDIX - VIDeo Interface for *niX.
This interface was designed and introduced as interface to userspace
drivers to provide DGA everywhere where it's possible (unline X11).
What is it:
  - It's portable successor of mga_vid technology which is located in
    user-space.
  - Unlikely X11 it's provides DGA everywhere where it's possible.
  - Unlikely v4l it provides interface for video playback
  - Unlikely linux's drivers it uses mathematics library.

This package contents VIDIX drivers.


%prep
%setup -q -n %name-svn-r%svnrev
%patch0 -p1
%patch1 -p1


%build
%add_optflags %optflags_shared
CFLAGS="%optflags" sh ./configure --prefix=%_prefix --libdir=%_libdir --cc=gcc
%make_build
%{?_enable_static:%make_build %lname.a}


%install
%make_install LIBDIR=%buildroot%_libdir INCDIR=%buildroot%_includedir/vidix install
%{?_enable_static:install -m 0644 %lname.a %buildroot%_libdir/}


%files -n %lname
%doc README
%_libdir/*.so.*


%files -n %lname-devel
%_includedir/%name
%_libdir/*.so


%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif


%files drivers
%dir %_libdir/%name
%_libdir/%name/*


%changelog
* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt0.2.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libvidix
  * postun_ldconfig for libvidix

* Wed Jan 10 2007 Led <led@altlinux.ru> 1.0.0-alt0.2
- new SVN snapshot (revision 21861)
- updated %name-svn-r21861-configure.patch
- updated %name-svn-r21861-include.patch

* Wed Aug 30 2006 Led <led@altlinux.ru> 1.0.0-alt0.1
- sources from MPlayer SVN
- remade spec
- fixed %%changelog

* Thu Jul 20 2006 Led <led@altlinux.ru> 0.9.9.1-alt4
- added kernel-source-dhahelper
- added dhahelper-0.9.9.1-linux-2.6.11.patch

* Mon Jul 10 2006 Led <led@altlinux.ru> 0.9.9.1-alt3
- added Conflicts for MPlayer-vidix and MPlayer-vidix-driver

* Thu Jul 06 2006 Led <led@altlinux.ru> 0.9.9.1-alt2
- added vidix-0.9.9.1-static.patch
- added making static %lname

* Thu Jul 06 2006 Led <led@altlinux.ru> 0.9.9.1-alt1
- inital build
- added vidix-0.9.9.1-pm3_vid.patch
