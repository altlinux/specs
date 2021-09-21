Name:       yospellchecker
Version:    0.0
Release:    alt1
License:    GPLv3+
Summary:    Vim API and plugin for restoring Russian YO letter in place of YE
Group:      Text tools
Source:     %name-%version.tar
URL:        https://github.com/zerro009/yospellchecker
BuildArch:  noarch

%description
%summary

%prep
%setup

%install
install -d %buildroot%_datadir/vim/vimfiles/plugin/%name
install main.vim %buildroot%_datadir/vim/vimfiles/plugin/%name.vim
install *.py *.txt %buildroot%_datadir/vim/vimfiles/plugin/%name/

%files
%_datadir/vim/vimfiles/plugin/%{name}*


%changelog
* Tue Aug 17 2021 Fr. Br. George <george@altlinux.ru> 0.0-alt1
- Initial build for ALT
