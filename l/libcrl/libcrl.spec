%define soname 0.0
Name: libcrl
Version: 0.1
Release: alt1

Summary: Concurrency Runtime Library for Telegram Desktop

Group: Networking/Instant messaging
License: %gpl3only

Url: https://github.com/telegramdesktop/crl
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/telegramdesktop/crl.git
Source: %name-%version.tar
Source1: crl.gyp

BuildRequires: gyp gcc-c++

BuildRequires(pre): rpm-build-licenses rpm-macros-qt5
BuildRequires: qt5-base-devel

%add_optflags -fPIC

%description
Concurrency Runtime Library for Telegram Desktop.

%package devel
Group: Development/Other
Summary: Development files for %name

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
cp %SOURCE1 .

%build
# --no-parallel due gyp in hasher:
#    sl = self._semlock = _multiprocessing.SemLock(kind, value, maxvalue)
#OSError: [Errno 38] Function not implemented
gyp --depth=. --no-parallel
%make_build CXXFLAGS="%optflags -std=c++17 $(pkg-config --cflags Qt5Core)" CFLAGS="%optflags" V=1

cat <<EOF >%name.pc
includedir=%_includedir

Name: %name
Description: %summary
URL: %url
Version: %version
Requires:
Conflicts:
Libs: -lcrl
Libs.private:
Cflags: -I\${includedir}/%name
EOF

%install
install -m644 -D out/Default/lib.target/%name.so.%soname %buildroot%_libdir/%name.so.%soname
install -m644 -D %name.pc %buildroot%_pkgconfigdir/%name.pc
ln -s %name.so.%soname %buildroot%_libdir/%name.so
for i in "" qt dispatch common ; do
    mkdir -p %buildroot%_includedir/%name/crl/$i
    cp -a src/crl/$i/*.h %buildroot%_includedir/%name/crl/$i/
done

%files
%_libdir/%name.so.%soname

%files devel
%_libdir/%name.so
%_includedir/%name/
%_pkgconfigdir/%name.pc

%changelog
* Sat May 26 2018 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus
