
Name: extra-cmake-modules
Version: 1.6.0
Release: alt0.1

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
BuildRequires: cmake qt5-tools
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
* Fri Jan 16 2015 Sergey V Turchin <zerg@altlinux.org> 1.6.0-alt0.1
- initial build
