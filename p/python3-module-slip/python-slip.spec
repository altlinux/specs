%define _unpackaged_files_terminate_build 1

%define mname slip

Name: python3-module-slip
Version: 0.6.5
Release: alt3
Summary: Miscellaneous convenience, extension and workaround code for Python

Group: Development/Python3
License: %gpl2plus
Url: https://github.com/nphilipp/python-slip

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

BuildRequires(pre): rpm-build-python3

%description
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides the "slip" and the "slip.util" modules.

%package dbus
Summary: Convenience functions for dbus services
Group: Development/Python3
Requires: %name = %version-%release

%description dbus
The Simple Library for Python packages contain miscellaneous code for
convenience, extension and workaround purposes.

This package provides slip.dbus.service.Object, which is a dbus.service.Object
derivative that ends itself after a certain time without being used and/or if
there are no clients anymore on the message bus, as well as convenience
functions and decorators for integrating a dbus service with PolicyKit.

# No python3-slip-gtk because there is no pygtk2 for Python 3.x

%prep
%setup
find . -name '*.py' -o -name '*.py.in' | xargs sed -i '1s|^#!/usr/bin/python|#!/usr/bin/python3|'

%build
%make_build PYTHON=/usr/bin/python3

%install
%makeinstall_std PYTHON=/usr/bin/python3

%files
%dir %python3_sitelibdir/slip/
%python3_sitelibdir/slip/__init__.py*
%python3_sitelibdir/slip/util
%python3_sitelibdir/slip/_wrappers
%python3_sitelibdir/slip/__pycache__
%python3_sitelibdir/slip-%version-py%_python3_version.egg-info

%files dbus
%doc doc/dbus
%python3_sitelibdir/slip/dbus
%python3_sitelibdir/slip.dbus-%version-py%_python3_version.egg-info

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.6.5-alt3
- Rename package, cleanup spec.

* Mon Mar 18 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.5-alt2
- Disabled building modules for python-2.

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
