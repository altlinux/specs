%define oname libarchive

Name: python-module-%oname
Version: 3.1.2.1
Release: alt5

Summary: A libarchive wrapper for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/python-libarchive/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
BuildRequires: libarchive-devel swig zip

%py_provides %oname
Requires: zip


%description
A complete wrapper for the libarchive library generated using SWIG. Also
included in the package are compatibility layers for the Python zipfile
and tarfile modules.

%prep
%setup

rm -f %oname/*.c

%build
%make -C %oname _libarchive_wrap.c
%python_build_debug

%install
%python_install

%check
%__python setup.py test
rm -fR %oname
export PYTHONPATH=%buildroot%python_sitelibdir
%__python tests.py

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.1.2.1-alt5
- Rebuild with new setuptools.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.1.2.1-alt4.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jul 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.2.1-alt4
- Fixed build with new libarchive

* Mon Feb 08 2016 Sergey Alembekov <rt@altlinux.ru> 3.1.2.1-alt3
- Fixed _libarchive.i

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2.1-alt2
- Fixed build

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2.1-alt1
- Initial build for Sisyphus

