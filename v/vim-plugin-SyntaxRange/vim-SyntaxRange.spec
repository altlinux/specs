%define		reponame vim-SyntaxRange
Name:           vim-plugin-SyntaxRange 
Summary:        Use multiple vim syntax highlighters based on context
# TODO more thorough version from git
Version:        1.02
Release:        alt1
License:        MIT
Group:          Editors
URL:            https://github.com/inkarkat/vim-SyntaxRange

Source:         %reponame-%version.tar.gz
BuildRequires(pre): rpm-build-vim
BuildArch:      noarch

%description
This plugin provides commands and functions to set up regions in the current
buffer that either use a syntax different from the buffer's 'filetype', or
completely ignore the syntax.

%prep
%setup -n %reponame-%version

%install
mkdir -p %buildroot%vim_runtime_dir
cp -a [a-u]* %buildroot%vim_runtime_dir

%files
%doc README*
%vim_runtime_dir/*/*

%changelog
* Mon May 20 2024 Fr. Br. George <george@altlinux.org> 1.02-alt1
- Initial build for ALT
