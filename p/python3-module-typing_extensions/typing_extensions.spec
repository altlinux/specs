%define _unpackaged_files_terminate_build 1
%global modname typing_extensions

%def_with check

Name: python3-module-%modname
Version: 4.5.0
Release: alt1
Summary: Python Typing Extensions
Group: Development/Python3
License: Python
Url: https://github.com/python/typing/blob/master/typing_extensions
Source: %name-%version.tar

BuildArch: noarch
Provides: python3-module-typing-extensions = %EVR
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-flit

%if_with check
BuildRequires: python3-test
BuildRequires: python3(tox)
%endif

%description
Typing Extensions - Backported and Experimental Type Hints for Python

The typing module was added to the standard library in Python 3.5 on a
provisional basis and will no longer be provisional in Python 3.7.
However, this means users of Python 3.5 - 3.6 who are unable to upgrade will not
be able to take advantage of new types added to the typing module, such as
typing.Text or typing.Coroutine.

The typing_extensions module contains both backports of these changes as well as
experimental types that will eventually be added to the typing module, such as
Protocol.

Users of other Python versions should continue to install and use the typing
module from PyPi instead of using this one unless specifically writing code that
must be compatible with multiple Python versions or requires experimental types.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
changedir = src_py3
commands = python -m unittest discover
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -s false

%files
%doc README.md
%python3_sitelibdir/typing_extensions.py
%python3_sitelibdir/__pycache__/typing_extensions.cpython*
%python3_sitelibdir/%modname-%version.dist-info

%changelog
* Wed Feb 15 2023 Grigory Ustinov <grenka@altlinux.org> 4.5.0-alt1
- Automatically updated to 4.5.0.

* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 4.4.0-alt1
- Automatically updated to 4.4.0.

* Tue Sep 13 2022 Grigory Ustinov <grenka@altlinux.org> 4.3.0-alt1
- Build new version.

* Tue Sep 07 2021 Stanislav Levin <slev@altlinux.org> 3.10.0.2-alt1
- 3.7.4.3 -> 3.10.0.2.

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 3.7.4.3-alt2
- Fixed BuildRequires.

* Sun Sep 06 2020 Alexey Shabalin <shaba@altlinux.org> 3.7.4.3-alt1
- Initial release.
