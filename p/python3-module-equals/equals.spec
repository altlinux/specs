%define _unpackaged_files_terminate_build 1
%define oname equals

Name: python3-module-%oname
Version: 0.0.25
Release: alt3

Summary: Fuzzy equality test objects for testing
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/equals/
# https://github.com/toddsifleet/equals.git
BuildArch: noarch

Source: %{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flake8 python3-module-mock
BuildRequires: python3-module-doubles python3-module-coverage
BuildRequires: python3-module-coveralls python3-module-html5lib

%py3_provides %oname


%description
Equals is a stricter version of Mock.Any.

Equals allows you to assert certain equality constraints between python
objects during testing. There are times where we don't want to assert
absolute equality, e.g. we need to ensure two lists have the same
elements, but don't care about order. This was designed specifically for
usage with Mock and doubles.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Fri Nov 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.25-alt3
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.25-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.25-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.25-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.22-alt1.git20150210.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.22-alt1.git20150210.1
- NMU: Use buildreq for BR.

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.22-alt1.git20150210
- Initial build for Sisyphus

