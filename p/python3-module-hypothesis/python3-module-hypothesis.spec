%define _unpackaged_files_terminate_build 1

%define oname hypothesis

%def_with check

Name: python3-module-%oname
Version: 6.36.0
Release: alt2.1

Summary: A library for property based testing

License: MPL-2.0-no-copyleft-exception
Group: Development/Python3
Url: https://pypi.org/project/hypothesis/

BuildArch: noarch

Source: %name-%version.tar
Source1: pytest.ini
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: /dev/pts

# install_requires:
BuildRequires: python3(attr)
BuildRequires: python3(sortedcontainers)

# extras:
BuildRequires: python3(lark)
BuildRequires: python3(numpy)
BuildRequires: python3(black)
BuildRequires: python3(dateutil)
BuildRequires: python3(libcst)
BuildRequires: python3(pandas)
BuildRequires: python3(pytz)
BuildRequires: python3(redis)

# tests
BuildRequires: python3(fakeredis)
BuildRequires: python3(numpy.testing)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(pexpect)
BuildRequires: python3(pytest_xdist)
%endif

%add_python3_req_skip dpcontracts

%description
Hypothesis is an advanced testing library for Python. It lets you write tests
which are parametrized by a source of examples, and then generates simple and
comprehensible examples that make your tests fail. This lets you find more bugs
in your code with less work.

%prep
%setup
cp %SOURCE1 ./
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}-custom
tox.py3 --sitepackages -vvr --no-deps -- --numprocesses auto tests

%files
%doc LICENSE.txt README.rst
%_bindir/%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%python3_sitelibdir/__pycache__/_hypothesis_pytestplugin.*
%python3_sitelibdir/_hypothesis_pytestplugin.py

%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 6.36.0-alt2.1
- NMU: used %%add_python3_req_skip because Sisyphus does not provide debugpy.

* Wed Feb 02 2022 Stanislav Levin <slev@altlinux.org> 6.36.0-alt2
- Fixed FTBFS (Python3.10).

* Sat Jan 22 2022 Stanislav Levin <slev@altlinux.org> 6.36.0-alt1
- 6.14.8 -> 6.36.0.

* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 6.14.8-alt1
- new version 6.14.8

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 6.14.3-alt1
- new version 6.14.3

* Wed Apr 21 2021 Vitaly Lipatov <lav@altlinux.ru> 6.10.0-alt1
- new version 6.10.0

* Fri Apr 16 2021 Stanislav Levin <slev@altlinux.org> 6.9.2-alt1
- 5.41.2 -> 6.9.2.

* Fri Jan 22 2021 Vitaly Lipatov <lav@altlinux.ru> 5.41.2-alt1
- new version 5.41.2

* Thu Oct 15 2020 Stanislav Levin <slev@altlinux.org> 5.37.3-alt1
- 5.7.0 -> 5.37.3.

* Sun Mar 22 2020 Vitaly Lipatov <lav@altlinux.ru> 5.7.0-alt1
- new version 5.7.0 (with rpmrb script)
- separated build python3 module

* Wed Aug 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.66.30-alt1
- Updated to upstream version 3.66.30.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.18.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.18.1-alt1
- Updated to upstream version 3.18.1.

* Thu Jan 19 2017 Anton Midyukov <antohami@altlinux.org> 3.6.1-alt1
- Initial build for ALT Linux Sisyphus.
