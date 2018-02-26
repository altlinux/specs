%define _libexecdir /usr/libexec
%define buildtarget obj-%_target_platform

Name: mingw32-gcc
Version: 4.4.2
Release: alt1
Summary: MinGW Windows cross-compiler (GCC) for C

License: GPLv3+ and GPLv2+ with exceptions
Group: Development/C

# We use the same source as Fedora's native gcc.
Url: http://gcc.gnu.org
Packager: Boris Savelev <boris@altlinux.org>

Source: gcc-%version.tar
Source2: README.libgcjwebplugin.so
Source3: protoize.1

# RH patches.
Patch00: gcc44-rh-hack.patch
Patch01: gcc44-rh-build-id.patch
Patch02: gcc44-rh-c++-builtin-redecl.patch
Patch03: gcc44-rh-ia64-libunwind.patch
Patch04: gcc44-rh-java-nomulti.patch
Patch05: gcc44-rh-ppc32-retaddr.patch
Patch09: gcc44-rh-pr33763.patch
Patch10: gcc44-rh-rh330771.patch
Patch11: gcc44-rh-rh341221.patch
Patch12: gcc44-rh-java-debug-iface-type.patch
Patch13: gcc44-rh-i386-libgomp.patch
Patch15: gcc44-rh-sparc-config-detection.patch
Patch16: gcc44-rh-libgomp-omp_h-multilib.patch
Patch20: gcc44-rh-libtool-no-rpath.patch
Patch21: gcc44-rh-cloog-dl.patch
Patch24: gcc44-rh-unwind-debug-hook.patch
Patch28: gcc44-rh-pr38757.patch
Patch29: gcc44-rh-libstdc++-docs.patch

# Debian patches.
Patch301: gcc44-deb-gcc-textdomain.patch
Patch311: gcc44-deb-alt-libstdc++-doclink.patch
Patch312: gcc44-deb-libstdc++-man-3cxx.patch
Patch321: gcc44-deb-libjava-stacktrace.patch
Patch322: gcc44-deb-alt-libjava-subdir.patch
Patch323: gcc44-deb-libjava-sjlj.patch
Patch324: gcc44-deb-libjava-disable-static.patch
Patch331: gcc44-deb-boehm-gc-getnprocs.patch
Patch341: gcc44-deb-armv4-eabi.patch
Patch351: gcc44-deb-protoize.patch
Patch361: gcc44-deb-ada-gnatvsn.patch
Patch371: gcc44-deb-libjava-armel-unwind.patch
Patch372: gcc44-deb-armel-hilo-union-class.patch

# ALT patches.
Patch701: gcc43-alt-install.patch
Patch702: gcc43-alt-nowrap.patch
Patch703: gcc43-alt-as-needed.patch
Patch704: gcc44-alt-libgfortran-makefile.patch
Patch705: gcc43-alt-libjava-makefile.patch
Patch706: gcc44-alt-ada-link.patch
Patch707: gcc44-deb-alt-ada-gcc-name.patch
Patch708: gcc43-alt-spp-buffer-size.patch
Patch709: gcc44-deb-alt-defaults-format-security.patch
Patch710: gcc43-alt-defaults-FORTIFY_SOURCE.patch
Patch711: gcc43-alt-defaults-stack-protector.patch
Patch712: gcc43-alt-defaults-relro.patch
Patch713: gcc43-alt-fixinc.patch
Patch714: gcc43-alt-libjava-ltdl.patch
Patch721: gcc43-alt-testsuite.patch
Patch722: gcc44-deb-alt-testsuite-format.patch
Patch723: gcc44-deb-alt-testsuite-printf.patch
Patch724: gcc44-alt-escalate-always-overflow.patch
Patch725: gcc44-alt-arm-pr41684-workaround.patch
Patch726: gcc44-up-libstdc-unpreciousize.patch
Patch750: libiberty.h-asprintf-glibc-2.8.patch

Patch800: libtool.m4-gcj.patch

BuildRequires: texinfo
BuildRequires: rpm-build-mingw32
BuildRequires: mingw32-binutils
BuildRequires: coreutils, cvs
BuildRequires: mingw32-runtime
BuildRequires: mingw32-w32api
BuildRequires: mingw32-pthreads
BuildRequires: libgmp-devel
BuildRequires: libmpfr-devel
BuildRequires: libgomp-devel
BuildRequires: flex

