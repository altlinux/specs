%define oname hachibee_sphinx_theme

Name: python-module-%oname
Version: 0.2.5
Release: alt2

Summary: A simple sphinx theme
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/hachibee-sphinx-theme/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires: python-module-setuptools
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest


%description
Sphinx hachibee theme.

%package -n python3-module-%oname
Summary: A simple sphinx theme
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Sphinx hachibee theme.

%prep
%setup

cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc *.rst
%python_sitelibdir/*

%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*


%changelog
* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.5-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.5-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1.1
- NMU: Use buildreq for BR.

* Thu Apr 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus

