Name: rack
Version: 2.4.1
Release: alt1

Summary: VCV virtual Eurorack host
License: GPLv3
Group: Sound
Url: https://github.com/VCVRack/Rack

ExclusiveArch: aarch64 x86_64

Source0: %name-%version-%release.tar
Source1: deps-%version-%release.tar

BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(glew)
BuildRequires: pkgconfig(glfw3)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(jansson)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(speexdsp)

%package devel
Summary: VCV virtual Eurorack host SDK
Group: Development/C++
Requires: gcc-c++ jq
Requires: pkgconfig(alsa)
Requires: pkgconfig(glew)
Requires: pkgconfig(glfw3)
Requires: pkgconfig(jack)
Requires: pkgconfig(jansson)
Requires: pkgconfig(libarchive)
Requires: pkgconfig(libcurl)
Requires: pkgconfig(libpulse)
Requires: pkgconfig(libssl)
Requires: pkgconfig(libzstd)
Requires: pkgconfig(samplerate)
Requires: pkgconfig(speexdsp)

%description
Rack is the host application for the VCV virtual Eurorack
modular synthesizer platform.

%description devel
Rack is the host application for the VCV virtual Eurorack
modular synthesizer platform.
This package contains Rack plugin SDK.

%prep
%setup -a1

%build
%make_build -C dep
%make_build

%install
install -pm0755 -D rack %buildroot%_bindir/rack

mkdir -p %buildroot%_libdir/rack
install -pm0644 librack.so %buildroot%_libdir/librack.so.0.0.0
ln -s librack.so.0.0.0 %buildroot%_libdir/librack.so.0
ln -s librack.so.0 %buildroot%_libdir/librack.so

install -pm0644 -D Core.json %buildroot%_datadir/rack/Core.json
install -pm0644 template.vcv %buildroot%_datadir/rack
cp -a res %buildroot%_datadir/rack

mkdir -p %buildroot%_datadir/rack/sdk/dep
cp -prv include %buildroot%_datadir/rack/sdk
cp -prv dep/include %buildroot%_datadir/rack/sdk/dep
cp -pv *.mk %buildroot%_datadir/rack/sdk

%files
%doc LICENSE* README*
%_bindir/rack
%_libdir/*.so.*
%_libdir/rack
%_datadir/rack
%exclude %_datadir/rack/sdk

%files devel
%_libdir/librack.so
%_datadir/rack/sdk

%changelog
* Wed Feb 21 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.1-alt1
- initial
