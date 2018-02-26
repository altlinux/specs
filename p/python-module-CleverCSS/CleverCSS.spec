%define oname CleverCSS

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt2
Summary: Funky css preprocessor dammit
License: GPL
Group: Development/Python
Url: http://pypi.python.org/pypi/CleverCSS/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%description
CleverCSS is a small markup language for CSS inspired by Python that can
be used to build a style sheet in a clean and structured way. In many
ways it's cleaner and more powerful than CSS2 is.

The most obvious difference to CSS is the syntax: it is indentation
based and not flat. While this is obviously against the Python Zen, it's
nonetheless a good idea for structural styles.

%if_with python3
%package -n python3-module-%oname
Summary: Funky css preprocessor dammit (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
CleverCSS is a small markup language for CSS inspired by Python that can
be used to build a style sheet in a clean and structured way. In many
ways it's cleaner and more powerful than CSS2 is.

The most obvious difference to CSS is the syntax: it is indentation
based and not flat. While this is obviously against the Python Zen, it's
nonetheless a good idea for structural styles.
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
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

