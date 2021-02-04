%define _unpackaged_files_terminate_build 1
%define plugname coc-sh

Name: vim-plugin-%plugname
Version: 0.6.0
Release: alt2

Summary: SH language server extension for coc-plugin
License: MIT
Group: Editors
URL: https://github.com/josa42/coc-sh.git
BuildArch: noarch

Requires: vim-plugin-coc-core
Requires: node-%plugname

Source0: %name-%version.tar
Source1: node_modules.tar

BuildRequires(pre): rpm-build-nodejs

%description
SH language server extension using bash-language-server for coc-plugin

%package -n node-%plugname
Group: Development/Other
Summary: SH language server extension coc-plugin
Requires: node-bash-language-server

%description -n node-%plugname
%plugname node module

%prep
%setup -a 1

%build
npm run build
npm prune --production

%install
mkdir -p %buildroot%nodejs_sitelib/%plugname
cp -a node_modules snippets lib package.json %buildroot%nodejs_sitelib/%plugname

%files -n node-%plugname
%doc LICENSE README.md
%nodejs_sitelib/%plugname

%files

%changelog
* Wed Dec 09 2020 Nikita Obukhov <nickf@altlinux.org> 0.6.0-alt2
- Build plugin from its own src

* Thu Nov 26 2020 Nikita Obukhov <nickf@altlinux.org> 0.6.0-alt1
- Initial build
