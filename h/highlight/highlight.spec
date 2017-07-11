Name:    highlight
Summary: Universal source code to formatted text converter
Version: 3.38
Release: alt1
Group:   Development/Tools
License: GPLv3
URL:     http://www.andre-simon.de/

Packager: Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar

BuildRequires: boost-devel-headers gcc-c++ liblua5-devel libstdc++-devel pkg-config

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
* Tue Jul 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.38-alt1
- Updated to upstream version 3.38

* Sun Mar 03 2013 Alexey Gladkov <legion@altlinux.ru> 3.13-alt1
- New version (3.13).

* Tue May 04 2010 Alexey Gladkov <legion@altlinux.ru> 2.16-alt1
- New version (2.16).

* Thu Sep 24 2009 Alexey Gladkov <legion@altlinux.ru> 2.12-alt1
- New version (2.12).

* Thu Apr 09 2009 Alexey Gladkov <legion@altlinux.ru> 2.8-alt1
- Initial build.
