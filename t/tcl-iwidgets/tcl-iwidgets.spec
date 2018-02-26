Name: tcl-iwidgets
Version: 4.0.2
Release: alt3

Summary: [incr Widgets] is an object-oriented mega-widget set based on [incr Tk]
License: BSD
Group: Development/Tcl
Url: http://incrtcl.sourceforge.net/

Source: %name-%version-%release.tar

Provides: iwidgets
Obsoletes: iwidgets

BuildRequires: tcl-devel tk-devel
BuildArch: noarch

%package demos
Summary: A collection of programs to demonstrate the features of the [incr Widgets]
Group: Development/Tcl
Requires: %name = %version-%release
Provides: itcl-demos iwidgets-demos
Obsoletes: itcl-demos iwidgets-demos

%description
[incr Widgets] is an object-oriented mega-widget set which extends Tcl/Tk
and is based on [incr Tcl] and [incr Tk].  This set of mega-widgets
delivers many new, general purpose widgets like option menus, comboboxes, 
selection boxes, and various dialogs whose couterparts are found in Motif 
and Windows.

%description demos
[incr Widgets] is an object-oriented mega-widget set which extends Tcl/Tk
and is based on [incr Tcl] and [incr Tk].  This set of mega-widgets
delivers many new, general purpose widgets like option menus, comboboxes, 
selection boxes, and various dialogs whose couterparts are found in Motif 
and Windows.

This package contains a collection of programs to demonstrate
the features of the widget set, based on [incr Widgets].

%prep
%setup
%__autoreconf
%configure

%install
%make_install \
    libdir=%buildroot%_tcldatadir \
    MAN_INSTALL_DIR=%buildroot%_mandir/mann \
    install

%files
%doc README license.terms
%_tcldatadir/iwidgets%version
%exclude %_tcldatadir/iwidgets%version/demos
%exclude %_tcldatadir/iwidgets%version/license.terms
%_mandir/mann/iwidgets_*.n*

%files demos
%_tcldatadir/iwidgets%version/demos

%changelog
* Thu Dec 27 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.2-alt3
- CVS snapshot @20070611

* Fri Jul 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.2-alt2
- CVS snapshot @20060411

* Sat Feb 28 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.2-alt1
- built separately and renamed

* Sat Sep 20 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1:3.2.1-alt4
- rebuilt in new env

* Sat Oct 19 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1:3.2.1-alt3
- iwidget-demos now obsoletes %name-demos

* Mon Oct  7 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 3.2.1-alt2
- rebuilt with tcl 8.4

* Tue Jul 16 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 3.2.1-alt1
- itcl 3.2.1
- iwidgets 4.0.0
- libpath changed to %%_tcllibpath
- src rpm splitted

* Mon Mar 18 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.3.4-alt7
- fixed encoding file for koi8-u

* Tue Mar 05 2002 Stanislav Ievlev <inger@altlinux.ru> 8.3.4-alt6
- removed all -lieee, 'cause
  fist: Programs can work with -lm and without -lieee
  second: Programs cannot link with lieee library

* Fri Dec  7 2001 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.3.4-alt5
- tclx fixes
- fixed tls build with stubs from tcl build dir
- fixed permissions for %_libdir/lib*stub*.a

* Wed Oct 24 2001 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.3.4-alt4
- Tcl/Tk 8.3.4
- SSL support added (tcl-tls)

* Mon Jul 23 2001 Dmitry V. Levin <ldv@altlinux.ru> 8.3.3-alt3
- Removed unnecessary provides and obsoletes.
- Added *_rel macros for subpackages and corrected inter-requires.
- Merged RH patches.

* Sat Jun 16 2001 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.3.3-alt2
- Rearranged files in subpackages: tcl, tcl-devel
- Tk splitted to: tk tk-devel tk-demos
- tclX 8.3.0, splitted to: tclx tclx-devel
- tix 8.1, splitted to: tix tix-devel tix-demos
- itcl 3.2, splitted to: itcl itcl-devel itcl-demos compat-itcl compat-itcl-demos. Huh :)
- tcllib removed to separate package
- Dropped most of changelog entries
- Group fixed

* Tue May 15 2001 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.3.3-alt1
- Tcl/Tk 8.3.3
- tcllib 0.8
- expect 5.32, splitted to subpackages.

* Wed Feb 07 2001 Dmitry V. Levin <ldv@fandra.org> 8.3.2-ipl8mdk
- Moved include files and C programming manual to tcl-devel subpackage.
- Fixed out empty manpages.

* Wed Nov 29 2000 AEN <aen@logic.ru> 8.3.2-ipl7mdk
- build for RE
- ps patch from Viktor Wagner
- bad requires patch

