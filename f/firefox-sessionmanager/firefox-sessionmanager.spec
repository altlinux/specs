# SPEC file for Session Manager extension

%define rname	sessionmanager
%define version 0.7.8.1
%define release alt1
%define cid 	\{1280606b-2510-4fe0-97ef-9b5a22eafe30\}
%define ciddir  %firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	%version
Release:	%release

Summary:	saves and restores the state of all windows
Summary(ru_RU.UTF-8):	сохраняет и восстанавливает состояние всех окон

License:	%mpl 1.1 / %gpl2plus / %lgpl2plus
Group:		Networking/WWW
URL:		http://sessionmanager.mozdev.org/
BuildArch:	noarch

Packager:       Nikolay A. Fetisov <naf@altlinux.ru>

Source0:	session_manager-%version-fx+sm.xpi

BuildRequires(pre):     rpm-build-firefox rpm-build-licenses
BuildRequires:  unzip
Conflicts:	firefox-sessionsaver firefox-TabMixPlus


%description
Session Manager extension for Firefox browser allows you to save
the current state of Firefox  (history, text data,  cookies) and 
return to that state  at any later moment.  Besides the manually 
saved states,  Session Manager  automatically stores the current 
state in case of a crash.

%description -l ru_RU.UTF-8
Расширение 'Session Manager' для Firefox позволяет сохранить текущее
состояние браузера (содержимое окон, историю, текстовые данные, 
cookies) и в дальнейшем в любой момент вернуться к этому состоянию. 
Помимо ручного сохранения, Session Manager автоматически запоминает
текущее состояние на случай восстановления после аварийного завершения
работы браузера.

%prep
%setup -c

%install
mkdir -p -- %buildroot/%ciddir
cp -r -- * %buildroot/%ciddir
touch %buildroot/%ciddir/chrome.manifest

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Sun Feb 05 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.7.8.1-alt1
- New version

* Sat Aug 13 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.7.6.1-alt1
- Rebuild for Firefox 5.0
- New version

* Thu Apr 14 2011 Alexey Gladkov <legion@altlinux.ru> 0.7.5-alt1
- New version

* Wed Oct 21 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.7-alt1
- New version

* Fri Jun 05 2009 Alexey Gladkov <legion@altlinux.ru> 0.6.4.3-alt2
- Rebuild for Firefox 3.5

* Sun Mar 15 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.4.3-alt1
- New version

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.2.6-alt1
- New version

* Thu Jul 10 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.1.13-alt1
- New version

* Sat Dec 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.1.6-alt1
- New version
  * Bug fixes
  * Added Korean localization 

* Fri Nov 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.1.5-alt2
- Rebuild for Firefox 2.0.0.9

* Fri Oct 26 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.1.5-alt1
- New version
  * A lot of feature enhancements, see 
    http://sessionmanager.mozdev.org/history.html for details

* Thu Aug 30 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.6.0.2-alt1
- New version
  * Added code to encrypt session and closed window data
  * Added caching of closed window list
  * Added Autosave functionality
  * Other small improvements and bug fixes

* Fri Aug 03 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.4.1-alt1
- New version
  * Added mk-MK and fi-FI locales.

* Sat Jul 21 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.4-alt1
- New version
  * Added the ability to clear out Session Manager saved session data through the Firefox "Clear Private Data..." menu. 
  * Fix several compatibility issues with Tab Mix Plus
  * cs-CZ locale added.
 
* Thu Jul 05 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.3.4-alt1
- New version
  * zh-CN and pt-BR locales updated

* Mon May 07 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.3.3-alt1
- New version
  * Updated zh-CN, pt-BR, fr-FR locales, added hu-HU, de-DE, sr-Yu, pt-PT locales.
  * Added option to disable crash recovery
  * Several other bugfixes and improvements

* Wed Mar 14 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.5.3.2-alt1
- New version
  * Automatically enables SessionStore and crysh recovery in Firefox settings
  * Added clear list menu option to list menu
  * Updated ru-RU locale, added da-DK, tr-TR and sk-SK locales
  * Some code optimization, interface improvements and bug fixes

* Mon Jan 08 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.5-alt1
- New version
  * full support for Firefox 2.0+
- removes obsolete macros
- replace 'set_firefox_noarch' macro with 'BuildArch' tag

* Sun Sep 24 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.3-alt2
- Rebuild for Firefox 1.5.0.7

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.3-alt1
- New version 0.4.3
-- reduced Session Manager's impact while typing into text fields
-- added a Dutch locale
-- several bug fixes

* Wed Aug 09 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.2-alt2
- Rebuild for Firefox 1.5.0.6

* Tue Jun 20 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.2-alt1
- Rebuild with firefox 1.5.0.4
- New version 0.4.2
  - improved error reporting
  - several bug fixes

* Wed May 24 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.1.1-alt1
- First build for ALT Linux

* Sun May 21 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.4.1.1-alt0
- Initial build
