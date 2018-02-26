Name: libtunepimp
Version: 0.5.3
Release: alt5.1

Group: System/Libraries
Summary: Library that provides access to the MusicBrainz server
License: LGPL

Packager: Motsyo Gennadi <drool@altlinux.ru>

Url: http://www.musicbrainz.org/

Source: ftp://ftp.musicbrainz.org/pub/musicbrainz/%name-%version.tar.gz
Patch0: libtunepimp-0.5.3-alt-system-ltdl.patch
Patch1: libtunepimp-0.5.3-alt-gcc43.patch
Patch2: %name-0.5.3-gcc44.patch
Patch3: %name-0.5.3-curl.patch

# Automatically added by buildreq on Mon Mar 26 2007
BuildPreReq: rpm-build-python zlib-devel
BuildRequires: gcc-c++ libcurl-devel libexpat-devel libflac-devel libltdl7-devel
BuildRequires: libmad-devel libmpcdec-devel libmpeg4ip-devel libmusicbrainz-devel
BuildRequires: libofa-devel libtag-devel libvorbis-devel

# for python module
BuildRequires: python-devel >= 2.4 python python-module-setuptools

%description
MusicBrainz is the second generation incarnation of the CD Index. This
server is designed to enable Audio CD and MP3/Vorbis players to download
metadata about the music they are playing.

The TunePimp library (also referred to as libtunepimp) is a development
library geared towards developers who wish to create MusicBrainz enabled
tagging applications.

%package devel
Summary: Include Files and Libraries mandatory for Development
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require TunePimp library.

%package -n python-module-tunepimp
Summary: Python module for libtunepimp
Group: Development/Python
BuildArch: noarch
Requires: %name >= %version

%description -n python-module-tunepimp
Python module for libtunepimp

%prep
%setup

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%autoreconf
%configure \
	--disable-static

%make_build

%install
%makeinstall_std

pushd python
%python_build_install --optimize=2 --record=INSTALLED_FILES
popd

%files
%doc AUTHORS ChangeLog README.*
%_bindir/puid
%_libdir/*.so.*
%_libdir/tunepimp

%files devel
%_includedir/tunepimp-0.5
%_libdir/*.so

%files -n python-module-tunepimp
%_target_libdir_noarch/python%_python_version/site-packages/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.3-alt5.1
- Rebuild with Python-2.7

* Thu Aug 04 2011 Motsyo Gennadi <drool@altlinux.ru> 0.5.3-alt5
- fix build wich new curl (without curl/types.h)

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt4.2.3
- Fixed build

* Tue Dec 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt4.2.2
- Rebuilt for soname set-versions

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt4.2.1
- Rebuilt with python 2.6

* Sat Oct 03 2009 Alexey Morsov <swi@altlinux.ru> 0.5.3-alt4.2
- enable python binding

* Wed Aug 26 2009 Motsyo Gennadi <drool@altlinux.ru> 0.5.3-alt4.1
- fixed build with gcc44 (added patch from Gentoo)

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.3-alt4
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Mon Oct 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.5.3-alt3
- fixed build with gcc4.3

* Wed May 09 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.3-alt2
- rebuild with libmpcdec.so.5

* Mon Mar 26 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.5.3-alt1
- 0.5.3

* Wed Dec 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.4.4-alt1
- NMU: update to 0.4.4:
  + Fixed cycling in case of unsupported file format.
  + Fixed buffer overflow in lookuptools.cpp (patch by urs_fleisch at yahoo dot de).
  + Fixed memleaks in the WMA plugin.

* Mon Feb 13 2006 Mikhail Yakshin <greycat@altlinux.org> 0.4.2-alt1
- 0.4.2

* Fri Dec 23 2005 Mikhail Yakshin <greycat@altlinux.org> 0.4.0-alt2
- added patch to disallow several characters for FAT32/NTFS systems

* Mon Dec 05 2005 Mikhail Yakshin <greycat@altlinux.org> 0.4.0-alt1
- 0.4.0

* Tue Feb 22 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.3.0-alt1.1.1
- Rebuilt with libflac-1.1.2-alt1

* Tue Jan 18 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt1.1
- rebuild with g++-3.4.

* Thu Oct 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.3.0-alt1
- First build for Sisyphus.

