%define major 4
%define oname itk

Name: tcl-incrtk4
Version: 4.0.2
Release: alt1

Summary: [incr Tk] is a framework for building mega-widgets
License: BSD
Group: Development/Tcl
Url: http://incrtcl.sourceforge.net/

# http://git.altlinux.org/gears/t/tcl-incrtcl4.git
Source: %name-%version-%release.tar

BuildRequires: rpm-build-tcl >= 0.4-alt1 tk-devel >= 8.6.6
BuildRequires: tcl-incrtcl4-devel
Provides: tcl-incrtk = %EVR
Obsoletes: tcl-incrtk < 4.0.0
Conflicts: tcl-iwidgets <= 4.0.2-alt3

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
%setup
%teapatch
sed -i 's/\$dir \"/\$dir .. .. .. %_lib tcl \"/' pkgIndex.tcl.in

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
make test

%files
%_tcllibdir/lib%oname%version.so
%_tcldatadir/itk%version
%_mandir/mann/*.n*

%files devel
%_includedir/*.h

%changelog
* Wed Apr 26 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.2-alt1
- 4.0.2
