# llvm needs for unregisterised architectures
%ifarch armh aarch64
%define _llvm_version 12.0
%define optflags_lto %nil
%endif

%ifarch aarch64
# configure: error: Your linker is affected by binutils #16177 on armh
%def_disable ld_override
%endif

%def_with bootstrap

Name: ghc9.2.8
Version: 9.2.8
Release: alt1

Summary: Glasgow Haskell Compilation system
License: BSD-3-Clause and HaskellReport
Group: Development/Haskell
Url: http://haskell.org/ghc/

Source: %name-%version.tar
Source1: ghc.macros
Patch: ghc-%version-%release.patch

Requires: libffi-devel libgmp-devel
# <https://bugzilla.altlinux.org/show_bug.cgi?id=31576>:
# maybe this bug requires more investigation to understand
# who goes crazy: a GHC lib or glibc,
# but now we simply work-around it:
Requires: glibc-gconv-modules

# The installed Haskell libs will be processed:
Requires(pre,postun): haskell-filetrigger >= 0.0.5-alt3
# <https://www.altlinux.org/RPM_Macros_Packaging_Policy>:
Requires: rpm-build-haskell >= 1.4.6-alt1
# (rpm-build-haskell-1-alt26 has been adapted to allow builds
# of Haskell modules without ghcN.N.N-common.)

# For ghc-pkg with rpath running during install, see:
# https://www.altlinux.org/Hasher/FAQ
# https://lists.altlinux.org/pipermail/devel/2018-April/204171.html
# Not needed after rebuild with separate single directory for shared libraries
BuildRequires: /proc

# Bootstrap with the previous version
%if_with bootstrap
BuildPreReq: ghc8.10.7-common
%else
BuildPreReq: ghc9.2.8-common
%endif

# Generally, this could work with APT, after the "ghc" pseudo-package
# is brought back through Provides (allowing to rebuild this package in
# different environments):
#
# <https://ghc.haskell.org/trac/ghc/wiki/Building/Preparation/Tools>:
# In general, we support building with the previous 2 major releases, e.g.:
#BuildPreReq: ghc >= 7.2
# Newer GHC may be incompatible with the code of the current GHC:
#BuildPreReq: ghc <= %version

# Automatically added by buildreq on Fri Apr 26 2013
# optimized out: ghc7.6.1-common gnu-config libgpg-error libtinfo-devel pkg-config python-base time xml-common xml-utils zlib-devel
BuildRequires: binutils-devel docbook-dtds docbook-style-xsl libelf-devel libffi-devel libgmp-devel libncurses-devel xsltproc

# Can't build when installed
#BuildRequires: dblatex

# Needs for build man
BuildRequires: python3-module-sphinx-sphinx-build-symlink

%def_without hscolour
%if_with hscolour
BuildRequires: ghc(hscolour)
%endif

Provides: haskell(abi) = %version

%ifarch armh aarch64
BuildRequires: rpm-macros-llvm-common
BuildRequires: llvm%{?_llvm_version}
Requires: llvm%{?_llvm_version}
%endif

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

%package common
BuildArch: noarch
Summary: Selects the default version of Glasgow Haskell Compilation system
Group: Development/Haskell

Provides: ghc = %EVR
Conflicts: ghc < %EVR
Conflicts: ghc > %EVR

Requires: %name = %EVR
Requires: rpm-macros-%{name}-common = %EVR

# <https://www.haskell.org/ghc/download_ghc_7_6_1>:
Conflicts: cabal-install < 0.8

Conflicts: ghc7.4.1-common
Conflicts: ghc7.4.2-common

%description common
Install this package to select %version as the default version
of Glasgow Haskell Compiler.

It will provide the common names for the GHC executables
(like unversioned /usr/bin/ghc).

And it will make rpm-build-haskell use this version of GHC for
building other Haskell packages
(if their .spec refers to %%ghc_version and %%_ghclibdir).

%package libs
Summary: Dynamic libraries of Glasgow Haskell Compilation system
Group: Development/Haskell

%description libs
Dynamic link libraries Glasgow Haskell Compiler.
It will automaticaly requires by not static applications.

