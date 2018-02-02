%define module_name amqp

%def_with python3

Name: python-module-%module_name
Version: 2.2.2
Epoch: 1
Release: alt1.1
Group: Development/Python
License: GPLv2
Summary: fork of amqplib used by Kombu containing additional features and improvements
URL: http://github.com/celery/py-amqp.git

Source: %name-%version.tar

BuildRequires: python-module-setuptools
BuildRequires: python-module-alabaster python-module-html5lib python-module-objects.inv python-module-sphinxcontrib-issuetracker python2.7(sphinx_celery)
BuildRequires: python2.7(vine) python2.7(case)
BuildRequires: python-module-unittest2
BuildRequires: python-module-mock
BuildRequires(pre): rpm-macros-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pytest
BuildRequires: python3(vine) python3(case)
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

%if_with python3
%package -n python3-module-%module_name
Summary: fork of amqplib used by Kombu containing additional features and improvements
Group: Development/Python3

%description -n python3-module-%module_name
This is a fork of amqplib_ which was originally written by Barry Pederson.
It is maintained by the Celery_ project, and used by kombu as a pure python
alternative when librabbitmq is not available.
%endif

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

%if "%_target_libdir_noarch" != "%_libdir"
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%module_name/

%check
python setup.py test

%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS Changelog LICENSE README.rst
%python_sitelibdir/%module_name
%python_sitelibdir/%module_name-%version-py*.egg-info
%exclude %python_sitelibdir/%module_name/pickle

%files pickles
%python_sitelibdir/%module_name/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%module_name
%doc AUTHORS Changelog LICENSE README.rst
%python3_sitelibdir/%module_name
%python3_sitelibdir/%module_name-%version-py*.egg-info
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:2.2.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.2.2-alt1
- Updated to upstream version 2.2.2.

* Wed Oct 26 2016 Alexey Shabalin <shaba@altlinux.ru> 1:1.4.9-alt1
- 1.4.9

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4.6-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4.6-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:1.4.6-alt1.1
- NMU: Use buildreq for BR.

* Mon Sep 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.4.6-alt1
- downgrade to 1.4.6

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1.git20150615
- New snapshot
- Extracted tests into separate package

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1.git20140930
- Version 2.0.0a1

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.5-alt1.git20140415
- Version 1.4.5
- Added modulefor Python 3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.11-alt1.1
- Fixed build

* Sat Apr 13 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.11-alt1
- build for ALT
