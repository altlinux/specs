%define _unpackaged_files_terminate_build 1
%define pypi_name gssapi

%def_with check

Name: python3-module-%pypi_name
Version: 1.8.2
Release: alt1

Summary: Python GSSAPI Wrapper
License: ISC
Group: Development/Python3
VCS: https://github.com/pythongssapi/python-gssapi.git
Url: https://pypi.org/project/gssapi/

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(Cython)

BuildRequires: libkrb5-devel >= 1.15

%if_with check
# install_requires
BuildRequires: python3(decorator)

BuildRequires: python3(k5test)
BuildRequires: python3(parameterized)
BuildRequires: krb5-kdc >= 1.15
%endif

Requires: libkrb5 >= 1.15

%description
Python-GSSAPI provides both low-level and high level wrappers around the GSSAPI
C libraries. While it focuses on the Kerberos mechanism, it should also be
useable with other GSSAPI mechanisms.

%prep
%setup
%patch -p1

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%check
# see ci/test.sh
cat > tox.ini <<'EOF'
[testenv]
allowlist_externals = bash
commands =
    bash -c 'cd gssapi/tests && python -m unittest'
EOF
%tox_check_pyproject -c tox.ini

%files
%doc LICENSE.txt README.rst
%python3_sitelibdir/gssapi/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%exclude %python3_sitelibdir/gssapi/tests/

%changelog
* Wed Oct 26 2022 Stanislav Levin <slev@altlinux.org> 1.8.2-alt1
- 1.8.1 -> 1.8.2.

* Thu Oct 06 2022 Stanislav Levin <slev@altlinux.org> 1.8.1-alt1
- 1.7.3 -> 1.8.1.

* Thu Feb 24 2022 Stanislav Levin <slev@altlinux.org> 1.7.3-alt1
- 1.7.2 -> 1.7.3.

* Mon Nov 01 2021 Stanislav Levin <slev@altlinux.org> 1.7.2-alt1
- 1.7.0 -> 1.7.2.

* Mon Sep 20 2021 Stanislav Levin <slev@altlinux.org> 1.7.0-alt1
- 1.6.14 -> 1.7.0.

* Wed Jul 28 2021 Stanislav Levin <slev@altlinux.org> 1.6.14-alt1
- 1.6.12 -> 1.6.14.

* Thu Jan 21 2021 Stanislav Levin <slev@altlinux.org> 1.6.12-alt1
- 1.6.10 -> 1.6.12.

* Mon Nov 16 2020 Stanislav Levin <slev@altlinux.org> 1.6.10-alt1
- 1.6.5 -> 1.6.10.
- Applied upstream fixes(closes: #39167).

* Mon Jul 06 2020 Stanislav Levin <slev@altlinux.org> 1.6.5-alt1
- 1.6.1 -> 1.6.5.
- Stopped build Python2 package.

* Fri Oct 18 2019 Stanislav Levin <slev@altlinux.org> 1.6.1-alt1
- 1.5.1 -> 1.6.1.

* Sat Mar 23 2019 Stanislav Levin <slev@altlinux.org> 1.5.1-alt3
- Fixed errors found by a new flake8 3.7.7.

* Sun Oct 28 2018 Stanislav Levin <slev@altlinux.org> 1.5.1-alt2
- Fixed errors found by a new pycodestyle 2.4.

* Mon Jul 23 2018 Stanislav Levin <slev@altlinux.org> 1.5.1-alt1
- 1.5.0 -> 1.5.1

* Wed Apr 11 2018 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1
- 1.4.1 -> 1.5.0

* Fri Mar 30 2018 Stanislav Levin <slev@altlinux.org> 1.4.1-alt1
- 1.3.0 -> 1.4.1

* Thu Dec 07 2017 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 1.2.2 -> 1.3.0

* Thu Nov 16 2017 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1
- 1.2.0 -> 1.2.2
- Build Python3 package
- Enable tests

* Tue May 10 2016 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- Initial build.

