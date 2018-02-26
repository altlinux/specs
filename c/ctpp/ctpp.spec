Name: ctpp
Version: 2.7.1
Release: alt1
Summary: HTML templater
License: BSD
Group: Development/Other
Url: http://ctpp.havoc.ru/

Packager: Mikhail A Pokidko <pma@altlinux.org>
Source: %name-%version.tar

BuildPreReq: cmake
BuildPreReq: gcc-c++

Requires: lib%name = %version-%release

BuildRequires: openssl-devel

%description
CTPP (CT++) is the tool that divides data processing process and data presentation.
CT++ is the best choice for projects where programmer and HTML maker-up are different persons.

%package -n lib%name-devel
Summary: The CTPP development header files and libraries
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
The ctpp-devel package contains the CTPP devel-library.


%package -n lib%name-devel-static
Summary: The CTPP development static libraries.
Group: Development/Other
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
The ctpp-devel package contains the CTPP static library,

%package -n lib%name
Summary: The shared libraries for ctpp
Group: System/Libraries

%description -n lib%name
The ctpp-libs package provides the essential shared libraries for CTPP templater.
You will need to install this package to use CTPP package.

%prep
%setup -q

%build
%cmake_insource
%make_build VERBOSE=1

%install
%makeinstall_std
mkdir -p %buildroot%_man1dir
mv %buildroot/usr/man/man1/* %buildroot%_man1dir/

%find_lang ctpp2

%files
%doc CHANGES INSTALL NOTTODO LICENSE TODO
%_bindir/*
%_man1dir/*

%files -n lib%name -f ctpp2.lang
%_libdir/libctpp2.so.*

%files -n lib%name-devel
%_libdir/libctpp2.so
%_includedir/ctpp2

%files -n lib%name-devel-static
%_libdir/libctpp2-st.a

%changelog
* Fri Jul 15 2011 Mikhail Pokidko <pma@altlinux.org> 2.7.1-alt1
- v2.7.1

* Mon Mar 28 2011 Mikhail Pokidko <pma@altlinux.org> 2.6.12-alt1
- 2.6.12

* Sun Feb 06 2011 Denis Smirnov <mithraen@altlinux.ru> 2.6.8-alt1
- 2.6.8

* Fri Jun 11 2010 Mikhail A Pokidko <pma@altlinux.org> 2.6.0-alt1
- initial build

