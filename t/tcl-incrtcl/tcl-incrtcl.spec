%define major 3.4

Name: tcl-incrtcl
Version: 3.4.0
Release: alt1

Summary: [Incr Tcl] is an object-oriented extension of the Tcl language
License: BSD
Group: Development/Tcl
Url: http://incrtcl.sourceforge.net/

Source: %name-%version-%release.tar

BuildRequires: rpm-build-tcl >= 0.4-alt1 tk-devel >= 8.5.0

%package devel
Summary: Header files and C programming manual for [Incr Tcl]
Group: Development/C
Requires: %name = %version-%release

%package -n tcl-incrtk
Summary: [incr Tk] is a framework for building mega-widgets
Group: Development/Tcl

%package -n tcl-incrtk-devel
Summary: Header files and C programming manual for [Incr Tk]
Group: Development/C
Requires: tcl-incrtk = %version-%release %name-devel = %version-%release

%description
[incr Tcl] is an object-oriented extension of the Tcl language.  It
was created to support more structured programming in Tcl and
introduces the notion of objects. This object-oriented paradigm
adds another level of organization on top of the basic variable/procedure
elements, and the resulting code is easier to understand and maintain.

%description -n tcl-incrtk
[incr Tk] is a framework for building mega-widgets.  It uses [incr Tcl]
to  support  the  object  paradigm, and adds base classes which provide
default widget behaviors.

%description devel
[incr Tcl] is an object-oriented extension of the Tcl language.  It
was created to support more structured programming in Tcl and
introduces the notion of objects. This object-oriented paradigm
adds another level of organization on top of the basic variable/procedure
elements, and the resulting code is easier to understand and maintain.

This package includes header files and C programming manual for [incr Tcl].

%description -n tcl-incrtk-devel
[incr Tk] is a framework for building mega-widgets.  It uses [incr Tcl]
to  support  the  object  paradigm, and adds base classes which provide
default widget behaviors.

This package includes header files and C programming manual for [incr Tk].

%prep
%setup
%teapatch -C itcl
%teapatch -C itk
sed -i 's/\$dir \"/\$dir .. .. .. %_lib tcl \"/' itcl/pkgIndex.tcl.in itk/pkgIndex.tcl.in

%build
%configure 
%make_build

%install
%make_install DESTDIR=%buildroot install
ln -sf tcl/libitk%major.so %buildroot%_libdir/libitk.so
ln -sf tcl/libitcl%major.so %buildroot%_libdir/libitcl.so
mv %buildroot%_tcllibdir/lib*stub*.a %buildroot%_libdir/

%files
%doc README
%_tcllibdir/libitcl%major.so
%_tcldatadir/itcl%major
%_mandir/mann/body.n*
%_mandir/mann/class.n*
%_mandir/mann/code.n*
%_mandir/mann/configbody.n*
%_mandir/mann/delete.n*
%_mandir/mann/ensemble.n*
%_mandir/mann/find.n*
%_mandir/mann/is.n*
%_mandir/mann/itcl.n*
%_mandir/mann/itclvars.n*
%_mandir/mann/local.n*
%_mandir/mann/scope.n*

%files devel
%_includedir/itcl*.h
%_libdir/libitcl.so
%_libdir/libitclstub%major.a
%_libdir/itclConfig.sh

%files -n tcl-incrtk
%doc itk/examples itk/demos
%_tcllibdir/libitk%major.so
%_tcldatadir/itk%major
%_mandir/mann/Archetype.n*
%_mandir/mann/itk.n*
%_mandir/mann/itkvars.n*
%_mandir/mann/Toplevel.n*
%_mandir/mann/usual.n*
%_mandir/mann/Widget.n*

%files -n tcl-incrtk-devel
%_includedir/itk*.h
%_libdir/libitk.so
#_libdir/libitkstub%major.a

%changelog
* Thu Dec 27 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.4.0-alt1
- updated to CVS shapshot @ 20071106 and rebuilt against tcl8.5

* Fri Jul 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.3.0-alt4
- CVS snapshot @20060606

* Sat Feb 25 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.3.0-alt3
- fixed build with bash3

* Fri May  6 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.3.0-alt2
- rebuilt in new env

* Sat Feb 28 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.3.0-alt1
- CVS snapshot @ 20040212
- renamed to tcl-incrtcl
- tk part splitted
- iwidgets now have own package

* Sat Sep 20 2003 Sergey Bolshakov <s.bolshakov@sam-solutions.net> 1:3.2.1-alt4
- rebuilt in new env

* Sat Oct 19 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1:3.2.1-alt3
- iwidget-demos now obsoletes %name-demos

* Mon Oct  7 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 3.2.1-alt2
- rebuilt with tcl 8.4

* Tue Jul 16 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 3.2.1-alt1
- itcl 3.2.1
- iwidgets 4.0.0
- libpath changed to %_tcllibdir
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

