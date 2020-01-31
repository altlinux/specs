%define oname pyrelic

Name:       python3-module-%oname
Version:    0.8.0
Release:    alt3

Summary:    Python API Wrapper for NewRelic API
License:    MIT / GPL
Group:      Development/Python3
Url:        https://pypi.python.org/pypi/pyrelic

BuildArch:  noarch

# https://github.com/andrewgross/pyrelic.git
Source:     %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-requests python3-module-sure
BuildRequires: python3-module-nose python3-module-coverage
BuildRequires: python3-module-httpretty python3-module-html5lib
BuildRequires: python3-module-mimeparse python3-module-pbr
BuildRequires: python3-module-unittest2 python3-module-mock

%py3_provides %oname
%py3_requires six requests


%description
A New Relic client library written in Python.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.8.0-alt3
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt2.git20150520.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 26 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.0-alt2.git20150520
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.git20150520.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.0-alt1.git20150520.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20150520
- Initial build for Sisyphus

