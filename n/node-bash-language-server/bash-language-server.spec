%define node_module bash-language-server
%define _unpackaged_files_terminate_build 1

Name: node-bash-language-server
Version: 1.17.0
Release: alt2
Summary: Bash language server
Group: Development/Other
License: MIT
Url: https://github.com/bash-lsp/bash-language-server.git
Source0: %name-%version.tar
Source1: node_modules.tar
BuildArch: noarch

BuildRequires(pre): rpm-macros-nodejs

%description
Bash language server implementation based on Tree Sitter
and its grammar for Bash with explainshell integration

%prep
%setup -a1 -n %name-%version/server

%build

%install
mkdir -p %buildroot%nodejs_sitelib/%node_module
cp -rp ./* %buildroot/%nodejs_sitelib/%node_module

%files
%doc README.md
%nodejs_sitelib/%node_module/

%changelog
* Thu Dec 17 2020 Nikita Obukhov <nickf@altlinux.org> 1.17.0-alt2
- Don't archive node_modules
- Change unpacking method
- Remove source code compression
- Move source files to correct directory 

* Tue Nov 17 2020 Nikita Obukhov <nickf@altlinux.org> 1.17.0-alt1
- Initial build

