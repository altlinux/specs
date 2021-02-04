%define _unpackaged_files_terminate_build 1
%define plugname coc-calc

Name: vim-plugin-%plugname
Version: 2.0.2
Release: alt2

Summary: Calculate extension for coc-plugin
License: MIT
Group: Editors
URL: https://github.com/weirongxu/coc-calc.git
BuildArch: noarch

Requires: vim-plugin-coc-core
Requires: node-%plugname

Source0: %name-%version.tar
Source1: node_modules.tar

BuildRequires(pre): rpm-build-nodejs

%description
Calculate extension for coc-plugin

%package -n node-%plugname
Group: Development/Other
Summary: Calculate extension for coc-plugin

%description -n node-%plugname
%plugname node module

%prep
%setup -a 1

%build
npm run build
npm prune --production

%install
mkdir -p %buildroot%nodejs_sitelib/%plugname
cp -a lib package.json %buildroot%nodejs_sitelib/%plugname

%files -n node-%plugname
%doc LICENSE readme.md
%nodejs_sitelib/%plugname

%files 

%changelog
* Wed Dec 09 2020 Nikita Obukhov <nickf@altlinux.org> 2.0.2-alt2
- Build plugin from its own src

* Thu Nov 26 2020 Nikita Obukhov <nickf@altlinux.org> 2.0.2-alt1
- Initial build
