%define oname pinocchio

Name: python3-module-%oname
Version: 0.4.2
Release: alt3

Summary: pinocchio plugins for the nose testing framework
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/pinocchio/

# https://github.com/mkwiatkowski/pinocchio.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python3-module-colorama

%py3_provides %oname
%py3_requires nose colorama


%description
Extra plugins for the nose testing framework. Provides tools for
flexibly assigning decorator tags to tests, choosing tests based on
their runtime, doing moderately sophisticated code coverage analysis of
your unit tests, and making your test descriptions look like
specifications.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc IDEAS *.rst doc/* examples
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.2-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.2-alt2.git20141201.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.2-alt2.git20141201
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.git20141201.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1.git20141201.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20141201
- Initial build for Sisyphus

