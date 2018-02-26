
Name: kmail-aegypten-plugins
Version: 1.0
Release: alt7

Group: Graphical desktop/KDE
Summary: The Sphinx project launched by German authorities aims to improve secure email exchange
Url: http://www.gnupg.org/aegypten/index.html
License: GPL

BuildArch: noarch

#Requires:		kdebase >= 3.1
Requires: kdepim-kmail
#Requires:		kdenetwork-kgpgcertmanager >= 3.1
Requires: gnupg >= 1.0.7
Requires: libgcrypt >= 1.1.10
Requires: libksba >= 0.4.5
Requires: gnupg-agent >= 0.9.2
Requires: libgpgme >= 0.3.12
Requires: dirmngr >= 0.4.2
Requires: pinentry >= 0.6.5
#Requires: cryptplug >= 0.3.15

Source0: kmail-pgp-smime.txt.tar.bz2

%description
The Sphinx project launched by German authorities aims to improve secure email
exchange. The projects technological base is the protocol 'TeleTrust e.V.
MailTrusT Version 2'. This includes the standards S/MIME, X.509v3 and others.

Proprietary products are already on the way, but with the project aegypten
there is now also a Free Software solution going to be realized for popular
mail user agents (sphinx-enabling KMail and mutt are essential goals).

%prep
%setup -n kmail-pgp-smime.txt

%files
%doc kmail-pgp-smime.txt.*

%changelog
* Mon Dec 29 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt7
- don't require cryptplug
- recode text to UTF-8

* Tue Apr 06 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt6
- fix requires to libgcrypt

* Wed Feb 04 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt5
- fix requires to libgcrypt0

* Tue Nov 04 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt4
- fix non-latin1 in description

* Thu Mar 13 2003 Sergey V Turchin <zerg@altlinux.ru> 1.0-alt3
- add short help to documentation

* Mon Feb 10 2003 Sergey V Turchin <zerg@altlinux.ru> 1.0-alt2
- fix requires

* Fri Feb 07 2003 Sergey V Turchin <zerg@altlinux.ru> 1.0-alt1
- build for ALT

* Wed Dec 11 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.0-2mdk
- Update from Fabrice MARIE <fabrice-marie-sec@ifrance.com>

* Sat Oct 19 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 1.0-1mdk
- Initial package
