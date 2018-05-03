%define oname Naked

%def_with python3
%def_disable check

Name: python-module-%oname
Epoch: 1
Version: 0.1.31
Release: alt1.1
Summary: A command line application framework
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Naked/

# https://github.com/chrissimpkins/naked.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires: python-devel
BuildRequires: python-module-Cython python-module-html5lib python-module-nose python-module-notebook python-module-pytest python-module-yaml
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-Cython python3-module-html5lib python3-module-nose python3-module-notebook python3-module-yaml
%endif

%py_provides %oname
%py_requires requests yaml json

%description
Naked is a new Python command line application framework that is in
development. The current release is a stable, testing release.

%package test
Summary: Test for %oname
Group: Development/Python
Requires: %name = %EVR

%description test
Naked is a new Python command line application framework that is in
development. The current release is a stable, testing release.

This package contains test for %oname.

%package -n python3-module-%oname
Summary: A command line application framework
Group: Development/Python3
%py3_provides %oname
%py3_requires requests yaml

%description -n python3-module-%oname
Naked is a new Python command line application framework that is in
development. The current release is a stable, testing release.

%package -n python3-module-%oname-test
Summary: Test for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-test
Naked is a new Python command line application framework that is in
development. The current release is a stable, testing release.

This package contains test for %oname.

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%add_optflags -fno-strict-aliasing
%python_build_debug
pushd lib/%oname/toolshed/c
rm -f *.c
./cythonize.sh
%python_build_debug
popd

%if_with python3
pushd ../python3
%python3_build_debug
pushd lib/%oname/toolshed/c
rm -f *.c
sed 's|cython|cython3|' cythonize.sh
./cythonize.sh
%python3_build_debug
popd
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -m644 lib/%oname/toolshed/c/build/lib*/*.so \
	 %buildroot%python_sitelibdir/%oname/toolshed/c/
rm -f %buildroot%python_sitelibdir/%oname/toolshed/c/*.sh \
	%buildroot%python_sitelibdir/%oname/toolshed/c/*.c \
	%buildroot%python_sitelibdir/%oname/toolshed/c/*.pyx \
	%buildroot%python_sitelibdir/%oname/toolshed/c/setup.py*

%if_with python3
pushd ../python3
install -m644 lib/%oname/toolshed/c/build/lib*/*.so \
	 %buildroot%python3_sitelibdir/%oname/toolshed/c/
popd
rm -f %buildroot%python3_sitelibdir/%oname/toolshed/c/*.sh \
	%buildroot%python3_sitelibdir/%oname/toolshed/c/*.c \
	%buildroot%python3_sitelibdir/%oname/toolshed/c/*.pyx \
	%buildroot%python3_sitelibdir/%oname/toolshed/c/setup.py \
	%buildroot%python3_sitelibdir/%oname/toolshed/c/__pycache__/setup.*
%endif

%check
export LC_ALL=en_US.UTF-8
export PATH=$PATH:%buildroot%_bindir
python setup.py test
export PYTHONPATH=%buildroot%python_sitelibdir
pushd tests
./test.sh all
popd
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd tests
sed -i 's|nosetests|nosetests3|' test.sh
sed -i 's|"naked"|"naked.py3"|' test_COMMANDS.py
./test.sh all
popd
popd
%endif

%files
%doc *.md docs/*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/test.*

%files test
%python_sitelibdir/*/*/test.*

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/*
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test.*
%exclude %python3_sitelibdir/*/*/*/test.*

%files -n python3-module-%oname-test
%python3_sitelibdir/*/*/test.*
%python3_sitelibdir/*/*/*/test.*
%endif

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.1.31-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Aug 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.1.31-alt1
- Updated to upstream version 0.1.31.
- Returned to upstream version naming.
- Updated build dependencies.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.29-alt2.git20140316.1.1.1
- (AUTO) subst_x86_64.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.29-alt2.git20140316.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.0.29-alt2.git20140316.1
- NMU: Use buildreq for BR.

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.29-alt2.git20140316
- Added necessary requirements

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.29-alt1.git20140316
- Initial build for Sisyphus

