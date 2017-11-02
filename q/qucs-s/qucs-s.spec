Name: qucs-s
Version: 0.0.20
Release: alt1

Summary: Circuit simulator
License: GPLv2+
Group: Education
Url: https://github.com/ra3xdh/qucs

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Buildrequires (pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ libqt4-devel
Requires: %name-data = %version-%release
Requires: qucs
Requires: ngspice

%description
Qucs-S is spin-off of Qucs.

Qucs is an integrated circuit simulator which means you are
able to setup a circuit with a graphical user interface (GUI)
and simulate the large-signal, small-signal and noise
behaviour of the circuit. After that simulation has finished
you can view the simulation results on a presentation page or
window.

%package data
Group: Education
Summary: Data files for %name, a circuit simulator
Buildarch: noarch

%description data
Data files  for %name, a circuit simulator.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std

for l in $(find %buildroot%_datadir/%name/lang -name \*.qm); do
    echo -n $l | sed 's,.*_\(.*\)\.qm,%%lang\(\1\) ,'
    echo $l | sed "s,%buildroot,,"
done > %name.lang

%files
%_bindir/*
%_desktopdir/*

%files data
%doc AUTHORS COPYING README.md README_qucs
%_datadir/%name
%_iconsdir/hicolor/*/apps/*
%_man1dir/*

%changelog
* Thu Nov 02 2017 Anton Midyukov <antohami@altlinux.org> 0.0.20-alt1
- Initial build for ALT Sisyphus.
