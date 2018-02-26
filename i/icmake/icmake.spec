Name: icmake
Version: 7.16.00
Release: alt1
Summary: Hybrid between a 'make' utility and a 'shell script' language
License: GPLv3
Group: Development/Tools
Url: http://icmake.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

%description
Icmake is a hybrid between a 'make' utility and a 'shell script'
language.  Originally, it was concocted to provide a useful tool for
automatic program maintenance and system administrative tasks on MS-DOS
platforms.  As we learned to appreciate its flexibility, Icmake was
eventually ported to Unix platforms (SCO and Linux). By now Icmake also
runs on a HP-Unix platform.

%package doc
Summary: Documentation for Icmake
Group: Development/Documentation
BuildArch: noarch

%description doc
Icmake is a hybrid between a 'make' utility and a 'shell script'
language.  Originally, it was concocted to provide a useful tool for
automatic program maintenance and system administrative tasks on MS-DOS
platforms.  As we learned to appreciate its flexibility, Icmake was
eventually ported to Unix platforms (SCO and Linux). By now Icmake also
runs on a HP-Unix platform.

This package contains documentation for Icmake.

%prep
%setup
sed -i 's|@LIBDIR@|%_libdir|g' INSTALL.im

%build
./icm_bootstrap /

%install
./icm_install all %buildroot

%files
%doc changelog LICENSE doc/*.doc
%_sysconfdir/*
%_bindir/*
%_libdir/%name
%_datadir/%name
%_man1dir/*
%_man7dir/*

%files doc
%_docdir/%name

%changelog
* Sun Aug 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.16.00-alt1
- Initial build for Sisyphus

