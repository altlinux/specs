Name: 		log4c
Version: 	1.2.1
Release: 	alt1.1.qa3

Summary: 	Log for C
License:	LGPLv2.1
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
BuildArch: noarch

%description devel
The %name-devel package contains the shared libraries and header files
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

rm -fv %buildroot%_libdir/*.a

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%_sysconfdir/*
%_libdir/*.so.*

%files devel
%_bindir/*
%_includedir/*
%_libdir/*.so
%_datadir/aclocal/*
%_man3dir/*

%files doc
%doc  doc/html

%changelog
* Tue Oct 12 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1.1.qa3
- Fixed FTBFS.

* Thu Apr 15 2021 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1.1.qa2
- Fixed FTBFS.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1.1.qa1
- NMU: applied repocop patch

* Tue Jul 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.1
- Rebuilt for set-versions

* Tue Feb 16 2010 Maxim Ivanov <redbaron at altlinux.org> 1.2.1-alt1
- Initial build for ALT Linux

