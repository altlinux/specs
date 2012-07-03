Name:    highlight
Summary: Universal source code to formatted text converter
Version: 2.16
Release: alt1
Group:   Development/Tools
License: GPLv3
URL:     http://www.andre-simon.de/

Packager: Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar

# Automatically added by buildreq on Thu Apr 09 2009
BuildRequires: gcc-c++

%description
A utility that converts sourcecode to HTML, XHTML, RTF, LaTeX, TeX, XML or
terminal escape sequences with syntax highlighting.
It supports several programming and markup languages.
Language descriptions are configurable and support regular expressions.
The utility offers indentation and reformatting capabilities.
It is easily possible to create new language definitions and colour themes.

%prep
%setup -q -n highlight

%build
%make cli

%install
%makeinstall DESTDIR=%buildroot

rm -rf -- %buildroot/%_datadir/doc/%name

%files
%_sysconfdir/%name
%_bindir/%name
%_datadir/%name
%_man1dir/%name.*

%changelog
* Tue May 04 2010 Alexey Gladkov <legion@altlinux.ru> 2.16-alt1
- New version (2.16).

* Thu Sep 24 2009 Alexey Gladkov <legion@altlinux.ru> 2.12-alt1
- New version (2.12).

* Thu Apr 09 2009 Alexey Gladkov <legion@altlinux.ru> 2.8-alt1
- Initial build.
