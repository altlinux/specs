%define _unpackaged_files_terminate_build 1

%def_with python3
%define mname slip

Name: python-module-slip
Version: 0.6.5
Release: alt1
Summary: Miscellaneous convenience, extension and workaround code for Python

Group: Development/Python
License: %gpl2plus
Url: https://github.com/nphilipp/python-slip

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides the "slip" and the "slip.util" modules.

%package dbus
Summary: Convenience functions for dbus services
Group: Development/Python
Requires: %name = %version-%release

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

# No python3-slip-gtk because there is no pygtk2 for Python 3.x

%if_with python3
%package -n python3-module-%mname
Summary: Miscellaneous convenience, extension and workaround code for Python 3.x
Group: Development/Python3

%description -n python3-module-%mname
The Simple Library for Python 3.x packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides the "slip" and the "slip.util" modules.

%package -n python3-module-%mname-dbus
Summary: Convenience functions for dbus services
Group: Development/Python3
Requires: python3-module-%mname = %version-%release

%description -n python3-module-%mname-dbus
The Simple Library for Python 3.x packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.dbus.service.Object, which is a dbus.service.Object
derivative that ends itself after a certain time without being used and/or if
there are no clients anymore on the message bus, as well as convenience
functions and decorators for integrating a dbus service with PolicyKit.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
find ../python3 -name '*.py' -o -name '*.py.in' | xargs sed -i '1s|^#!/usr/bin/python|#!/usr/bin/python3|'
%endif

%build
%make_build PYTHON=/usr/bin/python
%if_with python3
pushd ../python3
%make_build PYTHON=/usr/bin/python3
popd
%endif

%install
%makeinstall_std PYTHON=/usr/bin/python
%if_with python3
pushd ../python3
%makeinstall_std PYTHON=/usr/bin/python3
popd
%endif

%files
%dir %python_sitelibdir/slip/
%python_sitelibdir/slip/__init__.py*
%python_sitelibdir/slip/util
%python_sitelibdir/slip/_wrappers
%python_sitelibdir/slip-%version-py%_python_version.egg-info

%files dbus
%doc doc/dbus
%python_sitelibdir/slip/dbus
%python_sitelibdir/slip.dbus-%version-py%_python_version.egg-info

%files gtk
%python_sitelibdir/slip/gtk
%python_sitelibdir/slip.gtk-%version-py%_python_version.egg-info

%if_with python3
%files -n python3-module-%mname
%dir %python3_sitelibdir/slip/
%python3_sitelibdir/slip/__init__.py*
%python3_sitelibdir/slip/util
%python3_sitelibdir/slip/_wrappers
%python3_sitelibdir/slip/__pycache__
%python3_sitelibdir/slip-%version-py%_python3_version.egg-info

%files -n python3-module-%mname-dbus
%doc doc/dbus
%python3_sitelibdir/slip/dbus
%python3_sitelibdir/slip.dbus-%version-py%_python3_version.egg-info
%endif

%changelog
* Fri Sep 08 2017 Mikhail Efremov <sem@altlinux.org> 0.6.5-alt1
- Build Python 3.x module.
- Updated to 0.6.5.

* Wed Jan 23 2013 Mikhail Efremov <sem@altlinux.org> 0.2.24-alt1
- Add strict dependency on python-module-slip in dbus subpackage.
- Updated to 0.2.24 (closes: #27678).

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.9-alt1.1
- Rebuild with Python-2.7

* Sun Apr 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.9-alt1
- Initial from Fedora
