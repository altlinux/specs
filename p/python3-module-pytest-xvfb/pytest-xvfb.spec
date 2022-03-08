# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

#%%def_disable check

%define srcname pytest-xvfb

Name: python3-module-%srcname
Version: 2.0.0
Release: alt1
Summary: A pytest plugin to run Xvfb for tests

License: MIT
Group: Development/Python3
URL: https://github.com/The-Compiler/pytest-xvfb
# Source-url: %url/archive/refs/tags/v%version.tar.gz
Source: %srcname-%version.tar
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%if_disabled check
%else
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pyvirtualdisplay
BuildRequires: xauth
BuildRequires: xvfb-run
%endif

%description
With Xvfb and the plugin installed, your testsuite automatically runs with
Xvfb. This allows tests to be run without windows popping up during GUI tests
or on systems without a display (like a CI).

If Xvfb is not installed, the plugin does not run and your tests will still
work as normal. However, a warning message will print to standard output
letting you know that Xvfb is not installed.

If you're currently using xvfb-run in something like .travis.yml, simply remove
it and install this plugin instead - then you'll also have the benefits of Xvfb
locally.

%prep
%setup -n %srcname-%version
rm tests/test_xvfb_windows.py

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
py.test3 -v

%files
%doc CHANGELOG.rst README.rst
%python3_sitelibdir/pytest_xvfb.py
%python3_sitelibdir/__pycache__/pytest_xvfb.*
%python3_sitelibdir/pytest_xvfb-*.egg-info/

%changelog
* Sun Mar 06 2022 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- initial build
