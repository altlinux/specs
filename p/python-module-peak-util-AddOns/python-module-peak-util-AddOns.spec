%define oname AddOns
Name: python-module-peak-util-%oname
Version: 0.6
Release: alt2.1

Summary: Dynamically extend other objects with AddOns (formerly ObjectRoles)

License: PSF or ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/AddOns/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: python-module-setuptools

Requires: python-module-decoratortools

Requires: python-module-peak

%setup_python_module %oname

Source: http://pypi.python.org/packages/source/A/AddOns/%oname-%version.tar

%description
In any sufficiently-sized application or framework, it's common to end up
lumping a lot of different concerns into the same class.  For example, you may
have business logic, persistence code, and UI all jammed into a single class.
Attribute and method names for all sorts of different operations get shoved
into a single namespace -- even when using mixin classes.

Separating concerns into different objects, however, makes it easier to write
reusable and separately-testable components.  The AddOns package
(``peak.util.addons``) lets you manage concerns using ``AddOn`` classes.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/peak/util/addons.*
%python_sitelibdir/%{oname}*.egg-info
%python_sitelibdir/%{oname}*.pth

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt2.1
- Rebuild with Python-2.7

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt2
- fix packing peak/util dir

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- initial build for ALT Linux Sisyphus

