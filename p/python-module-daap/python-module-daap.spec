Name: python-module-daap
Version: 0.7.1
Release: alt1.1.1

Summary: PythonDaap is a DAAP client implemented in Python.
License: LGPL
Group: Development/Python
Url: http://jerakeen.org/code/PythonDaap/

Packager: Alexey Morsov <swi@altlinux.ru>
Source: %name-%version.tar

BuildPreReq: rpm-build-python
BuildRequires: python-devel >= 2.4 python-module-setuptools

%description
PythonDaap is a (under development) DAAP client implemented in
Python, and based on PyTunes by Davyd Madeley.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --optimize=2 --record=INSTALLED_FILES
mkdir -p %{buildroot}%_defaultdocdir/%name-%version/

cp -R examples/ CHANGELOG LICENSE README %{buildroot}%_defaultdocdir/%name-%version/


%files
%docdir examples
%doc CHANGELOG LICENSE README
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.1-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.1
- Rebuilt with python 2.6

* Sun Oct 04 2009 Alexey Morsov <swi@altlinux.ru> 0.7.1-alt1
- initial build




