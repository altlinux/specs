Name:           wf-recorder
Version:        0.4.1
Release:        alt2
Summary:        Utility program for screen recording of wlroots-based compositors
License:        MIT
Group:          Video
URL:            https://github.com/ammen99/wf-recorder
Source0:        %{name}-%{version}.tar
Source2:        wf_record.sh
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.54.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14

%description
Utility program for screen recording of wlroots-based compositors
(more specifically, those that support wlr-screencopy-v1 and xdg-output).

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

#install start script
install -D -m0755 %SOURCE2 %buildroot%_bindir/

# install "start button"
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name-start.desktop << EOF
[Desktop Entry]
Name=Start screen record
Name[ru]=Начать запись экрана
Comment=start button for wf-recorder
Exec=wf_record.sh &
Icon=record-desktop
Terminal=false
Type=Application
Categories=Video;
OnlyShowIn=Phosh;
X-Purism-FormFactor=Workstation;Mobile;
EOF

# install "stop button"
cat > %buildroot%_desktopdir/%name-stop.desktop << EOF
[Desktop Entry]
Name=Stop screen record
Name[ru]=Остановить запись экрана
Comment=stop button for wf-recorder
Exec=wf_record.sh &
Icon=media-playback-stop
Terminal=false
Type=Application
Categories=Video;
OnlyShowIn=Phosh;
X-Purism-FormFactor=Workstation;Mobile;
EOF


%files
%doc README.md LICENSE
%_bindir/wf-recorder
%_bindir/wf_record.sh
%_desktopdir/%name-start.desktop
%_desktopdir/%name-stop.desktop
%{_mandir}/man?/%{name}*

%changelog
* Fri Nov 10 2023 Artyom Bystrov <arbars@altlinux.org> 0.4.1-alt2
- Add run script and "buttons" to run and stop record


* Sun Nov  5 2023 Artyom Bystrov <arbars@altlinux.org> 0.4.1-alt1
- Initial commit for Sisyphus