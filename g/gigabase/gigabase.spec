Summary: GigaBASE is object-relational embedded database engine for C++ applications.
Name: gigabase
Version: 3.69
Release: alt1.1
License: MIT
Group: Emulators
Packager: Boris Savelev <boris@altlinux.org>
Url: http://sourceforge.net/projects/%name/
Source: http://download.sourceforge.net/sourceforge/%name/%name-%version.tar.gz
Patch: %name-install.patch

# Automatically added by buildreq on Mon May 18 2009
BuildRequires: gcc-c++ perl-DBI perl-devel

%description
GigaBASE is object-relational embedded database engine for C++ applications.
It provides SQL-like query language, smart C++ interface (loading objects instead of tupples),
transaction based on shadowing page algorithm (no separate log file and very fast.

%package -n lib%name
Summary: %name shared library
Group: System/Libraries

%description -n lib%name
This package contains %name shared library.

%package -n lib%name-devel
Summary: %name development files
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains %name development files.

%package -n perl-%name
Summary: %name perl module
Group: Development/Perl

%description -n perl-%name
This package contains %name perl module files.

%package -n perl-DBD-%name
Summary: %name perl DBD module
Group: Development/Perl

%description -n perl-DBD-%name
This package contains %name perl DBD module files.

%prep
%setup
%patch0 -p0

%build
%define _without_test 1
%configure
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build
for d in Perl* ; do
pushd $d
%perl_vendor_build
popd
done

%install
%makeinstall_std
for d in Perl* ; do
pushd $d
%perl_vendor_install
popd
done

%files
%doc GigaBASE.htm
%_bindir/subsql-gb

%files -n lib%name
%doc docs/
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/%name

%files -n perl-%name
%perl_vendor_privlib/G*

%files -n perl-DBD-%name
%perl_vendor_privlib/DBD/G*

%changelog
* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.69-alt1.1
- Removed bad RPATH

* Mon May 18 2009 Boris Savelev <boris@altlinux.org> 3.69-alt1
- initial build

