Name: libffcall
Version: 2.4
Release: alt3

Summary: Foreign Function Call Libraries
License: GPLv2
Group: System/Libraries

Url: https://www.gnu.org/software/libffcall/
Source: %name-%version.tar
Patch: libffcall-2.4-e2k.patch
Patch1: libffcall-2.4-loongarch64.patch

%define desc This is a library which can be used to build foreign function\
call interfaces in embedded interpreters.

%package devel
Summary: Development headers for Foreign Function Call Libraries
Group: Development/C
Requires: %name = %version-%release

%description
%desc

%description devel
%desc
This package contains development headers for FFCall libraries

%prep
%setup
%ifarch %e2k
%patch -p1
%endif
%ifarch loongarch64
%patch1 -p1
%endif

%build
%ifarch armh
%define optflags_lto %nil
%endif
%configure --disable-static
make

%check
make check

%install
%makeinstall_std
rm -v %buildroot%_libdir/*.a

%files
%doc COPYING NEWS PLATFORMS README
%_libdir/*.so.*

%files devel
%doc */*.html
%_includedir/*
%_libdir/*.so
%_mandir/man?/*

%changelog
* Tue Aug 06 2024 Ivan A. Melnikov <iv@altlinux.org> 2.4-alt3
- Add loongarch64 support via patch from Bruno Haible
  with minor fixes from iv@.

* Thu Apr 27 2023 Michael Shigorin <mike@altlinux.org> 2.4-alt2
- E2K: added arch support patch by ilyakurdyukov@

* Mon Aug 30 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4-alt1
- 2.4 released

* Mon Aug 30 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt3
- unpackaged static library dropped

* Fri Jul 19 2019 Ivan A. Melnikov <iv@altlinux.org> 2.1-alt2
- Applied patch from Debian to fix FPXX support on mipsel
- Added %%check

* Thu Dec 06 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt1
- 2.1 released

* Wed Dec 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt3
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt2
- Rebuilt for soname set-versions

* Fri Nov 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.10-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libffcall
  * postun_ldconfig for libffcall
  * postclean-05-filetriggers for spec file

* Thu Jul 15 2004 Sir Raorn <raorn@altlinux.ru> 1.10-alt1
- [1.10]
- Url updated (closes #3038)
- Explicitly enabled static

* Mon Dec 15 2003 Sir Raorn <raorn@altlinux.ru> 1.8d-alt5
- devel-static and *.la fixes

* Sun Sep 14 2003 Sir Raorn <raorn@altlinux.ru> 1.8d-alt4
- SMP build b0rken
- Some spec cleanups

* Tue Jul 30 2002 Sir Raorn <raorn@altlinux.ru> 1.8d-alt3
- Libraries made shared

* Wed Jul 17 2002 Sir Raorn <raorn@altlinux.ru> 1.8d-alt2
- Renamed to %name-devel

* Sat May 11 2002 Sir Raorn <raorn@altlinux.ru> 1.8d-alt1
- [1.8d]

* Mon Jan 07 2002 Sir Raorn <raorn@altlinux.ru> 1.8c-alt3
- Spec celanup

* Sat Jan 05 2002 Sir Raorn <raorn@altlinux.ru> 1.8c-alt2
- Fixed %doc for html documentation

* Sat Aug 18 2001 Sir Raorn <raorn@binec.ru>
- initial RPM release


