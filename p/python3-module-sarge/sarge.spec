%define srcname sarge

Name: python3-module-%srcname
Summary: Command pipelines for python 3
Version: 0.1.6
Release: alt1
License: BSD-3-Clause
Url: https://sarge.readthedocs.org/
Group: Development/Python3

Source: %srcname-%version.tar
# Source-url: https://files.pythonhosted.org/packages/source/s/sarge/sarge-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools

BuildArch: noarch

%description
A wrapper for subprocess which provides command pipeline functionality.

%prep
%setup -n %srcname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Thu Jul 29 2021 Anton Midyukov <antohami@altlinux.org> 0.1.6-alt1
- initial build
