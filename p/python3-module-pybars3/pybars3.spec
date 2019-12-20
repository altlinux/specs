%define oname pybars3

Name: python3-module-%oname
Version: 0.9.3
Release: alt2

Summary: Handlebars.js templating for Python 3 and 2
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pybars3/
BuildArch: noarch

# https://github.com/wbond/pybars3.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-pymeta3
BuildRequires: python3-module-pytest python3-module-testtools


%description
Handlebars.js template support for Python 3 and 2.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
py.test3 -vv

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Fri Dec 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.3-alt2
- build for python2 disabled

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.3-alt1
- Updated to upstream version 0.9.3.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.2-alt1.git20150123.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.2-alt1.git20150123.1
- NMU: Use buildreq for BR.

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.git20150123
- Initial build for Sisyphus

