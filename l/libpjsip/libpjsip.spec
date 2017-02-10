%define oname pjproject
Name: libpjsip
Version: 2.5.5
Release: alt1

Summary: Libraries for building embedded/non-embedded VoIP applications

License: GPLv2+
Group: System/Libraries
Url: http://www.pjsip.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.pjsip.org/release/%version/%oname-%version.tar
#Source: %name-%version.tar

# Nothing like carrying a 500k patch just to fix the FSF address :-)
Patch: pjproject_fix_old_FSF_address.patch
# Tell the build system not to use most of the third_party directory
Patch1: pjproject_no_third_party.patch
# Keep the .pc file clean
# see https://bugzilla.redhat.com/show_bug.cgi?id=728302#c66
Patch2: pjproject_fixup_pc_file.patch
# Fix ARMv7 endianness
Patch3: pjproject-armv7.patch
# Add aarch64
Patch4: pjproject-aarch64.patch
# Fix ppc64 endiannes
Patch5: pjproject-ppc64.patch

BuildRequires: gcc-c++
BuildRequires: libalsa-devel
BuildRequires: libgsm-devel
BuildRequires: libsrtp-devel
BuildRequires: libuuid-devel
BuildRequires: libssl-devel
BuildRequires: pkg-config
BuildRequires: libportaudio2-devel
# TODO: check for correct version
#BuildRequires: libresample-devel
BuildRequires: libspeex-devel
BuildRequires: libspeexdsp-devel

%description
This package provides the Open Source, comprehensive, high performance,
small footprint multimedia communication libraries written in C
language for building embedded/non-embedded VoIP applications.
It contains:
- PJSIP - Open Source SIP Stack
- PJMEDIA - Open Source Media Stack
- PJNATH - Open Source NAT Traversal Helper Library
- PJLIB-UTIL - Auxiliary Library
- PJLIB - Ultra Portable Base Framework Library
- PJSUA2 - Object Oriented abstractions layer for PJSUA

%package devel
Summary: Development files to use pjproject
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header information for:
- PJSIP - Open Source SIP Stack
- PJMEDIA - Open Source Media Stack
- PJNATH - Open Source NAT Traversal Helper Library
- PJLIB-UTIL - Auxiliary Library
- PJLIB - Ultra Portable Base Framework Library

%prep
%setup -n %oname-%version
#patch0 -p1 -b .fsf
%patch1 -p1 -b .3rd
%patch2 -p1 -b .pkg
%patch3 -p1 -b .arm
%patch4 -p1 -b .aarch64
%patch5 -p1 -b .ppc64

# make sure we don't bundle these third-party libraries
# (They're excluded through ./configure, but this is an
# additional safety net)
rm -rf third_party/BaseClasses
rm -rf third_party/bdsound
rm -rf third_party/bin
rm -rf third_party/g7221
rm -rf third_party/gsm
rm -rf third_party/milenage
rm -rf third_party/mp3
rm -rf third_party/portaudio
#rm -rf third_party/resample
rm -rf third_party/speex
rm -rf third_party/srtp
rm -rf third_party/ilbc
rm -rf third_party/build/baseclasses
rm -rf third_party/build/g7221
rm -rf third_party/build/gsm
rm -rf third_party/build/milenage
rm -rf third_party/build/portaudio/src
#rm -rf third_party/build/resample
rm -rf third_party/build/samplerate
rm -rf third_party/build/speex
rm -rf third_party/build/srtp
rm -rf third_party/build/ilbc

%build
# We're building without audio or video support, as Asterisk isn't using
# that functionality, and it made it easier to ensure that we don't
# bundle any unnecessary libraries.  Please contact me if your project
# needs this support, and I'll re-enable it
export CFLAGS="-DPJ_HAS_IPV6=1 ${ARCHFLAGS} %optflags"

%configure --enable-shared        \
           --disable-static       \
           --with-external-gsm    \
           --with-external-pa     \
           --with-external-speex  \
           --with-external-srtp   \
           --disable-opencore-amr \
           --enable-resample      \
           --enable-sound         \
           --disable-video        \
           --disable-v4l2         \
           --disable-ilbc-codec   \
           --disable-libyuv       \
           --disable-g7221-codec

%make_build dep
%make_build

%install
%makeinstall_std

# Remove the static libraries, as they aren't wanted
find %buildroot -type f -name "*.a" -delete
# random extras due to patching for the FSF address change
find %buildroot -type f -name "*.fsf" -delete

# rpmlint complains that this is an empty file, so let's fix that
echo "" >> %buildroot%_includedir/pj/config_site.h

