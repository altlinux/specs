%define ghc_version 8.6.4
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hxt
%define f_pkg_name hxt
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 9.3.1.18
Release: alt2
License: MIT
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: https://github.com/UweSchmidt/hxt
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: A collection of tools for processing XML with Haskell.

BuildPreReq: haskell(abi) = %ghc_version


# Automatically added by buildreq on Sun Jun 21 2020 (-bb)
# optimized out: bashrc elfutils ghc8.6.4 ghc8.6.4-aeson ghc8.6.4-aeson-pretty ghc8.6.4-ansi-terminal ghc8.6.4-ansi-wl-pprint ghc8.6.4-asn1-encoding ghc8.6.4-asn1-parse ghc8.6.4-asn1-types ghc8.6.4-async ghc8.6.4-attoparsec ghc8.6.4-base-compat ghc8.6.4-base16-bytestring ghc8.6.4-base64-bytestring ghc8.6.4-basement ghc8.6.4-bitarray ghc8.6.4-blaze-builder ghc8.6.4-case-insensitive ghc8.6.4-cereal ghc8.6.4-chronos ghc8.6.4-clock ghc8.6.4-co-log-core ghc8.6.4-colour ghc8.6.4-conduit ghc8.6.4-contravariant ghc8.6.4-cryptohash-sha256 ghc8.6.4-cryptonite ghc8.6.4-data-default-class ghc8.6.4-digest ghc8.6.4-dlist ghc8.6.4-ed25519 ghc8.6.4-exceptions ghc8.6.4-hashable ghc8.6.4-hourglass ghc8.6.4-hslua ghc8.6.4-hxt-charproperties ghc8.6.4-integer-logarithms ghc8.6.4-ldap ghc8.6.4-memory ghc8.6.4-mono-traversable ghc8.6.4-network ghc8.6.4-network-uri ghc8.6.4-old-locale ghc8.6.4-old-time ghc8.6.4-parsec ghc8.6.4-pem ghc8.6.4-polyparse ghc8.6.4-primitive ghc8.6.4-random ghc8.6.4-regex-base ghc8.6.4-resourcet ghc8.6.4-safe ghc8.6.4-scientific ghc8.6.4-semigroups ghc8.6.4-split ghc8.6.4-splitmix ghc8.6.4-statevar ghc8.6.4-tagged ghc8.6.4-tar ghc8.6.4-temporary ghc8.6.4-th-abstraction ghc8.6.4-time-locale-compat ghc8.6.4-torsor ghc8.6.4-transformers-compat ghc8.6.4-typerep-map ghc8.6.4-unix-compat ghc8.6.4-unliftio-core ghc8.6.4-unordered-containers ghc8.6.4-uuid-types ghc8.6.4-vector ghc8.6.4-vector-algorithms ghc8.6.4-zlib glibc-kernheaders-generic glibc-kernheaders-x86 libffi-devel libgmp-devel perl pkg-config python-modules python2-base python3 python3-base python3-dev rpm-build-haskell rpm-build-python3 sh4
BuildRequires: ghc8.6.4-adldap ghc8.6.4-base-noprelude ghc8.6.4-blaze-markup ghc8.6.4-bytestring-encoding ghc8.6.4-cmark-gfm ghc8.6.4-co-log ghc8.6.4-common ghc8.6.4-cookie ghc8.6.4-cpphs ghc8.6.4-data-default-instances-containers ghc8.6.4-data-default-instances-dlist ghc8.6.4-data-default-instances-old-locale ghc8.6.4-doc ghc8.6.4-doclayout ghc8.6.4-echo ghc8.6.4-edit-distance ghc8.6.4-entropy ghc8.6.4-errors ghc8.6.4-filemanip ghc8.6.4-generic-deriving ghc8.6.4-glob ghc8.6.4-hackage-security ghc8.6.4-haddock-library ghc8.6.4-hfuse ghc8.6.4-hscolour ghc8.6.4-hslogger ghc8.6.4-hslua-module-system ghc8.6.4-hslua-module-text ghc8.6.4-hsyaml ghc8.6.4-http ghc8.6.4-http-types ghc8.6.4-hxt-regex-xmlschema ghc8.6.4-hxt-unicode ghc8.6.4-ipynb ghc8.6.4-juicypixels ghc8.6.4-markdown-unlit ghc8.6.4-mime-types ghc8.6.4-optparse-applicative ghc8.6.4-quickcheck ghc8.6.4-regex-tdfa ghc8.6.4-relude ghc8.6.4-resolv ghc8.6.4-sandi ghc8.6.4-sha ghc8.6.4-socks ghc8.6.4-streaming-commons ghc8.6.4-syb ghc8.6.4-tagsoup ghc8.6.4-unicode-transforms ghc8.6.4-utf8-string ghc8.6.4-x509 ghc8.6.4-xml ghc8.6.4-zip-archive libdb4-devel python-modules-compiler python3-module-mpl_toolkits 

