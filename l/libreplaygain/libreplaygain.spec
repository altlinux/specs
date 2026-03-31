Name: libreplaygain
Version: r483
Release: alt2.svn20131021

Summary: Analyzes input samples and give the recommended dB change
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://www.musepack.net/

# http://svn.musepack.net/libreplaygain/
Source: %name-%version.tar

BuildRequires(Pre): rpm-build-cmake

%description
ReplayGainAnalysis - analyzes input samples and give the recommended dB
change

%package devel
Summary: Development files of %name
Group: Development/C
Requires: %name = %EVR

%description devel
ReplayGainAnalysis - analyzes input samples and give the recommended dB
change

This package contains development files of %name.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
rm -v %buildroot%_libdir/libreplaygain.a

%files
%_libdir/libreplaygain.so.*

%files devel
%_includedir/replaygain
%_libdir/libreplaygain.so

%changelog
* Mon Mar 16 2026 Ulysses Apokin <ulysses@altlinux.org> r483-alt2.svn20131021
- Fixed FTBFS.

* Thu Sep 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r483-alt1.svn20131021
- Initial build for Sisyphus
