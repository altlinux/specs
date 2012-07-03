Name: tcl-tix
Version: 8.4.3
Release: alt1

Summary: A set of capable widgets for Tk
License: BSD
Group: Development/Tcl
Url: http://tix.sourceforge.net/

Source: %name-%version-%release.tar

BuildRequires(pre): rpm-build-tcl
BuildRequires: tk-devel >= 8.5.0

Provides: tix = 1:%version-%release
Obsoletes: tix

Provides: tcl-tix-devel = %version-%release
Obsoletes: tcl-tix-devel

%package demos
Summary: A collection of programs to demonstrate the features of the Tix
Group: Development/Tcl
Requires: %name = %version-%release
Provides: tix-demos = 1:%version-%release
Obsoletes: tix-demos

%description
Tix (Tk Interface Extension), an add-on for the Tk widget set, is an
extensive set of over 40 widgets.  In general, Tix widgets are more
complex and more capable than the widgets provided in Tk.  Tix widgets
include a ComboBox, a Motif-style FileSelectBox, an MS Windows-style
FileSelectBox, a PanedWindow, a NoteBook, a hierarchical list, a
directory tree and a file manager.

Install the tix package if you want to try out more complicated widgets
for Tk.  You'll also need to have the tcl and tk packages installed.

%description demos
Tix (Tk Interface Extension), an add-on for the Tk widget set, is an
extensive set of over 40 widgets.  In general, Tix widgets are more
complex and more capable than the widgets provided in Tk.  Tix widgets
include a ComboBox, a Motif-style FileSelectBox, an MS Windows-style
FileSelectBox, a PanedWindow, a NoteBook, a hierarchical list, a
directory tree and a file manager.

This package contains a collection of programs to demonstrate
the features of the Tix widget set.

%prep
%setup
%teapatch

%build
%autoreconf
%configure
%make_build

%install 
%makeinstall
rm -f %buildroot%_tcldatadir/Tix%version/pref/WmDefault.py
cp -a demos %buildroot%_tcldatadir/Tix%version

%files
%doc README.txt docs/FAQ.txt
%doc docs/html

%_tcllibdir/libTix%version.so

%_tcldatadir/Tix%version
%exclude %_tcldatadir/Tix%version/demos

%files demos
%_tcldatadir/Tix%version/demos

%changelog
* Tue Dec 16 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.3-alt1
- 8.4.3 released

* Sat Dec 22 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.4.2-alt1
- 8.4.2 released

* Sat Jul 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.2.0-alt4
- fixed build for x86_64

* Mon Mar 27 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.2.0-alt3
- rebuilt in new env

* Sat Sep 27 2003 Sergey Bolshakov <sbolshakov@altlinux.ru> 8.2.0-alt2
- rebuilt in new env

* Tue Sep 24 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.2.0-alt1
- 8.2.0
- rebuilt with tcl 8.4

* Mon Jun 3 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 8.1.1-alt8
- tixwish dropped
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

