%define oname mass

%def_disable check

Name: python3-module-%oname
Version: 0.1
Release: alt3

Summary: MASS is Music and Audio in Sample Sequences
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/music/
# https://github.com/ttm/mass.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-numpy python3-module-matplotlib
BuildRequires: python3-module-scipy python3-module-pygobject3
BuildRequires: python3-module-pycairo

%py3_provides %oname
%py3_requires numpy matplotlib scipy gi cairo


%description
This project delivers routines for music oriented sound synthesis in a
sample based system. MASS can be though of as a sample level DAW system,
in which the objects manipulated are in fact the array of samples
describing the sound wave that will reach a listener ear.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test
export PYTHONPATH=$PWD
xvfb-run py.test3 -vv tests/*.py mass/*.py

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt3
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1-alt2.dev4.git20150320.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt2.dev4.git20150320
- Disabled check.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.dev4.git20150320.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.dev4.git20150320
- Initial build for Sisyphus

