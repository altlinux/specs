Name: dbus-inspector
Version: 0
Release: alt2.svn7.1.1
BuildArch: noarch

Summary: show the contents of the DBus message bus
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.vitavonni.de/projekte/dbus-inspector.html.en
Packager: Alex V. Myltsev <avm@altlinux.ru>

Source: %name-%version.tar

%py_requires libglade

%description
DBus-Inspector is a development tool to show the contents of the DBus
message bus. It uses the "Introspection" data provided by most
applications.

It mostly shows methods (later versions will also allow you to trigger
methods directly for testing purposes) and signals with their signature.

%prep
%setup

%install
%make_install DESTDIR=%buildroot sitelibdir=%python_sitelibdir

%files
%_bindir/%name
%_datadir/%name
%python_sitelibdir/dbusinspect.py*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0-alt2.svn7.1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0-alt2.svn7.1
- Rebuilt with python 2.6

* Sun Aug 23 2009 Alexander Myltsev <avm@altlinux.ru> 0-alt2.svn7
- Add explicit dependency on Glade (closes #18928).

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0-alt1.svn7.1
- Rebuilt with python-2.5.

* Tue Sep 18 2007 Alex V. Myltsev <avm@altlinux.ru> 0-alt1.svn7
- Initial build for Sisyphus.

