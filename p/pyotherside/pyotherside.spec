%define _unpackaged_files_terminate_build 1

%ifarch %arm
%def_without check
%endif

Name: pyotherside
Version: 1.6.1
Release: alt1

Summary: A Qt plugin providing access to a Python 3 interpreter from QML
License: ISC
Group: System/Libraries
Url: https://thp.io/2011/pyotherside/
Vcs: https://github.com/thp/pyotherside

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-qt5
BuildRequires: python3-dev
BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-svg-devel
BuildRequires: xvfb-run

%description
A Qt plugin providing access to a Python 3 interpreter from QML for creating
asynchronous mobile and Desktop UIs with Python.

%prep
%setup

%build
%qmake_qt5 CONFIG+=nostrip pyotherside.pro
%make_build

%install
%install_qt5
%make_install

rm -f %buildroot%_qt5_datadir/tests/qtquicktests/qtquicktests

%check
xvfb-run ./tests/tests

%files
%doc LICENSE examples
%_qt5_qmldir/*

%changelog
* Mon May 20 2024 Anton Zhukharev <ancieg@altlinux.org> 1.6.1-alt1
- Updated to 1.6.1.

* Wed Sep 28 2022 Anton Zhukharev <ancieg@altlinux.org> 1.6.0-alt1
- 1.5.9 -> 1.6.0

* Sat Jul 23 2022 Anton Zhukharev <ancieg@altlinux.org> 1.5.9-alt1
- initial build for Sisyphus

