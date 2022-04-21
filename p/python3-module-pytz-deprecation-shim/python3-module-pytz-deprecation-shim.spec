%define _unpackaged_files_terminate_build 1
%define oname pytz-deprecation-shim

Name: python3-module-%oname
Version: 0.1.0.post0
Release: alt1

Summary: Shims to help you safely remove pytz
License: Apache-2.0
Group: Development/Python

Url: https://github.com/pganssle/pytz-deprecation-shim
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildArch: noarch

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-build
BuildRequires: python3-module-installer
BuildRequires: python3-module-wheel

BuildRequires: python3-module-pytest
BuildRequires: python3-module-hypothesis

%description
%summary

%prep
%setup
%patch0 -p1

%build
%__python3 -m build --wheel --no-isolation

%install
%__python3 -m installer --destdir="%buildroot" dist/*.whl

%check
export PYTHONPATH="$PYTHONPATH:%buildroot/%python3_sitelibdir"
%__python3 -m pytest tests

%files
%doc LICENSE README.rst CHANGELOG.rst
%python3_sitelibdir/*

%changelog
* Thu Apr 21 2022 Egor Ignatov <egori@altlinux.org> 0.1.0.post0-alt1
- Initial build for ALT
