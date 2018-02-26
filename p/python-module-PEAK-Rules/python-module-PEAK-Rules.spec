%define oname PEAK-Rules
%define rel .dev-r2659
Name: python-module-%oname
Version: 0.5a1
Release: alt2.1

Summary: Python module with Generic functions and business rules support systems

License: ZPL 2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/PEAK-Rules

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: python-module-setuptools

%setup_python_module PEAK-Rules

Requires: python-module-peak

Requires: python-module-decoratortools python-module-Extremes
Requires: python-module-peak-util-BytecodeAssembler
Requires: python-module-peak-util-AddOns

Source: http://files.turbogears.org/eggs/%oname-%version%rel.tar

%description
PEAK-Rules is a highly-extensible framework for creating and using generic
functions, from the very simple to the very complex.  Out of the box, it
supports multiple-dispatch on positional arguments using tuples of types,
full predicate dispatch using strings containing Python expressions,
and CLOS-like method combining.  (But the framework allows you to mix
and match dispatch engines and custom method combinations, if you need
or want to.)

%prep
%setup -n %oname-%version%rel

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/peak/rules/
%python_sitelibdir/PEAK_Rules*.egg-info
%python_sitelibdir/PEAK_Rules*.pth

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5a1-alt2.1
- Rebuild with Python-2.7

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5a1-alt2
- fix packing

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 0.5a1-alt1
- initial build for ALT Linux Sisyphus

