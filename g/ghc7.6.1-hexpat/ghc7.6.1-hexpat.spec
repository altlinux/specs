%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name hexpat
%define f_pkg_name hexpat
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.20.3
Release: alt2
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://haskell.org/haskellwiki/Hexpat/
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: XML parser/formatter based on expat



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1 ghc7.6.1-common ghc7.6.1-transformers libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1-cpphs ghc7.6.1-doc ghc7.6.1-extensible-exceptions ghc7.6.1-hscolour ghc7.6.1-list ghc7.6.1-text ghc7.6.1-utf8-string

%description
This package provides a general purpose Haskell XML library using Expat to
do its parsing (<http://expat.sourceforge.net/> - a fast stream-oriented
XML parser written in C). It is extensible to any string type, with
@String@, @ByteString@ and @Text@ provided out of the box.

Basic usage: Parsing a tree (/Tree/), formatting a tree (/Format/). Other
features: Helpers for processing XML trees (/Proc/), trees annotated with
XML source location (/Annotated/), extended XML trees with comments,
processing instructions, etc (/Extended/), XML cursors (/Cursor/),
SAX-style parse (/SAX/), and access to the low-level interface in case
speed is paramount (/Internal.IO/).

The design goals are speed, speed, speed, interface simplicity and
modularity.

For introduction and examples, see the /Text.XML.Expat.Tree/ module. For
benchmarks, <http://haskell.org/haskellwiki/Hexpat/>

If you want to do interactive I\/O, an obvious option is to use lazy
parsing with one of the lazy I\/O functions such as hGetContents. However,
this can be problematic in some applications because it doesn't handle I\/O
errors properly and can give no guarantee of timely resource cleanup.
Because of the generalized list, Hexpat is designed to allow for chunked
I/O, but as of this writing I haven't done a nice integration with
enumerator and friends.

/IO/ is filed under /Internal/ because it's low-level and most users won't
want it. The other /Internal/ modules are re-exported by /Annotated/,
/Tree/ and /Extended/, so you won't need to import them directly.

Credits to Iavor Diatchki and the @xml@ (XML.Light) package for /Proc/ and
/Cursor/. Thanks to the many contributors.

ChangeLog: 0.15 changes intended to fix a (rare) \"error: a C finalizer
called back into Haskell.\" that seemed only to happen only on ghc6.12.X;
0.15.1 Fix broken Annotated parse; 0.16 switch from mtl to transformers;
0.17 fix mapNodeContainer & rename some things.; 0.18 rename
defaultEncoding to overrideEncoding. 0.18.3 formatG and indent were
demanding list items more than once (inefficient in chunked processing);
0.19 add Extended.hs; 0.19.1 fix a memory leak introduced in 0.19, delegate
parsing to bound thread if unbound (see note above); 0.19.2 include expat
source code so \'cabal install\' just works on Linux, Mac and Windows
(thanks Jacob Stanley); 0.19.3 fix misconfiguration of expat which broke
entity parsing; 0.19.4 bump version constraint for text; 0.19.5 bump text
to < 0.12 and fix text-0.10.0.1 breakage; 0.19.6 dependency breakage with
List; 0.19.7 ghc-7.2.1 compatibility; 0.19.8 fix space leak on lazy parse
under ghc-7.2.1; 0.19.9 fix formatting of > character + improve
performance; 0.19.10 ghc-7.4.x compatibility; 0.20.1 fix an unfortunate
crash when used in parallel processing and greatly improve performance;
0.20.2 make parseSaxG lazier.

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.20.3-alt2
- rebuild

* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.20.3-alt1
- Spec created by cabal2rpm 0.20_08
