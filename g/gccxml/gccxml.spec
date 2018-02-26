Name: gccxml
Version: 0.9
Release: alt1.cvs20081111

Summary: XML output frontend for GNU C++
License: GPLv2
Group: Development/Other
Url: http://gccxml.org
Packager: Alexander Myltsev <avm@altlinux.ru>

Source: %name-%version.tar

BuildRequires: cmake gcc-c++

Requires: gcc-c++

%description
The purpose of GCC-XML is to generate an XML description of a C++
program from GCC's internal representation. Since XML is easy to
parse, other development tools will be able to work with C++
programs without the burden of a complicated C++ parser.

%prep
%setup

%build
mkdir gccxml-build
cd gccxml-build
cmake ../gccxml -DCMAKE_INSTALL_PREFIX:PATH=%prefix
make

%install
cd gccxml-build
make install DESTDIR=%buildroot

%files
%_bindir/gccxml
%_bindir/gccxml_cc1plus
%_datadir/gccxml-*
%_man1dir/*.1*
%doc %_defaultdocdir/%name-%version

%changelog
* Tue Nov 11 2008 Alexander Myltsev <avm@altlinux.ru> 0.9-alt1.cvs20081111
- Initial build for Sisyphus.

