%define major 4
%define oname itcl

Name: tcl-incrtcl4
Version: 4.0.5
Release: alt1

Summary: [Incr Tcl] is an object-oriented extension of the Tcl language
License: BSD
Group: Development/Tcl
Url: http://incrtcl.sourceforge.net/

# http://git.altlinux.org/gears/t/tcl-incrtcl4.git
Source: %name-%version-%release.tar

BuildRequires: rpm-build-tcl >= 0.4-alt1 tcl-devel >= 8.6.6 tk-devel >= 8.6.6
Provides: tcl-incrtcl = %EVR
Obsoletes: tcl-incrtcl < 4.0.0
Conflicts: tcl-incrtk < 4.0.0
Conflicts: tcl-iwidgets <= 4.0.2-alt3

%package devel
Summary: Header files and C programming manual for [Incr Tcl]
Group: Development/C
Provides: tcl-incrtcl-devel = %EVR
Conflicts: tcl-incrtcl-devel < 4.0.0
Requires: %name = %version-%release

%description
[incr Tcl] is an object-oriented extension of the Tcl language.  It
was created to support more structured programming in Tcl and
introduces the notion of objects. This object-oriented paradigm
adds another level of organization on top of the basic variable/procedure
elements, and the resulting code is easier to understand and maintain.

%description devel
[incr Tcl] is an object-oriented extension of the Tcl language.  It
was created to support more structured programming in Tcl and
introduces the notion of objects. This object-oriented paradigm
adds another level of organization on top of the basic variable/procedure
elements, and the resulting code is easier to understand and maintain.

This package includes header files and C programming manual for [incr Tcl].

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
ln -sf tcl/libitcl%version.so %buildroot%_libdir/libitcl%major.so
ln -sf libitcl%major.so %buildroot%_libdir/libitcl.so

%check
make test

%files
%_libdir/lib%oname%major.so
%_tcldatadir/itcl%version
%_tcllibdir/lib%oname%version.so
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
%_mandir/mann/itclcomponent.n*
%_mandir/mann/itcldelegate.n*
%_mandir/mann/itclextendedclass.n*
%_mandir/mann/itcloption.n*
%_mandir/mann/itclwidget.n*
%_mandir/mann/local.n*
%_mandir/mann/scope.n*

%files devel
%_includedir/*.h
%_libdir/itclConfig.sh
%_libdir/lib%oname.so
%_tcllibdir/libitclstub%version.a

%changelog
* Wed Apr 26 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 4.0.5-alt1
- 4.0.5
