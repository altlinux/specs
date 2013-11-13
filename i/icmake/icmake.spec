Name: icmake
Version: 7.21.00
Release: alt1.git20130802
Summary: Hybrid between a 'make' utility and a 'shell script' language
License: GPLv3
Group: Development/Tools
Url: http://icmake.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://icmake.git.sourceforge.net/gitroot/icmake/icmake
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
sed -i 's|@LIBDIR@|%_libdir|g' %name/INSTALL.im

%build
pushd %name
./icm_bootstrap /
popd

./manpages

%install
pushd %name
./icm_install all %buildroot
popd

%files
%doc %name/changelog %name/doc/*.doc
%_sysconfdir/*
%_bindir/*
%_libdir/%name
%_datadir/%name
%_man1dir/*
%_man7dir/*

%files doc
%_docdir/%name

%changelog
* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.21.00-alt1.git20130802
- Version 7.21.00

* Thu Sep 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.19.00-alt1.git20120722
- Version 7.19.00

* Sun Aug 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.16.00-alt1
- Initial build for Sisyphus