%package -n rpm-macros-%{name}-common
Summary: Set of RPM macros for packaging %name-based applications
Group: Development/Other
# uncomment if macroses are platform-neutral
BuildArch: noarch
# helps old apt to resolve file conflict at dist-upgrade (thanks to Stanislav Ievlev)
Conflicts: ghc7.6.1-common <= 7.6.1-alt1

Conflicts: rpm-macros-ghc7.6.1-common
Provides: rpm-macros-ghc-common = %EVR
Conflicts: rpm-macros-ghc-common < %EVR
Conflicts: rpm-macros-ghc-common > %EVR

%description -n rpm-macros-%{name}-common
Set of RPM macros for packaging %name-based applications for ALT Linux.
Install this package if you want to create RPM packages that use %name.

%package doc
Summary: Documentation for GHC
Group: Development/Haskell

%description doc
Preformatted documentation for the Glasgow Haskell Compiler
(GHC) and its libraries. Install it if you like to have local
access to the documentation in PostScript and HTML format.
Alternatively, the documentation is available online at
http://haskell.org/ghc/documentation.html

%prep
%setup
%patch -p1
%ifarch armh aarch64
sed -ri '/^BuildFlavour/ s,perf$,perf-llvm,' mk/build.mk
%endif

%build
%ifarch armh
%define _configure_target armv7l-unknown-linux-gnueabihf
%else
%define _configure_target %nil
%endif
#autoreconf -fisv
./boot
%configure --with-system-libffi --disable-unregisterised %{?_disable_ld_override:--disable-ld-override}
# Work around for haddock build trouble:
#  commitAndReleaseBuffer: invalid argument (invalid character)
# https://gitlab.haskell.org/ghc/ghc/-/issues/8118
export LC_ALL=C.UTF-8
%make_build V=1

%install
%define docdir %_docdir/%name-%version
%makeinstall_std docdir=%docdir
mv %buildroot%docdir/html/* %buildroot%docdir/
rmdir %buildroot%docdir/html

# generate fake .pkg configs for core packages.
# haskell.prov will convert them to package provides.
for lib in %buildroot%_libdir/ghc-%version/*-[0-9]*; do
       namever="$(basename "$lib")"
       name="${namever%%-*}"
       echo -e "name: $name\nversion: ${namever##*-}" >"$lib/$name.pkg"
done
cp -a LICENSE README.md %buildroot%docdir/

# generate the file list for lib/ _excluding_ all files needed for profiling
# only
#
# * generating file lists in a BUILD_ROOT spec is a bit tricky: the file list
#   has to contain complete paths, _but_ without the BUILD_ROOT, we also do
#   _not_ want to have directory names in the list; furthermore, we have to make
#   sure that any leading / is removed from %%_libdir, as find has to
#   interpret the argument as a relative path; however, we have to include the
#   leading / again in the final file list (otherwise, rpm complains)
# * isn't there an easier way to do all this?
{
pushd %buildroot >/dev/null
find .%_libdir ! -type d ! -name 'package.conf*' \
     -print | sed 's|^\.||'
find .%_libdir -type d -print | sed 's|^\.|%%dir |'
popd >/dev/null
} > rpm-files 

# touch our "ghost". ghc-pkg may create him later.
touch %buildroot%_libdir/ghc-%version/package.conf.old
# package-provided *.confs go in this directory:
mkdir -p %buildroot%_libdir/ghc-%version/package.conf.d

# generate separate single directory for core dynamic libraries
mkdir -p %buildroot%_libdir/ghc-%version/lib
for so in %buildroot%_libdir/ghc-%version/*/*-ghc%version.so; do
       relpath="$(relative "$so" "%buildroot%_libdir/ghc-%version/lib/")"
       ln -s "$relpath" %buildroot%_libdir/ghc-%version/lib/
done

mkdir -p %buildroot%_sysconfdir/ld.so.conf.d
echo "%_libdir/ghc-%version/lib" >%buildroot%_sysconfdir/ld.so.conf.d/ghc-%version.conf

# need for multiple ghc versions installed
for s in hp2ps hpc hsc2hs; do
    mv %buildroot%_bindir/"$s" %buildroot%_bindir/"$s"-%version
    ln -s "$s"-%version %buildroot%_bindir/"$s"
