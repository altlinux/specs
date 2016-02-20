%define oname soundtouch

Name: libsoundtouch
Version: 1.9.2
Release: alt1

Summary: SoundTouch audio processing library
Group: System/Libraries
License: LGPLv2.1
Url: http://www.surina.net/soundtouch/

Source: http://www.surina.net/%oname/%{oname}-%version.tar.gz

BuildRequires: gcc-c++ libstdc++-devel

%description
SoundTouch is an open-source audio processing library that allows changing
the sound tempo, pitch and playback rate parameters independently from
each other, i.e.:
 - Sound tempo can be increased or decreased while maintaining the original pitch
 - Sound pitch can be increased or decreased while maintaining the original tempo
 - Change playback rate that affects both tempo and pi

%package devel
Summary: Libraries/include files for development with %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Libraries/include files for development with %name.

%prep
%setup -n %oname

%build
#touch NEWS README AUTHORS ChangeLog
#%autoreconf
./bootstrap
%configure --disable-static
%make_build

%install
%makeinstall_std
rm -rf %buildroot/%_prefix/doc

%files
%_bindir/soundstretch
%_libdir/libSoundTouch.so.*
%doc README.html

%files devel
%_includedir/%oname/
%_libdir/libSoundTouch.so
%_aclocaldir/%oname.m4
%_pkgconfigdir/%oname.pc

%changelog
* Fri Feb 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.9.2-alt1
- 1.9.2

* Tue Nov 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0
- removed obsolete patches

* Sat Aug 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt2.qa2
- Rebuilt for debuginfo

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Mon Dec 15 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt2
- fix build with gcc 4.3

* Thu Dec 07 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- correct version (download 1.3.1 from surina.net)
- use native soundtouch-1.0.pc (fix bug #10366, thanks eostapets@)

* Tue Jun 06 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt0.3
- add libSoundTouch.pc (fix bug #9677). Thanks, Debian.

* Mon May 29 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt0.2
- fixes for as-needed

* Mon Feb 06 2006 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt0.1
- initial build for ALT Linux Sisyphus
- build without asm optimization
