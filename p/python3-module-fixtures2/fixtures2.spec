%define oname fixtures2

Name: python3-module-%oname
Version: 0.1.7
Release: alt2

Summary: Extension of the fixtures test framework
License: Free
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/fixtures2/

# https://github.com/CooledCoffee/fixtures2.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-mox python3-module-fixtures
BuildRequires: python3-module-pytest python3-module-html5lib

%py3_provides %oname
%py3_requires mox fixtures


%description
Fixtures2 is an extension of the fixtures test framework.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3 -vv

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.7-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.7-alt1.git20171218.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.7-alt1.git20171218
- Updated to upstream version 0.1.7.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20140528.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1.git20140528.1
- NMU: Use buildreq for BR.

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20140528
- Initial build for Sisyphus

