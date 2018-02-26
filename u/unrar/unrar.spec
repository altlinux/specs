Name: unrar
Version: 4.2.1
Release: alt1

Summary: RAR unarchiver
License: Freely distributable
Group: Archiving/Compression

Url: http://www.rarlab.com
Source: %url/rar/unrarsrc-%version.tar.gz

# Automatically added by buildreq on Mon Feb 07 2011
BuildRequires: gcc-c++

%description
The unrar utility is a freeware program, distributed with source code and
developed for extracting, testing and viewing the contents of archives created
with the RAR archiver, version 1.50 and above.

%prep
%setup -n unrar

%build
%make -f makefile.unix CXXFLAGS="%optflags"

%install
install -pD -m755 unrar %buildroot%_bindir/unrar

%files
%_bindir/*
%doc *.txt

%changelog
* Tue May 15 2012 Victor Forsiuk <force@altlinux.org> 4.2.1-alt1
- 4.2.1

* Sun Jan 29 2012 Victor Forsiuk <force@altlinux.org> 4.1.4-alt1
- 4.1.4

* Sat Nov 12 2011 Victor Forsiuk <force@altlinux.org> 4.1.3-alt1
- 4.1.3

* Mon Mar 28 2011 Victor Forsiuk <force@altlinux.org> 4.0.7-alt1
- 4.0.7

* Mon Feb 07 2011 Victor Forsiuk <force@altlinux.org> 4.0.6-alt1
- 4.0.6

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 4.0.5-alt1
- 4.0.5

* Mon Dec 20 2010 Victor Forsiuk <force@altlinux.org> 4.0.3-alt1
- 4.0.3

* Fri Nov 26 2010 Victor Forsiuk <force@altlinux.org> 4.0.2-alt1
- 4.0.2

* Mon Nov 15 2010 Victor Forsiuk <force@altlinux.org> 4.0.1-alt1
- 4.0.1

* Tue Mar 16 2010 Victor Forsiuk <force@altlinux.org> 3.9.10-alt1
- 3.9.10

* Mon Feb 15 2010 Victor Forsiuk <force@altlinux.org> 3.9.9-alt1
- 3.9.9

* Tue Jan 26 2010 Victor Forsyuk <force@altlinux.org> 3.9.8-alt1
- 3.9.8

* Sun Dec 20 2009 Victor Forsyuk <force@altlinux.org> 3.9.7-alt1
- 3.9.7

* Thu Sep 03 2009 Victor Forsyuk <force@altlinux.org> 3.9.6-alt1
- 3.9.6

* Wed Jul 01 2009 Victor Forsyuk <force@altlinux.org> 3.9.5-alt1
- 3.9.5

* Thu Nov 06 2008 Victor Forsyuk <force@altlinux.org> 3.8.5-alt1
- 3.8.5

* Thu Oct 23 2008 Victor Forsyuk <force@altlinux.org> 3.8.4-alt1
- 3.8.4

* Wed Oct 08 2008 Victor Forsyuk <force@altlinux.org> 3.8.3-alt1
- 3.8.3

* Thu Jun 19 2008 Victor Forsyuk <force@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Dec 18 2007 Victor Forsyuk <force@altlinux.org> 3.7.8-alt1
- 3.7.8

* Wed Sep 05 2007 Victor Forsyuk <force@altlinux.org> 3.7.7-alt1
- 3.7.7

* Tue Jul 17 2007 Victor Forsyuk <force@altlinux.org> 3.7.6-alt2
- Security fix: see CVE-2007-3726.

* Tue Jun 05 2007 Victor Forsyuk <force@altlinux.org> 3.7.6-alt1
- 3.7.6

* Tue Apr 24 2007 Victor Forsyuk <force@altlinux.org> 3.7.5-alt1
- 3.7.5
- Apply optflags.

* Tue Mar 20 2007 Victor Forsyuk <force@altlinux.org> 3.7.4-alt1
- 3.7.4

* Thu Feb 08 2007 Victor Forsyuk <force@altlinux.org> 3.7.3-alt1
- 3.7.3

* Fri Oct 20 2006 Victor Forsyuk <force@altlinux.org> 3.6.8-alt1
- 3.6.8

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.4.3-alt1.1
- Rebuilt with libstdc++.so.6.

* Sun Nov 21 2004 Andrey Astafiev <andrei@altlinux.ru> 3.4.3-alt1
- 3.4.3

* Sun Jul 25 2004 Andrey Astafiev <andrei@altlinux.ru> 3.4.1-alt1
- 3.4.1

* Thu Mar 11 2004 Andrey Astafiev <andrei@altlinux.ru> 3.3.6-alt1
- 3.3.6

* Fri Jan 23 2004 Andrey Astafiev <andrei@altlinux.ru> 3.3.4-alt1
- 3.3.4

* Wed Dec 10 2003 Andrey Astafiev <andrei@altlinux.ru> 3.3.2-alt1
- 3.3.2

* Fri Aug 22 2003 Andrey Astafiev <andrei@altlinux.ru> 3.2.3-alt1
- 3.2.3

* Fri Jun 13 2003 Andrey Astafiev <andrei@altlinux.ru> 3.2.2-alt1
- 3.2.2

* Fri Apr 11 2003 Andrey Astafiev <andrei@altlinux.ru> 3.2.1-alt1
- 3.2.1

* Wed Mar 26 2003 Andrey Astafiev <andrei@altlinux.ru> 3.2.0-alt1
- 3.2.0

* Fri Mar 07 2003 Andrey Astafiev <andrei@altlinux.ru> 3.1.3-alt1
- 3.1.3

* Fri Dec 27 2002 Andrey Astafiev <andrei@altlinux.ru> 3.1.2-alt1
- 3.1.2

* Mon Sep 16 2002 Stanislav Ievlev <inger@altlinux.ru> 3.00-alt2
- rebuild with gcc3

* Mon Aug 19 2002 Andrey Astafiev <andrei@altlinux.ru> 3.00-alt1
- 3.00
- some spec cleanup.

* Thu Apr 05 2001 Sergie Pugachev <fd_rag@altlinux.ru> 2.71-alt1
- new version 2.71

* Thu Feb 08 2001 Dmitry V. Levin <ldv@fandra.org> 2.50.1-ipl2
- Fixed group tag.

* Fri Dec 01 2000 Dmitry V. Levin <ldv@fandra.org> 2.50.1-ipl1
- 2.50.1
- FHSification.

* Mon Aug 09 1999 Dmitry V. Levin <ldv@fandra.org>
- Initial revision.