%description
The Haskell XML Toolbox bases on the ideas of HaXml and HXML, but
introduces a more general approach for processing XML with Haskell. The
Haskell XML Toolbox uses a generic data model for representing XML
documents, including the DTD subset and the document subset, in Haskell. It
contains a validating XML parser, a HTML parser, namespace support, an
XPath expression evaluator, an XSLT library, a RelaxNG schema validator and
funtions for serialization and deserialization of user defined data. The
library makes extensive use of the arrow approach for processing XML. Since
version 9 the toolbox is partitioned into various (sub-)packages. This
package contains the core functionality, hxt-curl, hxt-tagsoup,
hxt-relaxng, hxt-xpath, hxt-xslt, hxt-regex-xmlschema contain the
extensions. hxt-unicode contains encoding and decoding functions,
hxt-charproperties char properties for unicode and XML.

Changes from 9.3.1.15: Bug in quoting PI instructions in showXmlTrees fixed

Changes from 9.3.1.14: For ghc-7.10 network-uri is automatically selected

Changes from 9.3.1.13: ghc-7.10 compatibility

Changes from 9.3.1.12: Bug when unpickling an empty attribute value removed

Changes from 9.3.1.11: Bug fix in haddock comments

Changes from 9.3.1.10: Bug in DTD validation, space and time leak in delta
removed

Changes from 9.3.1.9: lower bound of mtl dependency lowered to 2.0.1

Changes from 9.3.1.8: Bug in hread removed

Changes from 9.3.1.7: Foldable and Traversable instances for NTree added
Control.Except used instead of deprecated Control.Error

Changes from 9.3.1.6: canonicalize added in hread and hreadDoc

Changes from 9.3.1.4: conditionally (no default) dependency from networt
changed to network-uri with flag "network-uri"

Changes from 9.3.1.3: warnings from ghc-7.8.1 removed

Changes from 9.3.1.2: https as protocol added

Changes from 9.3.1.1: new parser xreadDoc

Changes from 9.3.1.0: in readString all input decoding switched off

Changes from 9.3.0.1: lower bound for network set to be >= 2.4

Changes from 9.3.0: upper bound for network set to be < 2.4 (URI signatures
changed in 2.4)

Changes from 9.2.2: XMLSchema validation integrated

Changes from 9.2.1: user defined mime type handlers added

Changes from 9.2.0: New warnings from ghc-7.4 removed

%prep
%setup
%patch -p1

%build
%hs_configure2
%hs_build

%install
%hs_install
%hs_gen_filelist

%files -f %name-files.all

%changelog
* Thu Aug 17 2023 Anton Zhukharev <ancieg@altlinux.org> 9.3.1.18-alt2
- Fixed FTBFS.

* Sun Jun 21 2020 Denis Smirnov <mithraen@altlinux.ru> 9.3.1.18-alt1
- Spec created by cabal2rpm 0.20_10
