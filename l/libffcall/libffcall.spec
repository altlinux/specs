Name: libffcall
Version: 2.1
Release: alt1

Summary: Foreign Function Call Libraries
License: GPL
Group: System/Libraries
Url: https://www.gnu.org/software/libffcall/

Source: %name-%version.tar

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

%build
%configure --disable-static
make

%install
%makeinstall_std

%files
%doc COPYING NEWS PLATFORMS README
%_libdir/*.so.*

%files devel
%doc */*.html
%_includedir/*
%_libdir/*.so
%_mandir/man?/*

%changelog
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


