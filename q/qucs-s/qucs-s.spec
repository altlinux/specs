# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: qucs-s
Version: 1.0.0
Release: alt1

Summary: Circuit simulator
License: GPLv2+
Group: Education
Url: https://github.com/ra3xdh/qucs

Source: %name-%version.tar
Patch: fix_S4Q_workdir.patch

Buildrequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-script-devel
BuildRequires: qt5-svg-devel
BuildRequires: rpm-build-python3
Requires: %name-data = %EVR
#Requires: qucs
Requires: ngspice
%add_python3_path %_datadir/%name/python

Obsoletes: qucs-s-data =< %EVR
Provides: qucs-s-data = %EVR

%description
Qucs-S is spin-off of Qucs.

Qucs is an integrated circuit simulator which means you are
able to setup a circuit with a graphical user interface (GUI)
and simulate the large-signal, small-signal and noise
behaviour of the circuit. After that simulation has finished
you can view the simulation results on a presentation page or
window.

%prep
%setup
%autopatch -p1

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
%doc AUTHORS COPYING README.md README_qucs
%_bindir/*
%_desktopdir/*
%_datadir/%name
%_iconsdir/hicolor/*/apps/*
%_man1dir/*

%changelog
* Mon Oct 31 2022 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Sun Jul 03 2022 Anton Midyukov <antohami@altlinux.org> 0.0.24-alt1
- new version 0.0.24

* Fri Mar 18 2022 Anton Midyukov <antohami@altlinux.org> 0.0.23-alt2
- fix S4Q_workdir variable with first running (Closes: 42122)

* Mon Feb 21 2022 Anton Midyukov <antohami@altlinux.org> 0.0.23-alt1
- new version 0.0.23
- drop subpackage qucs-s-data
- do not require qucs (qucs needed qt4, qucsator is not default more)

* Fri May 21 2021 Anton Midyukov <antohami@altlinux.org> 0.0.22-alt1
- new version 0.0.22

* Fri Nov 02 2018 Anton Midyukov <antohami@altlinux.org> 0.0.21-alt1
- new version 0.0.21

* Fri Jul 13 2018 Anton Midyukov <antohami@altlinux.org> 0.0.20-alt2.1
- rebuilt for aarch64

* Tue Nov 14 2017 Anton Midyukov <antohami@altlinux.org> 0.0.20-alt2
- Fix path to xspice

* Thu Nov 02 2017 Anton Midyukov <antohami@altlinux.org> 0.0.20-alt1
- Initial build for ALT Sisyphus.
