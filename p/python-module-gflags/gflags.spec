%define oname gflags

%def_with python3

Name: python-module-%oname
Version: 2.0
Release: alt2

Summary: Google Commandline Flags Module
License: BSD
Group: Development/Python

Url: https://pypi.python.org/pypi/python-gflags

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%setup_python_module %oname

%description
Google Commandline Flags Module.

%package -n python3-module-%oname
Summary: Google Commandline Flags Module
Group: Development/Python3

%description -n python3-module-%oname
Google Commandline Flags Module.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
	$(find ./ -name '*.py')
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

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS ChangeLog NEWS README
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2
- Added module for Python 3

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Initial build for Sisyphus