done

# Check the correctness of our packaging:
# all unversioned executables must be symlinks:
for s in %buildroot%_bindir/*; do
    case "$s" in
    *-%{version}) :
    ;;
    *) test -L "$s"
    ;;
    esac
done

mv %buildroot%_man1dir/ghc.1 %buildroot%_man1dir/%name.1

sed -i 's!/html/!/!' %buildroot%_libdir/ghc-%version/package.conf.d/*.conf

# install and fix up the macros file
mkdir -p %buildroot%_rpmmacrosdir
install %SOURCE1 %buildroot%_rpmmacrosdir/ghc
sed -i 's/@GHC_VERSION@/%version/' %buildroot%_rpmmacrosdir/ghc

%files
%dir %_libdir/ghc-%version
%_libdir/ghc-%version
%dir %docdir/
%docdir/[ALR]*
%_bindir/*-%version
%_man1dir/%name.1*
%ghost %_libdir/ghc-%version/package.conf.old
%dir %_libdir/ghc-%version/package.conf.d
%exclude %_libdir/ghc-%version/*/*-ghc%version.so
%exclude %_libdir/ghc-%version/lib

%files libs
%dir %_libdir/ghc-%version/lib
%_libdir/ghc-%version/lib/*.so
%_libdir/ghc-%version/*/*-ghc%version.so
%config %_sysconfdir/ld.so.conf.d/ghc-%version.conf

