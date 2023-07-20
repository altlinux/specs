%define _unpackaged_files_terminate_build 1

%define pypi_name pyga
%define mod_name %pypi_name

%def_disable check

Name: python3-module-%pypi_name
Version: 2.6.2
Release: alt4

Summary: Server side implemenation of Google Analytics in Python
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/pyga/
Vcs: https://github.com/kra3/py-ga-mob
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%add_pyproject_deps_runtime_filter setuptools
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps -- prereq
%pyproject_builddeps_build

%description
pyga is an iplementation of Google Analytics in Python; so that it can
be used at server side. This project only helps you with Data Collection
part of Google Analytics. ie., You can consider this as a replacement
for ga.js at client side.

%prep
%setup
# pep517 hooks fail due to missing six
%pyproject_deps_resync prereq pip_reqfile requirements.txt
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%__python3 setup.py test

%files
%doc *.rst RELEASES
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/tests

%changelog
* Thu Jul 20 2023 Stanislav Levin <slev@altlinux.org> 2.6.2-alt4
- Fixed FTBFS (missing build dependency on six).

* Mon May 30 2022 Grigory Ustinov <grenka@altlinux.org> 2.6.2-alt3
- Fixed BuildRequires.

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 2.6.2-alt2
- drop unused BR: rpm-macros-sphinx

* Wed Apr 28 2021 Vitaly Lipatov <lav@altlinux.ru> 2.6.2-alt1
- NMU: new version 2.6.2 (with rpmrb script)
- NMU: cleanup spec

* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.5.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1.git20140809.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.5.0-alt1.git20140809.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.5.0-alt1.git20140809.1
- NMU: Use buildreq for BR.

* Fri Oct 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.0-alt1.git20140809
- Initial build for Sisyphus

