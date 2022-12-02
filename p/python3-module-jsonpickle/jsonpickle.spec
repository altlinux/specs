%define _unpackaged_files_terminate_build 1
%define pypi_name jsonpickle

%def_with check

Name: python3-module-%pypi_name
Version: 3.0.0
Release: alt1
Summary: Python library for serializing any arbitrary object graph into JSON
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/jsonpickle/
VCS: https://github.com/jsonpickle/jsonpickle.git

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools_scm)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(numpy)
BuildRequires: python3(numpy.testing)
BuildRequires: python3(pandas)
BuildRequires: python3(pytz)
BuildRequires: python3(gmpy2)
%endif

%description
jsonpickle converts complex Python objects to and from JSON.

%prep
%setup
%autopatch -p1

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject -- -vra

%files
%doc CHANGES.rst README.rst
%python3_sitelibdir/jsonpickle/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Fri Dec 02 2022 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1
- 2.1.0 -> 3.0.0.

* Mon Feb 07 2022 Stanislav Levin <slev@altlinux.org> 2.1.0-alt1
- 2.0.0 -> 2.1.0.

* Tue Oct 12 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt2
- Updated build and runtime dependencies.

* Tue Aug 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.0-alt1
- Updated to upstream version 2.0.0.
- Enabled tests.

* Mon Sep 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt1
- Updated to upstream version 1.4.1.
- Disabled build for python-2.

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 0.9.5-alt2
- Added missing dep on `numpy.testing`.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.5-alt1
- Updated to upstream version 0.9.5.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.git20150116.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.git20150116.1
- NMU: Use buildreq for BR.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20150116
- Version 0.9.0

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.git20141022
- Initial build for Sisyphus

