%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define	oname emulationstation

Summary: A cross-platform graphical front-end for emulators
Name: emulationstation-batocera
Epoch: 1
Version: 39
Release: alt17.gitc3d5c67
License: MIT
Group: Emulators
Url: https://github.com/Maks1mS/batocera-emulationstation

Source0: %{name}-%{version}.tar.gz
Source1: es_icon.png
# Sample config file
Source2: es_systems.cfg
Source3: themes.tar.gz
Source4: run_emulationstation.sh

Patch0: 0001-Switch-to-system-version-of-Pugixml.patch

BuildRequires(Pre):  rpm-macros-cmake rpm-build-python3
BuildRequires:  libalsa-devel
BuildRequires:  boost-devel
BuildRequires:  cmake gcc-c++
BuildRequires:  eigen3-devel rapidjson-devel
BuildRequires:  libfreeimageplus-devel libfreeimage-devel
BuildRequires:  libfreetype-devel
BuildRequires:  gcc-c++ cmake
BuildRequires:  libSDL2-devel
BuildRequires:  boost-devel
BuildRequires:  libcurl-devel libvlc-devel
BuildRequires:  libpugixml-devel
BuildRequires:  libcec-devel libudev-devel
BuildRequires:  libSDL2-devel libSDL2_mixer-devel
BuildRequires:  libglvnd-devel
BuildRequires:  pkgconfig(sdbus-c++)

Conflicts: emulationstation
Obsoletes: emulationstation

%description
A graphical and themeable front-end for emulators with controller navigation:
it allows you to access all your favorite games in one place, even without a
keyboard!
WARNING: Before running this program you will have customize the provided
sample system config file, according to the SYSTEMS.md instructions. If you
forget to do this, the program will not run at all or will crash.

This is version of original ES from Batocera project.

%prep
%setup -qn %{name}-%{version} -a 3

%patch0 -p1

# Fix perms
chmod 0755 resources/help

%build

cmake . \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DDISABLE_KODI=1 \
    -DENABLE_FILEMANAGER=0 \
    -DEXPERIMENTAL_COMMON_LINUX=1 \
    -DUSE_SYSTEM_PUGIXML=1 -DCEC=0 \
    -DCMAKE_CXX_STANDARD=20 \
    -DCMAKE_CXX_STANDARD_REQUIRED=ON \
%ifarch aarch64
    -DUSE_GLES2=1
%else
    -DUSE_GL=1
%endif

%make_build

%install
%makeinstall_std PREFIX=%_prefix

mkdir -p %{buildroot}%{_datadir}/%{name}/resources
cp -r resources/* %{buildroot}%{_datadir}/%{name}/resources/

# Install our stuff: icon and sample config file
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/gamelists
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/es_icon.png
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}/es_systems.cfg
install -m 0775 %{SOURCE4} %{buildroot}%{_bindir}/run_emulationstation

# Install themes
cp -R ./themes %{buildroot}%{_datadir}/%{name}/

# Provide a .desktop file
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{oname}
GenericName=%{oname}
Comment= A cross-platform graphical front-end for emulators
Comment[it]= Un front-end grafico per emulatori multi-piattaforma
Comment[ru]= Кросс-плаформенная графическая оболочка для эмуляторов
Exec=run_emulationstation
Icon=es_icon
StartupNotify=true
Terminal=false
Type=Application
Categories=Game;Simulation;
EOF

rm -rf %{buildroot}%{_includedir}

%find_lang emulationstation2

%files -f emulationstation2.lang
%doc GAMELISTS.md LICENSE.md README.md SYSTEMS.md THEMES.md
%dir %{_datadir}/%{name}
%dir %{_sysconfdir}/%{name}/gamelists/
%dir %{_datadir}/%{name}/themes/
%dir %{_datadir}/%{name}/themes/simple/
%config(noreplace) %{_datadir}/%{name}/themes/simple/*
%config(noreplace) %{_sysconfdir}/%{name}/es_systems.cfg
%{_bindir}/%oname
%{_bindir}/run_emulationstation
%{_datadir}/%{name}/
%{_datadir}/pixmaps/es_icon.png
%{_datadir}/applications/%{name}.desktop
%_libexecdir/libid3v2.a

%changelog
* Wed May 27 2026 Artyom Bystrov <arbars@altlinux.org> 1:39-alt17.gitc3d5c67
- Fixed build with GCC15
- Set bluetooth behavior (at last time, i hope).

* Fri Apr 17 2026 Artyom Bystrov <arbars@altlinux.org> 1:39-alt16.gitc3d5c67
- Fixed bluetooth behavior

* Tue Oct 28 2025 Artyom Bystrov <arbars@altlinux.org> 1:39-alt15.gitc3d5c67
- Update run script

* Mon Oct 27 2025 Artyom Bystrov <arbars@altlinux.org> 1:39-alt14.gitc3d5c67
- Update run script

* Sun Oct 26 2025 Artyom Bystrov <arbars@altlinux.org> 1:39-alt13.gitc3d5c67
- Add quotes for every variabels
- Change wrong variable for themes path

* Fri Oct 24 2025 Artyom Bystrov <arbars@altlinux.org> 1:39-alt12.gitc3d5c67
- Fix definitions of variable in run script

* Thu Oct 23 2025 Artyom Bystrov <arbars@altlinux.org> 1:39-alt11.gitc3d5c67
- Fix mistype in run script

* Tue Oct 21 2025 Artyom Bystrov <arbars@altlinux.org> 1:39-alt10.gitc3d5c67
- Add path for log directory
- Update theme adding scheme

* Mon Oct  6 2025 Artyom Bystrov <arbars@altlinux.org> 1:39-alt9.gitc3d5c67
- Fix path for copying themes in run_emulationstation

* Thu Oct  2 2025 Artyom Bystrov <arbars@altlinux.org> 1:39-alt8.gitc3d5c67
- Fix path for copying themes

* Thu Oct  2 2025 Artyom Bystrov <arbars@altlinux.org> 1:39-alt7.gitc3d5c67
- Add check of es_systems.cfg
- Update es_systems.cfg

* Wed Oct  1 2025 Artyom Bystrov <arbars@altlinux.org> 1:39-alt6.gitc3d5c67
- WiFi settings is working now

* Tue Sep 30 2025 Artyom Bystrov <arbars@altlinux.org> 1:39-alt5.gitc3d5c67
- Fix name of API

* Mon Sep 29 2025 Artyom Bystrov <arbars@altlinux.org> 1:39-alt4.gitc3d5c67
- Fix defining custom paths

* Tue Sep 23 2025 Artyom Bystrov <arbars@altlinux.org> 1:39-alt3.gitc3d5c67
- Minor cleanup
- Fix path to resource dir in run_emulationstation script

* Tue Sep 23 2025 Artyom Bystrov <arbars@altlinux.org> 1:39-alt2.gitc3d5c67
- Update sources

* Tue Aug 26 2025 Artyom Bystrov <arbars@altlinux.org> 1:39-alt1.gitc3d5c67
- Update sources
- Fix bluetooth control

* Fri Mar 21 2025 Artyom Bystrov <arbars@altlinux.org> 1:39-alt1.git07e87f4
- Switch to fork of Maks1mS@ with next improvements:
- Add basic common linux API system
- Fixed query battery information for gaming handhelds
- Switch power options on systemctl base
- Basic bluetooth control support
- Add TIMEZONES support
- Update pugixml patch

* Mon Sep 2 2024 Artyom Bystrov <arbars@altlinux.org> 39-alt1.gitde2cc99
- Initial release