%define libname libmpeg2
%define cvsdate 20030612
%undefine cvsdate

Name: mpeg2dec
Version: 0.5.1
%define release alt3

%ifdef cvsdate
Release: %{release}cvs%cvsdate.qa1
%else
Release: %release
%endif

Packager: Pavlov Konstantin <thresh@altlinux.ru>
Summary: mpeg-1 and mpeg-2 streams decoder
License: GPL
Group: Video
Url: http://%libname.sourceforge.net

%ifndef cvsdate
Source: %url/files/%name-%version.tar.bz2
%else
Source: %name-%cvsdate.tar.bz2
%endif

Requires: %libname = %version-%release

# Automatically added by buildreq on Mon Jun 12 2006
BuildRequires: esound imake libSDL-devel libXt-devel libXv-devel xorg-cf-files

%description
%libname is a free library for decoding mpeg-2 and mpeg-1 video streams

%name is a test program for %libname. It decodes mpeg-1 and mpeg-2
video streams, and also includes a demultiplexer for mpeg-1 and mpeg-2
program streams. It is purposely kept simple : it does not include
features like reading files from a DVD, CSS, fullscreen output,
navigation, etc... The main purpose of %name is to have a simple test
bed for %libname.

%package -n %libname
Summary: Shared version of %libname library
Group: System/Libraries

%description -n %libname
Shared library for decoding mpeg-2 and mpeg-1 video streams.

%package -n %libname-devel
Summary: %libname development files
Group: Development/C
Requires: %libname = %version-%release

%description -n %libname-devel
This package contains header files and development libraries for %libname

%package -n %libname-devel-static
Summary: Static version of %libname library
Group: Development/C
Requires: %libname-devel = %version-%release

%description -n %libname-devel-static
This package contains static versions of %libname

%prep
%ifndef cvsdate
%setup -q -n %name-0.4.1
%else
%setup -q -n %name-%cvsdate
%endif

%build
%add_optflags %optflags_shared
%autoreconf
%configure --enable-shared
%make_build

%install
%make_install DESTDIR=%buildroot install

# remove non-packaged files
rm -f %buildroot%_libdir/*.la

%files
%_bindir/*
%_man1dir/*

%files -n %libname
%_libdir/*.so.*
%doc AUTHORS ChangeLog NEWS README

%files -n %libname-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*
%doc CodingStyle TODO doc/*.txt

%files -n %libname-devel-static
%_libdir/*.a

%changelog
* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt3
- Rebuilt for debuginfo

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt2
- Rebuilt for soname set-versions

* Fri Nov 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.5.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libmpeg2
  * postun_ldconfig for libmpeg2
  * postclean-05-filetriggers for spec file

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.5.1-alt1
- 0.5.1.

* Tue Oct 17 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.4.1-alt1
- 0.4.1.
- Removed patches.

* Mon Jun 12 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.4.0b-alt2
- Updated build dependencies

* Fri Dec 09 2005 Anton D. Kachalov <mouse@altlinux.org> 0.4.0b-alt1
- 0.4.0b
- multiarch

* Tue Dec 23 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Fri Nov 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.3.1-alt1.6cvs20030612
- updated cvs snapshot (requires for vlc-0.6.2)
- do not package .la files.

* Thu Apr 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.3.1-alt1.5cvs20030408
- cvs snapshot to build vlc.

* Sat Dec 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Wed Dec 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Mon Oct 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.1-alt2
- Rebuild with gcc-3.2. 

* Sat May 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.2.1-alt1
- First build for Sisyphus. 
