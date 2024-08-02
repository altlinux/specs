%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define	oname es-de
%define _localedir %_datadir/locale
Summary: A cross-platform graphical front-end for emulators
Name: emulationstation
Version: 3.0.3
Release: alt1.gitf9d5b2b1
License: MIT
Group: Emulators
Url: https://gitlab.com/es-de/emulationstation-de

Source0: %{oname}-%{version}.tar.gz
Source1: es_icon.png
# Sample config file
Source2: es_systems.cfg
Source3: themes.tar.gz

Patch0: install.patch
Patch1: pugixml.patch

BuildRequires(Pre):  rpm-macros-cmake rpm-build-python3
BuildRequires:  libalsa-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  eigen3-devel rapidjson-devel
BuildRequires:  libfreeimageplus-devel libfreeimage-devel
BuildRequires:  libfreetype-devel
BuildRequires:  gcc-c++ cmake
BuildRequires:  libSDL2-devel
BuildRequires:  libboost_date_time1.84.0
BuildRequires:  libboost_filesystem1.84.0
BuildRequires:  libboost_locale1.84.0
BuildRequires:  libboost_system1.84.0
BuildRequires:  libcurl-devel libvlc-devel libavcodec-devel libavfilter-devel libavformat-devel libgit2-devel libpoppler-devel libswresample-devel libswscale-devel libpostproc-devel libpoppler-gir-devel libpoppler-cpp-devel
BuildRequires:  libpugixml-devel
BuildRequires:  libcec-devel libudev-devel
BuildRequires:  libSDL2-devel libSDL2_mixer-devel

%description
A graphical and themeable front-end for emulators with controller navigation:
it allows you to access all your favorite games in one place, even without a
keyboard!
WARNING: Before running this program you will have customize the provided
sample system config file, according to the SYSTEMS.md instructions. If you
forget to do this, the program will not run at all or will crash.

This is fork of original ES from Batocera project.

%prep
%setup -qn %{oname}-%{version} -a 3
#%%patch0 -p1
#%%patch1 -p1

# Fix perms
# chmod 0755 resources/help

%build
%cmake
%make -C ./%_cmake__builddir

%install
%makeinstall_std -C ./%_cmake__builddir

# The program need its resource files, but they don't get automatically
# installed: put them in %%{_datadir} and use them (see P0)
mkdir -p %{buildroot}%{_datadir}/%{oname}/resources
cp -r resources/* %{buildroot}%{_datadir}/%{oname}/resources/

# Install our stuff: icon and sample config file
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/gamelists
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/es_icon.png
install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}/es_systems.cfg

# Install themes
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/themes/simple
cp -R ./themes %{buildroot}%{_sysconfdir}/%{name}/


# The sources want to build and install the pugixml library, but we
# don't want it because we already have the system pugixml
# FIXME: Teach cmake to look for a system pugixml library and use it
rm -rf %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_includedir}

%files
%doc README.md THEMES.md
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/gamelists/
%dir %{_sysconfdir}/%{name}/themes/
%dir %{_sysconfdir}/%{name}/themes/modern-es-de/
%dir %{_sysconfdir}/%{name}/themes/slate-es-de/
%dir %{_sysconfdir}/%{name}/themes/simple/
%config(noreplace) %{_sysconfdir}/%{name}/themes/simple/*
%config(noreplace) %{_sysconfdir}/%{name}/themes/modern-es-de/*
%config(noreplace) %{_sysconfdir}/%{name}/themes/slate-es-de/*
%config(noreplace) %{_sysconfdir}/%{name}/es_systems.cfg
%{_bindir}/es-de
%{_bindir}/es-pdf-convert
%{_datadir}/%{oname}/
%{_datadir}/pixmaps/es_icon.png
%{_desktopdir}/org.es_de.frontend.desktop
%{_iconsdir}/hicolor/scalable/apps/org.es_de.frontend.svg
%{_man6dir}/%oname.6.xz
%{_datadir}/metainfo/org.es_de.frontend.appdata.xml
%{_datadir}/pixmaps/org.es_de.frontend.svg

%changelog
* Fri Aug  2 2024 Artyom Bystrov <arbars@altlinux.org> 3.0.3-alt1.gitf9d5b2b1
- update version

* Mon Jul 22 2024 Artyom Bystrov <arbars@altlinux.org> 3.0.3-alt1.gitb8bae01c
- update version

* Fri Jun  7 2024 Artyom Bystrov <arbars@altlinux.org> 2.11.2-alt1
- Initial commit