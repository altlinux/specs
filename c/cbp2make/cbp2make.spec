Name: cbp2make
Version: 147
Release: alt1

Summary: Makefile generation tool for Code::Blocks IDE
License: GPLv3
Group: Development/Tools
Url: https://sourceforge.net/projects/cbp2make/

Packager: Alexey Appolonov <alexey@altlinux.org>

# https://sourceforge.net/projects/cbp2make/files/cbp2make-stl-rev147-all.tar.7z/download
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: doxygen

%description
cbp2make is a stand-alone build tool that allows you
to generate makefile(s) for GNU Make out of
Code::Blocks IDE project or workspace file.

%prep
%setup

%build
find bin/ -type f -delete
find dox/ -type f -delete
%make_build -f cbp2make.cbp.mak.unix release doxygen

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_docdir/%name-%version/dox/
cp bin/Release/%name %buildroot%_bindir
cp COPYING %buildroot%_defaultdocdir/%name-%version/
cp changelog.txt %buildroot%_defaultdocdir/%name-%version/
cp usage.txt %buildroot%_defaultdocdir/%name-%version/
cp -r dox/html/ %buildroot%_defaultdocdir/%name-%version/dox/html/

%files
%_defaultdocdir/%name-%version/
%_bindir/%name

%changelog
* Fri Nov 17 2017 Alexey Appolonov <alexey@altlinux.org> 147-alt1
- Initial ALT Linux release.
