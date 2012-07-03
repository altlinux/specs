Name: argtable2
Version: 10
Release: alt2

Summary: An ANSI C library for parsing GNU style command line arguments
License: LGPL
Group: System/Libraries

Url: http://argtable.sf.net/
Source: %name-%version.tar.gz

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

BuildPreReq: gcc-c++

%description
Argtable is an ANSI C library for parsing GNU style command line
arguments. It enables a program's command line syntax to be defined in
the source code as an array of argtable structs. The command line is
then parsed according to that specification and the resulting values
are returned in those same structs where they are accessible to the
main program. Both tagged (-v, --verbose, --foo=bar) and untagged
arguments are supported, as are multiple instances of each argument.
Syntax error handling is automatic and the library also provides the
means for displaying the command line syntax directly from the array
of argument specifications.

%package -n lib%name
Summary: Dynamic libraries from %name
Group: System/Libraries

%description -n lib%name
Dynamic libraries from %name.

%package -n lib%name-devel
Summary: Header files and static libraries from %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Libraries and includes files for developing programs based on %name.

%package doc-ps
Summary: Development documentation for %name (PostScript format)
Group: Development/C
BuildArch: noarch

%description doc-ps
Documentation for developing programs based on %name in PostScript format.

%package doc-pdf
Summary: Development documentation for %name (PDF format)
Group: Development/C
BuildArch: noarch

%description doc-pdf
Documentation for developing programs based on %name in PDF format.

%package doc-html
Summary: Development documentation for %name (HTML format)
Group: Development/C
BuildArch: noarch

%description doc-html
Documentation for developing programs based on %name in HTML format.

%package doc-examples
Summary: Development documentation for %name (examples)
Group: Development/C
BuildArch: noarch

%description doc-examples
Examples for developing programs based on %name.

%prep
%setup

%build
%configure --disable-static
%make_build
%make -C tests check

%install
%makeinstall

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS ChangeLog README

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_man3dir/*

%files doc-ps
%_defaultdocdir/%name/*.ps

%files doc-pdf
%_defaultdocdir/%name/*.pdf

%files doc-html
%_defaultdocdir/%name/*.html
%_defaultdocdir/%name/*.gif

%files doc-examples
%_defaultdocdir/%name/example/


%changelog
* Fri Oct 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10-alt2
- Rebuilt for soname set-versions

* Wed Jan 28 2009 Andrey Rahmatullin <wrar@altlinux.ru> 10-alt1
- 10
- remove obsolete macros

* Fri Aug 04 2008 Andrey Rahmatullin <wrar@altlinux.ru> 9-alt1
- 9
- make doc subpackages noarch

* Wed Jan 02 2008 Andrey Rahmatullin <wrar@altlinux.ru> 8-alt1
- 8

* Tue Jul 24 2007 Andrey Rahmatullin <wrar@altlinux.ru> 7-alt1
- 7

* Sat Sep 30 2006 Andrey Rahmatullin <wrar@altlinux.ru> 6-alt1
- initial build

