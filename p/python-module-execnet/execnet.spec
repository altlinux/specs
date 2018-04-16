%define oname execnet
%define fname python-module-%oname
%define descr \
execnet provides carefully tested means to ad-hoc interact with Python \
interpreters across version, platform and network barriers. It provides \
a minimal and fast API targetting the following uses: \
\
* distribute tasks to local or remote processes \
* write and deploy hybrid multi-process applications \
* write scripts to administer multiple hosts

Name: %fname
Version: 1.2.0
Release: alt4

%if ""==""
Summary: Rapid multi-Python deployment
Group: Development/Python
%else
Summary: Documentation for %oname
Group: Development/Documentation
%endif

License: MIT
Url: https://pypi.python.org/pypi/execnet/
Source: %name-%version.tar
BuildArch: noarch

%if ""==""
%py_provides %oname
%add_python_req_skip win32event win32evtlogutil win32service
%add_python_req_skip win32serviceutil register
%if ""=="3"
# hasn't got version for Python3
%add_python_req_skip rlcompleter2
%endif
%filter_from_provides /^python(execnet\.script\.shell)/d
# IndexError: list index out of range
%filter_from_provides /^python(execnet\.script\.socketserverservice)/d
# No module named 'win32serviceutil'
%filter_from_provides /^python(execnet\.script\.quitserver)/d
# No module named 'execnet.quitserver'
%if ""=="3"
%filter_from_provides /^python(execnet\.script\.xx)/d
# depends from rlcompleter2
%endif
%endif

%if ""!=""
Conflicts: %fname < %EVR
Conflicts: %fname > %EVR
%endif

BuildRequires(pre): rpm-macros-sphinx rpm-build-python
BuildRequires: python-module-setuptools_scm
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv python3-module-setuptools rpm-build-python3 time

%description
%descr
%if ""!=""

This package contains documentation for %oname.

%package -n %fname-pickles
Summary: Pickles for %oname
Group: Development/Python

%description -n %fname-pickles
%descr

This package contains pickles for %oname.
%endif

%prep
%setup
%if ""!=""
%prepare_sphinx .
ln -s ../objects.inv doc/
%endif

%build
%python_build

%install
%if ""==""
%python_install
%else
export PYTHONPATH=%buildroot%python_sitelibdir
%make -C doc pickle
%make -C doc html
mkdir -p %buildroot%python_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%if ""==""

%files
%doc CHANGELOG *.txt
%python_sitelibdir/%oname
%python_sitelibdir/*.egg-info*

%else

%files
%doc doc/_build/html/*

%files -n %fname-pickles
%python_sitelibdir/*/pickle
%endif

%changelog
* Mon Apr 16 2018 Stanislav Levin <slev@altlinux.org> 1.2.0-alt4
- fix wrong Provides of pythonX.X(execnet) by docs packages

* Mon Apr 09 2018 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt3
- Fix regular expressions in provides' filters.

* Thu Mar 29 2018 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt2
- Tranfer package to subst-packaging system.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1.1
- NMU: Use buildreq for BR.

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus

