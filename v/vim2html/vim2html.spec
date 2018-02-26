Name: vim2html
Version: 1.46
Release: alt2

Summary: Vim-editable file converter to HTML
License: GPL
Group: Text tools
URL: http://norlug.org/~chipster/vim2html
BuildArch: noarch

Source0: http://norlug.org/~chipster/download_handler/cat5/%name-%version.tar.gz
Patch0: %name-1.46-alt-vim-home.patch

Requires: /usr/bin/vim vim-common
Requires: tidy

%description
vim2html is a small program that exports any Vim-editable file into
well-formed HTML - simulating a Vim session. Fully supports Vim
colorization (customizable) and Syntax Highlighting. This program
provides an excellent method of presenting your
programs/HTML/scripts/etc. on the web.

%description -l ru_RU.CP1251
vim2html позволяет экспортировать любой текстовый файл в HTML так,
как он выглядел бы в Vim, с учетом цветовых схем и подсветки
синтаксиса. Это очень удобный способ для представления программ, html,
скриптов и т.д. в Сети.

%prep
%setup -q
%patch0 -p1

%install
%__install -d %buildroot{%_bindir,%_mandir/man1}
%__install -p %name %buildroot%_bindir
%__install man/* %buildroot%_mandir/man1

%files
%doc docs/{AUTHORS,ChangeLog,INSTALL,README}
%_bindir/%name
%_mandir/man1/%name.*

%changelog
* Thu May 12 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.46-alt2
- fix path to 2html.vim

* Sat Mar 12 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.46-alt1
- 1.46

* Fri Sep 17 2004 Andrey Rahmatullin <wrar@altlinux.ru> 1.45-alt1
- initial build
