%define _unpackaged_files_terminate_build 1

Name: liblmdbxx
Version: 1.0.0
Release: alt1

Summary: A C++11 wrapper for LMDB

Group: Development/Other
License: Public Domain
Url: https://github.com/hoytech/lmdbxx

Source: %name-%version.tar
Patch0: lmdbxx-1.0.0-check-without-sanitizers-alt.patch

BuildRequires: gcc-c++ doxygen
BuildRequires: liblmdb-devel >= 0.9.14

%description
This is a comprehensive C++ wrapper for the LMDB_ embedded database library,
offering both an error-checked procedural interface and an object-oriented
resource interface with RAII_ semantics.

%package devel
Summary: Development files for %name
Group: Development/Other

%description devel
The %name-devel package contains C++ header files for developing
applications that use %name.

%prep
%setup
%patch0 -p2

%build
%make_build doxygen

%install
%makeinstall_std PREFIX=%_prefix

%check
%make_build check CFLAGS='%optflags'

%files devel
%doc README.md FUNCTIONS.rst
%doc UNLICENSE
%doc .doxygen/html
%_includedir/*

%changelog
* Tue Sep 14 2021 Paul Wolneykien <manowar@altlinux.org> 1.0.0-alt1
- Update to v1.0.0.

* Fri Jun 26 2020 Paul Wolneykien <manowar@altlinux.org> 0.9.14.1-alt3
- Added patch fixing new pandoc smartypants syntax.

* Tue Dec 04 2018 Paul Wolneykien <manowar@altlinux.org> 0.9.14.1-alt2
- Package the Doxygen docs. Use pandoc for README if available.

* Mon Dec 03 2018 Paul Wolneykien <manowar@altlinux.org> 0.9.14.1-alt1
- Update to version 0.9.14.1.

* Mon Dec 03 2018 Paul Wolneykien <manowar@altlinux.org> 0.9.14.0-alt1
- Initial version (0.9.14.0).
