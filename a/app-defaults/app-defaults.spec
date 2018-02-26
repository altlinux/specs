Name: app-defaults
Version: 0.2.8.5
Release: alt1

Summary: Localized X11 Resources
License: GPL
Group: System/Internationalization
BuildArch: noarch
Packager: Etcskel Development Team <etcskel@packages.altlinux.org>

Source: %name-%version.tar

%define old_list uk uk-cp1251 ru-koi8r ru-cp1251
%define old_provides %(for i in %old_list;do echo -n "%name-$i = %version ";done)
%define old_obsoletes %(for i in %old_list;do echo -n "%name-$i ";done)

%define locales ru_RU.KOI8-R ru_RU.CP1251 uk_UA.CP1251 uk_UA.KOI8-U be_BY.CP1251

Provides: %old_provides
Obsoletes: %old_obsoletes

# Localized font settings for Emacs were removed in 0.2.4.
# This is supported in emacs-21.2-alt14:
Conflicts: emacs-common < 21.2-alt14

# Due to %%_x11x11dir.
BuildPreReq: rpm-build >= 4.0.4-alt42

%description
Localized X11 Resources.

%prep
%setup -q

%install
%makeinstall X11X11DIR=%buildroot%_x11x11dir

:>%name.locales
for l in %locales; do \
    cat >> %name.locales <<EOF
%%lang(${l%%.*}) %%dir %_x11x11dir/$l
%%lang(${l%%.*}) %%dir %_x11x11dir/$l/app-defaults
%%lang(${l%%.*}) %%config(noreplace) %_x11x11dir/$l/app-defaults/*
%%lang(${l%%.*}) %%config(noreplace) %_sysconfdir/X11/Xresources.$l
%%lang(${l%%.*}) %%config(noreplace) %_sysconfdir/X11/Xresources-site.$l

EOF
done

%triggerpostun -- xinitrc < 2.4.5-alt3
[ $2 -gt 0 ] || exit 0
cd %_sysconfdir/X11 || exit 0
if [ ! -f Xresources ]; then
	if [ -f Xresources.rpmsave ]; then
		cp -pf Xresources.rpmsave Xresources
	elif [ -f Xresources.rpmnew ]; then
		cp -pf Xresources.rpmnew Xresources
	fi
fi

%files -f %name.locales
%config(noreplace) %_sysconfdir/X11/Xresources
%config(noreplace) %_sysconfdir/X11/Xresources-site

%changelog
* Thu Nov 20 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2.8.5-alt1
- add *customization: -color to Xresources
  this tells libXt to load *-color app-defaults if possible
  (see http://www.faqs.org/faqs/Xt-FAQ/ section 20)

* Fri May 11 2007 Stanislav Ievlev <inger@altlinux.org> 0.2.8.4-alt1
- Second part of hack for kbs vs. Emacs: 
    xterm will use escape sequence from terminfo database
    remove previous VT100 translations

* Wed Dec 20 2006 Stanislav Ievlev <inger@altlinux.org> 0.2.8.3-alt1
- Remove emacs resources (#10390)
- Remove Xmh,Xditview* resources

* Mon Mar 27 2006 Dmitry V. Levin <ldv@altlinux.org> 0.2.8.2-alt1
- Removed vim resources (#5406).
- Fixed build with X11 in /usr.

* Fri Jun 17 2005 Dmitry V. Levin <ldv@altlinux.org> 0.2.8.1-alt2
- Replaced %%_x11libdir/X11 with %%_x11x11dir.

* Mon Aug 09 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.8.1-alt1
- Added "*VT100.allowC1Printable: true" (#4953).

* Tue Aug 03 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.8-alt1
- Changed default Xcursor theme to "jimmac".

* Wed Jun 09 2004 Dmitry V. Levin <ldv@altlinux.org> 0.2.7-alt1
- Cleaned up and commented out xterm part of the Xresources file.
- Added "*VT100.eightBitInput: false" (#1477).
- Added Xresources-site siteconfig support (#2230).

* Tue Apr 15 2003 Peter Novodvorsky <nidd@altlinux.com> 0.2.6.1-alt1
- Repacked tarball with --owner=root --group=root --mode=a+r,go-w. 
  Thanks to Dmitry V. Levin for a hint.

* Thu Apr 10 2003 Peter Novodvorsky <nidd@altlinux.com> 0.2.6-alt1
- Xresources:
  + added Xcursor.theme.

* Wed Mar 05 2003 Dmitry V. Levin <ldv@altlinux.org> 0.2.5-alt1
- Xresources:
  + replaced Vim*geometry resource with Vim.geometry (raorn).

* Mon Feb 10 2003 Ivan Zakharyaschev <imz@altlinux.ru> 0.2.4-alt1
- Xresources:
  + remove Emacs*font and Emacs.menu.attributeFamily settings;
  + add "Emacs.default.attributefamily: fixed";
- localized Xresources.*: remove font settings for Emacs (which specified 
  fonts with special encodings; correct usage of all available Cyrillic 
  fonts is supported in emacs-21.2-alt14);
- the 2 changes together with emacs-21.2-alt14 fix No. 0000825, 0001681;
- Summary changed (removed the word "russification").

* Mon Dec 02 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2.3-alt1
- Fixed description of TiteInhibit resource,
  thanks to Alexey Voinov for the hint.
- Removed duplicated emacs comments.

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2.2-alt3
- rebuild

* Mon Jun 10 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2.2-alt2
- Removed requires on XFree86 (%_x11x11dir now lives in filesystem).

* Sun Apr 14 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.2.2-alt1
- uk_UA.KOI8-U: s/koi8-ub/koi8-u/g for X font resources (koi8-u is the new
  name used in XFree86-cyr_rfx-fonts-koi8-u-1.1-alt1)
  (resolves \#834 at bugs.altlinux.ru);

* Mon Apr  4 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.2.1-alt1
- s/emacs/Emacs/g: use class instead of simple name (the second part of the
  fix for \#764 at bugs.altlinux.ru).

* Mon Feb 18 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2-alt1
- join all app-defaults into one package
- Added Xresources from xinitrc.

* Sat Mar 17 2001 AEN <aen@logic.ru>
- Xedit removed

* Wed Jan 31 2001 AEN <aen@logic.ru>
- requires : locales-xx removed
- renamed to ru-koi8r

* Thu Jun 22 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 0.1-5mdk
- added requires: locales-xx, and included the specific dirs in the package
- removed file 'Netscape' as it is not translated and may conflict
  with a future netscape-xxxx translation

* Mon Jan 10 2000 AEN <aen@logic.ru> 0.1-ipl4mdk
- Ted.ad changed

* Thu Nov 25 1999 AEN <aen@logic.ru>
- Xman added

* Mon Nov 15 1999 AEN <aen@logic.ru>
- first spec

