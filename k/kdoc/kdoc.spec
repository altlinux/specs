Name: kdoc
Version: 3.0.0
Release: alt2
Serial: 1

Group: Development/KDE and QT
Summary: K Desktop Environment - Documentation tools
Url: http://www.kde.org/
License: GPL

Source: %name-%version.tar.bz2

BuildRequires: rpm-build perl-podlators

BuildArch: noarch
%define _perl_lib_path %_datadir/%name

%description
Documentation tools for the K Desktop Environment %version.

%prep
%setup -q -n %name-%version

make -f Makefile.cvs ||:

%build
export PATH="%_K3bindir:$PATH"
%configure

%make_build CXXFLAGS="-DNO_DEBUG -DNDEBUG"

%install
make install DESTDIR=%buildroot

mkdir -p %buildroot/%_docdir/HTML/en
mv %buildroot/%_docdir/%name %buildroot/%_docdir/HTML/en/%name
install -m644 doc/index.cache.bz2 %buildroot/%_docdir/HTML/en/%name/index.cache.bz2


%files
%defattr(-,root,root,-)
%doc README TODO
%doc %_docdir/HTML/en/%name
%doc %_mandir/*/*
%_bindir/*
%_datadir/%name

%changelog
* Sat Mar 05 2011 Sergey V Turchin <zerg@altlinux.org> 1:3.0.0-alt2
- fix to build

* Mon Sep 29 2003 Sergey V Turchin <zerg at altlinux dot org> 1:3.0.0-alt1
- define _perl_lib_path
  thanks at@altlinux

* Mon Nov 04 2002 Sergey V Turchin <zerg@altlinux.ru> 1:2.0-alt2.a54
- rebuild

* Thu Apr 04 2002 Sergey V Turchin <zerg@altlinux.ru> 1:2.0-alt1.a54
- snapshot for KDE3

* Fri Nov 23 2001 Sergey V Turchin <zerg@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Wed Sep 19 2001 Sergey V Turchin <zerg@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Wed Aug 22 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.2-alt2
- Some spec cleanup

* Wed Aug 15 2001 Sergey V Turchin <zerg@altlinux.ru> 2.2-alt1
- build for ALT

* Mon Aug 05 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-1mdk
- kde 2.2

* Tue Jul 31 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-0.pre1.1mdk
- kde 2.2.pre1

* Tue Jun 26 2001 David BAUDENS <baudens@mandrakesoft.com> 2.2-0.beta1.1mdk
- KDE 2.2.beta1
- Requires: perl >= 5.6.0

* Wed May 30 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-0.alpha2.1mdk
- kde2.2alpha2

* Wed Apr 18 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.2-0.alpha1.1mdk
- KDE 2.2alpha1

* Wed Mar 21 2001 David BAUDENS <baudens@mandrakesoft.com> 2.1.1-1mdk
- KDE 2.1.1

* Wed Feb 28 2001 David BAUDENS <baudens@mandrakesoft.com> 2.1-2mdk
- Add BuildRequires

* Fri Feb 23 2001 David BAUDENS <baudens@mandrakesoft.com> 2.1-1mdk
- KDE 2.1

* Tue Feb 13 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.1-0.20010213.1mdk
- Updated code

* Mon Jan 15 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 2.1-0.20010115.1mdk
- Updated code

* Thu Dec 02 2000 David BAUDENS <baudens@mandrakesoft.com> 2.1-0.20001203.2mdk
- Rewrite spec to make it LMDK compatible
- Fix Summary

* Sun Dec 01 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.1-0.20001203.1mdk
- Updated code

* Thu Nov 23 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.1-0.20001123.1mdk
- Updated code

* Tue Nov 21 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.0.1-0.1mdk
- Updated code

* Tue Nov 14 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.0-8mdk
- This version works with gcc 2.96. This includes code from the future 2.1
- Also repackage for a 7.2 update

* Fri Nov 10 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.0-7mdk
- This version works with gcc 2.96. This includes code from the future 2.1

* Mon Nov 06 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.0-6mdk
- Rebuilt for gcc 2.96 with debug. This needs turned off again.

* Mon Nov 06 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.0-5mdk
- Rebuilt for gcc 2.96 (Second Try)

* Fri Nov 03 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.0-4mdk
- Rebuilt for gcc 2.96.

* Thu Oct 26 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.0-3mdk
- Put the right branch into this.

* Thu Oct 26 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.0-2mdk
- Updated code to fix a bug report with kdelibs and kdoc

* Tue Oct 17 2000 Christopher Molnar <molnarc@mandrakesoft.com> 2.0-1mdk
- Updated code to kde 2.0 Release version

* Mon Oct 02 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.99-1mdk
- Updated code to kde 2.0 Release Candidate 1

* Fri Sep 29 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.94-6mdk
- Updated code

* Wed Sep 27 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.94-5mdk
- Updated code

* Mon Sep 25 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.94-4mdk
- Updated code

* Wed Sep 20 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.94-3mdk
- Updated code

* Fri Sep 15 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.94-2mdk
- Updated code

* Mon Sep 11 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.94-1mdk
- Updated code

* Fri Sep 08 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.93-7mdk
- Updated code

* Thu Sep 07 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.93-6mdk
- Updated code

* Sat Sep 02 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.93-5mdk
- Updated code

* Wed Aug 30 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.93-4mdk
- Updated code

* Mon Aug 28 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.93-3mdk
- Updated code

* Sat Aug 26 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.93-2mdk
- Updated code

* Mon Aug 21 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.93-1mdk
- Updated code

* Sat Aug 19 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.92-15mdk
- Updated code

* Wed Aug 16 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.92-14mdk
- Updated code

* Thu Aug 10 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.92-13mdk
- BM per bug report in cooker

* Thu Aug 10 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.92-12mdk
- Updated code

* Wed Aug 09 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.92-10mdk
- Updated code

* Tue Aug 08 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.92-7mdk
- Updated code for new QT2.2
- Removed auto file list generation

* Wed Aug 02 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.92-6mdk
- Updated code

* Tue Aug 01 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.92-4mdk
- Updated code

* Sat Jul 29 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.92-1mdk
- Updated code
- Changed revision number to standard

* Fri Jul 28 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.92-0.20000728mdk
- Updated code

* Wed Jul 26 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.92-0.20000726mdk
- Updated code

* Tue Jul 25 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.92-0.20000725mdk
- Updated code

* Fri Jul 21 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.92-0.20000721mdk
- Updated code

* Mon Jul 17 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.91-0.20000718mdk
- Updated code

* Sun Jul 16 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.91-0.20000716mdk
- Updated code

* Wed Jul 12 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.91-0.20000712mdk
- Moved to /usr
- Changed package name

* Tue Jul 11 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.91-0.20000712mdk
- Updated code
- moved kdedir to /usr/X11R6/kde2

* Sat Jul 08 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.91-0.20000708mdk
- Updated code snapshot

* Fri Jul 07 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.91-0.20000707mdk
- Updated code snapshot

* Fri Jun 30 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.91-0.20000630mdk
- Updated code snapshot

* Wed Jun 21 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.91-0.20000621mdk
- Updated snapshot

* Mon Jun 19 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.91-0.20000619mdk
- updated snapshot

* Sun Jun 11 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.91-0.20000611mdk
- updated to new version of kdoc

* Sun May 21 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.90-0.20000520mdk
- Updated code snapshot to more recent version

* Wed May 17 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.90-0.20000517mdk
- compiled for Mandrake
