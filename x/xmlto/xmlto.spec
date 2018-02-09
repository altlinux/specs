%def_with tex_subpkg

Name: xmlto
Version: 0.0.28
Release: alt2

Summary: A tool for converting XML files to various formats.
Group: Publishing
License: %gpl2plus
Url: https://fedorahosted.org/%name/

# VCS: http://svn.fedorahosted.org/svn/xmlto/
Source: https://fedorahosted.org/releases/x/m/%name/%name-%version.tar.gz

Requires: docbook-style-xsl >= 1.56
%{!?_with_tex_subpkg:Requires: passivetex >= 20040310}
Requires: docbook-dtds libpaper xml-utils xsltproc

BuildRequires(pre): rpm-build-licenses
BuildRequires: libpaper docbook-dtds docbook-style-xsl flex xsltproc

%description
This is a package for converting XML files to various formats using XSL
stylesheets.

%if_with tex_subpkg
%package tex
Group: Publishing
Summary: A set of %name backends with TeX requirements
BuildArch: noarch
Requires: passivetex
Requires: %name = %version-%release

%description tex
This subpackage contains %name backend scripts which do require
PassiveTeX/TeX for functionality.
%endif

%prep
%setup

%build
%autoreconf
%configure
%make_build
bzip2 --keep --best --force ChangeLog

%install
%makeinstall_std

%check
%make check

%files
%doc AUTHORS ChangeLog.* FAQ NEWS THANKS
%_bindir/*
%_man1dir/*
%_datadir/%name
%if_with tex_subpkg
%exclude %_datadir/%name/format/fo/dvi
%exclude %_datadir/%name/format/fo/ps
%exclude %_datadir/%name/format/fo/pdf

%files tex
%_datadir/%name/format/fo/dvi
%_datadir/%name/format/fo/ps
%_datadir/%name/format/fo/pdf
%endif


%changelog
* Fri Feb 09 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.28-alt2
- NMU: prepared for new texlive

* Wed Feb 01 2017 Yuri N. Sedunov <aris@altlinux.org> 0.0.28-alt1
- 0.0.28
- fixed urls
- %%check section

* Mon Jun 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.26-alt1
- Version 0.0.26

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.25-alt1
- Version 0.0.25

* Wed Mar 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.23-alt3
- Rebuilt for debuginfo

* Tue Nov 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.23-alt2
- Fixed requirements (thnx ldv@)

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.23-alt1
- Version 0.0.23

* Sun Jan 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.21-alt3.1
- Avoided requirement on concrete tex distribution

* Sat Feb 21 2009 Led <led@altlinux.ru> 0.0.21-alt3
- fixed Requires

* Fri Feb 20 2009 Led <led@altlinux.ru> 0.0.21-alt2
- cleaned up spec
- fixed parsing '--stringparam'

* Sat Jul 26 2008 Led <led@altlinux.ru> 0.0.21-alt1
- 0.0.21
- cleaned up spec

* Wed Feb 25 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.0.18-alt1
- Updated to upstream release 0.0.18
- xmlto.mak no longer needed

* Mon Oct  06 2003 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.0.12-alt2
- fixed buildreq

* Mon Dec 16 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 0.0.12-alt1
- new version, not noarch now

* Thu Oct 17 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 0.0.11-alt1
- new version

* Tue Sep 10 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 0.0.10-alt1
- first build for altlinux

* Tue Jul 9 2002 Tim Waugh <twaugh@redhat.com> 0.0.10-4
- Ship xmlto.mak.

* Thu Jun 27 2002 Tim Waugh <twaugh@redhat.com> 0.0.10-3
- Some db2man improvements from CVS.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 0.0.10-2
- automated rebuild

* Tue Jun 18 2002 Tim Waugh <twaugh@redhat.com> 0.0.10-1
- 0.0.10.
- No longer need texinputs patch.

* Tue Jun 18 2002 Tim Waugh <twaugh@redhat.com> 0.0.9-3
- Fix TEXINPUTS problem with ps and dvi backends.

* Thu May 23 2002 Tim Powers <timp@redhat.com> 0.0.9-2
- automated rebuild

* Wed May  1 2002 Tim Waugh <twaugh@redhat.com> 0.0.9-1
- 0.0.9.
- The nonet patch is no longer needed.

* Fri Apr 12 2002 Tim Waugh <twaugh@redhat.com> 0.0.8-3
- Don't fetch entities over the network.

* Thu Feb 21 2002 Tim Waugh <twaugh@redhat.com> 0.0.8-2
- Rebuild in new environment.

* Tue Feb 12 2002 Tim Waugh <twaugh@redhat.com> 0.0.8-1
- 0.0.8.

* Fri Jan 25 2002 Tim Waugh <twaugh@redhat.com> 0.0.7-2
- Require the DocBook DTDs.

* Mon Jan 21 2002 Tim Waugh <twaugh@redhat.com> 0.0.7-1
- 0.0.7 (bug #58624, bug #58625).

* Wed Jan 16 2002 Tim Waugh <twaugh@redhat.com> 0.0.6-1
- 0.0.6.

* Wed Jan 09 2002 Tim Powers <timp@redhat.com> 0.0.5-4
- automated rebuild

* Wed Jan  9 2002 Tim Waugh <twaugh@redhat.com> 0.0.5-3
- 0.0.6pre2.

* Wed Jan  9 2002 Tim Waugh <twaugh@redhat.com> 0.0.5-2
- 0.0.6pre1.

* Tue Jan  8 2002 Tim Waugh <twaugh@redhat.com> 0.0.5-1
- 0.0.5.

* Mon Dec 17 2001 Tim Waugh <twaugh@redhat.com> 0.0.4-2
- 0.0.4.
- Apply patch from CVS to fix silly typos.

* Sat Dec  8 2001 Tim Waugh <twaugh@redhat.com> 0.0.3-1
- 0.0.3.

* Wed Dec  5 2001 Tim Waugh <twaugh@redhat.com>
- Built for Red Hat Linux.

* Fri Nov 23 2001 Tim Waugh <twaugh@redhat.com>
- Initial spec file.
