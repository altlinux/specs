%define _unpackaged_files_terminate_build 1
%define oname dugong

%def_with check

Name: python3-module-%oname
Version: 3.7.5
Release: alt1
Summary: Provides an API for communicating with HTTP 1.1 servers
License: Python-2.0
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/dugong/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(asyncio)
BuildRequires: python3(tox)
%endif

%py3_provides %oname
%py3_requires asyncio

%description
The Python Dugong module provides an API for communicating with HTTP 1.1
servers. It is an alternative to the standard library's http.client
(formerly httplib) module.

%prep
%setup
%autopatch -p1

%build
%python3_build_debug

%install
%python3_install

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
whitelist_externals =
    /bin/cp
    /bin/sed
commands_pre =
    /bin/cp %_bindir/py.test3 {envbindir}/py.test
    /bin/sed -i '1c #!{envpython}' {envbindir}/py.test
commands =
    {envbindir}/py.test {posargs:-vra}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr

%files
%doc *.rst examples
%python3_sitelibdir/*

%changelog
* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 3.7.5-alt1
- 3.7.3 -> 3.7.5.

* Wed May 29 2019 Stanislav Levin <slev@altlinux.org> 3.7.3-alt2
- Fixed Pytest4.x compatibility errors.

* Wed Aug 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.7.3-alt1
- Updated to upstream version 3.7.3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.7.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.7.1-alt1
- Updated to upstream version 3.7.1.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.7-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1
- Initial build for Sisyphus

