Name: gtkdbfeditor
Version: 1.0.4
Release: alt1

Summary: A GTK+ based DBF Editor
License: GPL
Group: Databases
URL: http://sdteffen.de/gtkdbfeditor

Source0: %name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Wed Oct 10 2012
BuildRequires: libglade-devel

%description
GTK DBF Editor is a program to edit dbf files. It supports simple
editing functions.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc ChangeLog NEWS README TODO
%_bindir/gtkdbfeditor
%dir %_datadir/gtkdbfeditor/
%_datadir/gtkdbfeditor/gtkdbfeditor.glade

%changelog
* Wed Oct 10 2012 Igor Zubkov <icesik@altlinux.org> 1.0.4-alt1
- 0.4.0 -> 1.0.4

* Sat Apr 19 2008 Igor Zubkov <icesik@altlinux.org> 0.4.0-alt1
- 0.2.0 -> 0.4.0

* Sat Apr 15 2006 Igor Zubkov <icesik@altlinux.ru> 0.2.0-alt1
- Initial build for Sisyphus
