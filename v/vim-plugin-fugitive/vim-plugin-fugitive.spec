%define oname vim-fugitive

Name: vim-plugin-fugitive
Version: 3.2
Release: alt1

Summary: A Git wrapper for Vim

License: Vim
Group: Editors
Url: https://github.com/tpope/vim-fugitive

VCS: git://git.altlinux.org/gears/v/vim-plugin-fugitive.git
Source: %name-%version-%release.tar
Source1: %name.watch

Provides: %oname
Requires: git-core curl

BuildRequires: rpm-build-vim
BuildArch: noarch

%description
%summary.

%prep
%setup -n %name-%version-%release

%install
mkdir -p %buildroot%vim_runtime_dir
cp -a autoload doc ftdetect plugin syntax %buildroot%vim_runtime_dir

%files
%doc README.*
%vim_runtime_dir/*/*

%changelog
* Thu Jul 09 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.2-alt1
- Initial build for ALT Sisyphus.

