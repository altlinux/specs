%define _unpackaged_files_terminate_build 1
%define oname packaging

%def_with check

Name: python3-module-%oname
Version: 21.3
Release: alt1

Summary: Core utilities for Python packages

License: Apache-2.0 or BSD-2-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/packaging

# Source-url: https://github.com/pypa/packaging.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pretend)
BuildRequires: python3(pyparsing)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
Core utilities for Python packages.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
cat > tox.ini <<EOF
[testenv]
usedevelop=True
commands =
    pytest {posargs:-vra}
EOF
tox.py3 --sitepackages --console-scripts -vvr

%files
%doc *.rst LICENSE*
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Tue Jan 11 2022 Stanislav Levin <slev@altlinux.org> 21.3-alt1
- 21.2 -> 21.3.

* Tue Nov 02 2021 Stanislav Levin <slev@altlinux.org> 21.2-alt1
- 21.0 -> 21.2.

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 21.0-alt1
- new version 21.0

* Fri Apr 23 2021 Stanislav Levin <slev@altlinux.org> 20.9-alt1
- 19.0 -> 20.9.

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 19.0-alt3
- build python3 package separately, cleanup spec

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 19.0-alt2
- Fixed testing against Pytest 5.

* Thu Jun 06 2019 Stanislav Levin <slev@altlinux.org> 19.0-alt1
- 16.8 -> 19.0.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 16.8-alt1.qa1
- NMU: applied repocop patch

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 16.8-alt1
- Updated to upstream version 16.8.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 15.4-alt2.dev0.git20150801.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 15.4-alt2.dev0.git20150801
- rebuild with clean buildreq
- disable tests 

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 15.4-alt1.dev0.git20150801
- Initial build for Sisyphus

