%define _unpackaged_files_terminate_build 1
%define oname dugong

%def_with check

Name: python3-module-%oname
Version: 3.8.2
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
BuildRequires: python3(tox_console_scripts)
%endif

%description
The Python Dugong module provides an API for communicating with HTTP 1.1
servers. It is an alternative to the standard library's http.client
(formerly httplib) module.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    {envbindir}/pytest -vra {posargs:test}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
# custom support for TLS in HTTPServerThread doesn't work with Python3.10
tox.py3 --sitepackages --console-scripts -vvr -s false --develop -- \
    --ignore test/test_dugong.py \
    test

%files
%doc *.rst examples
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Mon Mar 21 2022 Stanislav Levin <slev@altlinux.org> 3.8.2-alt1
- 3.7.5 -> 3.8.2.

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

