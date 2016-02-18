%define oname pymc

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.3.5
Release: alt1.git20150311.1
Summary: Markov Chain Monte Carlo sampling toolkit
License: Academic Free License & BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pymc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pymc-devs/pymc.git
Source: %name-%version.tar
Source1: site.cfg

#BuildPreReq: gcc-fortran liblapack-devel graphviz xvfb-run /proc
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-nose libnumpy-devel
#BuildPreReq: python-module-scipy python-module-matplotlib
#BuildPreReq: python-module-tables python-module-scikits.statsmodels
#BuildPreReq: python-module-pydot python-module-pycairo
#BuildPreReq: python-modules-multiprocessing python-modules-sqlite3
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose libnumpy-py3-devel
#BuildPreReq: python3-module-scipy python3-module-matplotlib
#BuildPreReq: python3-module-tables python3-module-scikits.statsmodels
#BuildPreReq: python3-module-pydot python3-module-pycairo
#BuildPreReq: python3-modules-sqlite3
%endif

%py_provides %oname
Requires: %name-tests = %EVR
%py_requires multiprocessing numpy scipy matplotlib tables sqlite3 cairo
%py_requires statsmodels pydot

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: at-spi2-atk at-spi2-core colord dbus dbus-tools-gui elfutils fontconfig fonts-bitmap-misc glib-networking gobject-introspection gobject-introspection-x11 ipython libat-spi2-core libatk-gir libcairo-gobject libcap-ng libgdk-pixbuf libgdk-pixbuf-gir libgfortran-devel libgpg-error libgtk+3-gir libhdf5-8-seq libnumpy-devel libopenblas-devel libpango-gir libquadmath-devel libwayland-client libwayland-cursor libwayland-egl libwayland-server python-base python-devel python-module-Numeric python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-Scientific python-module-apiclient python-module-apsw python-module-babel python-module-cffi python-module-cssselect python-module-cycler python-module-dateutil python-module-decorator python-module-docutils python-module-ecdsa python-module-enum34 python-module-functools32 python-module-future python-module-gdata python-module-greenlet python-module-html5lib python-module-httplib2 python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jdcal python-module-jinja2 python-module-jinja2-tests python-module-jupyter_client python-module-jupyter_core python-module-markupsafe python-module-matplotlib python-module-matplotlib-gtk3 python-module-mpmath python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-nose python-module-numdifftools python-module-numexpr python-module-numexpr-tests python-module-numpy python-module-numpy-tests python-module-ordereddict python-module-pandas python-module-path python-module-patsy python-module-pexpect python-module-pickleshare python-module-psycopg2 python-module-ptyprocess python-module-pyasn1 python-module-pycairo python-module-pycares python-module-pycrypto python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-scikits.statsmodels python-module-scipy python-module-serial python-module-setuptools python-module-simplegeneric python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-tables python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-twisted-core python-module-xlrd python-module-xlsxwriter python-module-xlwt-future python-module-xstatic python-module-xstatic-term.js python-module-yaml python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-sqlite3 python-modules-tkinter python-modules-unittest python-modules-wsgiref python3 python3-base python3-dev python3-module-numpy xauth xkbcomp xkeyboard-config xorg-server-common xorg-xvfb
BuildRequires: gcc-fortran liblapack-devel libnumpy-py3-devel python-module-alabaster python-module-notebook python-module-numpy-testing python-module-objects.inv python-module-pandas-tests python-module-pydot python3-module-numpy-testing python3-module-zope rpm-build-python3 time xvfb-run

%description
Bayesian estimation, particularly using Markov chain Monte Carlo (MCMC),
is an increasingly relevant approach to statistical estimation. However,
few statistical software packages implement MCMC samplers, and they are
non-trivial to code by hand. pymc is a python package that implements
the Metropolis-Hastings algorithm as a python class, and is extremely
flexible and applicable to a large suite of problems. pymc includes
methods for summarizing output, plotting, goodness-of-fit and
convergence diagnostics.

