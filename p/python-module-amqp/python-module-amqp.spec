%define module_name amqp

%def_with python3

Name: python-module-%module_name
Version: 1.4.5
Release: alt1.git20140415
Group: Development/Python
License: GPLv2
Summary: fork of amqplib used by Kombu containing additional features and improvements
URL: http://github.com/celery/py-amqp.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-sphinxcontrib-issuetracker
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%description
This is a fork of amqplib_ which was originally written by Barry Pederson.
It is maintained by the Celery_ project, and used by kombu as a pure python
alternative when librabbitmq is not available.

%package pickles
Summary: Pickles for %module_name
Group: Development/Python

%description pickles
This is a fork of amqplib_ which was originally written by Barry Pederson.
It is maintained by the Celery_ project, and used by kombu as a pure python
alternative when librabbitmq is not available.

This package contains pickles for %module_name.

%package docs
Summary: Documentation for %module_name
Group: Development/Documentation
BuildArch: noarch

%description docs
This is a fork of amqplib_ which was originally written by Barry Pederson.
It is maintained by the Celery_ project, and used by kombu as a pure python
alternative when librabbitmq is not available.

This package contains documentation for %module_name.

%package -n python3-module-%module_name
Summary: fork of amqplib used by Kombu containing additional features and improvements
Group: Development/Python3

%description -n python3-module-%module_name
This is a fork of amqplib_ which was originally written by Barry Pederson.
It is maintained by the Celery_ project, and used by kombu as a pure python
alternative when librabbitmq is not available.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/.build/pickle %buildroot%python_sitelibdir/%module_name/

%files
%doc AUTHORS Changelog LICENSE README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/.build/html/*

%if_with python3
%files -n python3-module-%module_name
%doc AUTHORS Changelog LICENSE README.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.5-alt1.git20140415
- Version 1.4.5
- Added modulefor Python 3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.11-alt1.1
- Fixed build

* Sat Apr 13 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.11-alt1
- build for ALT
