
#define pre_tag pre1
#define pre -%%pre_tag

Summary: CMU Common Lisp compiler
Name: cmucl
Version: 20b
Release: alt2
Packager: Ilya Mashkin <oddity@altlinux.ru>
License: BSD
Group: Development/Lisp
Url: http://www.cons.org/cmucl/
Source0: http://common-lisp.net/project/cmucl/downloads/release/%version%{?pre:/pre-release}/cmucl-src-%version%{?pre}.tar.bz2
#Source1: http://common-lisp.net/project/cmucl/downloads/release/%version%{?pre:/pre-release}/cmucl-src-%version%{?pre}.tar.bz2.asc

# bootstrap available for %%ix86 only: http://bugzilla.redhat.com/185085
ExclusiveArch: %ix86

Source10: http://common-lisp.net/project/cmucl/downloads/release/20b/cmucl-20b-x86-linux.tar.bz2
Source11: http://common-lisp.net/project/cmucl/downloads/release/20b/cmucl-20b-x86-linux.tar.bz2.asc

## ix86 section
%ifarch %ix86
%define cmucl_arch x86
#define bootstrap cmucl
%if "%{?bootstrap}" == "%nil"
%define bootstrap_src -a 10
%else
BuildRequires: cmucl = 20b
%define bootfile -B bootstrap.lisp
%endif
%endif

## x86_64 section
#ifarch x86_64
#endif

## ppc
#ifarch ppc
#endif

BuildRequires: bc
BuildRequires: gettext
BuildRequires: sed
BuildRequires: time
BuildRequires: lesstif-devel

%description
CMUCL is a free, high performance implementation of the Common Lisp
programming language which runs on most major Unix platforms. It
mainly conforms to the ANSI Common Lisp standard. CMUCL provides a
sophisticated native code compiler; a powerful foreign function
interface; an implementation of CLOS, the Common Lisp Object System,
which includes multimethods and a metaobject protocol; a source-level
debugger and code profiler; and an Emacs-like editor implemented in
Common Lisp. CMUCL is maintained by a team of volunteers collaborating
over the Internet, and is mostly in the public domain.

%package extras
Summary: Extra tools and libraries for CMU Common Lisp
Group: Development/Lisp
Requires: %name = %version-%release
%description extras
%summary.

%prep
%setup -q -c %name-%version %{?bootstrap_src}

%build
CFLAGS="$RPM_OPT_FLAGS" ; export CFLAGS

%if 0%{?bootfile:1}
pushd src/bootfiles/19e
cat \
  boot-2008-04-1.lisp \
  boot-2008-06-1.lisp \
  boot-2008-12.lisp \
  boot-2009-01-1.lisp \
  boot-19f.lisp \
 > bootstrap.lisp
popd
%endif

%if 1
## Simple build method

./src/tools/build.sh \
  -b %_target_platform \
  %{?bootfile} \
  -C "linux_gencgc %cmucl_arch" \
  -f x87 \
  -v "%version ALT Linux release %release" \
  %{!?bootstrap:-o "bin/lisp -noinit -batch -fpu x87"}

./src/tools/build.sh \
  -b %_target_platform \
  %{?bootfile} \
  -C "linux_gencgc %cmucl_arch" \
  -f sse2 \
  -v "%version ALT Linux release %release" \
  %{!?bootstrap:-o "bin/lisp -noinit -batch -fpu sse2"}

# make binary dist archives
./src/tools/make-dist.sh %_target_platform-4 %version %cmucl_arch linux

%else
## OLD complicated build method (but needed sometimes, e.g. cross-compiling)

# Create target buildroot
./src/tools/create-target.sh %_target_platform linux_gencgc %cmucl_arch
# Use binary-dist lisp to create initial kernel.core
./src/tools/build-world.sh %_target_platform %{!?bootstrap:bin/lisp}
# build native lisp binary
./src/tools/rebuild-lisp.sh %_target_platform
# Generate lisp.core
./src/tools/load-world.sh %_target_platform "%version ALT Linux release %release"
# rebuild kernel.core using native lisp
./src/tools/build-world.sh %_target_platform %_target_platform/lisp/lisp
# (Re)generate lisp.core
./src/tools/load-world.sh %_target_platform "%version ALT Linux release %release"
# Build auxilary stuff
./src/tools/build-utils.sh %_target_platform
# make binary dist archives
./src/tools/make-dist.sh %_target_platform %version %cmucl_arch linux
%endif

