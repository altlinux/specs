Name: libtgvoip
Version: 0.4.1
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

# https://bugzilla.altlinux.org/show_bug.cgi?id=33544
%add_debuginfo_skiplist %_libdir

%description
VoIP library for Telegram clients


%package devel
Group: Development/Other
Summary: Development files for %name

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.


%prep
%setup
%__subst "s|-msse2|-msse2 -I%_includedir/pulse|g" libtgvoip.gyp
%__subst "s|static_library|shared_library|g" libtgvoip.gyp
%__subst "s|.*dependencies.*|'link_settings': { 'libraries': ['-ldl', '-lpthread', '-lopus', '-lcrypto'], },|g" libtgvoip.gyp

%build
# --no-parallel due gyp in hasher:
#    sl = self._semlock = _multiprocessing.SemLock(kind, value, maxvalue)
#OSError: [Errno 38] Function not implemented
gyp --depth=. --no-parallel \
	-Dlinux_path_opus_include=%_includedir/opus/
%make_build CXXFLAGS="%optflags -std=gnu++14" CFLAGS="%optflags" V=1

%install
install -m644 -D out/Debug/lib.target/libtgvoip.so %buildroot%_libdir/libtgvoip.so.0
mkdir -p %buildroot%_includedir/tgvoip/audio/
cp -a *.h %buildroot%_includedir/tgvoip/
cp -a audio/*.h %buildroot%_includedir/tgvoip/audio/

%files
%_libdir/libtgvoip.so.0

%files devel
%_libdir/libtgvoip.so
%dir %_includedir/tgvoip/
%_includedir/tgvoip/*.h
%_includedir/tgvoip/audio/

%changelog
* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt1
- initial build for ALT Sisyphus