%files
%doc README.txt README-RTEMS
%attr(755, root, root) %_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/pj++/
%_includedir/pj/
%_includedir/pjlib-util/
%_includedir/pjmedia-audiodev/
%_includedir/pjmedia-codec/
%_includedir/pjmedia-videodev/
%_includedir/pjmedia/
%_includedir/pjnath/
%_includedir/pjsip-simple/
%_includedir/pjsip-ua/
%_includedir/pjsip/
%_includedir/pjsua-lib/
%_includedir/pjsua2/
%_includedir/*.h
%_includedir/*.hpp
%_pkgconfigdir/libpjproject.pc

%changelog
* Fri Feb 10 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5.5-alt1
- new version 2.5.5 (with rpmrb script)

* Mon Nov 30 2015 Igor Vlasenko <viy@altlinux.ru> 2.4.5-alt4.1
- NMU: added BR: libspeexdsp-devel

* Fri Nov 20 2015 Vitaly Lipatov <lav@altlinux.ru> 2.4.5-alt4
- cleanup spec
- build with internal resample from http://ccrma.stanford.edu/~jos/resample/
- enable sound

* Sun Nov 08 2015 Denis Smirnov <mithraen@altlinux.ru> 2.4.5-alt2
- rebuild with libsrtp-devel

* Thu Aug 20 2015 Vitaly Lipatov <lav@altlinux.ru> 2.4.5-alt1
- new version 2.4.5 (with rpmrb script)

* Thu Aug 20 2015 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt1
- initial build for ALT Linux Sisyphus

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May  5 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.4-1
- Upstream 2.4 release

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3-8
- Rebuilt for GCC 5 C++11 ABI change

* Thu Jan 29 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.3-7
- Fix endian support for aarch64
- Add speexdsp-devel dep as speex_echo.h has moved there

* Fri Nov 14 2014 Tom Callaway <spot@fedoraproject.org> - 2.3-6
- rebuild against new libsrtp

* Sun Oct 26 2014 Jared Smith <jsmith@fedoraproject.org> - 2.3-5
- Fix endianness support on ARM platform

* Wed Oct 15 2014 Jared Smith <jsmith@fedoraproject.org> - 2.3-3
- Add IPv6 support

* Wed Sep 10 2014 Jared Smith <jsmiht@fedoraproject.org> - 2.3-2
- Disable video support, and specifically tell it not to use libyuv,
  as the version of libyuv in Fedora is too old
- Disable ilbc codec support, as it is not needed

* Wed Sep 10 2014 Jared Smith <jsmiht@fedoraproject.org> - 2.3-1
- Update to upstream 2.3 release

* Fri Jun 20 2014 Jared Smith <jsmiht@fedoraproject.org> - 2.2.1-1
- Update to upstream 2.2.1 release

* Sun Mar 09 2014 Jared Smith <jsmiht@fedoraproject.org> - 2.2-4
- Instead of deleting the empty file pj/config_site.h, make it non-empty

* Fri Feb 28 2014 Jared Smith <jsmiht@fedoraproject.org> - 2.2-3
- Fix the location of the .so files
- Add a massive patch to fix the incorrect FSF address

* Fri Feb 28 2014 Jared Smith <jsmiht@fedoraproject.org> - 2.2-2
- Rebase a patch to simple eliminate the third_party directory
- Add a patch to fix up the .pc file

* Fri Feb 28 2014 Jared Smith <jsmiht@fedoraproject.org> - 2.2-1
- Update to upstream 2.2 release

* Fri Jan 17 2014 Dale Macartney <dbmacartney@fedoraproject.org> - 2.1-0.6.git217740d
- Shorten sumary, and moved libs to -devel package

* Mon Nov 25 2013 Anthony Messina <amessina@messinet.com> - 2.1-0.5.git217740d
- Enable G.722.1 and ILBC

* Mon Nov 25 2013 Anthony Messina <amessina@messinet.com> - 2.1-0.4.git217740d
- Build without opencore-amr

* Mon Nov 18 2013 Anthony Messina <amessina@messinet.com> - 2.1-0.3.git217740d
- Updates for SIP transaction handling

* Sat Nov 16 2013 Anthony Messina <amessina@messinet.com> - 2.1-0.2.gitde17f0e
- Rebuild for updates to OpenSSL

* Mon Oct 07 2013 Anthony Messina <amessina@messinet.com> - 2.1-0.1.gitde17f0e
- Package for Fedora & Asterisk: https://wiki.asterisk.org/wiki/display/AST/Installing+pjproject

* Mon Apr 22 2013 Anthony Messina <amessina@messinet.com> - 2.1-1
- Update to 2.1 release

* Sat Feb 16 2013 Mario Santagiuliana <fedora@marionline.it> - 2.0.1-1
- New version 2.0.1

* Mon Apr 16 2012 Mario Santagiuliana <fedora@marionline.it> - 1.12-2
- fix warning mixed-use-of-spaces-and-tabs from rpmlint
- use macro name and version

* Wed Apr 11 2012 Tom Callaway <spot@fedoraproject.org> - 1.12-1
- use system copy of libsrtp

* Thu Jan 12 2012 Mario Santagiuliana <fedora@marionline.it> 1.12-0
- Update to version 1.12

* Sun Jan 08 2012 Mario Santagiuliana <fedora@marionline.it> 1.10-7
- Follow the comment of Rex Dieter:
  https://bugzilla.redhat.com/show_bug.cgi?id=728302#c17

* Sat Jan 07 2012 Mario Santagiuliana <fedora@marionline.it> 1.10-6
- Follow the comment of Rex Dieter:
  https://bugzilla.redhat.com/show_bug.cgi?id=728302#c14
  https://bugzilla.redhat.com/show_bug.cgi?id=728302#c15

* Thu Dec 29 2011 Mario Santagiuliana <fedora@marionline.it> 1.10-5
- Follow the comment of Rex Dieter:
  https://bugzilla.redhat.com/show_bug.cgi?id=728302#c11

* Mon Aug 15 2011 Mario Santagiulaina <fedora@marionline.it> 1.10-4
- Forgot to write changelog for 1.10-3.
- Version 1.10.3 add patch to resolve libdir issue.

* Mon Aug 15 2011 Mario Santagiulaina <fedora@marionline.it> 1.10-2
- Follow the comment of Thomas Spura:
  https://bugzilla.redhat.com/show_bug.cgi?id=728302#c1

* Thu Aug 04 2011 Mario Santagiulaina <fedora@marionline.it> 1.10-1
- Initial RPM release
