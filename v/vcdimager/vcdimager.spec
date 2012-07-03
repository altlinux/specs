%define cvsdate 20040107
%undefine cvsdate
%define ver_major 0.7
%def_disable static

Name: vcdimager
Version: %ver_major.23
%define release alt2.3

%ifdef cvsdate
Release: %{release}cvs%cvsdate
%else
Release: %release
%endif

Summary: VideoCD (pre-)mastering and ripping tool
Group: Video
License: GPL
Url: http://%name.org
Packager: Pavlov Konstantin <thresh@altlinux.ru>

%ifndef cvsdate
Source: %url/pub/%name/%name%{ver_major}_UNSTABLE/%name-%version.tar.gz
%else
Source: %name-%version-%cvsdate.tar.bz2
%endif

%define libcdio_ver 0.72

Requires: libvcd = %version-%release

#BuildPreReq: kernel-headers-std26-up
BuildPreReq: help2man
BuildPreReq: libcdio-devel >= %libcdio_ver

# Automatically added by buildreq on Thu Jul 22 2004
BuildRequires: gcc-c++ glib2 libcdio-devel libpopt-devel libstdc++-devel libxml2-devel pkgconfig tetex-core tetex-latex zlib-devel

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
vcdinfo	    Dispalys information about VCD.
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
%ifndef cvsdate
%setup -q
%else
%setup -q -n %name
pushd docs
%__cp  version.texi version-vcd-info.texi
%__cp  version.texi version-vcdxrip.texi
popd
%endif

# hack to fix version-script generation
%__sed -i 's|\(\$(patsubst %%lo,%%o,\)\(\$(lib.*_la_OBJECTS))\)|\1$(patsubst %%,.libs/%%,\2)|' lib/Makefile*

%build
%ifdef cvsdate
NOCONFIGURE=1 ./autogen.sh
%endif

%configure \
    %{subst_enable static}

%make_build
%make_build -C docs pdf

%install
%makeinstall

%if 0
# build actual man pages.
export LD_LIBRARY_PATH=lib/.libs

for f in %buildroot%_bindir/*; do
    help2man -N \
    --manual="VCDIMAGER CDIO Branch" \
    "$f" > %buildroot%_man1dir/`basename "$f"`.1
done
%endif

# remove non-packaged files
%__rm -f %buildroot%_infodir/dir

%files
%_bindir/*
%_infodir/*.info*
%_man1dir/*
%doc AUTHORS BUGS FAQ TODO ChangeLog NEWS README THANKS 
%doc docs/*.pdf

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

