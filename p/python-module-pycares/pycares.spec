%define module_name pycares
%def_with python3
%def_with docs

Name: python-module-%module_name
Version: 2.1.1
Release: alt1

Summary: Python interface for c-ares
License: MIT
Group: Development/Python

Url: http://github.com/saghul/pycares
Source: pycares-%version.tar.gz
BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel

# Automatically added by buildreq on Wed Jul 20 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-docutils python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-Pygments python3-module-alabaster python3-module-babel python3-module-cssselect python3-module-docutils python3-module-jinja2 python3-module-markupsafe python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx_rtd_theme rpm-build-python3 xz
%if_with docs
BuildRequires: python-module-sphinx python-module-sphinx_rtd_theme
%endif

#BuildRequires: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%if_with docs
BuildRequires: python3-module-sphinx python3-module-sphinx_rtd_theme
%endif
%endif

%description
pycares is a Python module which provides an interface to c-ares. c-ares
(http://c-ares.haxx.se/) c-ares is a C library that performs DNS
requests and name resolves asynchronously.

%package -n python3-module-%module_name
Summary: Python interface for c-ares (Python3)
Group: Development/Python3

%description -n python3-module-%module_name
pycares is a Python module which provides an interface to c-ares. c-ares
(http://c-ares.haxx.se/) c-ares is a C library that performs DNS
requests and name resolves asynchronously.

%prep
%setup -n pycares-%version
sed -i 's@/setup.py@/pycares/_version.py@' docs/conf.py

%build
export LANG=en_US.UTF-8
%python_build -b build2
%if_with docs
make -C docs html BUILDDIR=_build2
%endif

%if_with python3
%python3_build -b build3
%if_with docs
make -C docs html SPHINXBUILD=py3_sphinx-build BUILDDIR=_build3
%endif
%endif

%install
export LANG=en_US.UTF-8
rm -f build && ln -sf build2 build && %python_install

%if_with python3
rm -f build && ln -sf build3 build && %python3_install
%endif

%files
%python_sitelibdir/pycares*
%doc README.rst LICENSE ChangeLog
%if_with docs
%doc docs/_build2/html
%endif

%if_with python3
%files -n python3-module-%module_name
%python3_sitelibdir/pycares*
%doc README.rst LICENSE ChangeLog
%if_with docs
%doc docs/_build3/html
%endif
%endif

%changelog
* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 2.1.1-alt1
- Autobuild version bump to 2.1.1

* Wed Jul 20 2016 Fr. Br. George <george@altlinux.ru> 2.1.0-alt1
- Autobuild version bump to 2.1.0
- Build documentation

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.3-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.3-alt1.1
- NMU: Use buildreq for BR.

* Fri Feb 13 2015 Vladimir Didenko <cow@altlinux.ru> 0.6.3-alt1
- new version

* Tue Sep 10 2013 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- first build for Sisyphus

