%define _unpackaged_files_terminate_build 1
%define pypi_name jq

%def_with check

Name: python3-module-%pypi_name
Version: 1.4.1
Release: alt1

Summary: Python bindings for jq
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/jq/
Vcs: https://github.com/mwilliamson/jq.py.git

Source0: %name-%version.tar
Source1: setup.py

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(Cython)

BuildRequires: libjq-devel

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
jq is a lightweight and flexible JSON processor.

This project contains Python bindings for jq.

%prep
%setup

# remove vendored libraries
rm -fvr deps

# provide self-written building instructions
cp -fv %SOURCE1 .
rm -fv pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Thu Mar 16 2023 Anton Zhukharev <ancieg@altlinux.org> 1.4.1-alt1
- 1.4.0 -> 1.4.0.

* Thu Jan 12 2023 Anton Zhukharev <ancieg@altlinux.org> 1.4.0-alt2
- remove unused liboniguruma-devel build requirement

* Thu Jan 12 2023 Anton Zhukharev <ancieg@altlinux.org> 1.4.0-alt1
- 1.4.0
- update whole package building
- use modern pyproject macros
- actualize Summary, License and Url tags

* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.6-alt2
- build for python2 disabled

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.6-alt1
- Updated to upstream version 0.1.6.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20150118.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1.git20150118.1
- NMU: Use buildreq for BR.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150118
- Initial build for Sisyphus

