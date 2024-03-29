Name: liblogging
Version: 1.0.6
Release: alt4

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
# Fix wrong ^M in the file
sed -i 's;\r;\n;g' rfc3195/src/oscallsUnix.c

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
* Sun Jun 12 2022 Alexey Shabalin <shaba@altlinux.org> 1.0.6-alt4
- use /usr/bin/rst2man from python3-module-docutils

* Sat Jan 08 2022 Michael Shigorin <mike@altlinux.org> 1.0.6-alt3
- NMU: fix line endings to build on e2k (sem@)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt2
- NMU: use /usr/bin/rst2man.py from python3-module-docutils

* Mon Mar 06 2017 Alexey Shabalin <shaba@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Wed Jan 14 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Thu Apr 24 2014 Alexey Shabalin <shaba@altlinux.ru> 1.0.4-alt1
- initial build
