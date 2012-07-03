%global __strip %_mingw32_strip
%global __objdump %_mingw32_objdump

Name: mingw32-libffi
Version: 3.0.9
Release: alt2

Summary: A portable foreign function interface library for MinGW

Group: System/Libraries
License: BSD
Url: http://sourceware.org/libffi

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://sourceware.org/pub/libffi/libffi-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-mingw32
BuildRequires: gcc-c++

BuildRequires: mingw32-filesystem >= 56
BuildRequires: mingw32-binutils
BuildRequires: mingw32-gcc
Source44: import.info

%description
Foreign function interface library for MinGW.

%prep
%setup -n libffi-%version

%build
%_mingw32_configure --disable-static --enable-shared
%make_build

%install
%makeinstall_std
rm -rf %buildroot%_mingw32_infodir
rm -rf %buildroot%_mingw32_mandir

%files
%doc LICENSE README
%_mingw32_bindir/libffi-5.dll
%_mingw32_libdir/libffi.dll.a
%_mingw32_libdir/libffi.la
%_mingw32_libdir/pkgconfig/*.pc
%_mingw32_libdir/libffi-%version

%changelog
* Mon Jun 25 2012 Vitaly Lipatov <lav@altlinux.ru> 3.0.9-alt2
- cleanup spec

* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 3.0.9-alt1_2
- initial release by fcimport

