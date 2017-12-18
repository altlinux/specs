
%define common_lisp_controller 0

# generate/package docs
%define docs 1

# define to enable verbose build for debugging
#define sbcl_verbose 1
%define sbcl_shell /bin/bash

Name: sbcl
Summary: Steel Bank Common Lisp
Version: 1.4.2
Release: alt1
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group: Development/Lisp
License: BSD
Url: http://sbcl.sourceforge.net/
Source0: http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-%version-source.tar.bz2

ExclusiveArch: %arm %ix86 x86_64 ppc sparcv9

# Pre-generated html docs
Source1: http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-%version-documentation-html.tar.bz2

## x86 section
#Source10: http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.0.15-x86-linux-binary.tar.bz2
%ifarch %ix86
%define sbcl_arch x86
BuildRequires: sbcl
# or
#define sbcl_bootstrap_src -b 10
%endif

## x86_64 section
#Source20: http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.2.0-x86-64-linux-binary.tar.bz2
%ifarch x86_64
%define sbcl_arch x86-64
BuildRequires: sbcl
# or
#define sbcl_bootstrap_src -b 20
#define sbcl_bootstrap_dir sbcl-1.2.0-x86-64-linux
%endif

## ppc section
# Thanks David!
#Source30: sbcl-1.0.1-patched_el4-powerpc-linux.tar.bz2
#Source30: sbcl-1.0.1-patched-powerpc-linux.tar.bz2
%ifarch ppc
%define sbcl_arch ppc
BuildRequires: sbcl
# or
#define sbcl_bootstrap_src -b 30
%endif

## sparc section
#Source40: http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-0.9.17-sparc-linux-binary.tar.bz2
%ifarch sparcv9
%define sbcl_arch sparc
BuildRequires: sbcl
# or
#define sbcl_bootstrap_src -b 40
%endif

## arm section
#Source50: http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.2.0-armel-linux-binary.tar.bz2
%ifarch armv5tel
%define sbcl_arch arm
BuildRequires: sbcl
# or
#define sbcl_bootstrap_src -b 50
#define sbcl_bootstrap_dir sbcl-1.2.0-armel-linux
%endif

#Source60: http://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.2.0-armhf-linux-binary.tar.bz2
# generated on a fedora20 arm box, sf bootstrap missing sb-gmp
#Source60: sbcl-1.2.0-armhf-linux-binary-2.tar.bz2
%ifarch armv6hl armv7hl
%define sbcl_arch arm
BuildRequires: sbcl
# or
#define sbcl_bootstrap_src -b 60
#define sbcl_bootstrap_dir sbcl-1.2.0-armhf-vfp
%endif

%if 0%{?common_lisp_controller}
BuildRequires: common-lisp-controller
Requires: common-lisp-controller
Requires(post): common-lisp-controller
Requires(preun): common-lisp-controller
Source200: sbcl.sh
Source201: sbcl.rc
Source202: sbcl-install-clc.lisp
%endif

Patch1: %name-1.0-lib_dir.patch
Patch2: sbcl-1.1.13-personality.patch
Patch3: sbcl-1.3.2-optflags.patch
Patch6: sbcl-0.9.5-verbose-build.patch
Patch7: sbcl-1.4.2-runtime.patch

## upstreamable patches
Patch50: sbcl-1.3.0-generate_version.patch




## upstream patches

# %%check/tests
BuildRequires: ed /proc sbcl /usr/bin/tex
BuildRequires: hostinfo coreutils
%if 0%{?docs}
#Requires(post): /sbin/install-info
#Requires(preun): /sbin/install-info
# doc generation
BuildRequires: ghostscript
BuildRequires: texinfo
BuildRequires: time
%endif

%description
Steel Bank Common Lisp (SBCL) is a Open Source development environment
for Common Lisp. It includes an integrated native compiler,
interpreter, and debugger.

%prep
%setup -c -n sbcl-%version -a 1 %{?sbcl_bootstrap_src}

