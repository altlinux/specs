%define _unpackaged_files_terminate_build 1
%define pypi_name backcall

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.0
Release: alt2
Summary: Specifications for callback functions passed in to an API
License: BSD-3-Clause
Group: Development/Python3
Url: https://github.com/takluyver/backcall

BuildArch: noarch

# https://github.com/takluyver/backcall.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(flit_core)

%if_with check
BuildRequires: python3(pytest)
%endif

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
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE
%doc README.rst
%python3_sitelibdir/backcall/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 10 2022 Stanislav Levin <slev@altlinux.org> 0.2.0-alt2
- Fixed FTBFS (flit_core 3.7.1).

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt1
- Initial build for ALT.
