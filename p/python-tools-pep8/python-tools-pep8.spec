%def_with python3

%global module_name pep8

Name:           python-tools-%{module_name}
Version:        1.6.2
Release:        alt1.1
Summary:        Python style guide checker

Group:          Development/Python
# License is held in the comments of pep8.py
# setup.py claims license is Expat license, which is the same as MIT
License:        MIT
URL:            http://pypi.python.org/pypi/%{module_name}
Source0:        %{name}-%{version}.tar

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
BuildRequires:  python-module-sphinx
Requires:       python-module-setuptools

%description
pep8 is a tool to check your Python code against some of the style conventions
in PEP 8. It has a plugin architecture, making new checks easy, and its output
is parseable, making it easy to jump to an error location in your editor.

%if_with python3
%package -n python3-tools-pep8
Summary:    Python style guide checker
Group:      Development/Python

BuildRequires:  rpm-build-python3
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-sphinx
 
Requires:  python3-module-setuptools

%description -n python3-tools-pep8
pep8 is a tool to check your Python code against some of the style
conventions in PEP 8. It has a plugin architecture, making new checks
easy, and its output is parseable, making it easy to jump to an error
location in your editor.

This is a version for Python 3.

%endif


%prep
%setup
# Remove #! from pep8.py
sed --in-place "s:#!\s*/usr.*::" pep8.py

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build build_sphinx

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
mv %{buildroot}%{_bindir}/pep8 %{buildroot}%{_bindir}/python3-pep8
popd
%endif

%python_install

%check
python pep8.py --testsuite testsuite
python pep8.py --doctest

%if_with python3
pushd ../python3
PYTHONPATH="%{buildroot}%{python3_sitelibdir}:$PYTHONPATH" %{__python3} pep8.py --testsuite testsuite
popd
%endif


%files
%doc CHANGES.txt README.rst build/sphinx/html/*
%{_bindir}/pep8
%{python_sitelibdir}/%{module_name}.py*
%{python_sitelibdir}/%{module_name}-%{version}-*.egg-info

%if_with python3
%files -n python3-tools-pep8
%doc README.rst CHANGES.txt build/sphinx/html/*
%{_bindir}/python3-pep8
%{python3_sitelibdir}/%{module_name}.py*
%{python3_sitelibdir}/%{module_name}-%{version}-*.egg-info/
%{python3_sitelibdir}/__pycache__/%{module_name}*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt1
- Version 1.6.2

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1
- Version 1.6.1

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.7-alt1
- Version 1.5.7

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 1.5.6-alt1
- New version (based on Fedora 1.5.6-3.fc21.src)

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt2
- Rebuild with Python-2.7

* Wed Sep 28 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt1
- Initial based on Fedora spec build

