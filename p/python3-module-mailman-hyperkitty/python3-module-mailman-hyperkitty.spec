%define pypi_name mailman-hyperkitty

Name: python3-module-mailman-hyperkitty
Version: 1.2.1
Release: alt1
Summary: Mailman 3 archiver plugin for HyperKitty

License: GPL-3.0-or-later
Group: Development/Python3
URL: https://gitlab.com/mailman/mailman-hyperkitty
# Source-url: %__pypi_url mailman-hyperkitty
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
Mailman archiver plugin for HyperKitty.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
install -D -m644 mailman-hyperkitty.cfg \
    %buildroot%_sysconfdir/mailman3.d/hyperkitty.cfg

%files
%config(noreplace) %_sysconfdir/mailman3.d/hyperkitty.cfg
%python3_sitelibdir/mailman_hyperkitty/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Nov 02 2026 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- install the Mailman HyperKitty archiver configuration.
- initial build for ALT Sisyphus