pushd sbcl-%version
%patch1 -p1 
%patch2 -p1 -b .personality
%patch3 -p1 -b .optflags
%{?sbcl_verbose:%patch6 -p1 -b .verbose-build}
%ifarch x86_64
%patch7 -p1
%endif
%patch50 -p1 -b .generate_version

%__subst "s|/usr/lib/sbcl/|%_libdir/sbcl/|" src/runtime/runtime.c

# fix permissions (some have eXecute bit set)
find . -name '*.c' | xargs chmod 644

# set version.lisp-expr
sed -i.rpmver -e "s|\"%version\"|\"%version-%release\"|" version.lisp-expr

# make %%doc items available in parent dir to make life easier
cp -alf BUGS COPYING README CREDITS NEWS TLA TODO PRINCIPLES ..
ln -s sbcl-%version/doc ../doc
popd

%build
pushd sbcl-%version

export SBCL_HOME=%_libdir/sbcl/
export INSTALL_ROOT=%prefix


#export SBCL_HOME=%prefix/lib/sbcl
%{?sbcl_arch:export SBCL_ARCH=%sbcl_arch}
%{?sbcl_shell} \
./make.sh \
  --prefix=%prefix \
  %{?sbcl_bootstrap_dir:--xc-host="`pwd`/../%sbcl_bootstrap_dir/run-sbcl.sh"}

# docs
%if 0%{?docs}
make -C doc/manual info

