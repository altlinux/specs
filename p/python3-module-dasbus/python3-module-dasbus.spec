%define oname dasbus

Name: python3-module-%oname
Version: 1.7
Release: alt1
License: LGPL-2.1

Summary: DBus library in Python 3

Group: Development/Python3

Url: https://pypi.org/project/dasbus/
VCS: https://github.com/dasbus-project/dasbus.git

# Source-url: https://github.com/dasbus-project/dasbus/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: pyproject.toml

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-hatchling
BuildRequires: python3-module-setuptools

%add_python3_req_skip gi.repository.GLib

%description
This DBus library is written in Python 3,
based on GLib and inspired by pydbus.

%prep
%setup
install -vD %SOURCE1 pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Apr 01 2025 Kirill Unitsaev <fiersik@altlinux.org> 1.7-alt1
- Initial build
