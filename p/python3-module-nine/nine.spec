%define _unpackaged_files_terminate_build 1
%define oname nine

Name: python3-module-%oname
Version: 1.0.0
Release: alt2

Summary: Python 2 / 3 compatibility, like six, but favouring Python 3
License: Public Domain
Group: Development/Python3
Url: https://pypi.python.org/pypi/nine
BuildArch: noarch

Source0: https://pypi.python.org/packages/31/0b/b86e3453dd85bf48eda37f842c91bc6f5ce2d5ffc451b6a88039340ed262/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3


%description
Python 2 and 3 compatibility library, such that your code looks more
like Python 3.

%package test
Summary: Test for nine
Group: Development/Python3
Requires: %name = %EVR

%description test
Python 2 and 3 compatibility library, such that your code looks more
like Python 3.

This package contains test for nine.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files test
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*


%changelog
* Fri Nov 15 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt2
- python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt2
- Added module for Python 3

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus

