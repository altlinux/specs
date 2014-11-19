%define module_name django-tastypie

%def_with python3

Name: python-module-%module_name
Version: 0.12.2
Release: alt1.dev.git20141022
Group: Development/Python
License: BSD License
Summary: Creating delicious APIs for Django apps since 2010
URL: https://github.com/toastdriven/django-tastypie.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Creating delicious APIs for Django apps since 2010
There are other, better known API frameworks out there for Django. You need to
assess the options available and decide for yourself. That said, here are some
common reasons for tastypie.

%package -n python3-module-%module_name
Summary: Creating delicious APIs for Django apps since 2010
Group: Development/Python3

%description -n python3-module-%module_name
Creating delicious APIs for Django apps since 2010
There are other, better known API frameworks out there for Django. You need to
assess the options available and decide for yourself. That said, here are some
common reasons for tastypie.

%package docs
Summary: Documentation for %module_name
Group: Development/Documentation
BuildArch: noarch

%description docs
Creating delicious APIs for Django apps since 2010
There are other, better known API frameworks out there for Django. You need to
assess the options available and decide for yourself. That said, here are some
common reasons for tastypie.

This package contains documentation for %module_name.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
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
%make -C docs html

%files
%doc AUTHORS LICENSE README.rst TODO
%doc BACKWARDS-INCOMPATIBLE.txt CONTRIBUTING
%python_sitelibdir/tastypie*
%python_sitelibdir/django_tastypie*

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%module_name
%doc AUTHORS LICENSE README.rst TODO
%doc BACKWARDS-INCOMPATIBLE.txt CONTRIBUTING
%python3_sitelibdir/tastypie*
%python3_sitelibdir/django_tastypie*
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2-alt1.dev.git20141022
- Version 0.12.2-dev

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.1-alt1.dev.git20140925
- Version 0.12.1-dev

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.2-alt1.dev.git20140823
- Version 0.11.2-dev
- Added module for Python 3

* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.9.11-alt1
- build for ALT
