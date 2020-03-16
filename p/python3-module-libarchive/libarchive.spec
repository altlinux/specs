%define oname libarchive

%def_with check

Name: python3-module-%oname
Version: 4.0.1
Release: alt1

Summary: A libarchive wrapper for Python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-libarchive/

Source: %name-%version.tar
Patch0: compatibility-with-python38.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libarchive-devel swig zip

%py_provides %oname
Requires: zip


%description
A complete wrapper for the libarchive library generated using SWIG. Also
included in the package are compatibility layers for the Python zipfile
and tarfile modules.

%prep
%setup
%patch0 -p2

rm -f %oname/*.c

%build
%make -C %oname _libarchive_wrap.c
%python3_build_debug

%install
%python3_install

%check
%if 0
%__python3 setup.py test
rm -fR %oname
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 tests.py
%endif

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/*


%changelog
* Mon Mar 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.0.1-alt1
- Version updated to 4.0.1
- porting to python3.

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

