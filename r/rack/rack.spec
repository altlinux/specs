Name: rack
Version: 2.5.2
Release: alt1

Summary: VCV virtual Eurorack host
License: GPLv3
Group: Sound
Url: https://github.com/VCVRack/Rack

ExclusiveArch: aarch64 x86_64

Source0: %name-%version-%release.tar
Source1: deps-%version-%release.tar

BuildRequires: cmake gcc-c++ jq
BuildRequires: /usr/bin/convert
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

convert icon.ico icon.png
install -pm0644 -D icon-0.png %buildroot%_iconsdir/hicolor/32x32/apps/rack.png
install -pm0644 -D icon-1.png %buildroot%_iconsdir/hicolor/64x64/apps/rack.png

cat > rack.desktop << 'EOF'
[Desktop Entry]
Name=VCV Rack
Comment=Virtual Eurorack host
Exec=rack
Icon=rack
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Midi;X-Jack;
EOF

install -pm0644 -D rack.desktop %buildroot%_desktopdir/rack.desktop

%files
%doc LICENSE* README*
%_bindir/rack
%_libdir/*.so.*
%_libdir/rack
%_datadir/rack
%_iconsdir/*/*/*/*.png
%_desktopdir/rack.desktop
%exclude %_datadir/rack/sdk

%files devel
%_libdir/librack.so
%_datadir/rack/sdk

%changelog
* Mon May 13 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.5.2-alt1
- 2.5.2 released

* Thu Apr 18 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.5.1-alt1
- 2.5.1 released

* Tue Apr 09 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.5.0-alt1
- 2.5.0 released

* Fri Mar 15 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.4.1-alt3
- rack sdk tweaks

* Wed Feb 28 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.1-alt2
- desktop entry packaged

* Wed Feb 21 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.1-alt1
- initial
