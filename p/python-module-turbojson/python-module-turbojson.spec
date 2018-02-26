%define oname TurboJson
Name: python-module-turbojson
Version: 1.3
Release: alt1.1

Summary: a TurboGears support package which provides a template engine plugin

License: MIT
Group: Development/Python
Url: http://docs.turbogears.org/TurboJson

Packager: Vladimir V. Kamarzin <vvk@altlinux.org>

BuildArch: noarch

Source: http://pypi.python.org/packages/source/T/%oname/%oname-%version.tar

# Automatically added by buildreq on Mon Mar 30 2009
BuildRequires: python-module-setuptools

%setup_python_module turbojson

%py_requires peak.rules

%description
This package provides a template engine plugin, allowing you
to easily use JSON via the simplejson module with TurboGears, Buffet
or other systems that support python.templating.engines.

For information on simplejson, go here:

http://undefined.org/python/#simplejson

For information on using a template engine plugin with TurboGears
or writing a template engine plugin, go here:

http://docs.turbogears.org/1.0/TemplatePlugins
http://docs.turbogears.org/1.0/AlternativeTemplating

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/turbojson/
%python_sitelibdir/*.egg-info
%doc README*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt1.1
- Rebuild with Python-2.7

* Wed Oct 06 2010 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- new version (1.3) import in git
- move to TurboJson subdir
- add PEAK-Rules requires

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.1
- Rebuilt with python 2.6

* Mon Mar 30 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus

