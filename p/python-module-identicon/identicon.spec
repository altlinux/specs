%define _unpackaged_files_terminate_build 1

%define oname identicon

%def_with python3

Name: python-module-%oname
Version: 20101207
Release: alt2
Summary: Python identicon implementation
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://github.com/aerosol/identicon

# https://github.com/aerosol/identicon.git
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python-tools-2to3
%endif

%py_requires PIL

%description
identicon.py: identicon python implementation.

%if_with python3
%package -n python3-module-%oname
Summary: Python identicon implementation
Group: Development/Python3
%py3_requires PIL

%description -n python3-module-%oname
identicon.py: identicon python implementation.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
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
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 20101207-alt2
- NMU: rebuilt to regenerate dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 20101207-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 20101207-alt1.1
- NMU: Use buildreq for BR.

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20101207-alt1
- Initial build for Sisyphus