# NB: Explicit mingw32-filesystem dependency is REQUIRED here.
Requires: mingw32-filesystem >= 48
Requires: mingw32-binutils
Requires: mingw32-runtime
Requires: mingw32-w32api
Requires: mingw32-cpp
# libgomp dll is linked with pthreads, but since we don't run the
# automatic dependency scripts, it doesn't get picked up automatically.
Requires: mingw32-pthreads

# We don't run the automatic dependency scripts which would
# normally detect and provide the following DLL:
Provides: mingw32(libgcc_s_sjlj-1.dll)
Provides: mingw32(libgomp-1.dll)

%description
MinGW Windows cross-compiler (GCC) for C.

%package -n mingw32-cpp
Summary: MinGW Windows cross-C Preprocessor
Group: Development/C

%description -n mingw32-cpp
MinGW Windows cross-C Preprocessor

%package c++
Summary: MinGW Windows cross-compiler for C++
Group: Development/C++
Requires: %name = %version-%release

%description c++
MinGW Windows cross-compiler for C++.

%package objc
Summary: MinGW Windows cross-compiler support for Objective C
Group: Development/Objective-C
Requires: %name = %version-%release
#Requires: mingw32-libobjc = %version-%release

%description objc
MinGW Windows cross-compiler support for Objective C.

%package objc++
Summary: MinGW Windows cross-compiler support for Objective C++
Group: Development/Objective-C
Requires: %name-c++ = %version-%release
Requires: %name-objc = %version-%release

%description objc++
MinGW Windows cross-compiler support for Objective C++.

%package gfortran
Summary: MinGW Windows cross-compiler for FORTRAN
Group: Development/Other
Requires: %name = %version-%release

%description gfortran
MinGW Windows cross-compiler for FORTRAN.

%prep
%setup -n gcc-%version

# Set proper version info.
echo %version >gcc/BASE-VER
echo '%distribution %version-%release' >gcc/DEV-PHASE

# RH patches.
%patch00 -p0
%patch01 -p0
%patch02 -p0
%patch03 -p0
%patch04 -p0
%patch05 -p0
%patch09 -p0
#patch10 -p0
%patch11 -p0
%patch12 -p0
%patch13 -p0
%patch15 -p0
%patch16 -p0
#patch20 -p0
%if_with cloog
%patch21 -p0
%endif
%patch24 -p0
%patch28 -p0

# Debian patches.
%patch301 -p2
%patch311 -p2
%patch312 -p2
#patch321 -p2
#patch322 -p2
#patch323 -p2
#patch324 -p2
%patch331 -p2
%patch341 -p2
%patch351 -p2
%patch361 -p0
%ifarch %arm
%patch371 -p2
%patch372 -p2
%endif

# ALT patches.
%patch701 -p0
%patch702 -p0
%patch703 -p0
%patch704 -p0
#patch705 -p0
#patch706 -p0
#patch707 -p0
%patch708 -p0
%patch709 -p0
%patch710 -p0
#patch711 -p0
#patch712 -p0
%patch713 -p0
#patch714 -p0
%patch721 -p0
%patch722 -p2
%patch723 -p2
%patch724 -p1
%patch725 -p1
%patch726 -p0

%patch750 -p0

# Remove -I- gcc option.
find -type f -name Makefile\* -print0 |
	xargs -r0 fgrep -Zle '-I- ' -- |
	xargs -r0 sed -i 's/-I- //g' --

# Disable unwanted multilib builds.
%ifarch x86_64
sed -i 's/\$(CC_FOR_TARGET) --print-multi-lib/echo '"'.;'/" Makefile.*
sed -i 's/\${CC-gcc} --print-multi-lib/echo '"'.;'/" config-ml.in
sed -i 's/\[ -z "\$(MULTIDIRS)" \]/true/' config-ml.in
%endif

find -type f -name \*.orig -delete -print

# Automake >= 1.10 behaviour changed.
find -name Makefile.am -print0 |
	xargs -r0 fgrep -lZ '_LINK = ' -- |
	xargs -r0 sed -i 's/^\([^ ]\+\)_LINK = \$([^ ]\+)/& \$(\1_LDFLAGS)/' --

