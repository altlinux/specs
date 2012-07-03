Name: editmoin
Version: 1.10.1
Release: alt3.1
%define vim_syntax %_datadir/vim/syntax
%define vim_ftplugin %_datadir/vim/ftplugin
%define vim_ftdetect %_datadir/vim/ftdetect
URL: http://labix.org/editmoin
License: GPL
Group:   Networking/Other
Source: http://labix.org/download/%name/%name-%version.tar.gz
Source1: http://heap.altlinux.ru/engine/HowToNamePages/EditMoin
# http://moinmo.in/VimHighlighting?action=AttachFile&do=get&target=moin.vim
Source2: moin.vim
Source3: ftplugin.vim
Source4: ftdetect.vim
Patch: %name-edtitext.patch
Patch1: moin.vim-nohiclear.patch
BuildArch: noarch
Packager: Fr. Br. George <george@altlinux.ru>
BuildPreReq: alternatives
BuildRequires: iconv
Requires: python

Summary: Edit Moin pages remotely with your preferred editor

%description
This program allows you to edit moin (see http://moinmoin.wikiwikiweb.de) pages with your preferred editor. It means you can easily edit your pages, without the usual limitations of most web browsers' text areas.

%package -n vim-plugin-moin-syntax
Summary: MoinMoin syntax highlighting plugin for VIM
Group: Editors
Url: http://moinmoin.wikiwikiweb.de/VimHighlighting
BuildPreReq: alternatives
Requires: %_bindir/vim
%description -n vim-plugin-moin-syntax
MoinMoin syntax highlighting plugin for VIM provided by MoinMoin community

%prep
%setup -q
%patch
#patch1
cp %SOURCE1 README.alt.utf-8
iconv -f utf-8 -t koi8-r < %SOURCE1 > README.alt

%build
echo "%vim_syntax/moin.vim	%vim_syntax/%name.vim	30" > %name.vim.alt
echo "%vim_syntax/moin.vim	%vim_syntax/moinmoin.vim	60" > moinmoin.vim.alt

%install
install -D %name %buildroot%_bindir/%name
install -D  %name.1 %buildroot%_man1dir/%name.1
install -D %SOURCE3 %buildroot%vim_ftplugin/moin.vim
install -D moin1_6.vim %buildroot%vim_syntax/%name.vim
install -D moin1_5.vim %buildroot%vim_syntax/moin15.vim
install -D %name.vim.alt %buildroot%_altdir/%name.vim
#  David O'Callaghan from moinmo.in
install -D %SOURCE2 %buildroot%vim_syntax/moinmoin.vim
install -D moinmoin.vim.alt %buildroot%_altdir/moinmoin.vim
install -D %SOURCE4 %buildroot%vim_ftdetect/moin.vim

%files
%doc README.alt*
%_bindir/*
%vim_syntax/%name.vim
%vim_syntax/moin15.vim
%_altdir/%name.vim
%_man1dir/%name.*

%files -n vim-plugin-moin-syntax
%vim_syntax/moinmoin.vim
%vim_ftplugin/moin.vim
%vim_ftdetect/moin.vim
%_altdir/moinmoin.vim

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.10.1-alt3.1
- Rebuild with Python-2.7

* Sat Dec 19 2009 Fr. Br. George <george@altlinux.ru> 1.10.1-alt3
- Resurrect alternatives file gone while NMUing

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.1-alt2.qa1.1
- Rebuilt with python 2.6

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.10.1-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for vim-plugin-moin-syntax
  * vendor-tag for editmoin
  * postclean-05-filetriggers for spec file

* Fri Jul 10 2009 Fr. Br. George <george@altlinux.ru> 1.10.1-alt2
- FTDetect script added

* Mon Oct 27 2008 Fr. Br. George <george@altlinux.ru> 1.10.1-alt1
- Version up

* Thu Feb 22 2007 Fr. Br. George <george@altlinux.ru> 1.8-alt2
- Add MoinMoin ftplugin

* Fri Dec 15 2006 Fr. Br. George <george@altlinux.ru> 1.8-alt1
- Initial build: the package, external russian help, external syntax file
- Always-text-edit patch applied
- No-highlight-clear patch applied

