%global modname typing_extensions

Name: python3-module-%modname
Version: 3.7.4.3
Release: alt1
Summary: Python Typing Extensions
Group: Development/Python3
License: Python
Url: https://github.com/python/typing/blob/master/typing_extensions
Source: %modname-%version.tar.gz

BuildArch: noarch
Provides: python3-module-typing-extensions = %EVR
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
# For tests
BuildRequires: python3-test
BuildRequires: python3-module-discover

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
%setup -n %modname-%version

%build
%python3_build

%install
%python3_install

%check
%__python3 src_py3/test_typing_extensions.py

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Sun Sep 06 2020 Alexey Shabalin <shaba@altlinux.org> 3.7.4.3-alt1
- Initial release.
