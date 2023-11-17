Name:    highlight
Summary: Universal source code to formatted text converter
Version: 4.3
Release: alt2
Group:   Development/Tools
License: GPL-3.0
URL:     http://www.andre-simon.de/

Packager: Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar

Patch0001: highlight-alt-link-with-perl.patch

BuildRequires: boost-devel-headers
BuildRequires: gcc-c++
BuildRequires: liblua5-devel
BuildRequires: libstdc++-devel
BuildRequires: pkg-config

BuildRequires: swig

BuildRequires: rpm-build-perl
BuildRequires: perl-devel

Requires: highlight-common = %version-%release

%description
A utility that converts sourcecode to HTML, XHTML, RTF, LaTeX, TeX, XML or
terminal escape sequences with syntax highlighting.
It supports several programming and markup languages.
Language descriptions are configurable and support regular expressions.
The utility offers indentation and reformatting capabilities.
It is easily possible to create new language definitions and colour themes.

%package -n highlight-common
Summary: Source code to formatted text converter (architecture independent files)
Group: Development/Other

Conflicts: highlight <= 3.38-alt1

BuildArch: noarch

%description -n highlight-common
A utility that converts sourcecode to HTML, XHTML, RTF, LaTeX, TeX, XML or
terminal escape sequences with syntax highlighting.
It supports several programming and markup languages.
Language descriptions are configurable and support regular expressions.
The utility offers indentation and reformatting capabilities.
It is easily possible to create new language definitions and colour themes.

%package -n perl-highlight
Summary: perl bindings for highlight source code to formatted text converter
Group: Development/Perl

Provides: libhighlight-perl = %version-%release
Requires: highlight-common  = %version-%release

%description -n perl-highlight
A utility that converts sourcecode to HTML, XHTML, RTF, LaTeX, TeX, XML or
terminal escape sequences with syntax highlighting.
It supports several programming and markup languages.
Language descriptions are configurable and support regular expressions.
The utility offers indentation and reformatting capabilities.
It is easily possible to create new language definitions and colour themes.

%prep
%setup -q -n highlight
%autopatch -p2

%build
%add_optflags %optflags_shared

export CFLAGS="%optflags"
export CXXFLAGS="%optflags"

%make cli

pushd extras/swig
%make perl
popd

%install
%makeinstall DESTDIR=%buildroot

install -D extras/swig/highlight.pm %buildroot/%perl_vendor_archlib/highlight.pm
install -D extras/swig/highlight.so %buildroot/%perl_vendor_autolib/highlight/highlight.so

rm -rf -- %buildroot/%_datadir/doc/%name

%files
%_bindir/%name
%_man1dir/%name.*
%_man5dir/filetypes.conf.5*

%files -n highlight-common
%_sysconfdir/%name
%_datadir/%name

%files -n perl-highlight
%perl_vendor_autolib/*
%perl_vendor_archlib/*

%changelog
* Sat Nov 18 2023 Alexey Gladkov <legion@altlinux.ru> 4.3-alt2
- Link with -lperl (ALT#48474)

* Mon Oct 17 2022 Alexey Gladkov <legion@altlinux.ru> 4.3-alt1
- New version (4.3).

* Wed Jun 23 2021 Alexey Gladkov <legion@altlinux.ru> 4.1-alt1
- New version (4.1).

* Thu Oct 15 2020 Alexey Gladkov <legion@altlinux.ru> 3.58-alt1
- New version (3.58).

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
