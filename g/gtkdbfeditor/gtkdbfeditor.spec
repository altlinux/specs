Name: gtkdbfeditor
Version: 0.4.0
Release: alt1

Summary: A GTK+ based DBF Editor
License: GPL
Group: Databases
URL: http://gtkdbfeditor.sourceforge.net/

Source0: %name-%version.tar.gz

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sat Apr 19 2008
BuildRequires: gcc-c++ libglade-devel

%description
GTK DBF Editor is a program to edit dbf files. It supports simple
editing functions

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/gtkdbfeditor
%dir %_datadir/gtkdbfeditor/
%_datadir/gtkdbfeditor/gtkdbfeditor.glade

%changelog
* Sat Apr 19 2008 Igor Zubkov <icesik@altlinux.org> 0.4.0-alt1
- 0.2.0 -> 0.4.0

* Sat Apr 15 2006 Igor Zubkov <icesik@altlinux.ru> 0.2.0-alt1
- Initial build for Sisyphus
