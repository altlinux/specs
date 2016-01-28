%define module_name pycall

%def_with python3

Name: python-module-%module_name
Version: 2.1
Release: alt1.git20121125.1

Summary: flexible python library for creating and using Asterisk call files
License: Public Domain
Group: Development/Python
Url: http://pycall.org/

# https://github.com/rdegges/pycall.git
Source: python-module-%module_name-%version.tar

BuildArch: noarch

#BuildPreReq: python-module-setuptools
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

%setup_python_module %module_name

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-module-setuptools rpm-build-python3 time

%description
%summary

%package -n python3-module-%module_name
Summary: flexible python library for creating and using Asterisk call files
Group: Development/Python3

%description -n python3-module-%module_name
%summary

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html

%files
%doc AUTHORS README* CHANGES UNLICENSE docs/_build/html
%python_sitelibdir/pycall
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%module_name
%doc AUTHORS README* CHANGES UNLICENSE docs/_build/html
%python3_sitelibdir/pycall
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1-alt1.git20121125.1
- NMU: Use buildreq for BR.

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.git20121125
- Version 2.1
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt1.1
- Rebuild with Python-2.7

* Tue Jun 07 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.0-alt1
- Initial build for Sisyphus.
