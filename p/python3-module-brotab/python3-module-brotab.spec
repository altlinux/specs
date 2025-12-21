%define pypi_name brotab

Name: python3-module-%pypi_name
Version: 1.5.0
Release: alt1

Summary: Control your browser's tabs from the command line

License: MIT
Group: Development/Python3
Url: https://github.com/balta2ar/brotab

# Source-url: %__pypi_url %pypi_name
Source: %pypi_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%add_python3_req_skip albert

%description
Control your browser's tabs from the command line.

bt (brotab = Browser Tabs) is a command-line tool that helps you manage
browser tabs. It can help you list, close, reorder, open and activate your tabs.

%package -n %pypi_name
Summary: Control your browser's tabs from the command line
Group: Networking/WWW
Requires: python3-module-%pypi_name = %EVR

%description -n %pypi_name
Control your browser's tabs from the command line.

bt (brotab = Browser Tabs) is a command-line tool that helps you manage
browser tabs. It can help you list, close, reorder, open and activate your tabs.

%prep
%setup -n %pypi_name-%version
sed -i "s|'config'|'share/%pypi_name'|" setup.py

%build
%pyproject_build

%install
%pyproject_install

%python3_prune

%files -n %pypi_name
%doc README.md
%_bindir/bt
%_bindir/brotab
%_bindir/bt_mediator
%_datadir/%pypi_name/

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pypi_name}-%version.dist-info/

%changelog
* Sun Dec 21 2025 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- initial build for ALT Sisyphus
