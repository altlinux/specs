# vim: set ft=spec: -*- rpm-spec -*-

%define rep_archlibdir %(pkg-config --variable=repcommonexecdir librep)

Name: rep-gtk
Version: 0.90.8
Release: alt1

Summary: GTK+ binding for librep Lisp environment
Group: Development/Lisp
License: GPLv2
Url: http://rep-gtk.sourceforge.net/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Tue Mar 17 2009
BuildRequires: libgtk+2-devel librep-devel

%description
This is a binding of GTK+ for the librep Lisp interpreter. It is based
on Marius Vollmer's guile-gtk package (initially version 0.15, updated
to 0.17), with a new glue-code generator.

%package devel
Summary: Development files for %name
Group: Development/Lisp
Requires: %name = %version-%release

%description devel
This is a binding of GTK+ for the librep Lisp interpreter. It is based
on Marius Vollmer's guile-gtk package (initially version 0.15, updated
to 0.17), with a new glue-code generator.

This package contains development files for %name.

%prep
%setup
%patch -p1
cp -pfv %_datadir/automake/config.{guess,sub} .

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc NEWS README README.gtk-defs README.guile-gtk
%dir %rep_archlibdir/gui
%dir %rep_archlibdir/gui/gtk-2
%rep_archlibdir/gui/gtk-2/gtk.so

%files devel
%doc ChangeLog gtk.defs gdk.defs examples
%_includedir/rep-gtk
%_pkgconfigdir/rep-gtk.pc

%changelog
* Mon Nov 28 2011 Dmitry Derjavin <dd@altlinux.org> 0.90.8-alt1
- [0.90.8];
- *.la removed;
- docs cleanup.

* Sun Feb 14 2010 Alexey I. Froloff <raorn@altlinux.org> 0.90.2-alt1
- [0.90.2]

* Wed Nov 25 2009 Alexey I. Froloff <raorn@altlinux.org> 0.90.0-alt1
- [0.90.0]

* Tue Mar 17 2009 Sir Raorn <raorn@altlinux.ru> 0.18.4-alt1
- [0.18.4]
 + Dropped Glade and GNOME support
 + Added pkgconfig file

* Sun Feb 08 2009 Sir Raorn <raorn@altlinux.ru> 0.18-alt5
- Updated build deps

* Sat Dec 27 2008 Sir Raorn <raorn@altlinux.ru> 0.18-alt4
- Rebuilt with new librep

* Sat Dec 06 2008 Sir Raorn <raorn@altlinux.ru> 0.18-alt3
- Updated to trunk (svn r389)

* Sun Sep 21 2008 Sir Raorn <raorn@altlinux.ru> 0.18-alt2
- Updated to trunk (svn r378)

* Thu May 29 2008 Sir Raorn <raorn@altlinux.ru> 0.18-alt1
- Built for Sisyphus (0.18+cvs20060201 AKA svn r350)

