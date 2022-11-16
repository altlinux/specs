%define _unpackaged_files_terminate_build 1

Name: libtclap
Version: 1.2.5
Release: alt1
Summary: Templatized C++ Command Line Parser Library
Url: http://tclap.sourceforge.net/
License: MIT
Group: System/Libraries

Source: %name-%version.tar

BuildRequires: gcc-c++

%description
TCLAP is a small, flexible library that provides a simple interface for
defining and accessing command line arguments. It was intially inspired
by the user friendly CLAP libary. The difference is that this library is
templatized, so the argument class is type independent.
Type independence avoids identical-except-for-type objects,
such as IntArg, FloatArg, and StringArg. While the library is not
strictly compliant with the GNU or POSIX standards, it is close.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
TCLAP is a small, flexible library that provides a simple interface for
defining and accessing command line arguments. It was intially inspired
by the user friendly CLAP libary. The difference is that this library is
templatized, so the argument class is type independent.
Type independence avoids identical-except-for-type objects,
such as IntArg, FloatArg, and StringArg. While the library is not
strictly compliant with the GNU or POSIX standards, it is close.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
TCLAP is a small, flexible library that provides a simple interface for
defining and accessing command line arguments. It was intially inspired
by the user friendly CLAP libary. The difference is that this library is
templatized, so the argument class is type independent.
Type independence avoids identical-except-for-type objects,
such as IntArg, FloatArg, and StringArg. While the library is not
strictly compliant with the GNU or POSIX standards, it is close.

%prep
%setup

%build
%configure

%make_build

%install
%makeinstall

%check
%make -j1 check

%files devel
%doc COPYING README
%_includedir/tclap
%_pkgconfigdir/*.pc

%files doc
%_defaultdocdir/tclap

%changelog
* Wed Nov 16 2022 Leontiy Volodin <lvol@altlinux.org> 1.2.5-alt1
- New version.

* Mon Jun 28 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2.4-alt1
- Updated to upstream version 1.2.4.
- Enabled tests.
- Packaged documentation.

* Wed Nov 02 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.1-alt1
- first build
