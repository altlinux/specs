Name: libxdg-basedir
Version: 1.1.1
Release: alt1

Summary: This library implements functions to list the directories according to the specification and provides a few higher-level functions for use with the specification
License: MIT
Group: System/Libraries
Url: http://n.ethz.ch/~nevillm/download/%name/
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

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
%patch0 -p1

%build
%configure
make

%install
%makeinstall_std

%files
%_libdir/%{name}.so.*

%files devel
%_pkgconfigdir/%name.pc
%_libdir/%{name}.so
%_includedir/*

%changelog
* Mon Oct 25 2010 Terechkov Evgenii <evg@altlinux.org> 1.1.1-alt1
- 1.1.1
- Spec cleanup

* Sat Dec 19 2009 Terechkov Evgenii <evg@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Sun Apr 26 2009 Terechkov Evgenii <evg@altlinux.ru> 1.0.0-alt1
- Initial build for ALT Linux Sisyphus
