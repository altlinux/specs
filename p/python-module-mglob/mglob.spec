%define oname mglob

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt1.git20130423
Summary: Enhanced file name globbing module
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/mglob/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/vivainio/mglob.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
mglob - enhanced file list expansion utility/module.

Usable as stand-alone utility (for xargs, backticks etc.), or as a
globbing library for own python programs. Globbing the sys.argv is
something that almost every Windows script has to perform manually, and
this module is here to help with that task. Also Unix users will benefit
from enhanced features such as recursion, exclusion, and directory
omission.

%package -n python3-module-%oname
Summary: Enhanced file name globbing module
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
mglob - enhanced file list expansion utility/module.

Usable as stand-alone utility (for xargs, backticks etc.), or as a
globbing library for own python programs. Globbing the sys.argv is
something that almost every Windows script has to perform manually, and
this module is here to help with that task. Also Unix users will benefit
from enhanced features such as recursion, exclusion, and directory
omission.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20130423
- Initial build for Sisyphus

