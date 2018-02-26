
Name: svox-pico
Version: 20120212
Release: alt1
License: Apache License
Group: Sound
Summary: Text-To-Speech engine from Android project
URL: http://android.googlesource.com/platform/external/svox.git
Packager: Michael Pozhidaev <msp@altlinux.ru>

BuildRequires: libpopt-devel

Source0: %name-%version.tar
Patch1: %name-20120212-arch-x86_64.patch

%description
Text-To-Speech engine from Android project

%prep
%setup -q
%patch1 -p1
%build
cd pico
./autogen.sh
%configure
%make_build
cd ..

%install
cd pico
make DESTDIR=%buildroot install
cd ..

%files
%_bindir/*
%_includedir/*
%_libdir/libttspico*
%_datadir/pico

%changelog
* Sun Feb 12 2012 Michael Pozhidaev <msp@altlinux.ru> 20120212-alt1
- Initial ALT Linux release

