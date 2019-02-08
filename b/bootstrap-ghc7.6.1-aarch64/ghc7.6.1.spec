Name: bootstrap-ghc7.6.1-aarch64
Version: 0
Release: alt1

Summary: Glasgow Haskell Compilation system
License: BSD style w/o adv. clause
Group: Development/Haskell
Url: http://haskell.org/ghc/

ExclusiveArch: aarch64

Source0: ghc7.6.1-7.6.1-alt7.aarch64.rpm

Provides: ghc7.6.1 = 7.6.1-alt6.1

Requires: libffi-devel libgmp-devel
# <https://bugzilla.altlinux.org/show_bug.cgi?id=31576>:
# maybe this bug requires more investigation to understand
# who goes crazy: a GHC lib or glibc,
# but now we simply work-around it:
Requires: glibc-gconv-modules

Requires: rpm-macros-ghc7.6.1-common

# The installed Haskell libs will be processed:
PreReq: haskell-filetrigger
# <https://www.altlinux.org/RPM_Macros_Packaging_Policy>:
Requires: rpm-build-haskell >= 1-alt26
# (rpm-build-haskell-1-alt26 has been adapted to allow builds
# of Haskell modules without ghcN.N.N-common.)

%description
Haskell is a standard lazy functional programming language; the
current language version is Haskell 98, agreed in December 1998.

GHC is a state-of-the-art programming suite for Haskell.  Included is
an optimising compiler generating good code for a variety of
platforms, together with an interactive system for convenient, quick
development.  The distribution includes space and time profiling
facilities, a large collection of libraries, and support for various
language extensions, including concurrency, exceptions, and foreign
language interfaces (C, C++, whatever).

A wide variety of Haskell related resources (tutorials, libraries,
specifications, documentation, compilers, interpreters, references,
contact information, links to research groups) are available from the
Haskell home page at <http://www.haskell.org/>.

%install
mkdir -p %buildroot
cd %buildroot
rpm2cpio %SOURCE0 | cpio -id

%define oname ghc7.6.1
%define oversion 7.6.1

%files
%_libdir/ghc-%oversion
%_bindir/*-%oversion
%_man1dir/%oname.1*
%dir %_libdir/ghc-%oversion/package.conf.d

%changelog
* Thu Feb 07 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 0-alt1
- Package prebuilt ghc for aarch64 architecture.
