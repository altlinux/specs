%define node_module bash-language-server
%define _unpackaged_files_terminate_build 1

Name: node-bash-language-server
Version: 1.17.0
Release: alt1
Summary: Bash language server
Group: Development/Other
License: MIT
Url: https://github.com/bash-lsp/bash-language-server.git
Source: %name-%version.tar.gz
Source1: node_modules.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-macros-nodejs

%description
Bash language server implementation based on Tree Sitter
and its grammar for Bash with explainshell integration

%prep
%setup
tar -xzf %SOURCE1 -C "./server"

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module
cp -rp server/* %buildroot/%nodejs_sitelib/%node_module

%files
%doc server/README.md
%nodejs_sitelib/%node_module/

%changelog
* Tue Nov 17 2020 Nikita Obukhov <nickf@altlinux.org> 1.17.0-alt1
- Initial build

