%define oname CleverCSS

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt3.1.1
Summary: Funky css preprocessor dammit
License: GPL
Group: Development/Python
Url: http://pypi.python.org/pypi/CleverCSS/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base
BuildRequires: python-devel python-tools-2to3 rpm-build-python3 time

#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python-tools-2to3
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
find -type f -name '*.py' -exec 2to3 -w '{}' +
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt3.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt3.1
- NMU: Use buildreq for BR.

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-3.3

* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

