%define oname ntlm

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt2

Summary: NTLM support, including an authentication handler for urllib2
License: Free
Group: Development/Python

Url: https://pypi.python.org/pypi/python-ntlm

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
This package allows Python clients running on any operating
system to provide NTLM authentication to a supporting server.

python-ntlm is probably most useful on platforms that are not
Windows, since on Windows it is possible to take advantage of
platform-specific NTLM support.

%package -n python3-module-%oname
Summary: NTLM support, including an authentication handler for urllib2
Group: Development/Python3

%description -n python3-module-%oname
This package allows Python clients running on any operating
system to provide NTLM authentication to a supporting server.

python-ntlm is probably most useful on platforms that are not
Windows, since on Windows it is possible to take advantage of
platform-specific NTLM support.

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
%doc PKG-INFO
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Added module for Python 3

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

