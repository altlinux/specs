Name:	vim-plugin-moin-syntax
Version: 2008.01.27
Release: alt1
BuildArch: noarch
Source: moin.vim
Group: Editors
URL: http://moinmo.in/VimHighlighting
Summary: Syntax highlighting for editing MoinMoin contents with vim
License: GPLv2
Requires: vim-common

%description
Syntax highlighting for editing MoinMoin contents with vim

%prep

%build
echo 'au BufNewFile,BufRead *.moini			setf moin' > ftdetect.vim

%install
install -D %SOURCE0 %buildroot%_datadir/vim/syntax/moin.vim
install -D ftdetect.vim %buildroot%_datadir/vim/ftdetect/moin.vim

%files
%_datadir/vim/*/*


%changelog
* Wed Sep 09 2020 Fr. Br. George <george@altlinux.ru> 2008.01.27-alt1
- Tear out from editmoin package
