Name: libexplain
Version: 1.4
Release: alt2

Summary: Library functions to explain system call errors

Url: http://libexplain.sourceforge.net

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://downloads.sourceforge.net/%name/%name-%version.tar
Patch0: libexplain-1.4-syscall.patch
Patch1: libexplain-1.4-largefile.patch
Patch2: libexplain-1.4-missed-defines.patch
Patch3: libexplain-1.4-gcc-10.patch
Patch4: libexplain-1.4-nettstamp-needs-types.patch
Patch5: libexplain-1.4-sanitize-bison.patch
Patch6: libexplain-1.4-typos.patch

License: LGPLv3+
Group: System/Libraries

BuildRequires: bison libacl-devel libcap-devel libtool lsof gettext-tools
BuildRequires: ghostscript-utils groff-base groff-ps

%{!?_pkgdocdir: %global _pkgdocdir %_docdir/%name-%version}

%description
The libexplain project provides a library which may be used to explain
Unix and Linux system call errors. This will make your application's
error messages much more informative to your users.  The library is
not quite a drop-in replacement for strerror, but it comes close. Each
system call has a dedicated libexplain function.

The coverage for system calls is being improved all the time. Coverage
includes 159 system calls and 444 ioctl requests.

%package -n explain
Summary: Explains system call error reports
License: GPLv3+
Group: Development/Tools
Requires: libexplain = %EVR

%description -n explain
The explain command is used to decode an error return read from an
strace(1) listing, or similar.  Because this is being deciphered in a
different process than the original, the results will be less accurate
than if the program itself were to use libexplain(3).

%package devel
Summary: Development files for libexplain
License: LGPLv3+ and GPLv3+
Group: Development/C
Requires: libexplain = %EVR
Requires: pkg-config

%description devel
Development files for the libexplain library.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

# hack against missed dlci_add struct
%__subst "s|#ifdef SIOCADDDLCI|#ifdef IGNORE_SIOCADDDLCI|" libexplain/iocontrol/siocadddlci.c
%__subst "s|#ifdef SIOCDELDLCI|#ifdef IGNORE_SIOCDELDLCI|" libexplain/iocontrol/siocdeldlci.c

# Propagate %%{_pkgdocdir} into Makefile.in
case "%_pkgdocdir" in
*/libexplain-%version )
  sed -i "s,\$(datarootdir)/doc/libexplain,\$(datarootdir)/doc/libexplain-%version," Makefile.in
  ;;
esac

%build
# formerly used --disable-static, but configure says it is unrecognized
%configure
%make_build

%check
# TODO: 
# Invalid argument (EINVAL) because unknown protocol, or protocol family not available
# FAILED test of socket EPROTONOSUPPORT
make check || :

%install
# The install target is not smp-safe, so don't use smp_mflags.
make DESTDIR=%buildroot \
     install
# The shared library has to be executable!
chmod 755 %buildroot%_libdir/%name.so.*.*.*
# Get rid of the static library and libtool archives
rm %buildroot%_libdir/%name.{a,la}

# Add files to docs
install -m 0664 README LICENSE %buildroot%_pkgdocdir


%files
%_libdir/%name.so.*
%_datadir/locale/de/LC_MESSAGES/%name.mo
%dir %doc %_pkgdocdir
%doc %_pkgdocdir/README
%doc %_pkgdocdir/LICENSE
%doc %_pkgdocdir/readme.pdf
%doc %_pkgdocdir/reference.pdf

%files -n explain
%_bindir/explain
%_man1dir/*.1.*

%files devel
%_man3dir/*.3.*
%_includedir/%name/
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%dir %doc %_pkgdocdir
%doc %_pkgdocdir/building.pdf
%doc %_pkgdocdir/new_system_call.pdf

# NOTE rpmlint will complain about a use of mktemp.  This is because libexplain
# provides a wrapper for mktemp, not because it is used.

%changelog
* Sun Feb 28 2021 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt2
- fix build, add patches from Debian

* Wed Mar 27 2019 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- initial build for ALT Sisyphus

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 01 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.4-2
- Fix FTBFS on aarch64 and ppc64 (#1111453)

* Mon Jun 30 2014 Eric Smith <brouhaha@fedoraproject.org> - 1.4-1
- Updated to latest upstream.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 06 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.2-3
- Install docs into %%{_pkgdocdir} (RHBZ #993957).
- Use %%configure instead of ./configure.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Eric Smith <brouhaha@fedoraproject.org> - 1.2-1
- Updated to latest upstream.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.D001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.D001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 08 2012 Eric Smith <brouhaha@fedoraproject.org> - 1.0.D001-1
- Updated to latest upstream.

* Sun Jan 22 2012 Eric Smith <brouhaha@fedoraproject.org> - 0.52.D002-1
- Updated to latest upstream.

* Sun Jan 22 2012 Eric Smith <brouhaha@fedoraproject.org> - 0.50.D001-1
- Updated to latest upstream.
- Updated list of tests to skip.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.47.D001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 08 2011 Eric Smith <brouhaha@fedoraproject.org> - 0.47.D001-1
- Updated to latest upstream.
- Changed Patch0 to use of sed to better deal with new upstream releases.
- Removed BuildRoot, clean, defattr, etc.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40.D001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 02 2011 Eric Smith <brouhaha@fedoraproject.org> - 0.40.D001-1
- updated to latest upstream
- updated based on package review comments

* Tue Sep 07 2010 Eric Smith <brouhaha@fedoraproject.org> - 0.38.D001-1
- updated to latest upstream

* Mon May 10 2010 Eric Smith <brouhaha@fedoraproject.org> - 0.31.D001-1
- initial version
