
Name: extra-cmake-modules
Version: 5.18.0
Release: alt1

Group: Development/Other
Summary: Additional modules for CMake build system
License: BSD
Url: http://community.kde.org/KDE_Core/Platform_11/Buildsystem/FindFilesSurvey

BuildArch: noarch

Requires: cmake

Source: %name-%version.tar

# Automatically added by buildreq on Wed Dec 24 2014 (-bi)
# optimized out: cmake-modules libcloog-isl4 libqt5-core python-base python-devel python-module-BeautifulSoup python-module-PyStemmer python-module-cffi python-module-docutils python-module-google python-module-google-apputils python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-numpy python-module-pyExcelerator python-module-pycparser python-module-pyparsing python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-multiprocessing python-modules-unittest qt5-base-devel qt5-tools
#BuildRequires: cmake python-module-Pillow python-module-Pygments python-module-Reportlab python-module-html5lib python-module-matplotlib python-module-nss python-module-protobuf python-module-pygobject3 python-module-xlwt python-modules-tkinter qt5-tools-devel ruby ruby-stdlibs time
BuildRequires: cmake qt5-tools qt5-tools-devel
BuildRequires: /usr/bin/sphinx-build


%description
Additional modules for CMake build system needed by KDE Frameworks.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_datadir/ECM
%doc README.rst COPYING-CMAKE-SCRIPTS
%doc %_docdir/ECM
%doc %_man7dir/*

%changelog
* Mon Jan 11 2016 Sergey V Turchin <zerg@altlinux.org> 5.18.0-alt1
- new version

* Fri Dec 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.17.0-alt1
- new version

* Wed Nov 18 2015 Sergey V Turchin <zerg@altlinux.org> 5.16.0-alt1
- new version

* Mon Oct 12 2015 Sergey V Turchin <zerg@altlinux.org> 5.15.0-alt1
- new version

* Mon Sep 14 2015 Sergey V Turchin <zerg@altlinux.org> 5.14.0-alt1
- new version

* Wed Aug 19 2015 Sergey V Turchin <zerg@altlinux.org> 5.13.0-alt1
- new version

* Fri Jul 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.12.0-alt1
- new version

* Tue Jun 30 2015 Sergey V Turchin <zerg@altlinux.org> 5.11.0-alt1
- new version

* Mon May 11 2015 Sergey V Turchin <zerg@altlinux.org> 5.10.0-alt1
- new version

* Fri Apr 10 2015 Sergey V Turchin <zerg@altlinux.org> 5.9.0-alt1
- new version

* Mon Apr 06 2015 Sergey V Turchin <zerg@altlinux.org> 1.8.0-alt1
- new version

* Wed Mar 18 2015 Sergey V Turchin <zerg@altlinux.org> 1.8.0-alt0.1
- test

* Mon Feb 16 2015 Sergey V Turchin <zerg@altlinux.org> 1.7.0-alt0.1
- test

* Fri Jan 16 2015 Sergey V Turchin <zerg@altlinux.org> 1.6.0-alt0.1
- initial build
