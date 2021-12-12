%define oname vim-fugitive

Name: vim-plugin-fugitive
Version: 3.6
Release: alt1

Summary: A Git wrapper for Vim

License: Vim
Group: Editors
Url: https://github.com/tpope/vim-fugitive

VCS: git://git.altlinux.org/gears/v/vim-plugin-fugitive.git
Source: %oname-%version.tar
Source1: %name.watch

Provides: %oname
Requires: git-core curl

BuildRequires: rpm-build-vim
BuildArch: noarch

%description
%summary.

For more information, see `:help fugitive`.

%prep
%setup -n %oname-%version

%install
mkdir -p %buildroot%vim_runtime_dir
cp -a autoload doc ftdetect plugin syntax %buildroot%vim_runtime_dir

%files
%vim_runtime_dir/*/*

%changelog
* Sun Dec 12 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.6-alt1
- Updated to v3.6.

* Thu Sep 02 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.4-alt1
- Updated to v3.4.

* Sat Apr 17 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.3-alt1
- Updated to v3.3.
- Did not pack README.markdown.

* Thu Jul 09 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 3.2-alt1
- Initial build for ALT Sisyphus.