%install


mkdir -p dist
pushd dist
# unarchive newly creating binary dist archives
tar xvjf ../cmucl-%version-%cmucl_arch-linux.tar.bz2
tar xvjf ../cmucl-%version-%cmucl_arch-linux.extra.tar.bz2

mkdir -p %buildroot%prefix/lib/cmucl/
cp -a bin %buildroot%prefix/lib/cmucl/
cp -a lib/cmucl %buildroot%prefix/lib/

mkdir -p %buildroot%_mandir/man1
install -p man/man1/* %buildroot%_mandir/man1/
popd

## Setup app-wrapper
install -m755 -p -D %buildroot%prefix/lib/cmucl/sample-wrapper %buildroot%_bindir/cmucl
# Fixup paths in wrapper
sed -i -e "s|^CMUCLLIB=.*|CMUCLLIB=%prefix/lib/cmucl/lib|" %buildroot%_bindir/cmucl
sed -i -e "s|/<<your-cmucl-path>>|%prefix/lib/cmucl|"      %buildroot%_bindir/cmucl
#
ln -sf cmucl %buildroot%_bindir/cmulisp
# many apps (ie, maxima) expect to find the wrapper named 'lisp' too
ln -sf cmucl %buildroot%_bindir/lisp

## Unpackaged files
rm -f %buildroot%prefix/lib/cmucl/sample-wrapper

# lisp.core contains environment used to build, including %buildroot
QA_SKIP_BUILD_ROOT=1; export QA_SKIP_BUILD_ROOT

%files
%doc dist/doc/cmucl/README dist/doc/cmucl/release*.txt
%_bindir/cmucl
%_bindir/cmulisp
%_bindir/lisp
%dir %prefix/lib/cmucl
%prefix/lib/cmucl/internals.inc
%prefix/lib/cmucl/bin/
%dir %prefix/lib/cmucl/lib
%prefix/lib/cmucl/lib/lisp-x87.core
%prefix/lib/cmucl/lib/lisp-sse2.core
%prefix/lib/cmucl/lib/load-foreign.csh
# %%lang'ize these?  -- Rex
%prefix/lib/cmucl/lib/locale/
%prefix/lib/cmucl/lib/config
%prefix/lib/cmucl/lib/config.lisp
%prefix/lib/cmucl/lib/contrib/
%prefix/lib/cmucl/lib/ext-formats/
%prefix/lib/cmucl/lib/generic-site.lisp
%prefix/lib/cmucl/lib/linker.sh
%prefix/lib/cmucl/lib/lisp.a
%dir %prefix/lib/cmucl/lib/subsystems
%prefix/lib/cmucl/lib/subsystems/gray-*-library.*
%prefix/lib/cmucl/lib/subsystems/iodefs-library.*
%prefix/lib/cmucl/lib/subsystems/simple-*-library.*
%prefix/lib/cmucl/lisp.nm
%prefix/lib/cmucl/lisp.map
%prefix/lib/cmucl/internals.h
%_mandir/man1/*

%files extras
%prefix/lib/cmucl/lib/subsystems/clx-library.*
%prefix/lib/cmucl/lib/subsystems/hemlock-library.*
%prefix/lib/cmucl/lib/subsystems/clm-library.*
%prefix/lib/cmucl/lib/XKeysymDB
%prefix/lib/cmucl/lib/hemlock11.cursor
%prefix/lib/cmucl/lib/hemlock11.mask
%prefix/lib/cmucl/lib/spell-dictionary.bin
%prefix/lib/cmucl/lib/mh-scan
#prefix/lib/cmucl/lib/motifd

%changelog
* Sun Jan 09 2011 Ilya Mashkin <oddity@altlinux.ru> 20b-alt2
- minor spec fixes

* Sat Jan 08 2011 Ilya Mashkin <oddity@altlinux.ru> 20b-alt1
- Build 20b for ALT Linux

* Tue Sep 29 2009 Rex Dieter <rdieter@fedoraproject.org> - 20a-1
- cmucl-20a

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19f-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Mar 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 19f-1
- cmucl-19f
- build both x87 and sse2 cores

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19e-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jun 16 2008 Rex Dieter <rdieter@fedoraproject.org> 19e-1
- cmucl-19e (final)

* Mon Apr 21 2008 Rex Dieter <rdieter@fedoraproject.org> 19e-0.3.pre2
- cmucl-19e-pre2

* Fri Mar 14 2008 Rex Dieter <rdieter@fedoraproject.org> 19e-0.2.pre1
- gcc43 patch

* Thu Mar 13 2008 Rex Dieter <rdieter@fedoraproject.org> 19e-0.1.pre1
- cmucl-19e-pre1

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 19d-6
- Autorebuild for GCC 4.3

* Sat Aug 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 19d-5
- respin (BuildID)

* Fri Aug 10 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 19d-4
- License: BSD
- use rpm bootstrap
- s/Fedora Extras/Fedora/

* Mon Dec 18 2006 Rex Dieter <rdieter[AT]fedoraproject.org> 19d-3
- QA_SKIP_BUILD_ROOT=1

* Wed Nov 22 2006 Rex Dieter <rexdieter[AT]users.sf.net> 19d-2
- move bootstrap sources outside of %%ifarch block

* Thu Nov 16 2006 Rex Dieter <rexdieter[AT]users.sf.net> 19d-1
- cmucl-19d

* Thu Sep 07 2006 Rex Dieter <rexdieter[AT]users.sf.net> 19c-7
- BR: openmotif-devel -> lesstif-devel

* Wed Aug 16 2006 Rex Dieter <rexdieter[AT]users.sf.net> 19c-6
- respin for fc6
- use existing cmucl rpm for bootstrap

* Thu Mar 09 2006 Rex Dieter <rexdieter[AT]users.sf.net> 19c-4
- move bootstrap source outside of %%ifarch block

* Wed Mar 08 2006 Rex Dieter <rexdieter[AT]users.sf.net> 19c-3
- License: +MIT
- BR: bc, time

* Fri Dec 02 2005 Rex Dieter <rexdieter[AT]users.sf.net> 19c-2
- 19c (final)

* Fri Oct 21 2005 Rex Dieter <rexdieter[AT]users.sf.net> 19c-1.pre
- cleanup shared-motif patch
- use simpler build.sh script

* Fri Oct 21 2005 Rex Dieter <rexdieter[AT]users.sf.net> 19c-0.pre1
- 19c-pre1
- drop upstreamed gcc4 patch
- drop unused setarch/personality bits

* Fri Oct 07 2005 Rex Dieter <rexdieter[AT]users.sf.net> 19b-5
- use known-to-be-good cmucl-19a for bootstrap (19b has issues)
- drop personalility patch (not needed afterall)

* Mon Sep 19 2005 Rex Dieter <rexdieter[AT]users.sf.net> 19b-4
- move (re)exec/personality call runprog.c -> lisp.c (in main() )
- optflags patch
- better gcc4 patch
- use my_setarch.c instead of setarch

* Tue Sep 13 2005 Rex Dieter <rexdieter[AT]users.sf.net> 19b-3
- ADDR_NO_RANDOMIZE patch
- gcc4 patch

* Fri Aug 26 2005 Rex Dieter <rexdieter[AT]users.sf.net> 19b-2
- use setarch
- -extras subpkg

* Thu Aug 16 2005 Rex Dieter <rexdieter[AT]users.sf.net> 19b-1
- 19b release
- cleanup for Fedora Extras

* Thu Aug 26 2004 Rex Dieter <rexdieter at sf.net> 0:19-0.fdr.2.a
- Fix Release: 19e -> 19a

* Wed Aug 04 2004 Rex Dieter <rexdieter at sf.net> 0:19-0.fdr.1.a
- cmucl-19a release
- nix -extras subpkg, for now

* Tue Mar 30 2004 Rex Dieter <rexdieter at sf.net> 0:18-0.fdr.2.e
- remove extraneous macros
- include URL's for all Source's.

* Fri Oct 10 2003 Rex Dieter <rexdieter at sf.net> 0:18-0.fdr.1.e
- first try.

