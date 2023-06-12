# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

#%%def_disable check

%define srcname pytest-xvfb

Name: python3-module-%srcname
Version: 3.0.0
Release: alt1
Summary: A pytest plugin to run Xvfb for tests

License: MIT
Group: Development/Python3
URL: https://github.com/The-Compiler/pytest-xvfb
# Source-url: %url/archive/refs/tags/v%version.tar.gz
Source: %srcname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_disabled check
%else
BuildRequires: pytest3
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
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot/%python3_sitelibdir/
pytest3 -v

%files
%doc CHANGELOG.rst README.rst
%python3_sitelibdir/pytest_xvfb.py
%python3_sitelibdir/__pycache__/pytest_xvfb.*
%python3_sitelibdir/pytest_xvfb-%version.dist-info/

%changelog
* Mon Jun 12 2023 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt1
- new version (3.0.0) with rpmgs script

* Sun Mar 06 2022 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- initial build
