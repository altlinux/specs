Name: 	  vim-colorscheme-badwolf
Version:  1.6.0
Release:  alt1

Summary:  A color scheme Bad Wolf for Vim, pieced together by Steve Losh
License:  MIT/X11
Group:    Other
Url: 	  http://stevelosh.com/projects/badwolf/
# VCS:    https://github.com/sjl/badwolf/

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

PreReq: vim-common
BuildPreReq: rpm-build-vim
BuildArch: noarch

%description
A color scheme Bad Wolf for Vim, pieced together by Steve Losh.
Need export TERM=xterm-256color for work.

%prep
%setup

%install
install -Dm 0644 colors/badwolf.vim %buildroot%vim_colors_dir/badwolf.vim

%files
%doc *.markdown
%vim_colors_dir/badwolf.vim

%changelog
* Fri Mar 11 2016 Andrey Cherepanov <cas@altlinux.org> 1.6.0-alt1
- Initial build for ALT Linux