# Misdesign in libstdc++.
cp -a libstdc++-v3/config/cpu/i{4,3}86/atomicity.h

# remove libjava
rm -rf libjava

# Remove harmful autotools redeclarations.
>config/override.m4

# Replace m4_rename with m4_rename_force to fix build with autoconf >= 2.64.
if fgrep -wqs m4_rename_force %_datadir/autoconf/m4sugar/m4sugar.m4; then
	find -type f -name configure.ac -print0 |
		xargs -r0 fgrep -wlZ 'm4_rename' |
		xargs -r0 sed -i 's/\<m4_rename\>/&_force/' --
fi

# Adjust libstdc++ docs and its doxygen config.
%define onlinedocs http://gcc.gnu.org/onlinedocs
find libstdc++-v3/doc/ -type f -print0 |
	xargs -r0 grep -FZl libstdc++-html-USERS -- |
	xargs -r0 sed -i 's|libstdc++-html-USERS|%onlinedocs/libstdc++/&|' --
find libstdc++-v3/doc/ -type f -print0 |
	xargs -r0 grep -FZl '"latest-doxygen/' -- |
	xargs -r0 sed -i 's|"latest-doxygen/|"%onlinedocs/libstdc++/latest-doxygen/|' --
sed -i "s|\\(^INCLUDE_PATH[[:space:]]\\+=\\)[[:space:]]*$|\\1 $PWD/%buildtarget/%_target_platform/libstdc++-v3/include|" \
	libstdc++-v3/doc/doxygen/user.cfg.in

%build
libtoolize --copy --install --force
install -pm644 %_datadir/libtool/aclocal/*.m4 .
patch -p0 <%_sourcedir/libtool.m4-gcj.patch

# Regenerate configure scripts.
for f in */aclocal.m4; do
	d="${f%%/*}"
	grep ^m4_include "$d"/aclocal.m4 |
		egrep -v '\[(libltdl/)?acinclude\.m4\]' >acinclude.m4~ ||:
	touch "$d"/acinclude.m4
	cat "$d"/acinclude.m4 >>acinclude.m4~
	mv acinclude.m4~ "$d"/acinclude.m4
	%autoreconf "$d"
	sh -n "$d"/configure
done

./contrib/gcc_update --touch

rm -rf %buildtarget
mkdir %buildtarget
pushd %buildtarget

# GNAT is required to build Ada.  Don't build GCJ.
#languages="c,c++,objc,obj-c++,java,fortran,ada"
languages="c,c++,objc,obj-c++,fortran"

%define _configure_script ../configure
%define _configure_target --build=%_build --host=%_host --target=%_mingw32_target
%remove_optflags %optflags_nocpp %optflags_notraceback
export CC=%__cc \
	CFLAGS="%optflags" \
	CXXFLAGS="%optflags" \
	FFLAGS="%optflags" \
	GCJFLAGS="%optflags" \
	TCFLAGS="%optflags" \
	XCFLAGS="%optflags" \
	ac_cv_file__proc_self_exe=yes \
	#

%configure \
  --prefix=%prefix \
  --bindir=%_bindir \
  --includedir=%_includedir \
  --libdir=%_libdir \
  --mandir=%_mandir \
  --infodir=%_infodir \
  --datadir=%_datadir \
  --with-gnu-as --with-gnu-ld --verbose \
  --without-newlib \
  --disable-multilib \
  --enable-libgomp \
  --with-system-zlib \
  --disable-nls --without-included-gettext \
  --disable-win32-registry \
  --enable-version-specific-runtime-libs \
  --with-sysroot=%_mingw32_sysroot \
  --enable-languages="$languages" \
  --with-bugurl=http://bugzilla.altlinux.org

%make_build all
popd

%install
pushd %buildtarget
%makeinstall_std

