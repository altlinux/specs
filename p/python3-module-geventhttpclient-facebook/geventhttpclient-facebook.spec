%define oname geventhttpclient-facebook

Name: python3-module-%oname
Version: 0.4.4
Release: alt2

Summary: Port of the original facebook sdk to use geventhttpclient
License: ASL
Group: Development/Python3
Url: https://pypi.python.org/pypi/geventhttpclient-facebook/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Port of the original facebook sdk to use geventhttpclient.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst examples
%python3_sitelibdir/*


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.4-alt2
- disable python2

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.4.4-alt1.2
- Rebuild with python3.7.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.4-alt1.1
- NMU: Use buildreq for BR.

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1
- Initial build for Sisyphus

