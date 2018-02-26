Name: libmusicbrainz3
Version: 3.0.3
Release: alt1
Summary: A software library for accesing MusicBrainz servers
License: LGPLv2+
Group: Sound
Url: http://www.musicbrainz.org/
Packager: Afanasov Dmitry <ender@altlinux.org>
# ftp://ftp.musicbrainz.org/pub/musicbrainz/libmusicbrainz-%version.tar.gz
Source: libmusicbrainz-%version.tar
# BuildRequires: cmake
# BuildRequires: cppunit-devel
# BuildRequires: libneon-devel >= 0.25
# BuildRequires: libdiscid-devel
# BuildRequires: libstdc++-devel
# BuildRequires: libtool
# BuildRequires: pkgconfig

# Automatically added by buildreq on Fri Feb 15 2008
BuildRequires: ccmake cppunit-devel gcc-c++ libdiscid-devel libneon-devel

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%package devel
Summary: Headers for developing programs that will use libmusicbrainz
Group: Development/Other
Requires: %name = %version-%release
# Requires: libdiscid-devel
# Requires: libstdc++-devel
# Requires: libneon-devel >= 0.25

%description devel
This package contains the headers that programmers will need to
develop applications which will use libmusicbrainz.

%prep
%setup -n libmusicbrainz-%version

%build
cmake . -DCMAKE_INSTALL_PREFIX=%prefix -DCMAKE_VERBOSE_MAKEFILE=1 \
%if "%_lib" == "lib64"
	-DLIB_SUFFIX=64
%endif

%install
%makeinstall_std

%files
%_libdir/%name.so.*
%doc AUTHORS.txt NEWS.txt

%files devel
%_libdir/%name.so
%_includedir/musicbrainz3
%_pkgconfigdir/%name.pc

%changelog
* Wed Sep 28 2011 Dmitry V. Levin <ldv@altlinux.org> 3.0.3-alt1
- Updated to 3.0.3.
- Fixed interpackage dependencies.
- Rebuilt for debuginfo.

* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2-alt4.1
- Rebuilt for soname set-versions

* Tue May 12 2009 Afanasov Dmitry <ender@altlinux.org> 3.0.2-alt4
- fix gcc4.4 build

* Mon Dec 22 2008 Afanasov Dmitry <ender@altlinux.org> 3.0.2-alt3
- rebuild with libneon.so.27

* Tue Nov 25 2008 Afanasov Dmitry <ender@altlinux.org> 3.0.2-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Thu Nov 06 2008 Afanasov Dmitry <ender@altlinux.org> 3.0.2-alt1
- update to 3.0.2

* Fri Feb 15 2008 Terechkov Evgenii <evg@altlinux.ru> 3.0.1-alt1
- Initial build for ALT Linux Sisyphus (Thanks to PLD for initial spec)
- spec macro abuse cleanup

$Log: libmusicbrainz3.spec,v $
Revision 1.7  2008-02-02 02:40:25  glen
- fix internal deps; rel 3

Revision 1.6  2007-08-31 20:31:20  arekm
- rel 2

Revision 1.5  2007/08/05 21:09:11  qboosh
- lib64 support

Revision 1.4  2007/07/16 19:11:41  qboosh
- updated to 3.0.1

Revision 1.3  2007/06/12 17:10:48  qboosh
- let rpm detect lib deps

Revision 1.2  2007/05/28 22:39:21  qboosh
- libdiscid is ready

Revision 1.1  2007/05/28 21:13:06  qboosh
- new, rewrite, parallel installable with v2.x
