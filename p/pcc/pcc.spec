# Use our own configure in order to prevent --target, which makes autotools believe we are cross compiling
%global pccconfigure \
 export CFLAGS="${FLAGS}"; \
 export CXXFLAGS="${FLAGS}"; \
 export FFLAGS="${FLAGS}"; \
 ./configure --program-prefix= --prefix=%prefix --exec-prefix=%prefix --bindir=%_bindir --sbindir=%_sbindir --sysconfdir=%_sysconfdir --datadir=%_datadir --includedir=%_includedir --libdir=%_libdir --libexecdir=%_libexecdir --localstatedir=%_localstatedir --sharedstatedir=%_sharedstatedir --mandir=%_mandir --infodir=%_infodir

# Use pcc to build? (This option is for sanity testing the compiler)
%global usepcc 0
# RPM does not play well with pcc compiled package
%if %usepcc
%define debug_package %nil
%endif

# Release tag
%global rel 1

Name: pcc
Version: 1.0.0
%if %usepcc
Release: alt1
%else
Release: alt1
%endif
Summary: The Portable C Compiler
Group: Development/C
License: BSD with advertising and BSD and ISC
Url: http://pcc.ludd.ltu.se/
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: ftp://pcc.ludd.ltu.se/pub/pcc-releases/pcc-%version.tgz
Source1: ftp://pcc.ludd.ltu.se/pub/pcc-releases/pcc-libs-%version.tgz
# Patch to disable the use of -g on pcc-libs-090805/csu/linux/crtbegin.c which is partly assembler code
Patch0: pcc-090808-optflags.patch

# Currently only x86 and x86_64 supported both in ppc and ppc-libs

BuildRequires: bison flex
Requires: glibc-devel

%if %usepcc
BuildRequires: pcc
%endif

%description
The compiler is based on the original Portable C Compiler by Stephen C.
Johnson, written in the late 70's. Even though much of the compiler has been
rewritten, some of the basics still remain.
PCC debuted in Unix Version 7 and replaced the DMR compiler (Dennis Ritchie's
original C compiler) in both System V and the BSD 4.x releases. Some history
about pcc is in the A History of UNIX before Berkeley: UNIX Evolution:
1975-1984 and in the Evolution of C.

About 50%% of the frontend code and 80%% of the backend code has been rewritten.
Most stuff is written by Anders Magnusson, with the exception of the data-flow
analysis part and the SSA conversion code which is written by Peter A Jonsson,
and the Mips port that were written as part of a project by undergraduate
students at Lulea University of Technology (LTU).

Caution: the compiler is still undergoing heavy development.

%prep
%setup -q -a1
# Get rid of the default optimization flag
find . -name Makefile.in |xargs sed -i 's| -O | |g'
# Rename the libs directory for the patch to work
mv pcc-libs-%version pcc-libs
# Apply patch
%patch0 -p1

%build
# Set architecture directory needed for include flag
%ifarch x86_64
export archdir=amd64
%endif
%ifarch %ix86
export archdir=i386
%endif

# Use pcc to build?
%if %usepcc
export FLAGS="-g"
export CC="pcc"
export CPP="pcc -E"
%else
export FLAGS="%optflags"
export CC="gcc"
export CPP="gcc -E"
%endif

# Flags for files that can't be built as debug
export CFLAGS_NODEBUG=`echo ${FLAGS}|sed "s|-g||g"`

# First, build the library.
cd pcc-libs
%pccconfigure
make CFLAGS="-I${archdir} -Ilinux -I. ${FLAGS}" CFLAGS_NODEBUG="-I${archdir} -Ilinux -I. $CFLAGS_NODEBUG"
#%{?_smp_mflags}
cd ..
# Then, build the compiler
%pccconfigure --with-assembler=%_bindir/as --with-linker=%_bindir/ld \
 --with-libdir=%_libdir --with-incdir=%_includedir --enable-tls
make
#%{?_smp_mflags}

%install

# Install the libraries
make -C pcc-libs install DESTDIR=%buildroot strip=no
# Install the compiler
make install DESTDIR=%buildroot strip=no
# Fix man file perms
chmod 644 %buildroot%_mandir/man1/*
# Rename cpp man page
mv  %buildroot%_mandir/man1/{,pcc-}cpp.1
# Directory for pcc-specific include files
mkdir -p %buildroot%_includedir/pcc


%files
%_bindir/pcc
%_libdir/pcc/
%_includedir/pcc/
%_libexecdir/cpp
%_libexecdir/ccom
%_mandir/man1/ccom.1.*
%_mandir/man1/pcc-cpp.1.*
%_mandir/man1/pcc.1.*

%changelog
* Sat Apr 09 2011 Ilya Mashkin <oddity@altlinux.ru> 1.0.0-alt1
- Initial build for ALT Linux

* Fri Apr 01 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.0-1
- Switch to using stable releases.
- Update to 1.0.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-0.4.20110203cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-0.4.20110203cvs
- Update to 20110203.

* Fri Nov 19 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-0.4.101119cvs
- Update to 20101119. x86_64 works now.
- Added possibility in the spec file to build pcc with itself.

* Wed Apr 14 2010 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-0.4.100413cvs
- Update to 20100413.

* Sun Aug 16 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-0.4.090816cvs
- Update to 20090816, adding support for x86_64.
- Use own configure macro to disable cross compilation.

* Thu Aug 13 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-0.3.090813cvs
- Removed unneeded BR: byacc.
- Update to 20090813.

* Tue Aug 11 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-0.2.090811cvs
- Spec file cleanups.
- Update to 20090811.

* Sun Aug 09 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-0.2.090809cvs
- Changed --with-libdir to %%{_libdir} to make pcc use the glibc version of
  crt0.o by suggestion of upstream.
- Update to 20090809.

* Sat Aug 08 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 0.9.9-0.1.090808cvs
- First release.