# Handle pre-generated docs
tar xvjf %SOURCE1
cp -av %name-%version/doc/manual/* doc/manual/
%endif
popd

%install
pushd sbcl-%version
mkdir -p %buildroot{%_bindir,%_libdir,%_mandir}

#unset SBCL_HOME

export INSTALL_ROOT=%buildroot%prefix
export LIB_DIR=%buildroot%_libdir

%{?sbcl_shell} ./install.sh



%if 0%{?common_lisp_controller}
install -m744 -p -D %SOURCE200 %buildroot%_libdir/common-lisp/bin/sbcl.sh
install -m644 -p -D %SOURCE201 %buildroot%_sysconfdir/sbcl.rc
install -m644 -p -D %SOURCE202 %buildroot%_libdir/sbcl/install-clc.lisp
# linking ok? -- Rex
cp -p %buildroot%prefix/lib/sbcl/sbcl.core %buildroot%_libdir/sbcl/sbcl-dist.core
%endif
popd

## Unpackaged files
rm -rfv %buildroot%_docdir/sbcl
rm -fv  %buildroot%_infodir/dir
# CVS crud
find %buildroot -name CVS -type d | xargs rm -rfv
find %buildroot -name .cvsignore | xargs rm -fv
# 'test-passed' files from %%check
find %buildroot -name 'test-passed' | xargs rm -vf

%check
pushd sbcl-%version
ERROR=0
# sanity check, essential contrib modules get built/included?
CONTRIBS="sb-posix.fasl sb-bsd-sockets.fasl"
for CONTRIB in $CONTRIBS ; do
  if [ ! -f %buildroot%_libdir/sbcl/contrib/$CONTRIB ]; then
    echo "WARNING: ${CONTRIB} awol!"
    ERROR=1
    echo "ulimit -a"
    ulimit -a
  fi
done
pushd tests
# verify --version output
#test "$(source ./subr.sh; SBCL_ARGS= run_sbcl --version 2>/dev/null | cut -d' ' -f2)" = "%version-%release"
test "$(. ./subr.sh; "$SBCL_RUNTIME" --core "$SBCL_CORE" --version --version 2>/dev/null | cut -d' ' -f2)" = "%{version}-%{release}"
# still seeing Failure: threads.impure.lisp / (DEBUGGER-NO-HANG-ON-SESSION-LOCK-IF-INTERRUPTED)
time %{?sbcl_shell} ./run-tests.sh ||:
popd
exit $ERROR
popd

#mkdir -p %buildroot{%_libdir/sbcl/contrib,%_libdir/sbcl/site-systems}
#mv %buildroot%prefix/lib/sbcl/* %buildroot%_libdir/sbcl/*
#mv %buildroot%prefix/lib/contrib/* %_libdir/sbcl/contrib/
#mv %buildroot%prefix/lib/site-systems/* %_libdir/sbcl/site-systems/


%post
%if 0%{?common_lisp_controller}
/usr/sbin/register-common-lisp-implementation sbcl > /dev/null 2>&1 ||:
%endif

%preun

%if 0%{?common_lisp_controller}
/usr/sbin/unregister-common-lisp-implementation sbcl > /dev/null 2>&1 ||:
%endif


%files
%doc COPYING
%doc BUGS CREDITS NEWS PRINCIPLES README TLA TODO
%_bindir/sbcl
%dir %_libdir/sbcl/
%_libdir/sbcl/contrib/
%_libdir/sbcl/sbcl.mk
%_man1dir/sbcl.1*
%if 0%{?docs}
%doc doc/manual/sbcl.html
%doc doc/manual/asdf.html
#_infodir/asdf.info*
#_infodir/sbcl.info*
%endif
%if 0%{?common_lisp_controller}
%_libdir/common-lisp/bin/*
%_libdir/sbcl/install-clc.lisp
%_libdir/sbcl/sbcl-dist.core
%verify(not md5 size) %_libdir/sbcl/sbcl.core
%config(noreplace) %_sysconfdir/sbcl.rc
%else
%_libdir/sbcl/sbcl.core
%endif

%changelog
* Mon Dec 18 2017 Ilya Mashkin <oddity@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Thu Aug 24 2017 Ilya Mashkin <oddity@altlinux.ru> 1.3.20-alt1
- 1.3.20

* Wed May 31 2017 Ilya Mashkin <oddity@altlinux.ru> 1.3.18-alt1
- 1.3.18

* Tue Mar 28 2017 Ilya Mashkin <oddity@altlinux.ru> 1.3.16-alt1
- 1.3.16

* Thu Feb 02 2017 Ilya Mashkin <oddity@altlinux.ru> 1.3.14-alt1
- 1.3.14

* Fri Dec 02 2016 Ilya Mashkin <oddity@altlinux.ru> 1.3.12-alt1
- 1.3.12

* Mon Oct 03 2016 Ilya Mashkin <oddity@altlinux.ru> 1.3.10-alt1
- 1.3.10

* Fri Aug 12 2016 Ilya Mashkin <oddity@altlinux.ru> 1.3.8-alt1
- 1.3.8

* Thu Jun 02 2016 Ilya Mashkin <oddity@altlinux.ru> 1.3.6-alt1
- 1.3.6

* Wed Apr 06 2016 Ilya Mashkin <oddity@altlinux.ru> 1.3.4-alt1
- 1.3.4

* Sat Mar 19 2016 Ilya Mashkin <oddity@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Tue Oct 06 2015 Ilya Mashkin <oddity@altlinux.ru> 1.2.16-alt1
- 1.2.16

* Wed Sep 09 2015 Ilya Mashkin <oddity@altlinux.ru> 1.2.15-alt1
- 1.2.15
- sync spec with FC
- docs from SF
- info removed

* Wed Oct 30 2013 Ilya Mashkin <oddity@altlinux.ru> 1.1.12-alt1
- 1.1.12

* Wed Sep 04 2013 Ilya Mashkin <oddity@altlinux.ru> 1.1.11-alt1
- 1.1.11

* Sun Apr 07 2013 Ilya Mashkin <oddity@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Wed Mar 06 2013 Ilya Mashkin <oddity@altlinux.ru> 1.1.5-alt1
- 1.1.5

* Sun Dec 16 2012 Ilya Mashkin <oddity@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Tue Aug 27 2012 Ilya Mashkin <oddity@altlinux.ru> 1.0.58-alt1
- 1.0.58

* Fri Apr 27 2012 Ilya Mashkin <oddity@altlinux.ru> 1.0.56-alt1
- 1.0.56

* Sat Jan 07 2012 Ilya Mashkin <oddity@altlinux.ru> 1.0.54-alt1
- 1.0.54

* Wed Sep 14 2011 Ilya Mashkin <oddity@altlinux.ru> 1.0.51-alt1
- 1.0.51

* Mon Aug 15 2011 Ilya Mashkin <oddity@altlinux.ru> 1.0.50-alt1
- 1.0.50

* Mon Jun 13 2011 Ilya Mashkin <oddity@altlinux.ru> 1.0.49-alt1
- 1.0.49

* Sat Mar 26 2011 Ilya Mashkin <oddity@altlinux.ru> 1.0.46-alt1
- 1.0.46

* Sat Feb 19 2011 Ilya Mashkin <oddity@altlinux.ru> 1.0.45-alt1
- 1.0.45

* Tue Dec 21 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.44-alt0.M51.4
- Build for 5.1

* Sun Dec 05 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.44-alt4
- fix path to sbcl

* Sat Dec 04 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.44-alt3
- fix build again
- fix build on x86_64

* Fri Dec 03 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.44-alt2
- fix build

* Thu Nov 25 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.44-alt1
- 1.0.44

* Sat Oct 30 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.42-alt1
- 1.0.42

* Sun Jul 25 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.40-alt1
- 1.0.40

* Wed Jun 02 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.39-alt1
- 1.0.39

* Sat May 08 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.38-alt1
- 1.0.38

* Mon Dec 14 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.33-alt1
- 1.0.33
- SBCL's 10th Anniversary

* Fri Oct 30 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.32-alt1
- 1.0.32

* Sun Sep 06 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.30-alt1
- 1.0.30 (Closes: 21374)
- remove unneeded Mac OS X files

* Thu Jul 23 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.29-alt1
- 1.0.29

* Tue Mar 17 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.25-alt1
- 1.0.25

* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.24-alt1
- 1.0.24

* Sun Dec 14 2008 Ilya Mashkin <oddity@altlinux.ru> 1.0.23-alt1
- 1.0.23
- Dedicated to the 50th birthday of Lisp

* Sat Dec 15 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.12-alt1
- 1.0.12

* Fri Sep 21 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.9-alt1
- 1.0.9
- remove Russian description

* Fri May 04 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Thu Jan 11 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Sat Dec 16 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0-alt1
- 1.0

* Sun Oct 08 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.9.17-alt1
- 0.9.17

* Sat Mar 18 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.9.10-alt2
- rebuild with sbcl as compilation host

* Thu Mar 16 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.9.10-alt1
- new version
- using clisp as cross-compilation host
- builds on x86_64

* Wed Jan 11 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.9.8-alt2
- package /usr/lib/sbcl

* Mon Jan 09 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.9.8-alt1
- new version

* Fri Oct 14 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.9.5-alt1
- new version

* Sat Dec 11 2004 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.17-alt1
- new varsion

* Thu Sep 23 2004 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.14-alt1
- new version

* Sun Jul 18 2004 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.9.55-alt0.1
- rebuild

* Thu Mar 25 2004 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.8-alt3
- autoreq bug fixed

* Mon Mar 22 2004 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.8-alt2
- new version

* Sun Jan 18 2004 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.6-alt4
core path fixed

* Wed Jan 14 2004 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.6-alt3
Install_root fixed

* Thu Dec 25 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.6-alt2
core path bug fixed

* Wed Dec 17 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.6-alt1
- New version

* Fri Aug 29 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.3-alt1
- new version

* Tue Jun 24 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.0-alt1
- new version

* Tue Jan 07 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.7.11-alt1cvs0
- new version (with some modifications from CVS)

* Mon Dec 09 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.7.10-alt2
- spec cleanup

* Tue Dec 03 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.7.10-alt1
- new version

* Sat Oct 05 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.7.8-alt1
- 0.7.8 release

* Thu Aug 15 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.7.6-alt1
- 0.7.6 release

* Tue Jun 25 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.7.5-alt1
- 0.7.5 release

* Tue Apr 30 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.7.3-alt1
- 0.7.3 release

* Sun Jan 27 2002 Vitaly Lugovsky <warlock@skeptik.net>
- Bootstrap requirement added (rebuild)

* Sun Jan 27 2002 Vitaly Lugovsky <warlock@skeptik.net>
- First RPM release.

