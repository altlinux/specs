Name: liblogging
Version: 1.0.6
Release: alt1
Summary: LibLogging stdlog library
License: 2-clause BSD
Group: System/Libraries
Url: http://www.liblogging.org
Source: %name-%version.tar

BuildRequires: pkgconfig(libsystemd) >= 209
BuildRequires: /usr/bin/rst2man

%description
LibLogging stdlog library
Libstdlog component is used for standard logging (syslog replacement)
purposes via multiple channels (driver support is planned)

%package devel
Summary: Development files for LibLogging stdlog library
Group: Development/C
Requires: %name = %version-%release

%description devel
The liblogging-devel package includes header files, libraries necessary for
developing programs which use liblogging library.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	--enable-rfc3195 \
	--enable-stdlog \
	--enable-journal
	
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_libdir/*.so.*
%_bindir/stdlogctl
%_man1dir/*
%_man3dir/*

%files devel
%_libdir/*.so
%_includedir/liblogging
%_pkgconfigdir/*.pc

%changelog
* Mon Mar 06 2017 Alexey Shabalin <shaba@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Wed Jan 14 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Thu Apr 24 2014 Alexey Shabalin <shaba@altlinux.ru> 1.0.4-alt1
- initial build
