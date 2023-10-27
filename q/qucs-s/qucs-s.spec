# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: qucs-s
Version: 2.1.0
Release: alt3

Summary: Circuit simulator
License: GPL-2.0-or-later
Group: Education
Url: https://github.com/ra3xdh/qucs_s

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Buildrequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: flex
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-svg-devel
BuildRequires: rpm-build-python3
Requires: %name-data = %EVR
#Requires: qucs
Requires: ngspice
# https://bugzilla.altlinux.org/47318
Requires: qt6-svg
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
%patch -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DUPDATE_TRANSLATIONS=On
%cmake_build

%install
%cmake_install

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
* Fri Oct 27 2023 Anton Midyukov <antohami@altlinux.org> 2.1.0-alt3
- 2.1.0 release
- build with qt6

* Wed Oct 18 2023 Anton Midyukov <antohami@altlinux.org> 2.1.0-alt2.20231018
- update russian translation
- use git diff instead patches
- remove outdated patch

* Wed Oct 18 2023 Anton Midyukov <antohami@altlinux.org> 2.1.0-alt1.20231017
- new snapshot with update russian translations

* Sun Aug 20 2023 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- New version 2.0.0.
- Update Url.

* Thu Jun 08 2023 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- New version 1.1.0.

* Tue Apr 25 2023 Anton Midyukov <antohami@altlinux.org> 1.0.2-alt1
- New version 1.0.2.

* Sun Feb 05 2023 Anton Midyukov <antohami@altlinux.org> 1.0.1-alt1
- new version 1.0.1

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
