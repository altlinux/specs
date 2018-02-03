%define oname libmagic
%define sover 1

%def_with python3

Name: python-module-%oname
Version: 0.4.13
Release: alt1.1
Summary: File type identification using libmagic
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/python-magic/

# https://github.com/ahupp/python-magic.git
Source: %name-%version.tar

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools 
%endif

%py_provides magic
Conflicts: python-module-magic
Requires: %_libdir/libmagic.so.%sover

%description
This module uses ctypes to access the libmagic file type identification
library. It makes use of the local magic database and supports both
textual and MIME-type output.

%package -n python3-module-%oname
Summary: File type identification using libmagic
Group: Development/Python3
%py3_provides magic
Conflicts: python3-module-magic
Requires: %_libdir/libmagic.so.%sover

%description -n python3-module-%oname
This module uses ctypes to access the libmagic file type identification
library. It makes use of the local magic database and supports both
textual and MIME-type output.

%prep
%setup

%ifarch x86_64
LIB_SUFF=64
%endif
sed -i "s|@64@|$LIB_SUFF|" magic.py
sed -i "s|@SOVER@|%sover|" magic.py

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
export LC_ALL=en_US.UTF-8
python setup.py test ||:
%if_with python3
pushd ../python3
python3 setup.py test ||:
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.13-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.13-alt1
- Updated to upstream version 0.4.13.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.6-alt1.git20150107.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.6-alt1.git20150107.1
- NMU: Use buildreq for BR.

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt1.git20150107
- New snapshot

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt1.git20141111
- Initial build for Sisyphus

