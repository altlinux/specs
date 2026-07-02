%define soname 1

Name: libreadstat
Version: 1.1.9
Release: alt2

Summary: C library for reading files from SAS, Stata, and SPSS
Group: System/Libraries
License: MIT
Url: https://github.com/WizardMac/ReadStat
VCS: https://github.com/WizardMac/ReadStat

Source: %name-%version.tar
Patch0: readstat-1.1.9-upstream-fix-use-after-free.patch
Patch1: readstat-1.1.9-upstream-remove-gettext-iconv.patch

BuildRequires: gcc
BuildRequires: autoconf automake libtool
BuildRequires: zlib-devel

%description
ReadStat is a MIT-licensed C library for reading and writing binary and
transport files from SAS, Stata, and SPSS. Supported formats include:
SAS (SAS7BDAT and XPORT), Stata (DTA), and SPSS (POR, SAV, ZSAV).

%package -n libreadstat%soname
Summary: ReadStat shared library
Group: System/Libraries

%description -n libreadstat%soname
ReadStat shared library for reading and writing binary and transport
files from SAS, Stata, and SPSS.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: libreadstat%soname = %EVR

%description devel
Headers and libraries for developing applications that use %name.

%package -n readstat-tools
Summary: Command-line tools for converting stat files
Group: File tools
Requires: libreadstat%soname = %EVR

%description -n readstat-tools
Command-line tools for reading and converting files from SAS, Stata,
and SPSS. Includes readstat and extract_metadata utilities.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
autoreconf -fiv
%configure --disable-static
%make_build

%install
%makeinstall_std
# Remove libtool archives
rm -f %buildroot%_libdir/*.la

%files -n libreadstat%soname
%doc LICENSE README.md
%_libdir/libreadstat.so.%soname
%_libdir/libreadstat.so.%soname.*

%files devel
%_includedir/readstat.h
%_libdir/libreadstat.so

%files -n readstat-tools
%_bindir/readstat
%_bindir/extract_metadata
%_man1dir/readstat.1*
%_man1dir/extract_metadata.1*

%changelog
* Thu Jul 02 2026 Anton Farygin <rider@altlinux.org> 1.1.9-alt2
- fixed build with gettext 1.0 (upstream PR #342): drop obsolete
  AM_ICONV so autoreconf no longer needs the gettext m4 macros

* Sat Feb 08 2026 Anton Farygin <rider@altlinux.org> 1.1.9-alt1
- initial build for ALT Linux