%package tests
Summary: Tests and examples for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Bayesian estimation, particularly using Markov chain Monte Carlo (MCMC),
is an increasingly relevant approach to statistical estimation. However,
few statistical software packages implement MCMC samplers, and they are
non-trivial to code by hand. pymc is a python package that implements
the Metropolis-Hastings algorithm as a python class, and is extremely
flexible and applicable to a large suite of problems. pymc includes
methods for summarizing output, plotting, goodness-of-fit and
convergence diagnostics.

This package contains tests and examples for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Markov Chain Monte Carlo sampling toolkit
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-%oname-tests = %EVR
%py3_requires multiprocessing numpy scipy matplotlib tables sqlite3
%py3_requires statsmodels pydot cairo

%description -n python3-module-%oname
Bayesian estimation, particularly using Markov chain Monte Carlo (MCMC),
is an increasingly relevant approach to statistical estimation. However,
few statistical software packages implement MCMC samplers, and they are
non-trivial to code by hand. pymc is a python package that implements
the Metropolis-Hastings algorithm as a python class, and is extremely
flexible and applicable to a large suite of problems. pymc includes
methods for summarizing output, plotting, goodness-of-fit and
convergence diagnostics.

%package -n python3-module-%oname-tests
Summary: Tests and examples for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Bayesian estimation, particularly using Markov chain Monte Carlo (MCMC),
is an increasingly relevant approach to statistical estimation. However,
few statistical software packages implement MCMC samplers, and they are
non-trivial to code by hand. pymc is a python package that implements
the Metropolis-Hastings algorithm as a python class, and is extremely
flexible and applicable to a large suite of problems. pymc includes
methods for summarizing output, plotting, goodness-of-fit and
convergence diagnostics.

This package contains tests and examples for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Bayesian estimation, particularly using Markov chain Monte Carlo (MCMC),
is an increasingly relevant approach to statistical estimation. However,
few statistical software packages implement MCMC samplers, and they are
non-trivial to code by hand. pymc is a python package that implements
the Metropolis-Hastings algorithm as a python class, and is extremely
flexible and applicable to a large suite of problems. pymc includes
methods for summarizing output, plotting, goodness-of-fit and
convergence diagnostics.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Bayesian estimation, particularly using Markov chain Monte Carlo (MCMC),
is an increasingly relevant approach to statistical estimation. However,
few statistical software packages implement MCMC samplers, and they are
non-trivial to code by hand. pymc is a python package that implements
the Metropolis-Hastings algorithm as a python class, and is extremely
flexible and applicable to a large suite of problems. pymc includes
methods for summarizing output, plotting, goodness-of-fit and
convergence diagnostics.

This package contains documentation for %oname.

%prep
%setup

rm -fR blas lapack
install -m644 %SOURCE1 ./
sed -i 's|@LIBDIR@|%_libdir|' site.cfg

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
export LC_ALL=en_US.UTF-8
%add_optflags %optflags_shared -I%_includedir/openblas
%add_optflags -fno-strict-aliasing

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%add_optflags %optflags_shared -I%_includedir/openblas
%add_optflags -fno-strict-aliasing

%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=$PWD
FFLAGS="%optflags" CFLAGS="%optflags" \
	python setup.py build_ext -i
xvfb-run %make -C docs pickle
xvfb-run %make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
%add_optflags %optflags_shared -I%_includedir/openblas
%add_optflags -fno-strict-aliasing

export PYTHONPATH=$PWD
xvfb-run nosetests -v
%if_with python3
pushd ../python3
FFLAGS="%optflags" CFLAGS="%optflags" \
	python3 setup.py build_ext -i
export PYTHONPATH=$PWD
xvfb-run nosetests3 -v
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/examples

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/examples

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/examples

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/examples
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.3.5-alt1.git20150311.1
- NMU: Use buildreq for BR.

* Mon Mar 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.5-alt1.git20150311
- Initial build for Sisyphus

