Name: libfaketime
Version: 0.9.10
Release: alt3

Summary: Manipulate system time per process for testing purposes
License: GPLv2+
Group: Development/C

Url: https://github.com/wolfcw/libfaketime
# Source-url: https://github.com/wolfcw/libfaketime/archive/refs/tags/v%version.tar.gz
Source: libfaketime-%version.tar
Patch: libfaketime-symver.patch

#Provides: faketime
Conflicts: faketime

BuildRequires: perl-Time-HiRes
BuildRequires: libuthash-devel >= 2.0.2

%description
libfaketime intercepts various system calls which programs use to
retrieve the current date and time. It can then report faked dates and
times (as specified by you, the user) to these programs. This means you
can modify the system time a program sees without having to change the
time system- wide.

%prep
%setup
%patch -p1
# use external uthash.h from libuthash-devel
rm -v src/uthash.h

%build
cd src

# https://github.com/wolfcw/libfaketime/blob/master/README.packagers
# Upstream libfaketime requires a mess of different compile time flags
# for different glibc versions and architectures.
# https://github.com/wolfcw/libfaketime/pull/178
# Goal is to build time autodetect these with autotools in the next release ...

# TODO: see rpm-build-features
FAKETIME_COMPILE_CFLAGS="BOGUS"

# for reasons we don't know the old glibc workaround is required here
# but not on archv7hl and aarch64 ...
%ifarch %ix86 x86_64
    echo "force_monotonic"
    export FAKETIME_COMPILE_CFLAGS="-DFORCE_MONOTONIC_FIX"
%endif
%ifarch ppc64le
    echo "force_monotonic and pthread_nonver"
    export FAKETIME_COMPILE_CFLAGS="-DFORCE_MONOTONIC_FIX -DFORCE_PTHREAD_NONVER"
%endif
%ifarch armh aarch64 %e2k riscv64
    unset FAKETIME_COMPILE_CFLAGS
%endif
%ifarch loongarch64
    echo "force_pthread_nonver"
    export FAKETIME_COMPILE_CFLAGS="-DFORCE_PTHREAD_NONVER"
%endif

if [ "$FAKETIME_COMPILE_CFLAGS" == "BOGUS" ]; then
  echo "SHOULD NEVER REACH HERE ... YOU HAVE AN UNTESTED VERSION+ARCH, see rpm spec for details ... ABORT"
  exit 1
fi

%ifarch %e2k
# still needed as of lcc 1.26.21
%add_optflags -Wno-error=attributes
%endif

export CFLAGS="%optflags -Wno-nonnull-compare -Wno-strict-aliasing"
%make_build PREFIX="%prefix" LIBDIRNAME="/%_lib/faketime" all

%check
%ifnarch armh %ix86 mipsel
%make_build -C test
%endif

%install
%makeinstall_std PREFIX="%prefix" LIBDIRNAME="/%_lib/faketime"
rm -r %buildroot/%_docdir/faketime
# needed for stripping/debug package
#chmod a+rx %buildroot/%_libdir/faketime/*.so.*

%files
%doc COPYING
%doc README NEWS README.developers
%_bindir/faketime
%dir %_libdir/faketime/
%_libdir/faketime/libfaketime*so.*
%_man1dir/*

%changelog
* Tue Dec 12 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.9.10-alt3
- NMU: fixed FTBFS on LoongArch

* Mon Dec 11 2023 Michael Shigorin <mike@altlinux.org> 0.9.10-alt2
- build on e2k and other new arches too
- minor spec cleanup

* Sun Apr 03 2022 Vitaly Lipatov <lav@altlinux.ru> 0.9.10-alt1
- new version 0.9.10 (with rpmrb script)

* Wed Sep 08 2021 Vitaly Lipatov <lav@altlinux.ru> 0.9.9-alt1
- new version 0.9.9 (with rpmrb script)

* Wed Sep 08 2021 Vitaly Lipatov <lav@altlinux.ru> 0.9.8-alt1
- initial build for ALT Sisyphus

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 02 2020 Pablo Greco <pgreco@centosproject.org> - 0.9.8-10
- Conditionals to build 0.9.8-9 in f31 and epel7-8
- Use upstream's version of the gcc10 fix

* Wed Sep 02 2020 Jeff Law <law@redhat.com> - 0.9.8-9
- Use symver attribute instead of asms for symbol versioning
- Enable LTO

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jeff Law <law@redhat.com> - 0.9.8-7
- Disable LTO

* Sat Feb 08 2020 Pablo Greco <pgreco@centosproject.org> - 0.9.8-6
- Fix build with gcc10

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Paul Wouters <pwouters@redhat.com> - 0.9.8-5
- Resolves: rhbz#1766749 libfaketime rfe: please add Provides:faketime
- Use license tag, remove duplicate README entry, update make test target

* Tue Sep 03 2019 Warren Togami <warren@blockstream.com> - 0.9.8-4
- upstream says to use FORCE_PTHREAD_NONVER on any glibc+arch that gets stuck
  For Fedora 31+ "make test" gets stuck on i686 x86_64 ppc64le s390x

* Wed Aug 28 2019 Warren Togami <warren@blockstream.com> - 0.9.8-3
- 0.9.8
- x86_64  EL7: DFORCE_MONOTONIC_FIX
  aarch64 EL7: DFORCE_MONOTONIC_FIX and FORCE_PTHREAD_NONVER
  ppc64le EL7: DFORCE_MONOTONIC_FIX and FORCE_PTHREAD_NONVER
  ppc64le F30+ FORCE_PTHREAD_NONVER

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 12 2016 Paul Wouters <pwouters@redhat.com> - 0.9.6-4
- Add support for CLOCK_BOOTTIME (patch by Mario Pareja <pareja.mario@gmail.com>)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 28 2014 Paul Wouters <pwouters@redhat.com> - 0.9.6-1
- Upgraded to 0.9.6 which adds option to disable monotonic time faking
- fix permissions for symbol stripping for debug package

* Tue Oct 15 2013 Paul Wouters <pwouters@redhat.com> - 0.9.5-4
- Infinite recursion patch is still needed, make test causes
  segfaults otherwise.

* Mon Oct 14 2013 Paul Wouters <pwouters@redhat.com> - 0.9.5-3
- Work around from upstream for autodetecting glibc version bug on i686

* Mon Oct 14 2013 Paul Wouters <pwouters@redhat.com> - 0.9.5-2
- Remove use of ifarch for _lib macro for multilib

* Sun Oct 13 2013 Paul Wouters <pwouters@redhat.com> - 0.9.5-1
- Initial package
