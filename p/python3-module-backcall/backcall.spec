%define _unpackaged_files_terminate_build 1

%define oname backcall

Name: python3-module-%oname
Version: 0.2.0
Release: alt1
Summary: Specifications for callback functions passed in to an API
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/takluyver/backcall

BuildArch: noarch

# https://github.com/takluyver/backcall.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit
BuildRequires: /usr/bin/py.test3

%description
Specifications for callback functions passed in to an API

If your code lets other people supply callback functions, it's important
to specify the function signature you expect,
and check that functions support that. Adding extra parameters later
would break other peoples code unless you're careful.

backcall provides a way of specifying the callback signature
using a prototype function:

from backcall import callback_prototype

@callback_prototype
def handle_ping(sender, delay=None):
    # Specify positional parameters without a default, and keyword
    # parameters with a default.
    pass

def register_ping_handler(callback):
    # This checks and adapts the function passed in:
    callback = handle_ping.adapt(callback)
    ping_callbacks.append(callback)

If the callback takes fewer parameters than your prototype,
backcall will wrap it in a function that discards the extra arguments.
If the callback expects more arguments,
a TypeError is thrown when it is registered.

For more details, see the docs or the Demo notebook.

%prep
%setup

%build
flit build

%install
pip%{_python3_version} install -I dist/%oname-%version-*-none-any.whl --root %buildroot --prefix %prefix --no-deps

%check
export PYTHONDONTWRITEBYTECODE=1
export PYTEST_ADDOPTS='-p no:cacheprovider'
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3 -v tests \
	%nil

%files
%doc LICENSE
%doc README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt1
- Initial build for ALT.
