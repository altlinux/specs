# Based on spec file from PCLinuxOS by Agent Smith <ruidobranco@yahoo.com.br>

Name: picodrive
Summary: Megadrive / Genesis / Sega CD / Mega CD / 32X / SMS emulator
Version: 1.99
Release: alt2
License: ALT-Public-Domain
Group: Emulators
Source0: %{name}-%{version}.tar.xz
Source1: %{name}.png

# Patches for adding window scalability support 
# https://github.com/irixxxx/picodrive/issues/70
# Yes, it's buggy, but this better then nothing :)

Patch1: gl_support.patch
Patch2: x86_64-platform.patch

Packager: Artyom Bystrov <arbars@altlinux.org> 
Url:  https://github.com/irixxxx/picodrive

BuildRequires:	libalsa2-devel
BuildRequires:	libGLEW-devel
BuildRequires:	libGLES
BuildRequires:	libglvnd-devel
BuildRequires:	libGLU-devel
BuildRequires:	libcdio-devel
BuildRequires:	libSDL-devel
BuildRequires:	libSDL_net-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:  gcc-c++
BuildRequires:  libGL-devel 
BuildRequires:  libpng-devel
BuildRequires:	zlib-devel
BuildRequires:  zip
Requires: license-list-xml

ExcludeArch: armh

%description

This is yet another Megadrive / Genesis / Sega CD / Mega CD / 32X / SMS
emulator, which was written having ARM-based handheld devices in mind
(such as smartphones and handheld consoles like GP2X and Pandora),
but also runs on non-ARM little-endian hardware too.

PicoDrive requires a real BIOS for Sega CD/Mega CD emulation to work.

US: us_scd1_9210.bin us_scd2_9306.bin SegaCDBIOS9303.bin
EU: eu_mcd1_9210.bin eu_mcd2_9303.bin eu_mcd2_9306.bin
JP: jp_mcd1_9112.bin jp_mcd1_9111.bin

For the standalone emulator they can be placed in ~/.picodrive/ 

Sega CD games must be in the cue / iso format, and the audio tracks must be in WAV format.

%prep
%setup -q 
%patch1 -p1
%patch2 -p1

%build
 ./configure --platform=x86_64
make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -D -m755 PicoDrive  %{buildroot}%{_bindir}/%name
install -d -m 0755 %buildroot%_datadir/pixmaps
install -d -m 0755 %buildroot%_datadir/skin
cp $RPM_BUILD_DIR/%{name}-%{version}/skin/* %{buildroot}%{_datadir}/skin/
install -m 0644 %SOURCE1 %buildroot%_datadir/pixmaps/%{name}.png

install -d %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Name=PicoDrive
GenericName=picodrive
Comment=%{summary}
Exec=picodrive
Icon=%{name}.png
Categories=Game;X-MandrivaLinux-MoreApplications-Emulators;
EOF


%files
%defattr(0755,root,root,0755)
%doc AUTHORS COPYING ChangeLog README
%_bindir/*
%_datadir/pixmaps/*
%_datadir/applications/*
%_datadir/skin/*

%changelog
* Fri Mar 25 2022  Artyom Bystrov <arbars@altlinux.org> 1.99-alt2
- Fix name of exec in desktop file

* Fri Mar 25 2022  Artyom Bystrov <arbars@altlinux.org> 1.99-alt1
- imported from PCLinuxOS srpm.
- Add initial window scaling support (https://github.com/irixxxx/picodrive/issues/70)

* Fri Mar 25 2022  Agent Smith <ruidobranco@yahoo.com.br> 1.93-2pclos2022
- Changed the icon, for a better one.

* Thu Oct 17 2019  Agent Smith <ruidobranco@yahoo.com.br> 1.93-1pclos2019
- Created the package picodrive1.93-1pclos2019.rpm, with latest source.


