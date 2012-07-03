Name: vim-plugin-twiki-syntax
%define pname vim-twiki
Version: 0.7
Release: alt3.svn21
URL: http://vim-twiki.sourceforge.net/
License: GPL
Group: Editors
Source: http://heanet.dl.sourceforge.net/sourceforge/%pname/%pname-%version.tar.gz
Source1: ftdetect.vim

BuildArch: noarch
Packager: Fr. Br. George <george@altlinux.ru>

Summary: TWiki syntax highlighting plugin for VIM
Group: Editors
Requires: %_bindir/vim
%description
TWiki syntax highlighting/filetype plugin for VIM.

%prep
%setup -c -q

%build

%install
install -D syntax/twiki.vim %buildroot%_datadir/vim/syntax/twiki.vim
install -D ftplugin/twiki.vim %buildroot%_datadir/vim/ftplugin/twiki.vim
install -D %SOURCE1 %buildroot%_datadir/vim/ftdetect/twiki.vim

%files
%_datadir/vim/syntax/*
%_datadir/vim/ftplugin/*
%_datadir/vim/ftdetect/*
%doc README

%changelog
* Wed Jul 27 2011 Fr. Br. George <george@altlinux.ru> 0.7-alt3.svn21
- Update to SVN r21

* Fri Jul 10 2009 Fr. Br. George <george@altlinux.ru> 0.7-alt2
- FTDetect script added

* Wed Feb 07 2007 Fr. Br. George <george@altlinux.ru> 0.7-alt1
- Initial build

