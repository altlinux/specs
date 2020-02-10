%define _unpackaged_files_terminate_build 1

%define oname ratelim

Name: python3-module-%oname
Version: 0.1.6
Release: alt3

Summary: Makes it easy to respect rate limits
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/ratelim/
BuildArch: noarch

# https://github.com/themiurgo/ratelim.git
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-decorator

%py3_provides %oname
%py3_requires decorator


%description
Ratelim is a simple Python library that limits the number of times a
function can be called in during a time interval. It is particularly
useful when using online APIs, which commonly enforce rate limits.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.6-alt3
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.6-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt2
- Updated build dependencies.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150113.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1.git20150113.1
- NMU: Use buildreq for BR.

* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150113
- Initial build for Sisyphus

