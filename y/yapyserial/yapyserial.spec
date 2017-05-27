Name: yapyserial
Version: 0.0
Release: alt1.20170523.1

Summary: Dynamic library for replacing PySerial
Summary(ru_RU.UTF-8): Динамическая библиотека для замены PySerial

License: GPLv2+
Group: Engineering
Url: https://github.com/nucleron/YaPySerial

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Patch: make_install_add.patch
BuildPreReq: gcc-c++

%description
Dynamic library for replacing PySerial (it is noticed
that PySerial does not always correctly determine the
platform).

%description -l ru_RU.UTF-8
Динамическая библиотека для замены PySerial (замечено,
что PySerial не всегда корректно определяет платформу).

%prep
%setup
%patch -p1

%build
%make_build posix CFLAGS+=-fpic

%install
%makeinstall_std LIBDIR=%_libdir

%files
%_libdir/libYaPySerial.so

%changelog
* Sat May 27 2017 Anton Midyukov <antohami@altlinux.org> 0.0-alt1.20170523.1
- Initial build for ALT Linux Sisyphus.
