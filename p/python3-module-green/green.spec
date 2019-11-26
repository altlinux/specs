%define _unpackaged_files_terminate_build 1
%define oname green

%def_disable check

Name: python3-module-%oname
Version: 2.5.3
Release: alt2

Summary: Clean, colorful test runner for Python unit tests
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/green/
# https://github.com/CleanCut/green.git
BuildArch: noarch

Source0: https://pypi.python.org/packages/d2/a7/f4525dac4cf86c3e445bf4579da82f0e0a78ffab669d477e0144800681f5/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest


%description
Green is a colorful, clean, fast and powerful test runner for Python
unit tests. Compare it to trial or nose.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Green is a colorful, clean, fast and powerful test runner for Python
unit tests. Compare it to trial or nose.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst *.md PKG-INFO
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test


%changelog
* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.5.3-alt2
- python2 disabled

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.5.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.1-alt1.git20141125.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.1-alt1.git20141125.1
- NMU: Use buildreq for BR.

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt1.git20141125
- Version 1.7.1

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.4-alt1.git20140826
- Initial build for Sisyphus

