%define soname 0.0
Name: libtgvoip
Version: 0.4.2.1
Release: alt1

Summary: VoIP library for Telegram clients

Group: Networking/Instant messaging
License: Unlicense

Url: https://github.com/telegramdesktop/libtgvoip
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/telegramdesktop/libtgvoip.git
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
%__subst "s|-msse2|-msse2 -I%_includedir/pulse|g" libtgvoip.gyp
%__subst "s|static_library',|shared_library',\n'product_extension': 'so.%soname',|" libtgvoip.gyp
%__subst "s|.*dependencies.*|'link_settings': { 'libraries': ['-ldl', '-lpthread', '-lopus', '-lcrypto'], },|g" libtgvoip.gyp

# TODO
%if_with webrtc
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
cp -a *.h %buildroot%_includedir/tgvoip/
cp -a audio/*.h %buildroot%_includedir/tgvoip/audio/

%files
%_libdir/libtgvoip.so.%soname

%files devel
%doc UNLICENSE
%_libdir/libtgvoip.so
%dir %_includedir/tgvoip/
%_includedir/tgvoip/*.h
%_includedir/tgvoip/audio/
%_pkgconfigdir/%name.pc

%changelog
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
