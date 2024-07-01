Name: libeditline
Version: 1.17.1
Release: alt1

Summary: A small compatible replacement for readline
License: BSD
Group: System/Libraries

Url: https://github.com/troglobit/editline
# Source-url: https://github.com/troglobit/editline/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
%summary

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

# Avoid conflict with libedit-devel
rm -v %buildroot%_docdir/editline/{LICENSE,README.md}
rm -v %buildroot%_man3dir/editline.3

%files
%doc LICENSE
%_libdir/libeditline.so.1
%_libdir/libeditline.so.1.0.2

%files devel
%doc ChangeLog.md README.md
%_includedir/editline.h
%_libdir/libeditline.so
%_pkgconfigdir/libeditline.pc

%changelog
* Mon Jul 01 2024 Boris Yumankulov <boria138@altlinux.org> 1.17.1-alt1
- initial build for ALT Sisyphus

