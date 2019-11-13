%define oname pyclipper

Name: python3-module-%oname
Version: 1.0.6
Release: alt2

Summary: Cython wrapper for the C++ translation of the Angus Johnson's Clipper library
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyclipper/
# https://github.com/greginvm/pyclipper.git

Source: %name-%version.tar
Patch: pyclipper-setup.py.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libpolyclipping-devel
BuildRequires: python3-devel python3-module-pytest
BuildRequires: python3-module-Cython

%py3_provides %oname


%description
Pyclipper is a Cython wrapper exposing public functions and classes of
the C++ translation of the Angus Johnson's Clipper library.

%prep
%setup
%patch -p1

sed -i -e 's,use_scm_version=True,version="%version",' setup.py

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')

rm -f %oname/clipper.*

%build
%add_optflags -fno-strict-aliasing -I%_includedir/polyclipping

%python3_build_debug

%install
%python3_install

%check
#CFLAGS="-I%_includedir/polyclipping" python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.6-alt2
- python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.6-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Dec 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.6-alt1
- NMU: rebuild with libpolyclipping
- new version

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.2-alt1.b0.git20150320.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.b0.git20150320
- Initial build for Sisyphus

