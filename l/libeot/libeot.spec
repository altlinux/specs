Name: libeot
Version: 0.01
Release: alt1
Summary: A library for parsing Embedded OpenType font files

Group: System/Libraries
License: MPLv2.0
Url: https://github.com/umanwizard/libeot
Source: %name-%version.tar

%description
%name is a library for parsing Embedded OpenType files (Microsoft
embedded font "standard") and converting them to other formats.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package tools
Summary: Tools to transform EOT font files into other formats
Group: Publishing
Requires: %name = %version-%release

%description tools
Tools to transform EOT font files into other formats. Only TTF is
supported currently.

%prep
%setup

%build
%autoreconf
%configure --disable-silent-rules --disable-static
%make_build

%install
%makeinstall_std


%files
%doc LICENSE PATENTS
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files tools
%_bindir/*

%changelog
* Sat Jun 07 2014 Alexey Shabalin <shaba@altlinux.ru> 0.01-alt1
- initial build
