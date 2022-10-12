%define _unpackaged_files_terminate_build 1
%define pypi_name invoke

Name: python3-module-%pypi_name
Version: 1.7.3
Release: alt1

Summary: Simple Python task execution
License: BSD-2-Clause
Group: Development/Python3
Url: https://www.pyinvoke.org/
BuildArch: noarch

# Source-git: https://github.com/pyinvoke/invoke.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%py3_requires lexicon
%py3_requires six
%py3_requires yaml

%description
Invoke is a Python (2.6+ and 3.2+) task execution tool & library,
drawing inspiration from various sources to arrive at a powerful & clean
feature set.

%prep
%setup
%autopatch -p1

# drop everything except fluidity (not packaged (unmaintained))
find invoke/vendor/ \
    -mindepth 1 -maxdepth 1 \
    \( ! \( -name '__init__.py' -type f \) -a ! \( -name 'fluidity' -type d \) \) \
    -exec rm -rfv '{}' +

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/invoke/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Oct 11 2022 Stanislav Levin <slev@altlinux.org> 1.7.3-alt1
- 1.6.0 -> 1.7.3.

* Mon Jul 19 2021 Stanislav Levin <slev@altlinux.org> 1.6.0-alt2
- Restored back runtime dep on lexicon.

* Sun Jul 18 2021 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- new version 1.6.0

* Mon Jul 06 2020 Stanislav Levin <slev@altlinux.org> 1.4.1-alt1
- 0.21.0 -> 1.4.1.

* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.21.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.21.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Oct 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.21.0-alt1
- Updated to upstream version 0.21.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.1-alt2.git20150730.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 0.10.1-alt2.git20150730
- cleanup buildreq

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1.git20150730
- Version 0.10.1

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20141113
- Initial build for Sisyphus

