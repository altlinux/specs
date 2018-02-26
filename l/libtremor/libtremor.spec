%define origname tremor
%define origdate 02132004
%define gcc_ver 4.3

Name: lib%origname
Version: 1.0.0
Release: alt1.svn20040213.2
Summary: The Ogg Vorbis 'Tremor' integer playback codec
License: LGPL
Group: Sound
Url: http://Xiph.org
Packager: Eugeny A. Rostovtsev (REAL) <real@altlinux.org>

# svn co http://svn.xiph.org/trunk/Tremor
Source: %{origname}_snapshot_%origdate.tgz

BuildPreReq: gcc-c++ >= %gcc_ver
BuildPreReq: libstdc++-devel >= %gcc_ver
BuildPreReq: glibc-devel

# Automatically added by buildreq on Sun Dec 28 2008
#BuildRequires: gcc-c++ glibc-devel-static

%description
The Ogg Vorbis 'Tremor' integer playback codec.
Source date is 2002 09 02, version 1.0.0.

Now we can enable tremor while building Mplayer.

%package devel
Summary: Headers for objects for Tremor
Group: Development/C++
Requires: %name = %version-%release

%description devel
Headers for objects for Tremor.

%prep
%setup -n Tremor

%build
%set_gcc_version %gcc_ver
%autoreconf
%configure \
	--prefix=%prefix \
	--enable-shared \
	--disable-static \
	--with-gnu-ld
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/%origname/*.h

%changelog
* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20040213.2
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20040213.1
- Rebuilt for soname set-versions

* Sat Jan 03 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 1.0.0-alt1.svn20040213
- Initial build for Sisyphus

