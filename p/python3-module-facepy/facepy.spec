%define oname facepy

Name: python3-module-%oname
Version: 1.0.3
Release: alt2
Summary: Facepy makes it really easy to interact with Facebook's Graph API
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/facepy/

# https://github.com/jgorset/facepy.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx

%description
Facepy makes it really easy to interact with Facebook's Graph API.

%prep
%setup

sed -i 's|@VERSION@|%version|g' docs/source/conf.py

%prepare_sphinx3 docs
ln -s ../objects.inv docs/source/

%build
%python3_build

%install
%python3_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make SPHINXBUILD="sphinx-build-3" -C docs html

%files
%doc AUTHORS *.rst docs/build/html
%python3_sitelibdir/*

%changelog
* Wed Jun 09 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.3-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.3-alt1.git20140824.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.3-alt1.git20140824.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.3-alt1.git20140824.1
- NMU: Use buildreq for BR.

* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20140824
- Initial build for Sisyphus

