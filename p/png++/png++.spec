Name: png++
Version: 0.2.9
Release: alt1

Summary: C++ wrapper for libpng
License: BSD
Group: Development/C++

Url: http://www.nongnu.org/pngpp/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: http://download.savannah.gnu.org/releases/pngpp/%name-%version.tar.gz

BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: libpng-devel

%description
PNG++ aims to provide simple yet powerful C++ interface to libpng, the
PNG reference implementation library.

%package -n lib%name
Summary: C++ wrapper for libpng
Group: Development/C++
BuildArch: noarch

%description -n lib%name
PNG++ aims to provide simple yet powerful C++ interface to libpng, the
PNG reference implementation library.

%package -n lib%name-devel
Summary: C++ wrapper for libpng
Group: Development/C++
BuildArch: noarch
Requires: lib%name = %EVR

%description -n lib%name-devel
PNG++ aims to provide simple yet powerful C++ interface to libpng, the
PNG reference implementation library.

%prep
%setup

%build
%make docs

%install
%make install PREFIX=%buildroot%_prefix
%__rm -rf %buildroot%_docdir/%name

%files -n lib%name
%doc %_docdir/%name-%version

%files -n lib%name-devel
%_includedir/%name

%changelog
* Sun Jan 10 2016 Nazarov Denis <nenderus@altlinux.org> 0.2.9-alt1
- Initial release for ALT Linux

