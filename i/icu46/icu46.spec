Name: icu46
Version: 4.6.1
Release: alt1
Epoch: 1
Summary: International Components for Unicode
Group: System/Libraries
License: X License
URL: http://www.icu-project.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: http://download.icu-project.org/files/icu4c/4.6/icu4c-4_6_1-src.tgz

BuildRequires: doxygen gcc-c++ libstdc++-devel

%description
ICU is a C++ and C library that provides robust and full-featured Unicode
support

%package -n libicu46
Summary: International Components for Unicode (libraries)
Group: System/Libraries

%description -n libicu46
ICU is a C++ and C library that provides robust and full-featured Unicode
support. This package contains the runtime libraries for ICU

%prep
%setup -q -n icu

%build
cd source
%configure \
	--disable-samples \
	--disable-static
%make_build

%install
cd source
%make DESTDIR=%buildroot install

%files -n libicu46
%_libdir/*.so.*

%changelog
* Fri May 27 2011 Valery Inozemtsev <shrek@altlinux.ru> 1:4.6.1-alt1
- packaged library only

