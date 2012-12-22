%define ghc_version 7.6.1
%define hsc_name ghc
%define hsc_version %ghc_version
%define hsc_namever %hsc_name%hsc_version
%define h_pkg_name cryptohash
%define f_pkg_name cryptohash
%define pkg_libdir %_libdir/%hsc_name-%hsc_version/lib/%h_pkg_name-%version

Name: %hsc_namever-%f_pkg_name
Version: 0.8.2
Release: alt1
License: BSD3
Packager: Denis Smirnov <mithraen@altlinux.ru>
Group: Development/Haskell
Url: http://github.com/vincenthz/hs-cryptohash
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: collection of crypto hashes, fast, pure and practical



# Automatically added by buildreq on Sat Dec 22 2012 (-bb)
# optimized out: elfutils ghc7.4.2-common ghc7.6.1-common libgmp-devel pkg-config python-base rpm-build-haskell
BuildRequires: ghc7.6.1 ghc7.6.1-doc

%description
A collection of crypto hashes, with a practical incremental and one-pass,
pure APIs, with performance close to the fastest implementations available
in others languages.

The implementations are made in C with a haskell FFI wrapper that hide the
C implementation.

Simple examples using the unified API:

> import Crypto.Hash > > sha1 :: ByteString -> Digest SHA1 > sha1 = hash >
> hexSha3_512 :: ByteString -> String > hexSha3_512 bs = show (hash bs ::
Digest SHA3_512)

Simple examples using the module API:

> import qualified Crypto.Hash.SHA1 as SHA1 > > main = putStrLn $ show $
SHA1.hash (Data.ByteString.pack [1..256])

> import qualified Crypto.Hash.SHA3 as SHA3 > > main = putStrLn $ show $
digest > where digest = SHA3.finalize ctx > ctx = foldl' SHA3.update iCtx
(map Data.ByteString.pack [ [1,2,3], [4,5,6] ] > iCtx = SHA3.init 224

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
* Sat Dec 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.8.2-alt1
- Spec created by cabal2rpm 0.20_08
