%define major 4
%define oname itk

Name: tcl-incrtk4
Version: 4.1.0
Release: alt3

Summary: [incr Tk] is a framework for building mega-widgets
License: BSD
Group: Development/Tcl
Url: http://incrtcl.sourceforge.net/

# repacked %oname%version.tar.gz from https://sourceforge.net/projects/incrtcl/files/
Source: %oname%version.tar
Patch1: 0001-ALT-TEA.patch
Patch2: 0002-ALT-soname.patch

BuildRequires: rpm-build-tcl >= 0.4-alt1 tk-devel >= 8.6.6
BuildRequires: tcl-pkgs-devel
Provides: tcl-incrtk = %EVR
Obsoletes: tcl-incrtk < 4.0.0
Conflicts: tcl-iwidgets <= 4.0.2-alt3

Requires: tcl-incrtcl4 tk

%package devel
Summary: Header files and C programming manual for [Incr Tk]
Group: Development/C
Requires: %name = %EVR

%description
[incr Tk] is a framework for building mega-widgets.  It uses [incr Tcl]
to  support  the  object  paradigm, and adds base classes which provide
default widget behaviors.

%description devel
[incr Tk] is a framework for building mega-widgets.  It uses [incr Tcl]
to  support  the  object  paradigm, and adds base classes which provide
default widget behaviors.

This package includes header files and C programming manual for [incr Tk].

%prep
%setup -q -n %oname%version
# remove unneeded stuff
rm -r win/
%autopatch -p2

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_tcllibdir/lib%oname%version.so
%_tcllibdir/itk%version
%_mandir/mann/*.n*

%files devel
%_includedir/*.h

%changelog
* Wed Oct 09 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.1.0-alt3
- Built against tcl-incrtcl4 from tcl-pkgs.
- Adopted to new Tcl/Tk extension policy.

* Sat Aug 17 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.1.0-alt2
- Added missing dependencies to tcl-incrtcl4 and tk.
- Disabled tests cause they required X11 runtime.

* Mon Apr 15 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.1.0-alt1
- 4.1.0

* Wed Apr 26 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.2-alt1
- 4.0.2
