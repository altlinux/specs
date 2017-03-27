%define plugname nerdtree
%define plugver  5.0.0

Name: vim-plugin-%plugname
Version: %plugver
Release: alt1
Summary: A tree explorer plugin for the editor Vim
Group: Editors

License: WTFPL
Url: http://www.vim.org/scripts/script.php?script_id=1658
Source: %plugname-%version.tar

BuildRequires(pre): rpm-build-vim

Requires: %_bindir/vim

BuildArch: noarch

%description
The NERD tree allows you to explore your filesystem and to open files and
directories. It presents the filesystem to you in the form of a tree which
you manipulate with the keyboard and/or mouse. It also allows you
to perform simple filesystem operations.

%prep
%setup -n %plugname-%version

%install
mkdir -p %buildroot%vim_runtime_dir
cp -ar doc lib autoload nerdtree_plugin plugin syntax %buildroot%vim_runtime_dir

%postun
rm %vim_runtime_dir/doc/tags

%files
%doc README.markdown
%doc %vim_runtime_dir/doc/*
%vim_runtime_dir/nerdtree_plugin/
%vim_runtime_dir/plugin/*
%vim_runtime_dir/syntax/*
%vim_runtime_dir/autoload/*
%vim_runtime_dir/lib/*

%changelog
* Mon Mar 27 2017 Mikhail Gordeev <obirvalger@altlinux.org> 5.0.0-alt1
- first build for ALT Linux
