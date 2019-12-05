%define oname facebook-sdk

Name: python3-module-%oname
Version: 1.0.0
Release: alt2

Summary: Support the Facebook Graph API and the official Facebook JavaScript SDK
License: ASL
Group: Development/Python3
Url: https://pypi.python.org/pypi/facebook-sdk
BuildArch: noarch

# https://github.com/pythonforfacebook/facebook-sdk.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx


%description
This client library is designed to support the Facebook Graph API and
the official Facebook JavaScript SDK, which is the canonical way to
implement Facebook authentication.

This client library is designed to support the Facebook Graph API and
the official Facebook JavaScript SDK, which is the canonical way to
implement Facebook authentication. You can read more about the Graph API
by accessing its official documentation.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html

%files
%doc *.rst examples docs/_build/html
%python3_sitelibdir/*


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt2
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1.alpha.git20140828.2
- Rebuild with python3.7.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.alpha.git20140828.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1.alpha.git20140828.1
- NMU: Use buildreq for BR.

* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.alpha.git20140828
- Initial build for Sisyphus

