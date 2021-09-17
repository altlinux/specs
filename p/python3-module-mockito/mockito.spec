%define _unpackaged_files_terminate_build 1

%define oname mockito
%def_with check

Name: python3-module-%oname
Version: 1.2.2
Release: alt1

Summary: Spying framework
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mockito/
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(numpy)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
Mockito is a spying framework based on Java library with the same name.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
commands =
    {envbindir}/pytest {posargs:-vra}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr

%files
%doc AUTHORS *.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Fri Sep 10 2021 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1
- 0.7.1 -> 1.2.2.

* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7.1-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus

