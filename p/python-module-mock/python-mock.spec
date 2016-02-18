%global pypi_name mock
%def_with python3

Name: python-module-%{pypi_name}
Version: 1.3.0
Release: alt1.git20150731.1
Summary: A Python Mocking and Patching Library for Testing

Group: Development/Python
License: BSD
Url: https://pypi.python.org/pypi/%{pypi_name}

# https://github.com/testing-cabal/mock.git
Source: %name-%version.tar

BuildArch: noarch
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: git-core python-module-pbr python3-module-html5lib python3-module-pbr rpm-build-python3

#BuildRequires: python-devel python-module-setuptools git
#BuildRequires: python-module-pbr

%py_requires funcsigs

%description
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.

%if_with python3
%package -n python3-module-%{pypi_name}
Summary:        A Python Mocking and Patching Library for Testing
Group:		Development/Python
BuildArch:      noarch
BuildRequires(pre):  rpm-build-python3
#BuildRequires: python3-module-pbr python3-module-setuptools
%py3_requires funcsigs

%description -n python3-module-%{pypi_name}
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.

%endif

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

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
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%files
%doc docs/index.txt README.rst LICENSE.txt NEWS
%{python_sitelibdir}/*

%if_with python3
%files -n python3-module-mock
%doc docs/index.txt README.rst LICENSE.txt NEWS
%{python3_sitelibdir}/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt1.git20150731.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20150731
- Snapshot from git

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Version 1.3.0

* Fri Aug 29 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt2
- Rebuild with Python-2.7

* Mon Oct 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Mon Mar 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.0-alt1
- Initial
