%define module_name shapely

Name: python-module-%module_name
Version: 1.2b6
Release: alt2.1

Summary: Planar geometries, predicates, and operations

License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/Shapely

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-module-setuptools

%setup_python_module %module_name

%description
Planar geometries, predicates, and operations

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%{module_name}
%python_sitelibdir/Shapely*
%_bindir/dissolve.py
%_bindir/intersect.py

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2b6-alt2.1
- Rebuild with Python-2.7

* Tue Apr 13 2010 Denis Klimov <zver@altlinux.org> 1.2b6-alt2
- add build require to python-module-setuptools

* Tue Apr 13 2010 Denis Klimov <zver@altlinux.org> 1.2b6-alt1
- Initial build for ALT Linux

