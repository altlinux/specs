Name: fstrcmp
Version: 0.7
Release: alt2

Summary: Fuzzy string compare library
License: GPLv3
Group: File tools
Url: http://fstrcmp.sourceforge.net/

Source: %name-%version.tar

BuildRequires: groff

%package -n libfstrcmp
Summary: Fuzzy string compare library
Group: System/Libraries

%package devel
Summary: Fuzzy string compare library
Group: Development/C

%define desc The fstrcmp package provides a library which may be used to make \
fuzzy comparisons of strings and byte arrays. It also provides simple commands \
for use  in shell scripts.

%description
%desc

%description -n libfstrcmp
%desc
This package contains shared fstrcmp library.

%description devel 
%desc
This package contains development part of fstrcmp.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
rm -v %buildroot%_libdir/libfstrcmp.a

%files
%_bindir/fstrcmp
%_man1dir/fstrcmp*.1*

%files -n libfstrcmp
%_libdir/libfstrcmp.so.*

%files devel
%_includedir/fstrcmp.h
%_libdir/libfstrcmp.so
%_pkgconfigdir/fstrcmp.pc
%_man3dir/*

%changelog
* Mon Aug 30 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7-alt2
- unpackaged static library removed

* Wed Jan 30 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7-alt1
- initial
