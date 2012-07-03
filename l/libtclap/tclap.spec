Name: libtclap
Version: 1.2.1 
Release: alt1

Summary: Templatized C++ Command Line Parser Library
Url: http://tclap.sourceforge.net/
Source: %name-%version.tar
License: BSDlike 

BuildRequires: gcc-c++

Group: System/Libraries

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
Group: Development/C
Requires: %name = %version-%release

%description devel
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

%files

%files devel
%doc COPYING README
%_includedir/tclap
%_pkgconfigdir/*.pc


%changelog
* Wed Nov 02 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.2.1-alt1
- first build

