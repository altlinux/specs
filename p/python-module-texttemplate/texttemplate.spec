%define oname texttemplate

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt2
Summary: Text templating module
License: LGPL
Group: Development/Python
Url: http://pypi.python.org/pypi/texttemplate/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python-tools-2to3
%endif

%description
texttemplate converts text templates into simple Python-based object
models easily manipulated from ordinary Python code. Fast, powerful and
easy to use.

%if_with python3
%package -n python3-module-%oname
Summary: Text templating module (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
texttemplate converts text templates into simple Python-based object
models easily manipulated from ordinary Python code. Fast, powerful and
easy to use.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
sed -i 's|%_bindir/python|%_bindir/python3|' Examples/Tutorial_1.py
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt Documentation Examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt Documentation ../python3/Examples
%python3_sitelibdir/*
%endif

%changelog
* Tue Apr 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.0-alt1.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus

