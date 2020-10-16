%define _unpackaged_files_terminate_build 1
%define oname validators

%def_with check

Name: python3-module-%oname
Version: 0.18.1
Release: alt1

Summary: Python data validation for Humans
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/validators/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(decorator)
BuildRequires: python3(six)
BuildRequires: python3(tox)
%endif

%description
Python has all kinds of data validation tools, but every one of them seems to
require defining a schema or form. I wanted to create a simple validation
library where validating a simple value does not require defining a form or a
schema.

%prep
%setup

%build
%python3_build

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
tox.py3 --sitepackages -vvr -- tests

%files
%doc *.rst LICENSE
%python3_sitelibdir/*

%changelog
* Fri Oct 16 2020 Stanislav Levin <slev@altlinux.org> 0.18.1-alt1
- Initial build for Sisyphus.
