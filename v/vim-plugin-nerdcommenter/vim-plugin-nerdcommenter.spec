%define plugname nerdcommenter
%define plugver  2.5.0

Name: vim-plugin-%plugname
Version: %plugver
Release: alt1
Summary: A commenter plugin for the editor Vim
Group: Editors

License: WTFPL
Url: https://github.com/scrooloose/nerdcommenter
Source0: %plugname-%version.tar
Source1: WTFPL

BuildRequires(pre): rpm-build-vim

Requires: %_bindir/vim

BuildArch: noarch

%description
Comment functions so powerful -- no comment necessary.

%prep
%setup -n %plugname-%version
cp %SOURCE1 .

%install
mkdir -p %buildroot%vim_runtime_dir
cp -ar doc plugin %buildroot%vim_runtime_dir

%postun
rm %vim_runtime_dir/doc/tags

%files
%doc README.md
%doc WTFPL
%doc %vim_runtime_dir/doc/*
%vim_runtime_dir/plugin/*

%changelog
* Thu Mar 16 2017 Mikhail Gordeev <obirvalger@altlinux.org> 2.5.0-alt1
- first build for ALT Linux