# These files conflict with existing installed files.
rm -rf %buildroot%_infodir
rm -f %buildroot%_libdir/libiberty*
rm -f %buildroot%_man7dir/*
rm -f %_libdir/gcc/%_mingw32_target/%version/SYSCALLS.c.X

mkdir -p %buildroot/lib
ln -sf ..%prefix/bin/%_mingw32_target-cpp \
%buildroot/lib/%_mingw32_target-cpp
mkdir -p %buildroot%prefix/%_mingw32_target/bin

ln -sf ../../..%_bindir/%_mingw32_target-cpp \
%buildroot%prefix/%_mingw32_target/bin/cpp
ln -sf ../../..%_bindir/%_mingw32_target-gcc \
%buildroot%prefix/%_mingw32_target/bin/cc
ln -sf ../../..%_bindir/%_mingw32_target-gcc \
%buildroot%prefix/%_mingw32_target/bin/gcc
ln -sf ../../..%_bindir/%_mingw32_target-g++ \
%buildroot%prefix/%_mingw32_target/bin/g++

# Not sure why gcc puts this DLL into _bindir, but surely better if
# it goes into _mingw32_bindir.
mkdir -p %buildroot%_mingw32_bindir
mv %buildroot%_bindir/libgcc_s_sjlj-1.dll \
%buildroot%_mingw32_bindir
# Same goes for this DLL under _libdir.
mv %buildroot%_libdir/gcc/%_mingw32_target/bin/libgomp-1.dll \
%buildroot%_mingw32_bindir

# Don't want the *.la files.
find %buildroot -name '*.la' -delete

popd

%files
%_bindir/%_mingw32_target-gcc
%_bindir/%_mingw32_target-gcc-%version
%_bindir/%_mingw32_target-gccbug
%_bindir/%_mingw32_target-gcov
%_bindir/%_mingw32_target-protoize
%_bindir/%_mingw32_target-unprotoize
%prefix/%_mingw32_target/lib/libiberty.a
%prefix/%_mingw32_target/bin/cc
%prefix/%_mingw32_target/bin/gcc
%dir %_libdir/gcc/%_mingw32_target
%dir %_libdir/gcc/%_mingw32_target/%version
%dir %_libexecdir/gcc/%_mingw32_target
%dir %_libexecdir/gcc/%_mingw32_target/%version
%_libdir/gcc/%_mingw32_target/%version/crtbegin.o
%_libdir/gcc/%_mingw32_target/%version/crtend.o
%_libdir/gcc/%_mingw32_target/%version/crtfastmath.o
%_libdir/gcc/%_mingw32_target/%version/libgcc.a
%_libdir/gcc/%_mingw32_target/%version/libgcc_eh.a
%_libdir/gcc/%_mingw32_target/%version/libgcc_s.a
%_libdir/gcc/%_mingw32_target/%version/libgcov.a
%_libdir/gcc/%_mingw32_target/%version/libssp.a
%_libdir/gcc/%_mingw32_target/%version/libssp_nonshared.a
%_libdir/gcc/%_mingw32_target/%version/libssp.dll.a
%_libdir/gcc/%_mingw32_target/%version/libgomp.a
%_libdir/gcc/%_mingw32_target/%version/libgomp.dll.a
%_libdir/gcc/%_mingw32_target/%version/libgomp.spec
%dir %_libdir/gcc/%_mingw32_target/%version/include
%dir %_libdir/gcc/%_mingw32_target/%version/include-fixed
%dir %_libdir/gcc/%_mingw32_target/%version/include/ssp
%_libdir/gcc/%_mingw32_target/%version/include-fixed/README
%_libdir/gcc/%_mingw32_target/%version/include-fixed/*.h
%_libdir/gcc/%_mingw32_target/%version/include/*.h
%_libdir/gcc/%_mingw32_target/%version/include/ssp/*.h
%dir %_libdir/gcc/%_mingw32_target/%version/install-tools
%_libdir/gcc/%_mingw32_target/%version/install-tools/*
%dir %_libdir/gcc/%_mingw32_target/bin/
%_libdir/gcc/%_mingw32_target/bin/libssp-0.dll
%dir %_libexecdir/gcc/%_mingw32_target/%version/install-tools
%_libexecdir/gcc/%_mingw32_target/%version/install-tools/*
%_mingw32_bindir/libgcc_s_sjlj-1.dll
%_mingw32_bindir/libgomp-1.dll
%_man1dir/%_mingw32_target-gcc.1*
%_man1dir/%_mingw32_target-gcov.1*

%files -n mingw32-cpp
/lib/%_mingw32_target-cpp
%_bindir/%_mingw32_target-cpp
%prefix/%_mingw32_target/bin/cpp
%_man1dir/%_mingw32_target-cpp.1*
%dir %_libdir/gcc/%_mingw32_target
%dir %_libdir/gcc/%_mingw32_target/%version
%_libexecdir/gcc/%_mingw32_target/%version/cc1

%files c++
%_bindir/%_mingw32_target-g++
%_bindir/%_mingw32_target-c++
%_man1dir/%_mingw32_target-g++.1*
%prefix/%_mingw32_target/bin/g++
%_libdir/gcc/%_mingw32_target/%version/include/c++/
%_libdir/gcc/%_mingw32_target/%version/libstdc++.a
%_libdir/gcc/%_mingw32_target/%version/libsupc++.a
%_libexecdir/gcc/%_mingw32_target/%version/cc1plus
%_libexecdir/gcc/%_mingw32_target/%version/collect2

%files objc
%_libdir/gcc/%_mingw32_target/%version/include/objc/
%_libdir/gcc/%_mingw32_target/%version/libobjc.a
%_libexecdir/gcc/%_mingw32_target/%version/cc1obj

%files objc++
%_libexecdir/gcc/%_mingw32_target/%version/cc1objplus

%files gfortran
%_bindir/%_mingw32_target-gfortran
%_man1dir/%_mingw32_target-gfortran.1*
%_libdir/gcc/%_mingw32_target/%version/libgfortran.a
%_libdir/gcc/%_mingw32_target/%version/libgfortranbegin.a
%_libdir/gcc/%_mingw32_target/%version/finclude/omp_lib.f90
%_libdir/gcc/%_mingw32_target/%version/finclude/omp_lib.h
%_libdir/gcc/%_mingw32_target/%version/finclude/omp_lib.mod
%_libdir/gcc/%_mingw32_target/%version/finclude/omp_lib_kinds.mod
%_libexecdir/gcc/%_mingw32_target/%version/f951

%changelog
* Sat Mar 13 2010 Boris Savelev <boris@altlinux.org> 4.4.2-alt1
- new version
- build libgomp

* Thu Jul 30 2009 Boris Savelev <boris@altlinux.org> 4.4.0-alt3
- add symlinks to %prefix/%_mingw32_target/bin

* Mon Jul 27 2009 Boris Savelev <boris@altlinux.org> 4.4.0-alt2
- drop gcc43-alt-defaults-stack-protector.patch

* Mon Jul 27 2009 Boris Savelev <boris@altlinux.org> 4.4.0-alt1.1
- rebuild with new macros

* Mon Jul 20 2009 Boris Savelev <boris@altlinux.org> 4.4.0-alt1
- rebuild

* Sat Jul 18 2009 Boris Savelev <boris@altlinux.org> 4.4.0-alt0.7
- intial build

* Mon Mar 23 2009 Richard W.M. Jones <rjones@redhat.com> - 4.4.0-0.7
- New native Fedora version gcc 4.4.0 20090319 svn 144967.
- Enable _smp_mflags.

* Wed Mar  4 2009 Richard W.M. Jones <rjones@redhat.com> - 4.4.0-0.6
- Fix libobjc and consequently Objective C and Objective C++ compilers.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 4.4.0-0.4
- Rebuild for mingw32-gcc 4.4

* Thu Feb 19 2009 Richard W.M. Jones <rjones@redhat.com> - 4.4.0-0.2
- Move to upstream version 4.4.0-20090216 (same as Fedora native version).
- Added FORTRAN support.
- Added Objective C support.
- Added Objective C++ support.

* Mon Nov 24 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-12
- Rebuild against latest filesystem package.

* Fri Nov 21 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-11
- Remove obsoletes for a long dead package.

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-10
- Rebuild against mingw32-filesystem 37

* Wed Nov 19 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-9
- Rebuild against mingw32-filesystem 36

* Thu Oct 30 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-8
- Don't BR mpfr-devel for RHEL/EPEL-5 (Levente Farkas).

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-7
- Rename mingw -> mingw32.

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-6
- Use RPM macros from mingw-filesystem.

* Mon Jul  7 2008 Richard W.M. Jones <rjones@redhat.com> - 4.3.2-3
- Initial RPM release, largely based on earlier work from several sources.
