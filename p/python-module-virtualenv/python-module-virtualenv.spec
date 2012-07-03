%define modulename virtualenv

%def_with python3

Name: python-module-%modulename
Version: 1.7
Release: alt1.1

Summary: Virtual Python Environment builder
License: MIT
Group: Development/Python

Url: http://pypi.python.org/pypi/virtualenv
BuildArch: noarch

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif
Source: %name-%version.tar

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

Просто выполните "virtuakenv /your/dir" и полное виртуальное окружение Python будет
создано в каталоге, который вы указали (setuptools  и easy_install будут также установлены
и при вызове будут устанавливать новые библиотеки в ваше виртуальное окружение). Чтобы
выполнить ваши скрипты в вновь созданном окружение запускайте их при помощи
/your/dir/bin/python

%if_with python3
%package -n python3-module-%modulename
Summary: Virtual Python 3 Environment builder
Group: Development/Python3

%description -n python3-module-%modulename
Tool to create isolated Python environments.

With virtualenv it is became possible to keep separate set of python libraries
for each of your project.

Just exec "virtualenv /your/dir" and whole python enviroment (including 
setuptools and easy_install) will be installed there. You could exec scripts
in newly created environment by invoking /your/dir/bin/python
%endif

%prep
%setup
rm -f virtualenv_support/*.egg
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/virtualenv %buildroot%_bindir/virtualenv3
%endif
%python_install

%files
%_bindir/*
%exclude %_bindir/virtualenv3
%python_sitelibdir/*
%doc docs/*

%if_with python3
%files -n python3-module-%modulename
%_bindir/virtualenv3
%python3_sitelibdir/*
%endif

%changelog
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

