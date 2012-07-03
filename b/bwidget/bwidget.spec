Name: bwidget
Version: 1.9.1
Release: alt1

Summary: The BWidget Toolkit is a high-level Widget Set for Tcl/Tk
License: BSD
Group: Development/Tcl
Url: http://tcllib.sourceforge.net/

Source: %name-%version.tar

BuildRequires: tcl rpm-build >= 4.0.4-alt41 rpm-build-tcl >= 0.2-alt1
BuildArch: noarch

%description
The BWidget Toolkit is a high-level Widget Set for Tcl/Tk built using
native Tcl/Tk 8.x namespaces. The BWidgets have a professional look&feel
as in other well known Toolkits (Tix or Incr Widget) but the concept is
radically different because everything is native so no platform compilation,
no compiled extension library are needed. The code is 100%% Pure Tcl/Tk.

%prep
%setup

%install
mkdir -p %buildroot%_tcldatadir/%name-%version/{images,lang}
install -pm0644 *.tcl %buildroot%_tcldatadir/%name-%version
install -pm0644 images/*.{xbm,gif} %buildroot%_tcldatadir/%name-%version/images
install -pm0644 lang/* %buildroot%_tcldatadir/%name-%version/lang

%files
%doc ChangeLog README* LICENSE* demo BWman
%_tcldatadir/%name-%version

%changelog
* Thu Aug 25 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.9.1-alt1
- 1.9.1 released

* Tue Nov 14 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.0-alt1
- 1.8.0 released

* Wed Jul 13 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.0-alt3
- updated to CVS snapshot @ 20050225

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.0-alt2
- rebuilt against new shiny tcl reqprov finder

* Sun May 16 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Mon Jun  2 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1.6.0-alt1
- 1.6.0

* Tue Oct  8 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.4.1-alt2
- updated to CVS snapshot @ 20020925

* Thu Jun  6 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.4.1-alt1
- 1.4.1
- moved to %_tcldatadir

* Sat May 25 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.4.0-alt2
- updated from CVS

* Sat May 25 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.4.0-alt1
- 1.4.0

* Tue Jun 12 2001 Sergey Bolshakov <s.bolshakov@belcaf.com> 
- First spec file for ALT Linux distribution.
