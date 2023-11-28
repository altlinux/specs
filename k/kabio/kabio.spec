%def_disable check

Name: kabio
Version: 1.0.2
Release: alt1

Summary: Kabio is a program that recognizes notes from a signal
License: GPL-3.0
Group: Sound
Url: https://codeberg.org/george.bartolomey/kabio

Vcs: https://codeberg.org/george.bartolomey/kabio.git
Source: %url/archive/%version.tar.gz

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5UiTools)
BuildRequires: pkgconfig(aubio) >= 0.4.0
BuildRequires: pkgconfig(jack)
%{?_enable_check:BuildRequires: ctest}

%description
Kabio is a program that recognizes notes from a signal and sends these
to other program with MIDI in real time. This works with JACK Audio
Connection Kit.

%prep
%setup -n %name
# fix build with any jack's
sed -i 's/find_package(Qt5LinguistTools)/&\nfind_package(PkgConfig)\npkg_check_modules(JACK REQUIRED jack)/
        /target_link_libraries/s/jack/${JACK_LDFLAGS}/' CMakeLists.txt

# fix path to qm-files
sed -i '/\.qm/s|build|%_cmake__builddir|' src/resources.qrc

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release
%nil
%cmake_build --parallel 1

%install
%cmake_install
%find_lang %name

%check
%cmake_build -t test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/kabio.png
%_iconsdir/hicolor/*/apps/kabio.svg
%doc README*

%changelog
* Tue Nov 28 2023 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- first build for Sisyphus

