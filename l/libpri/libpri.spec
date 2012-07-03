Name: libpri
Summary: PRI library
Version: 1.4.12
Release: alt1
License: %gpl2only
Group: System/Servers
BuildPreReq: rpm-build-licenses
Epoch: 20080502
Url: ftp://ftp.asterisk.org/pub/%name/%name-%version.tar.gz
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar
Conflicts: libzap
Obsoletes: libzap

%package devel
Summary: %summary
Group: Development/C
Requires: libpri = %epoch:%version-%release

%description devel
%summary


%package devel-static
Summary: %summary
Group: Development/C
Requires: libpri-devel = %epoch:%version-%release

%description devel-static
%summary


%description
ISDN PRI library


%prep
%setup
sed -i 's/\$(INSTALL_BASE)\/lib/$(INSTALL_BASE)\/%_lib/' Makefile
sed -i '/if test/d' Makefile
sed -i 's!/sbin/ldconfig.*!!g' Makefile

%build
find -type f -name '.depend' -print0 \
	| xargs -0r rm -f
%make

%install
%make_install DESTDIR=%buildroot INSTALL_PREFIX=%buildroot install

%files
%_libdir/libpri.so.*

%files devel
%_libdir/libpri.so
%_includedir/libpri.h

%files devel-static
%_libdir/libpri.a

%changelog
* Thu Jul 07 2011 Denis Smirnov <mithraen@altlinux.ru> 20080502:1.4.12-alt1
- 1.4.12

* Sat Apr 02 2011 Denis Smirnov <mithraen@altlinux.ru> 20080502:1.4.11.5-alt2
- rebuild

* Tue Nov 30 2010 Denis Smirnov <mithraen@altlinux.ru> 20080502:1.4.11.5-alt1
- 1.4.11.5

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 20080502:1.4.11.4-alt2
- remove useless symbol versioning

* Thu Sep 02 2010 Denis Smirnov <mithraen@altlinux.ru> 20080502:1.4.11.4-alt1
- 1.4.11.4

* Sat Jul 17 2010 Denis Smirnov <mithraen@altlinux.ru> 20080502:1.4.11.3-alt1
- 1.4.11.3

* Sun Nov 08 2009 Denis Smirnov <mithraen@altlinux.ru> 20080502:1.4.10.1-alt1
- 1.4.10.2

* Thu Dec 18 2008 Denis Smirnov <mithraen@altlinux.ru> 20080502:1.4.8-alt3
- pack %_libdir/libpri.so only in %name-devel

* Mon Nov 24 2008 Denis Smirnov <mithraen@altlinux.ru> 20080502:1.4.8-alt2
- cleanup spec

