%define oname credis

Name: python3-module-%oname
Version: 2.0.2
Release: alt1

Summary: High performance redis client implemented with cython
License: Free
Group: Development/Python3
URL: https://pypi.org/project/credis
VCS: https://github.com/yihuang/credis

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-Cython
BuildRequires: python3-module-poetry

%py3_provides %oname
%py3_requires hiredis

%description
Minimal redis client written in cython, 5X faster than redis-py.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.rst benchmark test
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon May 27 2024 Grigory Ustinov <grenka@altlinux.org> 2.0.2-alt1
- Build new version.

* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.5-alt2
- python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.5-alt1.git20150211.2.1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.5-alt1.git20150211.2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sat Mar 26 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.5-alt1.git20150211.2
- NMU: Fixed BRs.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.5-alt1.git20150211.1
- NMU: Use buildreq for BR.

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.git20150211
- Initial build for Sisyphus
