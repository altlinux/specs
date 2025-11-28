Name: libraul
Version: 2.0.0
Release: alt1

Summary: Realtime Audio Utility Library
License: GPLv3
Group: System/Libraries
Url: https://gitlab.com/drobilla/raul

Source: %name-%version.tar

BuildRequires: gcc-c++ meson

%package devel
Summary: Headers for libraul
Group: Development/C

%description
Raul (Realtime Audio Utility Library) is a C++ utility library primarily aimed
at audio/musical applications.

%description devel
Headers for building software that uses libraul

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files devel
%_includedir/raul-2
%_pkgconfigdir/raul-2.pc

%changelog
* Tue Apr 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.0.0-alt1
- 2.0.0 released

* Thu Aug 06 2020 Pavel Vasenkov <pav@altlinux.org> 0.8.0-alt2
- NMU: set correct python2 executable in shebang and scripts

* Fri Sep 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1
- Version 0.8.0

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.7.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Nov 23 2010 Timur Batyrshin <erthad@altlinux.org> 0.7.0-alt1
- 0.7.0

* Mon Aug 03 2009 Timur Batyrshin <erthad@altlinux.org> 0.5.1-alt1
- Initial build for sisyphus

