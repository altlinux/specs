Name: ecl
Version: 20.4.24
Release: alt3
Summary: Embeddable Common-Lisp

License: LGPLv2+ and BSD and MIT and ALT-Public-Domain
Group: Development/Other
URL:     https://common-lisp.net/project/ecl/
Source0: https://common-lisp.net/project/ecl/static/files/release/%{name}-%{version}.tgz
Source1: %{name}.desktop
# A modified version of src/util/ecl.svg with extra whitespace removed.  The
# extra whitespace made the icon appear very small and shoved into a corner.
Source2: %{name}.svg
# This patch was sent upstream on 4 Feb 2012.  It fixes a few warnings
# from the C compiler that indicate situations that might be dangerous at
# runtime.
Patch0: %{name}-20.4.24-warnings.patch
# Do not use a separate thread to handle signals by default if built with
# boehm-gc support.
# This prevents a deadlock when building maxima with ecl support in
# fedora, and should handle by default these problems:
# http://trac.sagemath.org/sage_trac/ticket/11752
# http://www.mail-archive.com/ecls-list@lists.sourceforge.net/msg00644.html
Patch1: %{name}-20.4.24-signal_handling_thread.patch
# GCC does not implement support for #pragma STDC FENV_ACCESS
Patch2: %{name}-20.4.24-fenv-access.patch
# Fix setting the stack size.
# See https://gitlab.com/embeddable-common-lisp/ecl/-/merge_requests/215
Patch3: %{name}-20.4.24-stack-size.patch
# Fix the ECL_WITH_LISP_FPE macro.  See
# https://gitlab.com/embeddable-common-lisp/ecl/-/commit/75877dd8f0d534552284ba4380ba65baa74f028f
Patch4: %{name}-20.4.24-fpe-macro.patch
# Avoid an infinite loop if there is a write error on stderr.  See
# build/pkgs/ecl/patches/write_error.patch in the sagemath distribution.
Patch5: %{name}-20.4.24-write-error.patch
# Fix bogus test compromised by LTO.
Patch6: %{name}-20.4.24-configure.patch

BuildRequires: /usr/bin/desktop-file-install gcc-c++ perl(FileHandle.pm) perl(IPC/Open2.pm) texinfo
BuildRequires: desktop-file-utils
BuildRequires: docbook5-schemas
BuildRequires: docbook5-style-xsl
BuildRequires: emacs26-common
BuildRequires: libgmp-devel libgmpxx-devel
BuildRequires: pkgconfig(atomic_ops)
BuildRequires: pkgconfig(bdw-gc)
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(x11)
BuildRequires: makeinfo
BuildRequires: xmlto

Source44: import.info

%description
ECL (Embeddable Common Lisp) is an implementation of the Common Lisp
language as defined by the ANSI X3J13 specification.  ECL features a
bytecode compiler and interpreter, the ability to build standalone
executables and libraries, and extensions such as ASDF, sockets, and
Gray streams.

# no -devel package for header files is split off
# since they are required by the main package


%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0


# Remove spurious executable bits
find src/{c,h} -type f -perm /0111 -exec chmod a-x {} \+

# Temporary fix for missing braces in initializers, causes build failure
sed -i 's/{.*,.*,.*,.*,.*}/{&}/g' src/c/symbols_list.h


%build
%configure --enable-manual=html --with-sse=auto \
  CFLAGS="%{optflags} -Wno-unused -Wno-return-type -Wno-unknown-pragmas"

# Parallel build does NOT work.  Do NOT use _smp_mflags.
make

%install
%makeinstall_std

# Remove installed files that are in the wrong place
rm -fr $RPM_BUILD_ROOT%{_docdir}
rm -f $RPM_BUILD_ROOT%{_libdir}/Copyright
rm -f $RPM_BUILD_ROOT%{_libdir}/LGPL

# Install the man pages
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
sed -e "s|@bindir@|%{_bindir}|" src/doc/ecl.man.in > \
  $RPM_BUILD_ROOT%{_mandir}/man1/ecl.1
cp -p src/doc/ecl-config.man.in $RPM_BUILD_ROOT%{_mandir}/man1/ecl-config.1

# Add missing executable bits
chmod a+x $RPM_BUILD_ROOT%{_libdir}/ecl-%{version}/dpp
chmod a+x $RPM_BUILD_ROOT%{_libdir}/ecl-%{version}/ecl_min

# Install the desktop file
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}

# Install the desktop icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps


%files
%{_bindir}/ecl
%{_bindir}/ecl-config
%{_datadir}/applications/ecl.desktop
%{_datadir}/icons/hicolor/scalable/apps/ecl.svg
%{_libdir}/ecl*
%{_libdir}/libecl.so.20.*
%{_libdir}/libecl.so.20
%{_libdir}/libecl.so
%{_includedir}/ecl
%{_mandir}/man1/*
%doc examples CHANGELOG README.md build/doc/manual/html
%doc src/doc/amop.txt src/doc/types-and-classes
%doc --no-dereference COPYING LICENSE


%changelog
* Mon Jun 21 2021 Andrey Cherepanov <cas@altlinux.org> 20.4.24-alt3
- Inital build in Sisyphus.

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 20.4.24-alt2_3
- update to new release by fcimport

* Wed Nov 04 2020 Igor Vlasenko <viy@altlinux.ru> 20.4.24-alt1_3
- update

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 16.1.3-alt1_11
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 16.1.3-alt1_10
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 16.1.3-alt1_8
- update to new release by fcimport

* Fri Jan 25 2019 Igor Vlasenko <viy@altlinux.ru> 16.1.3-alt1_7
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 16.1.3-alt1_6
- update to new release by fcimport

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 16.1.3-alt1_5
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 16.1.3-alt1_3
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 16.1.3-alt1_1
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 16.1.2-alt1_1
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 16.0.0-alt1_2
- update to new release by fcimport

* Wed Apr 08 2015 Igor Vlasenko <viy@altlinux.ru> 13.5.1-alt1_9
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 13.5.1-alt1_7
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 13.5.1-alt1_6
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 13.5.1-alt1_3
- update to new release by fcimport

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 13.5.1-alt1_2
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 12.12.1-alt1_4
- update to new release by fcimport

* Thu Dec 20 2012 Igor Vlasenko <viy@altlinux.ru> 12.12.1-alt1_2
- fc import

