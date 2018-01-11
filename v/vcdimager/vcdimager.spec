%define ver_major 2.0
%def_disable static

Name: vcdimager
Version: %ver_major.1
Release: alt1

Summary: VideoCD (pre-)mastering and ripping tool
Group: Video
License: GPL
Url: http://%name.org

Source: ftp://ftp.gnu.org/gnu/%name/%name-%version.tar.gz

%define libcdio_ver 2.0.0

Requires: libvcd = %version-%release

BuildPreReq: help2man makeinfo
BuildPreReq: libcdio-devel >= %libcdio_ver

BuildRequires: gcc-c++ libcdio-devel >= %libcdio_ver libpopt-devel
BuildRequires: libxml2-devel zlib-devel
#BuildRequires: tetex-core tetex-latex

%description
GNU VCDImager is a full-featured mastering suite for authoring,
disassembling and analyzing Video CD's and Super Video CD's.

The core functionality consists of directly making Video CD
BIN/CUE-style CD images from mpeg files, which (after being written to
CDR(W) media) can be played on standalone VCD players or DVD players
and on computers running GNU/Linux, MacOS, Win32 or any other OS
capable of accessing VCD's. BIN/CUE images can be burned with [cdrdao]
(please use a recent version, since older ones do not support
BIN/CUE-style cuesheets) under GNU/Linux (and other supported
platforms by cdrdao, e.g. freeBSD, Irix, Solaris and even win32)

vcdimager   generates simple pbc-less VCD and SVCD disc images directly
vcddebug    Analyzing tool and report generator for VCD and SVCD discs.
vcdxgen     XML VCD-description generator
vcdxbuild   Builds a VCD/SVCD according to a supplied XML control file.
vcdxrip     Reverses the process for a given VCD or SVCD disc.
vcdxminfo   Debugging tool for displaying MPEG stream properties.
vcdinfo     Dispalys information about VCD.
cdxa2mpeg   Simple tool for converting RIFF CDXA file to plain mpeg.

%package -n libvcd
Summary: Libraries for %name
Group: System/Libraries
Requires: libcdio >= %libcdio_ver

%description -n libvcd
This package provides shared libraries required for %name to work.

%package -n libvcd-devel
Summary: Development files for libvcd.
Group: Development/C
Requires: libvcd = %version-%release
Requires: libcdio-devel >= %libcdio_ver

%description -n libvcd-devel
This package provides files to use for development programs using libvcd.

%package -n libvcd-devel-static
Summary: Static versions of vcd libraries
Group: Development/C
Requires: libvcd-devel = %version-%release

%description -n libvcd-devel-static
This package provides libraries to use for development programs
statically linked against libvcd.

%prep
%setup

%build
%autoreconf
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

# remove non-packaged files
%__rm -f %buildroot%_infodir/dir

%files
%_bindir/*
%_infodir/*.info*
%_man1dir/*
%doc AUTHORS BUGS FAQ TODO ChangeLog NEWS README THANKS
#%doc docs/*.pdf

%files -n libvcd
%_libdir/*.so.*

%files -n libvcd-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%if_enabled static
%files -n libvcd-devel-static
%_libdir/*.a
%endif

%changelog
* Thu Jan 11 2018 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Mon Nov 30 2015 Yuri N. Sedunov <aris@altlinux.org> 0.7.24-alt1.1
- buildreqs: added makeinfo

* Mon Jul 20 2015 Yuri N. Sedunov <aris@altlinux.org> 0.7.24-alt1
- 0.7.24

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.7.23-alt2.4
- NMU: rebuilt for debuginfo.

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.23-alt2.3
- Rebuilt for soname set-versions

* Tue Nov 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.7.23-alt2.2
- Rebuilt with new libcdio.

* Wed Aug 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.7.23-alt2.1
- Rebuilt with new libcdio.

* Tue May 30 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.7.23-alt2
- Rebuilt with new libcdio.

* Wed Nov 30 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.7.23-alt1
- 0.7.23 release.
- Some spec fixes.

* Tue Jul 12 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.7.22-alt1
- 0.7.22

* Sat Feb 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.7.20-alt1
- 0.7.20 release.

* Tue Jan 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.7.20-alt0.5cvs20040107
- switch to cdio branch.

* Fri Nov 29 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.12-alt3
- fixed %%build to enable XML frontends.

* Mon Oct 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.12-alt2
- Rebuild with gcc-3.2. 

* Sun Jan 13 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.7.12-alt1
- 0.7.12.

* Thu Jan 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.6.2-alt1
- First build for Sisyphus. 

