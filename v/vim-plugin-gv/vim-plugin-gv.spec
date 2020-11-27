%define oname vim-gv

Name: vim-plugin-gv
Version: 0.0+git20201016.486b5c4
Release: alt1

Summary: A git commit browser

License: MIT
Group: Editors
Url: https://github.com/junegunn/gv.vim

VCS: git://git.altlinux.org/gears/v/vim-plugin-gv.git
Source: %name-%version-%release.tar
Source1: %name.watch

Provides: %oname
Requires: vim-plugin-fugitive

BuildRequires: rpm-build-vim
BuildArch: noarch

%description
%summary.

%prep
%setup -n %name-%version-%release

%install
mkdir -p %buildroot%vim_runtime_dir
cp -a plugin %buildroot%vim_runtime_dir

%files
%doc README.md
%vim_runtime_dir/*/*

%changelog
* Fri Nov 27 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.0+git20201016.486b5c4-alt1
- Initial build for ALT Sisyphus.

