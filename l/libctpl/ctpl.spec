%define libname ctpl
Name: libctpl
Version: 0.3.4
Release: alt1
Summary: Template library and engine written in C
Group: Development/C

License: GPLv3+
Url: http://ctpl.tuxfamily.org/
Source0: http://download.tuxfamily.org/ctpl/releases/ctpl-%version.tar.gz

# Patch adds possibility to disable the build of the command line tool.
# The patch is pulled from upstream at
# http://git.tuxfamily.org/ctpl/ctpl/?p=gitroot/ctpl/ctpl.git;a=summary
Patch0: ctpl-0.3.2-add-disable-cli-tool.patch
Patch1: http://ausil.fedorapeople.org/aarch64/ctpl/ctpl-aarch64.patch

# Automatically added by buildreq on Wed Feb 27 2019
# optimized out: glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config pkg-config python-base sh4
BuildRequires: libgio-devel

BuildRequires: gcc
BuildRequires: glib2-devel >= 2.10

%description
CTPL is a template library written in C. It allows fast and easy parsing of
templates from many sources (including in-memory data and local and remote
streaming, thanks to GIO) and fine control over template parsing environment.

CTPL has following features:
* It is a library, then it can be easily used from programs
* Separated lexer and parser
* It is written in portable C
* Simple syntax
* Fast and strict parsing
* Possible in-memory parsing, allowing non-file data parsing and avoiding
  I/O-latency, through GIO's GMemoryInputStream and GMemoryOutputStream

%package devel
Summary: Development headers of the template library written in C
Group: Development/C

%description devel
This package contains the development headers of the CTPL library.

%package doc
Summary: Documentation for the CTPL library
Group: Development/C
BuildArch: noarch

%description doc
This package contains the HTML documentation reference for the CTPL library.

%package tools
Summary: Supplemental tools for the CTPL library
Group: Development/C
%description tools
%summary

%prep
%setup -n %libname-%version
sed -i 's/tempfile/mktemp check.XXXXXXXXXXX/' testsuite/tests.sh

%build
%configure  --disable-static

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%makeinstall

%check
LD_LIBRARY_PATH=%buildroot%_libdir make check

%files tools
%doc %_mandir/man1/%libname.1.*
%_bindir/%libname

%files
%doc AUTHORS
%doc COPYING
%doc NEWS
%_libdir/*.so.*

%files devel
%doc HACKING
%doc TODO
%_libdir/*.so
%_includedir/%libname/
%_libdir/pkgconfig/*.pc

%files doc
%doc README
%doc THANKS
%doc %_datadir/gtk-doc/html/*

%changelog
* Wed Feb 27 2019 Fr. Br. George <george@altlinux.ru> 0.3.4-alt1
- Autobuild version bump to 0.3.4

* Wed Feb 27 2019 Fr. Br. George <george@altlinux.ru> 0.3.3-alt1
- Initial build from Fedora
