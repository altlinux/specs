%define teaname tktreectrl
%define major 2.4

Name: tcl-%teaname
Version: %major.1
Release: alt1

Summary: TkTreeCtrl is a multi-column hierarchical listbox widget for the Tk GUI toolkit
License: BSD
Group: Development/Tcl
Url: http://tktreectrl.sourceforge.net/

# http://git.altlinux.org/gears/t/tcl-tktreectrl.git
Source: %name-%version-%release.tar

Requires: tk >= 8.4.0-alt1
BuildRequires: rpm-build >= 4.0.4-alt41 rpm-build-tcl >= 0.2-alt1 tk-devel >= 8.4.0-alt1

%description
TkTreeCtrl is a multi-column hierarchical listbox widget for the Tk GUI toolkit

%prep
%setup -c
%teapatch

%build
chmod +x ./configure
%configure
%make_build

%install
%makeinstall
mv %buildroot%_tcllibdir/htmldoc .
cat doc/man.macros doc/treectrl.n |grep -v '^.so man.macros' > treectrl.n
install -m0644 -D treectrl.n %buildroot%_mandir/mann/treectrl.n

%files
%doc ChangeLog demos htmldoc
%_tcllibdir/libtreectrl%major.so
%_tcldatadir/treectrl%version
%_mandir/mann/*

%changelog
* Tue Jul 04 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.4.1-alt1
- 2.4.1 released (ALT#30850)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.2-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Nov 27 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2-alt1
- 2.2 released

* Sat Jul 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt1
- CVS snapshot @20060405

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1-alt0.1
- CVS snapshot @ 20041009

* Sun May 16 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt4
- CVS snapshot @ 20040209

* Sat Dec 13 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt3
- CVS snapshot @ 20031202

* Sat Oct 25 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt2
- CVS snapshot @ 20031025

* Thu Dec 26 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.0-alt1
- first build for distribuition %distribution

