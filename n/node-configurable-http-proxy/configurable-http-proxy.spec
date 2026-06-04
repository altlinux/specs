%define node_module configurable-http-proxy

Name: node-configurable-http-proxy
Version: 5.2.0
Release: alt1

Summary: Node-http-proxy plus a REST API
License: BSD-3-Clause
Group: Other
Url: https://github.com/jupyterhub/configurable-http-proxy

Source: %name-%version.tar
Source1: node_modules.tar

BuildArch: noarch

BuildRequires: rpm-build-nodejs

Requires: node

AutoReq: no
AutoProv: no

%description
%summary.

%prep
%setup -a 1

%build
#

%install
mkdir -p %buildroot%_bindir
ln -sr %buildroot%nodejs_sitelib/%node_module/bin/%node_module %buildroot%_bindir/%node_module
mkdir -p %buildroot%nodejs_sitelib/%node_module/
cp -a * %buildroot/%nodejs_sitelib/%node_module/
rm -rf %buildroot/%nodejs_sitelib/%node_module/docs/

%files
%doc README.*
%_bindir/%node_module
%nodejs_sitelib/%node_module/

%changelog
* Thu Jun 04 2026 Anton Vyatkin <toni@altlinux.org> 5.2.0-alt1
- New version 5.2.0.

* Fri Dec 05 2025 Anton Vyatkin <toni@altlinux.org> 5.1.0-alt1
- New version 5.1.0.

* Sun Jun 01 2025 Anton Vyatkin <toni@altlinux.org> 5.0.1-alt1
- New version 5.0.1.

* Thu Feb 27 2025 Anton Vyatkin <toni@altlinux.org> 4.6.3-alt1
- Initial build for Sisyphus.
