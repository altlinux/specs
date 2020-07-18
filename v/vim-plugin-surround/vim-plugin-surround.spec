%define oname vim-surround

Name: vim-plugin-surround
Version: 2.1.0.18.gitf51a26d
Release: alt1

Summary: Vim plugin for easily delete, change and add such surroundings in pairs

License: Vim
Group: Editors
Url: https://github.com/tpope/vim-surround

VCS: git://git.altlinux.org/gears/v/vim-plugin-surround.git
Source: %name-%version-%release.tar
Source1: %name.watch

Provides: %oname

BuildRequires: rpm-build-vim
BuildArch: noarch

%description
Surround.vim is all about "surroundings": parentheses, brackets, quotes, XML
tags, and more. The plugin provides mappings to easily delete, change and add
such surroundings in pairs.

%prep
%setup -n %name-%version-%release

%install
mkdir -p %buildroot%vim_runtime_dir
cp -a doc plugin %buildroot%vim_runtime_dir

%files
%doc README.*
%vim_runtime_dir/*/*

%changelog
* Sat Jul 18 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.1.0.18.gitf51a26d-alt1
- Initial build for ALT Sisyphus.

