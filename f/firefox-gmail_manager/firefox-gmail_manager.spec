# SPEC file for Gmail Manager extension

%define rname	gmail_manager
%define version 0.6.4.5
%define release alt1
%define cid 	\{582195F5-92E7-40a0-A127-DB71295901D7\}
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	%version
Release:	%release

Summary:	Gmail Manager plugin for Firefox
Summary(ru_RU.UTF-8):	расширение Gmail Manager для Firefox

License:	%mpl 1.1 / %gpl2plus / %lgpl2plus
Group:		Networking/WWW
#URL:		http://www.longfocus.com/firefox/gmanager
URL:		https://addons.mozilla.org/firefox/1320/
BuildArch:	noarch

Source0:	gmail_manager-%version.xpi
Source1:	new-mail.wav

Packager:       Nikolay A. Fetisov <naf@altlinux.ru>

BuildRequires(pre): rpm-build-firefox rpm-build-licenses
BuildRequires:  unzip

%description
Gmail Manager extension for Firefox browser allows you to manage
multiple Gmail accounts and receive  new mail notifications.  It
displays your  account details including  unread messages, saved
drafts, spam messages, labels with new mail, space used, and new
mail snippets.

%description -l ru_RU.UTF-8
Расширение Gmail Manager для  Firefox позволяет управлять несколькими
учётными записями  Gmail  и  получать уведомления о новых сообщениях.
Оно отображает подробную информацию об учётной записи,  включая число
непрочитанных сообщений, сохранённых черновиков, спама, распределение
новых сообщений по ярлыкам, использованного места, и т.д.

%prep
%setup -c
subst 's#"notifications-sounds-file" type="Char" value=""#"notifications-sounds-file" type="Char" value="%_datadir/sounds/gmail_manager-new-mail.wav"#' components/gmParser.js

%install
mkdir -p --  %buildroot/%ciddir
cp -r -- * %buildroot/%ciddir

# Install default sound
mkdir -p -- %buildroot/%_datadir/sounds/
install -m 0644 %SOURCE1 %buildroot/%_datadir/sounds/gmail_manager-new-mail.wav

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir
%_datadir/sounds/*.wav

%changelog
* Thu Jan 05 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.4.5-alt1
- New version

* Wed Oct 19 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.4.1-alt3
- Rebuild for Firefox 7.0

* Thu Aug 04 2011 Alexey Gladkov <legion@altlinux.ru> 0.6.4.1-alt2
- Update maxVersion according to AMO.

* Sun Apr 17 2011 Alexey Gladkov <legion@altlinux.ru> 0.6.4.1-alt1
- New version (0.6.4.1).

* Wed Jan 27 2010 Alexey Gladkov <legion@altlinux.ru> 0.6-alt1
- New version (0.6).

* Wed Oct 21 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.7.5-alt1
- New version

* Fri Jun 05 2009 Alexey Gladkov <legion@altlinux.ru> 0.5.7.1-alt2
- Rebuild for Firefox 3.5

* Sun Mar 15 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.7.1-alt1
- New version

* Sat Nov 15 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.5-alt2
- Fix build with rpm > 4.0.4-alt96.6 (see #17407)

* Fri Jul 11 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.5-alt1
- New version
- Add sound file for new mail (closes #13963)

* Sat Dec 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.4-alt2
- Rebuild for Firefox 2.0.0.11

* Fri Nov 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.4-alt1
- New version:
  - Fixes checking accounts for the new Gmail version

* Fri Oct 26 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.3-alt6
- Rebuild for Firefox 2.0.0.8

* Fri Aug 03 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.3-alt5
- Rebuild for Firefox 2.0.0.6

* Sat Jul 21 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.3-alt4
- Rebuild for Firefox 2.0.0.5

* Thu Jul 05 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.3-alt3
- Rebuild for Firefox 2.0.0.4

* Wed Mar 14 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.3-alt2
- Rebuild for Firefox 2.0.0.2

* Mon Dec 04 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.3-alt1
- New version
  * Several bugfixes
  * Locales added: uk-UA
- Rebuild for Firefox 2.0
  * Removes obsolete macros
  * Replace 'set_firefox_noarch' macro with 'BuildArch' tag

* Sun Sep 24 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.2-alt1
- New version 0.5.2
  * Several bugfixes
  * Locales added: fa-IR

* Thu Aug 31 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.1-alt1
- New version 0.5.1
  * Added default mail client to the compose prompt window
  * Fixed passwords so they are now stored within Firefox
  * Added he-IL and hr-HR locales
  * Several bug fixes
  
* Wed Aug 09 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.5-alt1
- New version 0.5
  * Numerous improvements and bug fixes

* Wed Jun 28 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.3.6-alt1
- Initial build for ALTLinux Sisyphus
