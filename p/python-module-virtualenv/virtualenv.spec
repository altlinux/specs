%define modulename virtualenv

%def_with python3
%def_with check

Name: python-module-%modulename
Version: 15.1.0
Release: alt1.1

Summary: Virtual Python Environment builder
License: MIT
Group: Development/Python

Url: http://pypi.python.org/pypi/virtualenv
BuildArch: noarch

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif
%if_with check
BuildPreReq: python-module-mock
BuildPreReq: python-module-nose
BuildRequires: python-module-pytest
%if_with python3
BuildPreReq: python3-module-mock
BuildPreReq: python3-module-nose
BuildRequires: python3-module-pytest
%endif
%endif

# git://github.com/pypa/virtualenv.git
Source: %version.tar.gz
Patch1: python3_sitelibdir.patch
Patch2: allow_internal_symlinks.patch

%setup_python_module %modulename

%description
Tool to create isolated Python environments.

With virtualenv it is became possible to keep separate set of python libraries
for each of your project.

Just exec "virtualenv /your/dir" and whole python enviroment (including
setuptools and easy_install) will be installed there. You could exec scripts
in newly created environment by invoking /your/dir/bin/python

%description -l ru_RU.UTF-8
Утилита для создания изолированных окружений для Python.

С Virtualenv вы можете создать независимые наборы библиотек для каждого
вашего проекта. Опционально вы можете запретить использование системных библиотек.

Просто выполните "virtualenv /your/dir" и полное виртуальное окружение Python будет
создано в каталоге, который вы указали (setuptools  и easy_install будут также установлены
и при вызове будут устанавливать новые библиотеки в ваше виртуальное окружение). Чтобы
выполнить ваши скрипты в вновь созданном окружение запускайте их при помощи
/your/dir/bin/python

%if_with python3
%package -n python3-module-%modulename
Summary: Virtual Python 3 Environment builder
Group: Development/Python3
%py3_provides %modulename

%description -n python3-module-%modulename
Tool to create isolated Python environments.

With virtualenv it is became possible to keep separate set of python libraries
for each of your project.

Just exec "virtualenv /your/dir" and whole python enviroment (including
setuptools and easy_install) will be installed there. You could exec scripts
in newly created environment by invoking /your/dir/bin/python
%endif

%prep
%setup -n virtualenv-%version

rm -f virtualenv_support/*.egg
%patch1 -p1
%patch2 -p1

%build
export LC_ALL=en_US.UTF-8
python bin/rebuild-script.py

%python_build -b build2

%if_with python3
%python3_build -b build3
%endif

%install
export LC_ALL=en_US.UTF-8

%if_with python3
rm -rf build && ln -sf build3 build
%python3_install
mv %buildroot%_bindir/virtualenv %buildroot%_bindir/virtualenv3
%endif

rm -rf build && ln -sf build2 build
%python_install

%if_with check
%check
py.test

%if_with python3
py.test3
%endif
%endif

%files
%_bindir/*
%exclude %_bindir/virtualenv3
%python_sitelibdir/*
%doc docs/*

%if_with python3
%files -n python3-module-%modulename
%_bindir/virtualenv3
%python3_sitelibdir/*
%doc docs/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 15.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Fr. Br. George <george@altlinux.ru> 15.1.0-alt1
- Autobuild version bump to 15.1.0

* Fri Jul 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 15.0.3-alt2
- Fixed build spec with py.test3

* Thu Sep 01 2016 Fr. Br. George <george@altlinux.ru> 15.0.3-alt1
- Autobuild version bump to 15.0.3
- Fix build/tests

* Wed Aug 31 2016 Denis Medvedev <nbr@altlinux.org> 13.1.0-alt2
- fixed sitelibs for python3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 13.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 13.1.0-alt1
- Version 13.1.0

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 12.0.5-alt1
- Version 12.0.5

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 12.0.4-alt1
- Version 12.0.4

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 12.0.1-alt1
- Version 12.0.1

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.6-alt1
- Version 1.11.6

* Mon Aug 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.1-alt2
- Added provides '%modulename' for Python 3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.1-alt1.1
- Fixed build

* Tue Apr 02 2013 Aleksey Avdeev <solo@altlinux.ru> 1.9.1-alt1
- 1.9.1 (Closes: #28670)

* Sun Mar 03 2013 Aleksey Avdeev <solo@altlinux.ru> 1.8.4-alt1
- 1.8.4

* Mon May 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.1
- Added module for Python 3

* Wed Feb 08 2012 Vladimir V. Kamarzin <vvk@altlinux.org> 1.7-alt1
- New version (Closes: #26819)

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.3-alt1.1.1
- Rebuild with Python-2.7

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.3-alt1.1
- Rebuilt with python 2.6

* Sun May 17 2009 Maxim Ivanov <redbaron at altlinux.org> 1.3.3-alt1
- Bump to 1.3.3
- added docs

* Wed Sep 17 2008 Maxim Ivanov <redbaron at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

