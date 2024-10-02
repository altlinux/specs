%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%define	oname emulationstation

Summary: A cross-platform graphical front-end for emulators
Name: emulationstation-batocera
Version: 39
Release: alt1.gitde2cc99
License: MIT
Group: Emulators
Url: https://github.com/batocera-linux/batocera-emulationstation

Source0: %{oname}-%{version}.tar.gz
Source1: es_icon.png
# Sample config file
Source2: es_systems.cfg
Source3: themes.tar.gz

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

Conflicts: emulationstation

%description
A graphical and themeable front-end for emulators with controller navigation:
it allows you to access all your favorite games in one place, even without a
keyboard!
WARNING: Before running this program you will have customize the provided
sample system config file, according to the SYSTEMS.md instructions. If you
forget to do this, the program will not run at all or will crash.

This is version of original ES from Batocera project.

%prep
%setup -qn %{oname}-%{version} -a 3

# Fix perms
chmod 0755 resources/help

%build

cmake . \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DDISABLE_KODI=1 \
    -DENABLE_FILEMANAGER=0 \
    -DUSE_SYSTEM_PUGIXML=1 -DCEC=0 \
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

# Install themes
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/themes/simple
cp -R ./themes %{buildroot}%{_sysconfdir}/%{name}/

# Provide a .desktop file
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{oname}
GenericName=%{oname}
Comment= A cross-platform graphical front-end for emulators
Comment[it]= Un front-end grafico per emulatori multi-piattaforma
Comment[ru]= Кросс-плаформенная графическая оболочка для эмуляторов
Exec=%{oname}
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
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/gamelists/
%dir %{_sysconfdir}/%{name}/themes/
%dir %{_sysconfdir}/%{name}/themes/simple/
%config(noreplace) %{_sysconfdir}/%{name}/themes/simple/*
%config(noreplace) %{_sysconfdir}/%{name}/es_systems.cfg
%{_bindir}/%oname
%{_datadir}/%{name}/
%{_datadir}/pixmaps/es_icon.png
%{_datadir}/applications/%{name}.desktop
%_libexecdir/libid3v2.a

%changelog
* Mon Sep 2 2024 Artyom Bystrov <arbars@altlinux.org> 39-alt1.gitde2cc99
- Initial release