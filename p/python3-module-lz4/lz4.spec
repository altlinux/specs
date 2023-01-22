%define _unpackaged_files_terminate_build 1
%define oname lz4

%def_with check

Name: python3-module-%oname
Version: 4.3.2
Release: alt1

Summary: LZ4 Bindings for Python

License: BSD
Group: Development/Python3
Url: https://pypi.org/project/lz4/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3

BuildRequires: python3(pkgconfig)
BuildRequires: python3(setuptools_scm)
BuildRequires: py3c-devel
BuildRequires: liblz4-devel

%if_with check
BuildRequires: /proc
BuildRequires: python3(future)
BuildRequires: python3(psutil)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(tox)
%endif

%description
This package provides bindings for the lz4 compression library by Yann
Collet.

%prep
%setup
# remove bundled libs in favor of system ones
rm -r lz4libs

%build
# SETUPTOOLS_SCM_PRETEND_VERSION: when defined and not empty,
# its used as the primary source for the version number in which
# case it will be a unparsed string
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build_debug

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
%if_with check
%python3_check
%endif

%files
%doc *.rst
%python3_sitelibdir/lz4-%version-py%_python3_version.egg-info/
%python3_sitelibdir/lz4/

%changelog
* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 4.3.2-alt1
- new version 4.3.2 (with rpmrb script)

* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 4.0.2-alt1
- new version 4.0.2 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 3.1.10-alt1
- new version 3.1.10 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 3.1.3-alt1
- new version 3.1.3 (with rpmrb script)

* Sat Sep 19 2020 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- new version 3.1.0 (with rpmrb script)

* Sat Sep 19 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt3
- separated python3 build
- add BR: py3c-devel

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 2.1.6-alt2
- Fixed testing against Pytest 5.

* Sat Feb 16 2019 Stanislav Levin <slev@altlinux.org> 2.1.6-alt1
- 0.8.2 -> 2.1.6.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.2-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1.git20140728.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.git20140728.1
- NMU: Use buildreq for BR.

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20140728
- Initial build for Sisyphus

