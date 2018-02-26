%def_disable static

Name: Xbae
Version: 4.60.4
Release: alt2.qa1

Summary: The Motif matrix and caption widgets
License: MIT
Group: System/Libraries

Url: http://xbae.sourceforge.net
Source: xbae-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sat Dec 06 2008
BuildRequires: ctags gcc-c++ imake libXext-devel libXmu-devel libXp-devel libXpm-devel man openmotif-devel xorg-cf-files

%package -n lib%name
Summary: The %name Widget Set
Group: System/Libraries

%package -n lib%name-devel
Summary: Header files for %name development
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel = %version
Obsoletes: %name-devel

%if_enabled static
%package -n lib%name-devel-static
Summary: Static library for %name development
Group: Development/C
Requires: lib%name-devel = %version-%release
Provides: %name-devel-static = %version
Obsoletes: %name-devel-static
%endif

%package -n lib%name-docs
Summary: Documentation for development with %name
Group: Documentation
BuildArch: noarch

%description
This package provides the Motif matrix widget used in Xacc, as well as
the Motif caption widget. The matrix widget is widely used and will
display up to four billion rows of data in a spreadsheet-like form.
The Motif caption widget is a simple Motif manager widget that
associates a label with a child.  You will need to have either Motif
or LessTif installed in order to use %name's widgets.

%description -n lib%name
This package provides the Motif matrix widget used in Xacc, as well as
the Motif caption widget. The matrix widget is widely used and will
display up to four billion rows of data in a spreadsheet-like form.
The Motif caption widget is a simple Motif manager widget that
associates a label with a child.  You will need to have either Motif
or LessTif installed in order to use %name's widgets.

%description -n lib%name-devel
This package provides the Motif matrix widget used in Xacc, as well as
the Motif caption widget. The matrix widget is widely used and will
display up to four billion rows of data in a spreadsheet-like form.
The Motif caption widget is a simple Motif manager widget that
associates a label with a child.  You will need to have either Motif
or LessTif installed in order to use %name's widgets.

This package provides the libraries, include files, and other
resources needed for developing %name applications.

%if_enabled static
%description -n lib%name-devel-static
This package provides the Motif matrix widget used in Xacc, as well as
the Motif caption widget. The matrix widget is widely used and will
display up to four billion rows of data in a spreadsheet-like form.
The Motif caption widget is a simple Motif manager widget that
associates a label with a child.  You will need to have either Motif
or LessTif installed in order to use %name's widgets.

This package provides the static library needed for developing
statically linked %name applications.
%endif

%description -n lib%name-docs
This package contains documentation; please refer to source package
for useful examples if developing with %name.

%prep
%setup -n xbae-%version

%build
autoconf
CFLAGS="%optflags" \
%configure --enable-shared %{subst_enable static}
%make_build

%install
%make_install install DESTDIR=%buildroot
rm -rf %buildroot%_datadir/%name/

%files -n lib%name
%_libdir/*so.*

%files -n lib%name-devel
%_includedir/*
%_mandir/man?/*
%_libdir/*so

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files -n lib%name-docs
%doc doc/[^M]*

%changelog
* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 4.60.4-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sun May 24 2009 Michael Shigorin <mike@altlinux.org> 4.60.4-alt2
- rebuilt against openmotif-2.3.2

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 4.60.4-alt1
- 4.60.4
  + removed patch (applied upstream)
- fixed build on x86_64
- introduced docs subpackage
- spec cleanup

* Sun Feb 26 2006 Yury A. Zotov <yz@altlinux.ru> 4.60.2-alt1
- new version
- xbae-4.60.2-alt1-makefile-mandir.patch
- BuildRequires updated

* Mon Feb 21 2005 Yury A. Zotov <yz@altlinux.ru> 4.51.01-alt1
- new version
- spec cleanup

* Sat Aug 28 2004 Yury A. Zotov <yz@altlinux.ru> 4.50.97-alt1
- new version
- Xbae-4.50.93-alt1-configure-scripts_Makefile.patch revoked

* Sun Jun 20 2004 Yury A. Zotov <yz@altlinux.ru> 4.50.93-alt1
- new version
- do not make scripts/Makefile in ./configure
- do not make in scripts/

* Sat Dec 13 2003 Yury A. Zotov <yz@altlinux.ru> 4.50.2-alt3
- do not package *.la files

* Wed Oct 29 2003 Yury A. Zotov <yz@altlinux.ru> 4.50.2-alt2
- build with openmotif

* Tue Oct 07 2003 Dmitry V. Levin <ldv@altlinux.org> 4.50.2-alt1
- Updated to 4.50.2.

* Thu Oct 24 2002 Dmitry V. Levin <ldv@altlinux.org> 4.50.0-alt1
- Updated to 4.50.0.

* Tue Dec 04 2001 Dmitry V. Levin <ldv@alt-linux.org> 9.0.9-alt1
- ALT adaptions.
- Libificated.

* Wed Nov 28 2001 Than Ngo <than@redhat.com> 4.9.1-1
- separate rpm

* Mon Aug 7 2000 Tim Powers <timp@redhat.com>
- add Conflicts lesstif and lesstif-devel to fix bug #15617

* Tue Aug 1 2000 Tim Powers <timp@redhat.com>
- added postun section, fix bug #15001

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Sat Jul 22 2000 Tim Powers <timp@redhat.com>
- fixed missing BuildPreReq

* Wed Jul 12 2000 Tim Powers <timp@redhat.com>
- patched to compile cleanly (patch2)

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Apr 26 2000 TIm Powers <timp@redhat.com>
- updated to 4.7

* Thu Dec 23 1999 Tim Powers <timp@redhat.com>
- rebuilt for 6.2

* Tue Aug 17 1999 Tim Powers <timp@redhat.com>
- rebuilt, not including examples

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- fix perms in docs

* Fri Jul 2 1999 Tim Powers <timp@redhat.com>
- built for 6.1

* Thu Apr 15 1999 Michael Maher <mike@redhat.com>
- built package for 6.0

* Wed Oct 06 1998 Michael Maher <mike@redhat.com>
- rebuilt pacakge; cleaned up spec file

* Wed May 20 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to Xabelin-4.6.2.4

* Mon Jan 26 1998 Otto Hammersmith <otto@redhat.com>
- built the package.
