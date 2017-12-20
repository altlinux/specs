%define mname lmj
%define oname %mname.sound

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.4
Release: alt2.git20131028
Summary: An assemblage of code for manipulating sound data
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/lmj.sound/

# https://github.com/lmjohns3/py-sound.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-scipy python-module-scikits.audiolab
BuildRequires: python-module-scikits.samplerate python-module-matplotlib
BuildRequires: python-module-numpy python-module-pygobject3
BuildRequires: python-module-pycairo
BuildRequires: python-modules-logging python-modules-multiprocessing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-scipy python3-module-scikits.audiolab
BuildRequires: python3-module-scikits.samplerate python3-module-matplotlib
BuildRequires: python3-module-numpy python3-module-pygobject3
BuildRequires: python3-module-pycairo
%endif

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires scipy scikits.audiolab scikits.samplerate logging numpy gi
%py_requires multiprocessing matplotlib cairo

%description
This package contains several modules for manipulating sound data in
Python.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

%if_with python3
%package -n python3-module-%oname
Summary: An assemblage of code for manipulating sound data
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires scipy scikits.audiolab scikits.samplerate logging numpy gi
%py3_requires matplotlib cairo

%description -n python3-module-%oname
This package contains several modules for manipulating sound data in
Python.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core files of %mname.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

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

%if "%_lib" == "lib64"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python_sitelibdir/%mname/
%if_with python3
pushd ../python3
install -p -m644 %mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/
popd
%endif

%check
python setup.py test
xvfb-run py.test -vv %mname/sound/*.py
%if_with python3
pushd ../python3
python3 setup.py test
xvfb-run py.test3 -vv %mname/sound/*.py
popd
%endif

%files
%doc *.md
%python_sitelibdir/%mname/sound
%python_sitelibdir/*.egg-info
%python_sitelibdir/*-nspkg.pth

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/%mname/sound
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.*
%python3_sitelibdir/%mname/__pycache__/__init__.*
%endif

%changelog
* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.4-alt2.git20131028
- Disabled check.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20131028.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20131028.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Mar 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20131028
- Initial build for Sisyphus

