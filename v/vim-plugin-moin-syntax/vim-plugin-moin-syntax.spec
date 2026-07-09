Name:	vim-plugin-moin-syntax
Version: 2008.01.27
Release: alt2
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
echo 'au BufNewFile,BufRead *.moin			setf moin' > ftdetect.vim

%install
install -D %SOURCE0 %buildroot%_datadir/vim/syntax/moin.vim
install -D ftdetect.vim %buildroot%_datadir/vim/ftdetect/moin.vim

%files
%_datadir/vim/*/*


%changelog
* Thu Jul 09 2026 Fr. Br. George <george@altlinux.org> 2008.01.27-alt2
- Fix typo

* Wed Sep 09 2020 Fr. Br. George <george@altlinux.ru> 2008.01.27-alt1
- Tear out from editmoin package
