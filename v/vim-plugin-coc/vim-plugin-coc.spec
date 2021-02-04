%define _unpackaged_files_terminate_build 1
%define plugname coc

Name: vim-plugin-%plugname
Version: 0.0.78
Release: alt2

Summary: Vim-plugin-coc metapackage for coc plugins
License: MIT
Group: Editors
URL: https://github.com/neoclide/coc.nvim.git
BuildArch: noarch

Requires: vim-plugin-coc-calc
Requires: vim-plugin-coc-sh

Source0: %name-%version.tar
Source1: README.ALT

BuildRequires(pre): rpm-build-vim
BuildRequires(pre): rpm-build-nodejs

%description
Intellisense engine for Vim8 & Neovim, full
language server protocol support as VSCode

To enable this plugin define "did_coc_loaded" variable somewhere
in your .vimrc file.

#vim-plugin-coc-core
%package -n vim-plugin-coc-core
Summary: Core for vim-coc-plugin
Group: Editors
Requires: node-coc
Requires: npm
%description -n vim-plugin-coc-core
Core for vim-coc-plugin

%package -n node-coc
Summary: Syntax checking hacks for vim
Group: Development/Other

%description -n node-coc
coc node module

%prep
%setup
cp -- %SOURCE1 README.ALT
# Change path for ALTLinux
grep -rl '/build/index.js' |xargs sed -i "s|s:root.'/build/index.js'|'%nodejs_sitelib/%plugname/build/index.js'|"
sed -i "s|s:root.'/bin/server.js'|'%nodejs_sitelib/%plugname/bin/server.js'|" autoload/coc/util.vim
sed -i "s|'/bin/server.js'|'%nodejs_sitelib/%plugname/bin/server.js'|" package.json
# Fix activation mechanism for ALTLinux
sed -i '1s/exists/!exists/' plugin/coc.vim

%build

%install
mkdir -p %buildroot%vim_doc_dir/
mkdir -p %buildroot%vim_plugin_dir/
mkdir -p %buildroot%vim_autoload_dir
install -p -m644 doc/coc.txt %buildroot%vim_doc_dir/
install -p -m644 plugin/coc.vim %buildroot%vim_plugin_dir/
cp -r autoload/* %buildroot%vim_autoload_dir
mkdir -p %buildroot%nodejs_sitelib/%plugname
cp -a bin build data package.json %buildroot%nodejs_sitelib/%plugname

%files -n vim-plugin-coc-core
%doc LICENSE.md Readme.md README.ALT
%vim_doc_dir/*
%vim_plugin_dir/*
%vim_autoload_dir/*

%files -n node-coc
%nodejs_sitelib/%plugname

%files

%changelog
* Thu Feb 04 2021 Nikita Obukhov <nickf@altlinux.org> 0.0.78-alt2
- Split the source package into components

* Thu Nov 26 2020 Nikita Obukhov <nickf@altlinux.org> 0.0.78-alt1
- Initial build
