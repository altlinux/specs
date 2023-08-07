%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name
%define f_pkg_name pandoc
%define h_pkg_name pandoc
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: pandoc
Version: 2.9.2.1
Release: alt2
Summary: Markup conversion tool for markdown

Group: Publishing
License: GPLv2+
Url: http://hackage.haskell.org/package/%name

Source: http://hackage.haskell.org/packages/archive/%name/%version/%name-%version.tar.gz
Source100: pandoc.watch

# Automatically added by buildreq on Wed Jun 24 2020 (-bb)
# optimized out: elfutils ghc8.6.4 ghc8.6.4-aeson ghc8.6.4-aeson-pretty ghc8.6.4-ansi-terminal ghc8.6.4-ansi-wl-pprint ghc8.6.4-asn1-encoding ghc8.6.4-asn1-parse ghc8.6.4-asn1-types ghc8.6.4-async ghc8.6.4-attoparsec ghc8.6.4-base-compat ghc8.6.4-base16-bytestring ghc8.6.4-base64-bytestring ghc8.6.4-basement ghc8.6.4-bitarray ghc8.6.4-blaze-builder ghc8.6.4-blaze-html ghc8.6.4-blaze-markup ghc8.6.4-case-insensitive ghc8.6.4-cereal ghc8.6.4-chronos ghc8.6.4-clock ghc8.6.4-co-log-core ghc8.6.4-colour ghc8.6.4-conduit ghc8.6.4-connection ghc8.6.4-contravariant ghc8.6.4-cookie ghc8.6.4-cryptohash-sha256 ghc8.6.4-cryptonite ghc8.6.4-data-default-class ghc8.6.4-data-default-instances-containers ghc8.6.4-data-default-instances-dlist ghc8.6.4-data-default-instances-old-locale ghc8.6.4-digest ghc8.6.4-dlist ghc8.6.4-doclayout ghc8.6.4-ed25519 ghc8.6.4-errors ghc8.6.4-exceptions ghc8.6.4-hashable ghc8.6.4-hourglass ghc8.6.4-hslua ghc8.6.4-hsyaml ghc8.6.4-http-client ghc8.6.4-http-types ghc8.6.4-hxt ghc8.6.4-hxt-charproperties ghc8.6.4-hxt-regex-xmlschema ghc8.6.4-hxt-unicode ghc8.6.4-integer-logarithms ghc8.6.4-ldap ghc8.6.4-memory ghc8.6.4-mime-types ghc8.6.4-mono-traversable ghc8.6.4-network ghc8.6.4-network-uri ghc8.6.4-old-locale ghc8.6.4-old-time ghc8.6.4-pandoc-types ghc8.6.4-parsec ghc8.6.4-pem ghc8.6.4-polyparse ghc8.6.4-primitive ghc8.6.4-quickcheck ghc8.6.4-random ghc8.6.4-regex-base ghc8.6.4-regex-pcre-builtin ghc8.6.4-resourcet ghc8.6.4-safe ghc8.6.4-scientific ghc8.6.4-semigroups ghc8.6.4-skylighting-core ghc8.6.4-socks ghc8.6.4-split ghc8.6.4-splitmix ghc8.6.4-statevar ghc8.6.4-streaming-commons ghc8.6.4-syb ghc8.6.4-tagged ghc8.6.4-tar ghc8.6.4-temporary ghc8.6.4-text-conversions ghc8.6.4-th-abstraction ghc8.6.4-time-locale-compat ghc8.6.4-tls ghc8.6.4-torsor ghc8.6.4-transformers-compat ghc8.6.4-typerep-map ghc8.6.4-unix-compat ghc8.6.4-unliftio-core ghc8.6.4-unordered-containers ghc8.6.4-utf8-string ghc8.6.4-uuid-types ghc8.6.4-vector ghc8.6.4-vector-algorithms ghc8.6.4-x509 ghc8.6.4-x509-store ghc8.6.4-x509-system ghc8.6.4-x509-validation ghc8.6.4-xml ghc8.6.4-zlib glibc-kernheaders-generic glibc-kernheaders-x86 libffi-devel libgmp-devel pkg-config python-modules python2-base python3 python3-base python3-dev rpm-build-haskell rpm-build-python3 sh4 xz
BuildRequires: ghc8.6.4-adldap ghc8.6.4-base-noprelude ghc8.6.4-bytestring-encoding ghc8.6.4-cmark-gfm ghc8.6.4-co-log ghc8.6.4-common ghc8.6.4-cpphs ghc8.6.4-data-default ghc8.6.4-doc ghc8.6.4-doctemplates ghc8.6.4-echo ghc8.6.4-edit-distance ghc8.6.4-emojis ghc8.6.4-entropy ghc8.6.4-filemanip ghc8.6.4-generic-deriving ghc8.6.4-glob ghc8.6.4-hackage-security ghc8.6.4-haddock-library ghc8.6.4-hfuse ghc8.6.4-hscolour ghc8.6.4-hslogger ghc8.6.4-hslua-module-system ghc8.6.4-hslua-module-text ghc8.6.4-http ghc8.6.4-http-client-tls ghc8.6.4-ipynb ghc8.6.4-jira-wiki-markup ghc8.6.4-juicypixels ghc8.6.4-markdown-unlit ghc8.6.4-optparse-applicative ghc8.6.4-regex-tdfa ghc8.6.4-relude ghc8.6.4-resolv ghc8.6.4-sandi ghc8.6.4-sha ghc8.6.4-skylighting ghc8.6.4-tagsoup ghc8.6.4-texmath ghc8.6.4-unicode-transforms ghc8.6.4-zip-archive zlib-devel

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
if [ -f configure.ac -a ! -f configure ]; then autoreconf; fi;
%__hs_build_setup
./Setup configure \
    --prefix=%_prefix \
    --libdir=%_libdir \
    --docdir=%_docdir/%hsc_namever-%f_pkg_name-%version \
    --libsubdir='$compiler/$pkgid' \
    --dynlibdir='%_libdir/$compiler/lib' \
    --docdir=%_docdir/%name-%version \
    --datadir=%_datadir \
    --datasubdir=%name-%version \
    --disable-library-profiling \
    --disable-library-for-ghci \
    --disable-profiling \
    --disable-split-objs \
    --enable-shared \
     \
    -O0 \
    --ghc \
    --ghc-options="-O0 -g0"

%__hs_build_setup
if ./Setup makefile -f cabal-rpm.mk;
then
    %make_build -f cabal-rpm.mk || : ;
fi;
./Setup build --ghc-options="-O0 -g0 -j1" -v3
./Setup haddock || :
./Setup register --gen-pkg-config=%f_pkg_name.pkg;


%hs_build

%install
%hs_install
%hs_gen_filelist

grep -v %_libdir %name-files.all \
    | grep -v /usr/share/pandoc- > %name-files.bin
grep %_libdir %name-files.all > %name-files.lib

install -D -m644 man/pandoc.1 %buildroot%_man1dir/pandoc.1

%files -n ghc%ghc_version-pandoc -f %name-files.lib

%files -f %name-files.bin
%_man1dir/*
/usr/share/%name-%version

%changelog
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
