%define oname pycmd

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt1.hg20140627.1
Summary: Command line tools for helping with Python development
License: MIT
Group: Development/Python
Url: http://pylib.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

# hg clone https://bitbucket.org/hpk42/pycmd
Source: %name-%version.tar.gz

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
%endif

Conflicts: py

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

%description
Collection of command line tools for dealing with python files
(locating, counting LOCs, cleaning up pyc files ...)

%package -n python3-module-%oname
Summary: Command line tools for helping with Python development
Group: Development/Python3

%description -n python3-module-%oname
Collection of command line tools for dealing with python files
(locating, counting LOCs, cleaning up pyc files ...)

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
	%buildroot%python3_sitelibdir/%oname/*.py
%endif

%python_install

%files
%doc AUTHORS CHANGELOG LICENSE *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGELOG LICENSE *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1-alt1.hg20140627.1
- NMU: Use buildreq for BR.

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.hg20140627
- Version 1.1
- Added module for Python 3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.a2dev1-alt1.hg20130918
- New snapshot

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.a2dev1-alt1.hg20121007
- Version 1.0.a2dev1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.hg20101129.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.hg20101129
- New snapshot

* Mon Nov 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.hg20101108.1
- Added explicit conflict with py

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.hg20101108
- Initial build for Sisyphus

