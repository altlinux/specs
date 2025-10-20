Name: pandoc
Version: 3.8.2.1
Release: alt1
Summary: Markup conversion tool for markdown

Group: Publishing
License: GPLv2+
Url: http://hackage.haskell.org/package/pandoc

Source: %name-%version.tar
Source1: vendor.tar

Patch1: vendored_basement-github-fix_i586.patch
Patch2: vendored_cborg-github-fix_i586.patch
Patch3: vendored_memory-github-fix_i586.patch

BuildRequires: ghc-devel
BuildRequires: rpm-build-haskell-vendored

BuildRequires: zlib-devel
BuildRequires: gcc-c++

%description
Pandoc is a Haskell library for converting from one markup format to
another, and a command-line tool that uses this library. It can read
markdown and (subsets of) reStructuredText, HTML, and LaTeX, and it can
write markdown, reStructuredText, HTML, LaTeX, ConTeXt, Docbook,
OpenDocument, ODT, RTF, MediaWiki, groff man pages, EPUB, and S5 and
Slidy HTML slide shows.

%prep
%setup -q
%setup -a 1

%ifarch i586
%patch1 -p1
%patch2 -p1
%patch3 -p1
%endif

%build
%cabal_vendor_build --constraint="pandoc +embed_data_files"

%install
%cabal_vendor_install --constraint="pandoc +embed_data_files"

mkdir -p %buildroot%_datadir/bash-completion/completions
%buildroot%_bindir/pandoc --bash-completion > \
                          %buildroot%_datadir/bash-completion/completions/pandoc

install -pm 644 -D -t %buildroot%_man1dir \
                      ./man/pandoc*.1

%files
%_bindir/pandoc
%_datadir/bash-completion/completions/pandoc
%_man1dir/pandoc*.1.xz

%changelog
* Mon Oct 20 2025 Leonid Znamenok <respublica@altlinux.org> 3.8.2.1-alt1
- 3.8.2.1

* Wed Sep 17 2025 Leonid Znamenok <respublica@altlinux.org> 3.8-alt1
- 3.8

* Wed Jun 11 2025 Leonid Znamenok <respublica@altlinux.org> 3.7.0.2-alt1
- 3.7.0.2

* Sun Jun 08 2025 Leonid Znamenok <respublica@altlinux.org> 3.7.0.1-alt1
- 3.7.0.1

* Wed Apr 30 2025 Leonid Znamenok <respublica@altlinux.org> 3.6.4.1-alt2
- embed data files into executable

* Wed Apr 23 2025 Leonid Znamenok <respublica@altlinux.org> 3.6.4.1-alt1
- 3.6.4.1 (ALT#50484) (ALT#49673)
- rebuilt with rpm-build-haskell-vendored

* Mon Aug 07 2023 Vitaly Lipatov <lav@altlinux.ru> 2.9.2.1-alt2
- NMU: drop unneeded build requires

* Mon Jun 22 2020 Denis Smirnov <mithraen@altlinux.ru> 2.9.2.1-alt1
- 2.9.2.1 (ALT#35470) (ALT#37755) (ALT#37499)

* Mon Mar 13 2017 Denis Smirnov <mithraen@altlinux.ru> 1.11.1-alt2
- move pandoc haskell lib to separate subpackage (ALT 31654)

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.11.1-alt1.1
- NMU: updated watch file

* Mon May 06 2013 Denis Smirnov <mithraen@altlinux.ru> 1.11.1-alt1
- 1.11.1

* Fri Feb 08 2013 Denis Smirnov <mithraen@altlinux.ru> 1.9.4.5-alt2
- cleanup spec

* Mon Dec 24 2012 Denis Smirnov <mithraen@altlinux.ru> 1.9.4.5-alt1
- 1.9.4.5

* Sun Sep 23 2012 Denis Smirnov <mithraen@altlinux.ru> 1.9.4.2-alt3
- add watch-file for gear-cronbuild

* Sat Jul 28 2012 Denis Smirnov <mithraen@altlinux.ru> 1.9.4.2-alt1
- 1.9.4.2

* Wed May 02 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.2-alt1
- 1.9.2

* Mon Mar 19 2012 Denis Smirnov <mithraen@altlinux.ru> 1.9.1.2-alt1
- 1.9.1.2

* Wed Aug 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.8.2.1-alt1
- 1.8.2.1

* Wed Mar 09 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.0.1-alt1
- initial from Fedora
