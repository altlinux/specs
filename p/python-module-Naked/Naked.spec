%define oname Naked

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.0.29
Release: alt2.git20140316.1
Summary: A command line application framework
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/Naked/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/chrissimpkins/naked.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-requests python-module-yaml
#BuildPreReq: python-module-nose python-modules-json
#BuildPreReq: python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-requests python3-module-yaml
#BuildPreReq: python3-module-nose python3-module-Cython
%endif

%py_provides %oname
%py_requires requests yaml json

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: elfutils ipython ipython3 python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pexpect python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-dev python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-ndg-httpsclient python3-module-ntlm python3-module-numpy python3-module-pexpect python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-urllib3 python3-module-xstatic python3-module-xstatic-term.js python3-module-zmq python3-module-zope python3-module-zope.interface
BuildRequires: python-module-Cython python-module-html5lib python-module-nose python-module-notebook python-module-pytest python-module-yaml python3-module-Cython python3-module-html5lib python3-module-nose python3-module-notebook python3-module-yaml rpm-build-python3 time

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

%ifarch x86_64
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
* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.0.29-alt2.git20140316.1
- NMU: Use buildreq for BR.

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.29-alt2.git20140316
- Added necessary requirements

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.29-alt1.git20140316
- Initial build for Sisyphus

