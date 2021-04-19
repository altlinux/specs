%define _unpackaged_files_terminate_build 1
%define oname typing-inspect

%def_with check

Name: python3-module-%oname
Version: 0.6.0
Release: alt1

Summary: Runtime inspection of types defined in typing module
License: MIT
Group: Development/Python3
# Source-git: https://github.com/ilevkivskyi/typing_inspect.git
Url: https://pypi.org/project/typing-inspect/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(mypy_extensions)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(typing_extensions)
%endif

BuildArch: noarch

# PyPI name(dash, underscore)
%py3_provides %oname

# nested import
%py3_requires typing_extensions

%description
The typing_inspect module defines experimental API for runtime inspection of
types defined in the Python standard typing module. Works with typing version
3.7.4 and later.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
cat > tox.ini <<EOF
[testenv]
usedevelop=True
commands =
    pytest {posargs:-vra}
EOF
tox.py3 --sitepackages --console-scripts --no-deps -vvr

%files
%doc README.md
%python3_sitelibdir/typing_inspect.py
%python3_sitelibdir/__pycache__/typing_inspect.cpython-*
%python3_sitelibdir/typing_inspect-%version-py%_python3_version.egg-info/

%changelog
* Fri Apr 16 2021 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus.

