%define oname pymc

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.3.6
Release: alt1
Summary: Markov Chain Monte Carlo sampling toolkit
License: Academic Free License & BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/pymc/

# https://github.com/pymc-devs/pymc.git
Source: %name-%version.tar
Source1: site.cfg

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: gcc-fortran liblapack-devel xvfb-run
BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: libnumpy-devel python-module-numpy-testing
BuildRequires: python-module-pandas-tests python-module-pydot
BuildRequires: python-module-alabaster python-module-notebook python-module-objects.inv
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: libnumpy-py3-devel python3-module-numpy-testing
BuildRequires: python3-module-zope
%endif

%py_provides %oname
Requires: %name-tests = %EVR
%py_requires multiprocessing numpy scipy matplotlib tables sqlite3 cairo
%py_requires statsmodels pydot


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
* Tue Dec 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.6-alt1
- Updated to upstream version 2.3.6.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.5-alt1.git20150311.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.3.5-alt1.git20150311.1
- NMU: Use buildreq for BR.

* Mon Mar 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.5-alt1.git20150311
- Initial build for Sisyphus