%files common
%exclude %_bindir/*-%version
%_bindir/*

%files -n rpm-macros-%{name}-common
%_rpmmacrosdir/*

%files doc
%docdir/
%exclude %docdir/[AR]*

%changelog
* Tue Aug 29 2023 Evgeny Sinelnikov <sin@altlinux.org> 9.2.8-alt1
- Bootstrap from version 8.10.7 to 9.2.8
- Disabled LTO on armh and aarch64 due link problems with llvm:
  "-latomic is needed for sub-word-sized atomic operations... failed."
- Disabled overriding the default linker use by gcc on armh and aarch64 due
  problems with debugedit "Cannot handle 8-byte build ID" (based on GHC#21570)
- Avoid cycle dependency between basic and common packages
- Backport users-guide compatibility fixes (GHC#23807, GHC#23818)
- Backport update of rdt-theme to latest upstream version (GHC#23444)
- Add work around of haddock build trouble due locale encoding (GHC#8118)
- Fix debugedit problem with 'Cannot handle 8-byte build ID' on armh and aarch64

* Tue Aug 29 2023 Evgeny Sinelnikov <sin@altlinux.org> 9.2.7-alt1
- Bootstrap to version 9.2.7

* Sat Aug 26 2023 Evgeny Sinelnikov <sin@altlinux.org> 9.0.2-alt4
- Rebuild with ghc 9.0.2 after bootstrap

* Sat Aug 26 2023 Evgeny Sinelnikov <sin@altlinux.org> 9.0.2-alt3
- Continue bootstrap from version 8.10.7 to 9.0.2
- Fix build docs: use modern sphinx syntax for extlinks

* Tue Oct 25 2022 Evgeny Sinelnikov <sin@altlinux.org> 9.0.2-alt2
- Import ghc-9.0.2-testsuite to build directory

* Tue Oct 25 2022 Evgeny Sinelnikov <sin@altlinux.org> 9.0.2-alt1
- Bootstrap to version 9.0.2

* Mon Oct 24 2022 Evgeny Sinelnikov <sin@altlinux.org> 8.10.7-alt2
- Rebuild with ghc 8.10.7

* Mon Oct 24 2022 Evgeny Sinelnikov <sin@altlinux.org> 8.10.7-alt1
- Bootstrap to version 8.10.7

* Mon Oct 24 2022 Evgeny Sinelnikov <sin@altlinux.org> 8.10.5-alt2
- Replace dynamic libraries to separate package
- Apply no-missing-haddock-file-warning.patch from Debian/Fedora

* Tue Jun 29 2021 Evgeny Sinelnikov <sin@altlinux.org> 8.10.5-alt1
- Bootstrap to version 8.10.5

* Tue Jun 22 2021 Evgeny Sinelnikov <sin@altlinux.org> 8.6.4-alt6
- Fix build with configuration error in docs/users_guide/conf.py
- Apply patches to avoid haddock warnings from Fedora
- Set right license name in spec file
- Build with llvm-11.0 on armh and aarch64

* Wed Aug 12 2020 Evgeny Sinelnikov <sin@altlinux.org> 8.6.4-alt5
- Rebuild with llvm-10.0 on armh and aarch64

* Wed Aug 12 2020 Evgeny Sinelnikov <sin@altlinux.org> 8.6.4-alt4
- Rebuild with not fixed llvm version on armh and aarch64

* Tue Apr 28 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.6.4-alt3
- built on armh

* Thu Apr 18 2019 Evgeny Sinelnikov <sin@altlinux.org> 8.6.4-alt2
- Rebuild with ghc 8.6.4
- Add requires to llvm for aarch64

* Fri Mar 22 2019 Evgeny Sinelnikov <sin@altlinux.org> 8.6.4-alt1
- Bootstrap to version 8.6.4

* Wed Feb 27 2019 Evgeny Sinelnikov <sin@altlinux.org> 8.6.3-alt4
- Provides haskell(abi) with ld preload for dynamic libraries

* Mon Feb 25 2019 Evgeny Sinelnikov <sin@altlinux.org> 8.6.3-alt3
- Add separate single directory for shared libraries and ld.so.conf file for it

* Wed Feb 20 2019 Evgeny Sinelnikov <sin@altlinux.org> 8.6.3-alt2
- rebuild with ghc 8.6.3

* Wed Feb 20 2019 Evgeny Sinelnikov <sin@altlinux.org> 8.6.3-alt1
- bootstrap to version 8.6.3

* Wed Feb 20 2019 Evgeny Sinelnikov <sin@altlinux.org> 8.2.2-alt2
- rebuild with ghc 8.2.2

* Tue Feb 19 2019 Evgeny Sinelnikov <sin@altlinux.org> 8.2.2-alt1
- bootstrap to version 8.2.2

* Mon Feb 18 2019 Evgeny Sinelnikov <sin@altlinux.org> 7.10.3-alt2
- rebuild with ghc 7.10.3

* Mon Feb 18 2019 Evgeny Sinelnikov <sin@altlinux.org> 7.10.3-alt1
- bootstrap to next version

* Fri Feb 08 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.6.1-alt7
- Applied patches to add support of aarch64 and ppc64le architectures.
- Removed BuilArch: noarch from doc subpackage (ghc generates different
  list of documents for different archirectures).

* Wed Oct 21 2015 Ivan Zakharyaschev <imz@altlinux.org> 7.6.1-alt6.1
- "ghc-pkg recache" went crazy without glibc-gconv-modules (ALT#31576);
  we workaround it for now without an investigation whether it's a Haskell
  lib or glibc which goes crazy.
- Rearranged Reqs/Provs to make them more clear and to prepare for
  independent co-existence of several versions; not yet ready to make
  ghc7.6.1-common optional (it should be installed only to select the
  default GHC).

* Tue Oct 20 2015 Ivan Zakharyaschev <imz@altlinux.org> 7.6.1-alt6
- Simplified the packaging of ghc7.6.1-common.

* Sun Apr 28 2013 Dmitry V. Levin <ldv@altlinux.org> 7.6.1-alt5
- Added libffi-devel runtime requirement because ghc now
  unconditionally adds -lffi to linker options.

* Sat Apr 27 2013 Dmitry V. Levin <ldv@altlinux.org> 7.6.1-alt4
- Reintroduced libgmp-devel runtime requirement.

* Fri Apr 26 2013 Dmitry V. Levin <ldv@altlinux.org> 7.6.1-alt3
- Changed ghc defaults to use -fasm instead of -llvm.
- Built ghc using gcc instead of llvm.
- Fixed documentation packaging.
- Built with system libffi.
- Updated build dependencies.

* Fri Nov 30 2012 Denis Smirnov <mithraen@altlinux.ru> 7.6.1-alt2
- rebuild with ghc 7.6.1

* Sun Oct 07 2012 Denis Smirnov <mithraen@altlinux.ru> 7.6.1-alt1
- bootstrap build

