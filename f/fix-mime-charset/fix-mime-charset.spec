Name: fix-mime-charset
Version: 0.5.3
Release: alt3.1

Summary: Fix incorrect charset information in Content-Type MIME headers of e-mail messages
License: GPL v2
Group: Networking/Mail

Url: http://fix-mime-chr.sourceforge.net
Source: %name-%version.tar.gz
Patch: fix-mime-charset-0.5.3-alt-gcc43.patch
Packager: Michael Shigorin <mike@altlinux.org>

Requires: common-licenses

# Automatically added by buildreq on Sun Oct 05 2008
BuildRequires: gcc-c++

Summary(ru_RU.KOI8-R): Исправляет некорректную кодировку в MIME-заголовках e-mail сообщений
BuildRequires: perl-podlators

%description
Fix-mime-charset automatically detects character sets of email message
and modifies the Content-Type header appropriately.
It can be used as mail filter in mailing lists where users often set
the charset of their messages incorrectly. It processes messages fast and accurately,
ignoring attachments, and correctly interprets transfer-encodings.
None but the Content-Type header is changed.

%description -l ru_RU.KOI8-R
Fix-mime-charset автоматически определяет кодировку почтового сообщения и изменяет
соответствующим образом поле Content-Type  в заголовке.
Может использоваться как фильтр сообщений в списках рассылки, где пользователи
часто неправильно указывают кодировки своих сообщений.
Программа обрабатывает сообщения быстро и аккуратно, игнорируя вложения и корректно
интерпретирует transfer-encodings.
Кроме поля Content-Type ничего не изменяется.

%prep
%setup -n %name-%version
%patch -p1

%build
%configure --enable-enca
%make_build

%install
mkdir -p %buildroot/usr/bin
%makeinstall
mkdir -p %buildroot%_docdir/%name-%version
rm -f COPYING
ln -s %_licensedir/GPL-2 COPYING

%files
%doc ChangeLog INSTALL COPYING README README.koi8r
%_bindir/*
%_man1dir/*

%changelog
* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt3.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Nov 05 2008 Michael Shigorin <mike@altlinux.org> 0.5.3-alt3
- fixed build with gcc 4.3

* Sun Oct 05 2008 Michael Shigorin <mike@altlinux.org> 0.5.3-alt2
- fixed build (BR: gnome-libs-devel really unneeded)
- spec cleanup

* Sun Dec 17 2006 Michael Shigorin <mike@altlinux.org> 0.5.3-alt1
- 0.5.3
- fixed trivial #5107

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.5.2-alt1.1
- Rebuilt with libstdc++.so.6.

* Thu Jan 29 2004 Egor S. Orlov <oes@altlinux.ru> 0.5.2-alt1
- version 5.2

* Mon Dec 01 2003 Egor S. Orlov <oes@altlinux.ru> 0.5.0-alt1
- version 0.5.0

* Mon Sep 22 2003 Egor S. Orlov <oes@altlinux.ru> 0.4.0-alt1
- New version

* Wed Sep 03 2003 Egor S. Orlov <oes@altlinux.ru> 0.3.1-alt0.1
- Version 0.3.1

* Mon Sep 01 2003 Egor S. Orlov <oes@altlinux.ru> 0.3.0-alt0.1
- Version 0.3.0
- Changed description

* Fri Aug 29 2003 Egor S. Orlov <oes@altlinux.ru> 0.2.2-alt0.1
- Version 0.2.2
- Added READMEs

* Tue Aug 26 2003 Egor S. Orlov <oes@altlinux.ru> 0.2.0-alt0.2
- Fixing license link

* Mon Aug 25 2003 Egor S. Orlov <oes@altlinux.ru> 0.2.0-alt0.1
- Initial spec

