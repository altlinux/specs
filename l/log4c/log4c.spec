Name: 		log4c
Version: 	1.2.1
Release: 	alt1

Summary: 	Log for C
License:	LGPL
Group:		Development/C
Packager:	Maxim Ivanov <redbaron@altlinux.org>
Url:		http://%name.sourceforge.net/
Source:		%name-%version.tar
BuildRequires: 	doxygen

%description
%name is a Logging FrameWork for C, as Log4j or Log4Cpp.

%package devel
Summary: development tools for %name
Group: Development/C
Requires: %name = %version

%package doc
Summary: documentation for %name
Group: Development/C
Requires: %name = %version

%description devel
The %name-devel package contains the static libraries and header files
needed for development with %name.

%description doc
The %name-doc package contains the %name documentation

%prep
%setup -q

%build
%configure --enable-doc
%make_build

%install
%makeinstall

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%_sysconfdir/*
%_libdir/*.so.*

%files devel
%_bindir/*
%_includedir/*
%_libdir/*.so
%_libdir/*.a
%_datadir/aclocal/*
%_man3dir/*

%files doc
%doc  doc/html

%changelog
* Tue Feb 16 2010 Maxim Ivanov <redbaron at altlinux.org> 1.2.1-alt1
- Initial build for ALT Linux

