%define oname igakit

Name: python3-module-%oname
Version: 0.1
Release: alt3

Summary: Toolkit for IsoGeometric Analysis (IGA)
License: BSD
Group: Development/Python3
Url: https://petiga-igakit.readthedocs.org/en/latest/

# hg clone https://bitbucket.org/dalcinl/igakit
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libnumpy-py3-devel gcc-fortran
BuildRequires: python3-module-numpy


%description
igakit: Toolkit for IsoGeometric Analysis (IGA).

%prep
%setup

ln -s $(python3 -c 'import numpy; \
        print(numpy.get_include() + "/numpy-py3")') numpy

sed -i "s|Extension('igakit.igalib',|&include_dirs=['./'],|" setup.py

%build
%add_optflags %optflags_shared -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py build_ext -i
export PYTHONPATH=$PWD
%make testall PYTHON=python3

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Tue Mar 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt3
- Build for python3 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt2.hg20150514.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt2.hg20150514.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.hg20150514
- New snapshot
- Enabled check

* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.hg20130902
- Added module for Python 3

* Thu Jul 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.hg20130902
- Initial build for Sisyphus

