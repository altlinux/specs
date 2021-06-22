Name: symmetrica
Version: 3.0.1
Release: alt1

Summary: Symmetrica is a C library developed by Lehrstuhl Mathematik II of the University of Bayreuth 
License: MIT  
Group: System/Libraries
URL: https://gitlab.com/sagemath/symmetrica/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires: gcc-c++

%description
Symmetrica is a C library developed by Lehrstuhl Mathematik II of the
University of Bayreuth.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
%summary.

%prep
%setup

%build
%autoreconf
%configure --disable-static --disable-silent-rules
%make_build

%install
%makeinstall_std
rm -f %buildroot%_defaultdocdir/symmetrica/README.md

%check
%make_build check

%files
%doc README.md
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%changelog
* Tue Jun 22 2021 Andrey Cherepanov <cas@altlinux.org> 3.0.1-alt1
- Initial build in Sisyphus.
