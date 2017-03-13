%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define f_pkg_name pandoc
%define h_pkg_name pandoc
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: pandoc
Version: 1.11.1
Release: alt2
Summary: Markup conversion tool for markdown

Group: Publishing
License: GPLv2+
Url: http://hackage.haskell.org/package/%name

Source: http://hackage.haskell.org/packages/archive/%name/%version/%name-%version.tar.gz
Source100: pandoc.watch

# Automatically added by buildreq on Mon Dec 24 2012
# optimized out: ghc7.6.1 ghc7.6.1-blaze-builder ghc7.6.1-blaze-html ghc7.6.1-blaze-markup ghc7.6.1-common ghc7.6.1-digest ghc7.6.1-extensible-exceptions ghc7.6.1-hexpat ghc7.6.1-hs-bibutils ghc7.6.1-http ghc7.6.1-json ghc7.6.1-list ghc7.6.1-mtl ghc7.6.1-network ghc7.6.1-pandoc-types ghc7.6.1-parsec ghc7.6.1-regex-base ghc7.6.1-regex-pcre-builtin ghc7.6.1-syb ghc7.6.1-text ghc7.6.1-transformers ghc7.6.1-utf8-string ghc7.6.1-xml ghc7.6.1-zlib libgmp-devel pkg-config
BuildRequires: ghc7.6.1-alex ghc7.6.1-base64-bytestring ghc7.6.1-c2hs ghc7.6.1-citeproc-hs ghc7.6.1-cpphs ghc7.6.1-happy ghc7.6.1-highlighting-kate ghc7.6.1-hscolour ghc7.6.1-random ghc7.6.1-tagsoup ghc7.6.1-temporary ghc7.6.1-texmath ghc7.6.1-zip-archive zlib-devel ghc7.6.1-data-default

%package -n ghc%ghc_version-pandoc
Summary: Markup conversion tool for markdown
Group: Publishing

%description
Pandoc is a Haskell library for converting from one markup format to
another, and a command-line tool that uses this library. It can read
markdown and (subsets of) reStructuredText, HTML, and LaTeX, and it can
write markdown, reStructuredText, HTML, LaTeX, ConTeXt, Docbook,
OpenDocument, ODT, RTF, MediaWiki, groff man pages, EPUB, and S5 and
Slidy HTML slide shows.

%description -n ghc%ghc_version-pandoc
Pandoc is a Haskell library for converting from one markup format to
another, and a command-line tool that uses this library. It can read
markdown and (subsets of) reStructuredText, HTML, and LaTeX, and it can
write markdown, reStructuredText, HTML, LaTeX, ConTeXt, Docbook,
OpenDocument, ODT, RTF, MediaWiki, groff man pages, EPUB, and S5 and
Slidy HTML slide shows.

%prep
%setup -q

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist
grep -v %_libdir %name-files.all > %name-files.bin
grep %_libdir %name-files.all > %name-files.lib

%files -n ghc%ghc_version-pandoc -f %name-files.lib

%files -f %name-files.bin
%_man1dir/*
%_man5dir/*

%changelog
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
