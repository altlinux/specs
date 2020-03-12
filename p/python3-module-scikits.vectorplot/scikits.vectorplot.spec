%define mname scikits
%define oname %mname.vectorplot

Name: python3-module-%oname
Epoch: 1
Version: 0.2
Release: alt3

Summary: Vector fields plotting algorithms
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/scikits.vectorplot/

# https://github.com/aarchiba/scikits-vectorplot.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython libnumpy-py3-devel
BuildRequires: python3-module-matplotlib python3-module-nose
BuildRequires: python3-module-numpy-testing
BuildRequires: python-tools-2to3

%py3_provides %oname
%py3_requires numpy


%description
Line integral convolution for visualizing vector fields.

%prep
%setup

ln -s $(%__python3 -c 'import numpy; print(numpy.get_include() + "/numpy-py3")') numpy
sed -i "s|include_package_data=True,|&include_dirs=['.'],|" setup.py

echo "__version__ = '%version'" >vectorplot/version.py

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
%__python3 vectorplot/kernels.py

%files
%doc *.rst vectorplot/doc/*
%python3_sitelibdir/*


%changelog
* Thu Mar 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1:0.2-alt3
- Build for python2 disabled.

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 1:0.2-alt2.git20150130.1.1.1.1
- Added missing dep on `numpy.testing`.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:0.2-alt2.git20150130.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:0.2-alt2.git20150130.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.2-alt2.git20150130.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.2-alt2.git20150130
- Rebuilt with updated NumPy

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.2-alt1.git20150130
- Initial build for Sisyphus

