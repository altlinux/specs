%define plugname devicons

Name:    vim-plugin-%plugname
Version: 0.11.0
Release: alt1

Summary: Adds file type icons to Vim plugins such as: NERDTree, vim-airline, CtrlP, unite, Denite, lightline, vim-startify and many more

License: MIT
Group:   Editors
Url:     https://github.com/ryanoasis/vim-devicons

Source: %name-%version.tar

BuildRequires(pre): rpm-build-vim

Requires: %_bindir/vim
Requires: fonts-ttf-fira-code
Requires: fonts-ttf-fira-code-nerd

BuildArch: noarch

%description
%summary.

Features

* Adds filetype glyphs (icons) to various vim plugins.
* Customizable and extendable glyphs settings.
* Supports a wide range of file type extensions.
* Supports popular full filenames, like .gitignore, node_modules, .vimrc, and many more.
* Supports byte order marker (BOM).
* Works with patched fonts, especially Nerd Fonts.

%prep
%setup

%install
mkdir -p %buildroot%vim_runtime_dir
cp -ar doc autoload nerdtree_plugin plugin pythonx rplugin %buildroot%vim_runtime_dir

%files
%doc LICENSE *.md
%doc %vim_runtime_dir/doc/*
%vim_runtime_dir/autoload/*
%vim_runtime_dir/nerdtree_plugin/*
%vim_runtime_dir/plugin/*
%vim_runtime_dir/pythonx/*
%vim_runtime_dir/rplugin/*

%changelog
* Mon Mar 23 2026 Grigory Ustinov <grenka@altlinux.org> 0.11.0-alt1
- Initial build for Sisyphus.
