# see LIBTGVOIP_VERSION in VoIPController.h for a version

%def_without systemwebrtc
%define soname 0.4
Name: libtgvoip
Version: 2.4.2
Release: alt1

Summary: VoIP library for Telegram clients

Group: Networking/Instant messaging
License: Unlicense

Url: https://github.com/telegramdesktop/libtgvoip
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/grishka/libtgvoip.git
Source: %name-%version.tar

BuildRequires: gyp gcc-c++ libopus-devel libssl-devel libalsa-devel libpulseaudio-devel

%add_optflags -fPIC

%description
VoIP library for Telegram clients.
Dinamically loads libalsa or libpulse.


%package devel
Group: Development/Other
Summary: Development files for %name

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup
# TODO: we can use autotools
#__subst "s|-msse2|-msse2 -I%_includedir/pulse|g" libtgvoip.gyp
%__subst "s|static_library',|shared_library',\n'product_extension': 'so.%soname',|" libtgvoip.gyp
%__subst "s|.*dependencies.*|'link_settings': { 'libraries': ['-ldl', '-lpthread', '-lopus', '-lcrypto'], },|g" libtgvoip.gyp

# TODO
%if_with systemwebrtc
rm -rf webrtc_dsp/
%__subst "s|<(tgvoip_src_loc)/webrtc_dsp|/usr/include/webrtc_audio_processing|" libtgvoip.gyp
%endif

%build
# --no-parallel due gyp in hasher:
#    sl = self._semlock = _multiprocessing.SemLock(kind, value, maxvalue)
#OSError: [Errno 38] Function not implemented
gyp --depth=. --no-parallel \
	-Dlinux_path_opus_include=%_includedir/opus/
%make_build CXXFLAGS="%optflags -std=gnu++14" CFLAGS="%optflags" V=1

cat <<EOF >%name.pc
includedir=%_includedir

Name: %name
Description: %summary
URL: %url
Version: %version
Requires: opus
Conflicts:
Libs: -ltgvoip
Libs.private: -ldl -lpthread -lopus -lcrypto
Cflags: -I\${includedir}/tgvoip
EOF

%install
install -m644 -D out/Debug/lib.target/libtgvoip.so.%soname %buildroot%_libdir/libtgvoip.so.%soname
install -m644 -D %name.pc %buildroot%_pkgconfigdir/%name.pc
ln -s libtgvoip.so.%soname %buildroot%_libdir/libtgvoip.so
mkdir -p %buildroot%_includedir/tgvoip/audio/
mkdir -p %buildroot%_includedir/tgvoip/video/
cp -a *.h %buildroot%_includedir/tgvoip/
cp -a *.hpp %buildroot%_includedir/tgvoip/
cp -a audio/*.h %buildroot%_includedir/tgvoip/audio/
cp -a video/*.h %buildroot%_includedir/tgvoip/video/

%files
%_libdir/libtgvoip.so.%soname

%files devel
%doc UNLICENSE
%_libdir/libtgvoip.so
%dir %_includedir/tgvoip/
%_includedir/tgvoip/*.h
%_includedir/tgvoip/json11.hpp
%_includedir/tgvoip/audio/
%_includedir/tgvoip/video/
%_pkgconfigdir/%name.pc

%changelog
* Tue Jan 15 2019 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt1
- new version 2.4.2 (with rpmrb script)

* Tue Dec 11 2018 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt2
- real 2.4 release (tagged release from grishka@)

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt1
- new version 2.4 - merge with 78e584c443b93ce2 (used in TG 1.5.0)
- pack include/tgvoip/video/

* Mon Dec 10 2018 Vitaly Lipatov <lav@altlinux.ru> 2.3-alt1
- new version 2.3 (with rpmrb script)

* Sat Sep 08 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.4-alt1
- new version (2.2.4) from upsteam git
 + added --enable-audio-callback to configure
 + fixes

* Wed Aug 29 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt2
- rebuild with openssl 1.1

* Thu Aug 23 2018 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt1
- new verson (2.2.2)
 + Refactored audio I/O to allow sharing a common context between input and output
 + Rewritten periodic operation handling to use a "run loop" thingy
 + Fixed a bunch of compiler warnings (closes #13)

* Fri Jul 13 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version (2.1.1) with rpmgs script
 + Enabled delay-agnostic AEC on Windows & Linux, it seems to make a difference after all (telegramdesktop/tdesktop#4881)
 + Fixed PulseAudio crashes, at least I hope so (closes #42)
 + Fixed parsing of floating-point server config values in some locales in Linux

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 2.1-alt1
- build new version

* Mon May 28 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2.18t-alt2
- Sync with telegram submodule: Update libtgvoip to fix a possible crash

* Sun May 27 2018 Vitaly Lipatov <lav@altlinux.ru> 1.2.18t-alt1
- build new version (latests code from tdesktop)

* Thu Dec 14 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.2.1-alt1
- update to last git commit https://github.com/telegramdesktop/libtgvoip tdesktop

* Sun Jul 23 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.1.2-alt1
- add pkgconfig file

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.1.1-alt1
- update to last git commit
- fix soname

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt2
- rebuild with debuginfo (ALT bug 33544)

* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt1
- initial build for ALT Sisyphus
