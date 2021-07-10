Name: libxdg-basedir
Version: 1.2.3
Release: alt1

Summary: This library implements functions to list the directories according to the specification and provides a few higher-level functions for use with the specification
License: MIT
Group: System/Libraries
URL: https://github.com/devnev/libxdg-basedir
Source: %name-%version.tar

Packager: Evgenii Terechkov <evg@altlinux.org>

%description
Various specifications specify files and file formats. The XDG Base
Directory specification defines where these files should be looked for
by defining one or more base directories relative to which files
should be located.

%package devel
Group: Development/C
Summary: Header files for developing programs using %name
Requires: %name = %version-%release

%description devel
This package contains the header files you need to develop programs
based on %name

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/%{name}.so.*

%files devel
%_pkgconfigdir/%name.pc
%_libdir/%{name}.so
%_includedir/*

%changelog
* Sat Jul 10 2021 Andrey Cherepanov <cas@altlinux.org> 1.2.3-alt1
- New version (ALT #40390).
- Change upstream URL.
- Disable static library build.

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Oct 25 2010 Terechkov Evgenii <evg@altlinux.org> 1.1.1-alt1
- 1.1.1
- Spec cleanup

* Sat Dec 19 2009 Terechkov Evgenii <evg@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Sun Apr 26 2009 Terechkov Evgenii <evg@altlinux.ru> 1.0.0-alt1
- Initial build for ALT Linux Sisyphus
