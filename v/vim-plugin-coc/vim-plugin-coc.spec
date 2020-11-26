%define _unpackaged_files_terminate_build 1
%define plugname coc
%define coc_version 0.0.78
%define coc_calc_version 2.0.2
%define coc_sh_version 0.6.0

Name: vim-plugin-%plugname
Version: %coc_version
Release: alt1
Summary: Syntax checking hacks for vim
Group: Editors
License: MIT
URL: https://github.com/neoclide/coc.nvim.git
Source: %name-%version.tar.gz
Source1: coc-calc-%version.tar
Source2: coc-sh-%version.tar
Source3: node_modules.tar.gz
Source4: README.ALT
BuildArch: noarch

BuildRequires(pre): rpm-build-vim
BuildRequires(pre): rpm-build-nodejs

Requires: vim-plugin-coc-calc = %coc_calc_version
Requires: vim-plugin-coc-sh = %coc_sh_version

%description
Intellisense engine for Vim8 & Neovim, full
language server protocol support as VSCode

To enable this plugin define "did_coc_loaded" variable somewhere
in your .vimrc file.

#vim-plugin-coc-core
%package -n vim-plugin-coc-core
Group: Editors
Summary: Core for vim-coc-plugin
Requires: node-coc = %coc_version

%description -n vim-plugin-coc-core
Core for vim-coc-plugin

#vim-plugin-coc-calc
%package -n vim-plugin-coc-calc
Version: %coc_calc_version
Group: Editors
Summary: Calculate extension for coc-plugin
Requires: vim-plugin-coc-core = %coc_version
Requires: node-coc-calc = %coc_calc_version

%description -n vim-plugin-coc-calc
Calculate extension for coc-plugin

#vim-plugin-coc-sh
%package -n vim-plugin-coc-sh
Version: %coc_sh_version
Group: Editors
Summary: SH language server extension for coc-plugin
Requires: vim-plugin-coc-core = %coc_version
Requires: node-coc-sh = %coc_sh_version

%description -n vim-plugin-coc-sh
SH language server extension using bash-language-server for coc-plugin

%package -n node-coc
Group: Development/Other
Summary: Syntax checking hacks for vim

%description -n node-coc
coc node module

#node-coc-calc
#https://github.com/weirongxu/coc-calc.git
%package -n node-coc-calc
Version: %coc_calc_version
Group: Development/Other
Summary: Calculate extension for coc-plugin

%description -n node-coc-calc
coc-calc node module

#node-coc-sh
#https://github.com/josa42/coc-sh.git
%package -n node-coc-sh
Version: %coc_sh_version
Group: Development/Other
Summary: SH language server extension coc-plugin
Requires: node-bash-language-server

%description -n node-coc-sh
coc-sh node module

%prep
%setup -T -D -b 0 -a 1 -a 2 -a 3
for coc_plugin in coc-calc coc-sh
do
    mkdir -p ./modules/$coc_plugin
    cp -r ./node_modules ./modules/$coc_plugin/
done

cp -- %SOURCE4 README.ALT
# Change path for ALTLinux
grep -rl '/build/index.js' |xargs sed -i "s|s:root.'/build/index.js'|'%nodejs_sitelib/%plugname/build/index.js'|"
sed -i "s|s:root.'/bin/server.js'|'%nodejs_sitelib/%plugname/bin/server.js'|" autoload/coc/util.vim
sed -i "s|'/bin/server.js'|'%nodejs_sitelib/%plugname/bin/server.js'|" package.json
# Fix activation mechanism for ALTLinux
sed -i '1s/exists/!exists/' plugin/coc.vim

%build
for coc_plugin in coc-calc coc-sh
do
	pushd modules/$coc_plugin
	npm run build
	npm prune --production
	popd
done

%install
mkdir -p %buildroot%vim_doc_dir/
mkdir -p %buildroot%vim_plugin_dir/
mkdir -p %buildroot%vim_autoload_dir
install -p -m644 doc/coc.txt %buildroot%vim_doc_dir/
install -p -m644 plugin/coc.vim %buildroot%vim_plugin_dir/
cp -r autoload/* %buildroot%vim_autoload_dir
mkdir -p %buildroot%nodejs_sitelib/%plugname
mkdir -p %buildroot%nodejs_sitelib/%plugname-calc
mkdir -p %buildroot%nodejs_sitelib/%plugname-sh
cp -a bin build data package.json %buildroot%nodejs_sitelib/%plugname
pushd modules/coc-calc
         cp -a lib LICENSE package.json readme.md %buildroot%nodejs_sitelib/coc-calc
popd
pushd modules/coc-sh
         cp -a lib node_modules snippets package.json LICENSE README.md  %buildroot%nodejs_sitelib/coc-sh
popd

%files -n vim-plugin-coc-core
%doc Readme.md README.ALT
%vim_doc_dir/*
%vim_plugin_dir/*
%vim_autoload_dir/*

%files -n node-coc
%nodejs_sitelib/%plugname

%files -n node-coc-calc
%nodejs_sitelib/%plugname-calc

%files -n node-coc-sh
%nodejs_sitelib/%plugname-sh

%files -n vim-plugin-coc-calc

%files -n vim-plugin-coc-sh

%changelog
* Thu Nov 26 2020 Nikita Obukhov <nickf@altlinux.org> 0.0.78-alt1
- Initial build
