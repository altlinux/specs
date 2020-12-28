%define origname tremor
%define origdate 02132004

Name: libvorbisidec
Version: 1.2.1
Release: alt1.git.7c30a66
Summary: The Ogg Vorbis 'Tremor' integer playback codec
License: LGPL
Group: Sound
Url: http://Xiph.org

Obsoletes: libtremor < %EVR
Provides: libtremor = %version

# https://gitlab.xiph.org/xiph/tremor
Source: %origname.tar

# Automatically added by buildreq on Mon Dec 28 2020
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 perl pkg-config python2-base sh4
BuildRequires: libogg-devel

%description
Integer-only Ogg Vorbis decoder, AKA "tremor"

libvorbisidec is an Ogg Vorbis audio decoder (also known as "tremor"),
implemented with no floating point arithmetic. This makes it particularly
amenable to use on systems which lack floating point hardware.

%package devel
Summary: Headers for objects for %name
Group: Development/C
Requires: %name = %version-%release
Provides: libtremor-devel = %version

%description devel

Integer-only Ogg Vorbis decoder, AKA "tremor"

libvorbisidec is an Ogg Vorbis audio decoder (also known as "tremor"),
implemented with no floating point arithmetic. This makes it particularly
amenable to use on systems which lack floating point hardware.

Headers for objects for Tremor.

%prep
%setup -n tremor

%build
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
%doc CHANGELOG COPYING README*

%files devel
%_libdir/*.so
%_includedir/%origname/*.h
%_pkgconfigdir/*.pc
%doc doc

%changelog
* Mon Dec 28 2020 Ildar Mulyukov <ildar@altlinux.ru> 1.2.1-alt1.git.7c30a66
- new upstream URL
- changed package names: libtremor -> libvorbisidec

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20040213.2
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.svn20040213.1
- Rebuilt for soname set-versions

* Sat Jan 03 2009 Eugeny A. Rostovtsev (REAL) <real@altlinux.org> 1.0.0-alt1.svn20040213
- Initial build for Sisyphus

