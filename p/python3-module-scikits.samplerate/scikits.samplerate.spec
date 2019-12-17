%define mname scikits
%define oname %mname.samplerate

%def_without docs

Name: python3-module-%oname
Epoch: 1
Version: 0.4.0
Release: alt5

Summary: A python module for high quality audio resampling
License: GPLv2
Group: Development/Python3
Url: https://pypi.python.org/pypi/scikits.samplerate/

# git://github.com/cournape/samplerate.git
Source: %name-%version.tar
Source1: site.cfg
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libnumpy-devel libsamplerate-devel
BuildRequires: python3-module-Cython
BuildRequires: python3-module-nose python3-module-numpy-testing
BuildRequires: python3-module-html5lib python3-module-notebook
BuildRequires: python-tools-2to3
%if_with docs
BuildRequires: python3-module-sphinx python3-module-numpydoc
%endif

%py3_provides %oname
%py3_requires %mname numpy


%description
Samplerate is a small python package to do high quality audio resampling
for data in numpy arrays; IOW, it is a matlab resample replacement.

Samplerate is a wrapper around the Secret Rabbit Code from Erik de
Castro Lopo (http://www.mega-nerd.com/SRC/), which has high quality
converters based on the work of J.O Smith from CCRMA (see
http://ccrma.stanford.edu/~jos/resample/optfir.pdf).

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Samplerate is a small python package to do high quality audio resampling
for data in numpy arrays; IOW, it is a matlab resample replacement.

This package contains tests for %oname.

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Samplerate is a small python package to do high quality audio resampling
for data in numpy arrays; IOW, it is a matlab resample replacement.

This package contains pickles for %oname.
%endif

%prep
%setup
%patch1 -p1

%if_with docs
sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile
%endif

rm -f scikits/samplerate/_samplerate.c
install -m644 %SOURCE1 .
sed -i 's|\(library_dirs =\).*|\1 %_libdir|' site.cfg

mv scikits/samplerate/setup.py scikits/samplerate/setup.py.bak
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
mv scikits/samplerate/setup.py.bak scikits/samplerate/setup.py

sed -i 's|#!.*/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
cython3 scikits/samplerate/_samplerate.pyx
sed -i '1a\#define PyString_FromStringAndSize PyUnicode_FromStringAndSize' \
    scikits/samplerate/_samplerate.c
%python3_build_debug

%install
%python3_install

%if_with docs
%__python3 setup.py build_ext -i
export PYTHONPATH=$PWD:$PWD/docs/ext
%make -C docs pickle
%make -C docs html

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
pushd ~
export PYTHONPATH=%buildroot%python3_sitelibdir
nosetests3 -v %oname
popd

%files
%doc Changelog README TODO docs/src/examples
%if_with docs
%doc docs/build/html
%endif
%python3_sitelibdir/%mname/samplerate
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth
%exclude %python3_sitelibdir/%mname/samplerate/tests

%files tests
%python3_sitelibdir/%mname/samplerate/tests

%if_with docs
%files pickles
%python3_sitelibdir/*/pickle
%endif


%changelog
* Tue Dec 17 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:0.4.0-alt5
- build for python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.4.0-alt4.git20090722.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Feb 07 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:0.4.0-alt4.git20090722
- fix lib/lib64 stupidity, again

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:0.4.0-alt3.git20090722.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Nov 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.4.0-alt3.git20090722
- Fixed build.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.4.0-alt2.git20090722.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:0.4.0-alt2.git20090722.1
- NMU: Use buildreq for BR.

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.4.0-alt2.git20090722
- Rebuilt with updated NumPy

* Sat Feb 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.4.0-alt1.git20090722
- Initial build for Sisyphus

