%define oname nose-logpertest

Name: python3-module-%oname
Version: 0.0.1
Release: alt3

Summary: Logging nose plugin to create log per test
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/nose-logpertest
BuildArch: noarch

# https://github.com/taykey/nose-logpertest.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose
BuildRequires: python-tools-2to3

%py3_provides nose_logpertest


%description
This plugin creates a log file per test run by nose, holding the logs of
that specific test.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
nosetests3 -v

%files
%doc *.md *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.1-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.1-alt2.git20141127.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 30 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.1-alt2.git20141127
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.git20141127.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141127
- Initial build for Sisyphus