* Sun Nov 23 2008 Denis Smirnov <mithraen@altlinux.ru> 20080502:1.4.8-alt1
- 1.4.8
- q921.c: Fix a number of Q.921 bugs, found doing TBR4 compliance testing,
  thanks to Tzafrir, Xorcom, and co. (#12861). Thanks!
- pri.c, pri_internal.h, pri_q931.h, q931.c, pri_facility.c, pri_facility.h,
  libpri.h: Merging in additional Q.SIG features in 13454. Includes Q.SIG
  physical/logical channel mapping support, extended coding of Q.SIG name
  operations (calling name), and call rerouting support via added dialplan
  application.

* Fri Aug 08 2008 Denis Smirnov <mithraen@altlinux.ru> 20080502:1.4.7-alt1
- 1.4.7
- more correct license info (GPL2, not GPL2+)

* Tue Aug 05 2008 Denis Smirnov <mithraen@altlinux.ru> 20080502:1.4.6-alt3
- libpri-devel strict requires to libpri version

* Wed Jul 23 2008 Denis Smirnov <mithraen@altlinux.ru> 20080502:1.4.6-alt2
- split package (add -devel and -devel-static)

* Wed Jul 23 2008 Denis Smirnov <mithraen@altlinux.ru> 20080502:1.4.6-alt1
- 1.4.6

* Sun Jul 20 2008 Denis Smirnov <mithraen@altlinux.ru> 20080502:1.4.5-alt1
- 1.4.5
- multiple backports from trunk
- pri.c, pri_internal.h, q931.c, libpri.h: modify work done for issue #10552,
  making the support of inband audio after RELEASE a configurable option, since
  it is causing problems for a number of users (closes issue #13042)
- fix:   information channel selection field in the channel identification IE
  was displayed incorrectly when using 'pri intense debug'.

* Thu May 08 2008 Denis Smirnov <mithraen@altlinux.ru> 20080502:1.4.4-alt1
- 1.4.4

* Fri May 02 2008 Denis Smirnov <mithraen@altlinux.ru> 20080502:1.4.3-alt1
- 1.4.3

* Wed Jan 24 2007 Denis Smirnov <mithraen@altlinux.ru> 20060708:0.3.4-alt2
- svn update

* Sat Oct 28 2006 Denis Smirnov <mithraen@altlinux.ru> 20060708:0.3.4-alt1
- svn update

* Sat Jul 08 2006 Denis Smirnov <mithraen@altlinux.ru> 20060708:0.3.3-alt2
- svn update

* Wed Jun 07 2006 Denis Smirnov <mithraen@altlinux.ru> 20060607:0.3.3-alt1
- svn update

* Sat Jun 03 2006 Denis Smirnov <mithraen@altlinux.ru> 20060603:0.3.2-alt1
- multiple minor bugfixes

* Sat May 27 2006 Denis Smirnov <mithraen@altlinux.ru> 20060512:0.3.1-alt4
- x86_64 build fixed

* Sat May 13 2006 Denis Smirnov <mithraen@altlinux.ru> 20060512:0.3.1-alt3
- fix build with gcc 4.1

* Fri May 12 2006 Denis Smirnov <mithraen@altlinux.ru> 20060512:0.3.1-alt2
- svn update

* Sat Apr 29 2006 Denis Smirnov <mithraen@altlinux.ru> 20060429:0.3.1-alt1
- svn update

* Sat Feb 18 2006 Denis Smirnov <mithraen@altlinux.ru> 20060218:0.3.0-alt10
- svn update

* Tue Jan 03 2006 Denis Smirnov <mithraen@altlinux.ru> 20060103:0.3.0-alt8
- svn update

* Sat Dec 24 2005 Denis Smirnov <mithraen@altlinux.ru> 20051224:0.3.0-alt7
- cvs update
- bugfix for callerid

* Sat Dec 03 2005 Denis Smirnov <mithraen@altlinux.ru> 20051203:0.3.0-alt6
- cvs update

* Tue Nov 29 2005 Denis Smirnov <mithraen@altlinux.ru> 20051128:0.3.0-alt6
- building with debug info
- cvs update

* Tue Nov 29 2005 Denis Smirnov <mithraen@altlinux.ru> 20051128:0.3.0-alt5
- building with debug info

* Sun Oct 23 2005 Denis Smirnov <mithraen@altlinux.ru> 20051023:0.3.0-alt4
- cvs update
- user->user info parse/set

* Tue Oct 18 2005 Denis Smirnov <mithraen@altlinux.ru> 20051018:0.3.0-alt3
- cvs update
- debug patch added

* Mon Sep 19 2005 Denis Smirnov <mithraen@altlinux.ru> 20050919:0.3.0-alt2
- cvs update

* Thu Sep 15 2005 Denis Smirnov <mithraen@altlinux.ru> 20050915:0.3.0-alt1
- cvs update

* Sun Aug 14 2005 Denis Smirnov <mithraen@altlinux.ru> 20050813:1.0-alt1
- version update

* Tue Apr 19 2005 Denis Smirnov <mithraen@altlinux.ru> 20050419:1.0-alt0.4
- version update

* Wed Feb 02 2005 Denis Smirnov <mithraen@altlinux.ru> 20050202:1.0-alt0.3
- version update

* Mon Jan 24 2005 Denis Smirnov <mithraen@altlinux.ru> 20050124:1.0-alt0.2
- version update

* Thu Dec 30 2004 Denis Smirnov <mithraen@altlinux.ru> 20041230:1.0-alt0.1
- version update

* Sat Dec 25 2004 Denis Smirnov <mithraen@altlinux.ru> 20041225:1.0-alt0.1
- version update

* Sat Dec 18 2004 Denis Smirnov <mithraen@altlinux.ru> 20041218:1.0-alt0.1
- version update

* Thu Dec 02 2004 Denis Smirnov <mithraen@altlinux.ru> 20041201:1.0-alt0.1
- first build

