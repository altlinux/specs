%def_with python3

Name:           pyflakes
Version:        0.9.2
Release:        alt1.1
Summary:        A simple program which checks Python source files for errors

Group:          Development/Python
License:        MIT
URL:            https://launchpad.net/pyflakes

Source0:        %{name}-%{version}.tar
Source1:        pyflakes_0.7.3-1.debian.tar.gz

BuildArch:      noarch
BuildRequires:  python-module-setuptools
Requires:       python-module-setuptools

%description
Pyflakes is similar to PyChecker in scope, but differs in that it does\
not execute the modules to check them. This is both safer and faster,\
although it does not perform as many checks. Unlike PyLint, Pyflakes\
checks only for logical errors in programs; it does not perform any\
check on style.

%if_with python3
%package -n python3-%{name}
Summary:        A simple program which checks Python source files for errors
Group:          Development/Python

BuildRequires:  rpm-build-python3
BuildRequires:  python3-module-setuptools
Requires:       python3-module-setuptools

%description -n python3-%{name}
Pyflakes is similar to PyChecker in scope, but differs in that it does\
not execute the modules to check them. This is both safer and faster,\
although it does not perform as many checks. Unlike PyLint, Pyflakes\
checks only for logical errors in programs; it does not perform any\
check on style.
%endif

%prep
%setup -a 1

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
install -Dpm 644 debian/pyflakes.1 %{buildroot}%{_mandir}/man1/pyflakes.1

%if %{with python3}
pushd ../python3
%python3_install
mv %{buildroot}%{_bindir}/pyflakes %{buildroot}%{_bindir}/python3-pyflakes
popd
pushd %{buildroot}%{_mandir}/man1
echo ".so man1/pyflakes.1" > python3-pyflakes.1
touch -r pyflakes.1 python3-pyflakes.1
popd
%endif

%python_install

# %check
# %{__python} setup.py test
# %if %{with python3}
# pushd ../python3
# %{__python3} setup.py test
# popd
# %endif

%files
%doc AUTHORS LICENSE NEWS.txt PKG-INFO README.rst
%{_bindir}/pyflakes
%{python_sitelibdir}/pyflakes*
%exclude %{python_sitelibdir}/pyflakes/test/
%{_mandir}/man1/pyflakes.1*

%if %{with python3}
%files -n python3-%{name}
%doc AUTHORS LICENSE NEWS.txt PKG-INFO README.rst
%{_bindir}/python3-pyflakes
%{python3_sitelibdir}/pyflakes*
%exclude %{python3_sitelibdir}/pyflakes/test/
%{_mandir}/man1/python3-pyflakes.1*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1
- Version 0.9.2

* Fri Aug 01 2014 Lenar Shakirov <snejok@altlinux.ru> 0.8.1-alt1
- First build for ALT (based on Fedora 0.8.1-3.fc21.src)

