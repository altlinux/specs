Name: python-module-slip
Version: 0.2.9
Release: alt1.1
Summary: Miscellaneous convenience, extension and workaround code for Python

Group: Development/Python
License: GPLv2+
Url: http://fedorahosted.org/python-slip
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel

%description
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides the "slip" and the "slip.util" modules.

%package dbus
Summary: Convenience functions for dbus services
Group: Development/Python

%description dbus
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.dbus.service.Object, which is a dbus.service.Object
derivative that ends itself after a certain time without being used and/or if
there are no clients anymore on the message bus, as well as convenience
functions and decorators for integrating a dbus service with PolicyKit.

%package gtk
Summary: Code to make auto-wrapping gtk labels
Group: Development/Python

%description gtk
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.gtk.set_autowrap(), a convenience function which
lets gtk labels be automatically re-wrapped upon resizing.

%prep
%setup -q

%build
%make_build

%install
%makeinstall_std

%files
%doc COPYING doc/dbus
%dir %python_sitelibdir/slip/
%python_sitelibdir/slip/__init__.py*
%python_sitelibdir/slip/util
%python_sitelibdir/slip-%version-py%__python_version.egg-info

%files dbus
%doc doc/dbus/*
%python_sitelibdir/slip/dbus
%python_sitelibdir/slip.dbus-%version-py%__python_version.egg-info

%files gtk
%python_sitelibdir/slip/gtk
%python_sitelibdir/slip.gtk-%version-py%__python_version.egg-info

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.9-alt1.1
- Rebuild with Python-2.7

* Sun Apr 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.9-alt1
- Initial from Fedora
