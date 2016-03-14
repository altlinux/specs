%define modulename mailer

%def_with python3

Name: python-module-mailer
Version: 0.7
Release: alt1.hg20140606.1.1

Summary: A module to send email simply in Python

Group: Development/Python
License: MIT
Url: http://pypi.python.org/pypi/%modulename/

Packager: Mikhail A Pokidko <pma@altlinux.ru>

BuildArch: noarch

# hg clone https://bitbucket.org/ginstrom/mailer
Source: %name-%version.tar

#setup_python_module %modulename

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-module-setuptools rpm-build-python3 time

#BuildRequires: python-module-setuptools

#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

%description
A module that simplifies sending email.

%package -n python3-module-%modulename
Summary: A module to send email simply in Python
Group: Development/Python3

%description -n python3-module-%modulename
A module that simplifies sending email.

%prep
%setup
rm -fR build

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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
%doc docs/build/html/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modulename
%doc docs/build/html/*
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt1.hg20140606.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7-alt1.hg20140606.1
- NMU: Use buildreq for BR.

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.hg20140606
- Version 0.7
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.1
- Rebuild with Python-2.7

* Thu Jul 01 2010 Mikhail Pokidko <pma@altlinux.org> 0.5-alt1
- initial build

