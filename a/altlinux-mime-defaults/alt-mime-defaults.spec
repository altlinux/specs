Name: altlinux-mime-defaults
Version: 0.33
Release: alt1

Summary: System-wide MIME preferences.
License: BSD
Group: Graphical desktop/Other

URL: http://altlinux.org/
Source: mimeapps.list
Source1: mimeapps-KDE.list
Source2: defaults-GNOME.list
Source3: defaults-MATE.list
Packager: Igor Vlasenko <viy@altlinux.org>

BuildArch: noarch

%description
System-wide MIME preferences.

%prep

%build

%install
install -D -m 644 %{SOURCE0} %buildroot%_desktopdir/mimeapps.list
install -D -m 644 %{S:1} %buildroot/%_datadir/kde4/applications/kde4/mimeapps.list
install -D -m 644 %{S:2} %buildroot/%_datadir/gnome/applications/defaults.list
install -D -m 644 %{S:3} %buildroot/%_datadir/mate/applications/defaults.list
ln -s kde4/mimeapps.list %buildroot/%_datadir/kde4/applications/mimeapps.list

touch %buildroot/%_desktopdir/defaults.list


%files
#%doc README
%_desktopdir/mimeapps.list
%_datadir/kde4/applications/kde4/mimeapps.list
%_datadir/kde4/applications/mimeapps.list
%_datadir/gnome/applications/defaults.list
%_datadir/mate/applications/defaults.list
%_desktopdir/defaults.list

%changelog
* Thu Jan 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- updated priorities
- fixed bug with applicatons/* (closes: #31725)

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- switched to defaults.list for mate

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- support for MATE

* Thu Oct 29 2015 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- updated priorities

* Mon Dec 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- updated tex priorities
- new release to repair broken p7

* Sat Nov 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- updated priorities

* Wed Dec 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- updated priorities; support for LibreOffice41; deadbeef (closes: 29263)

* Tue Jul 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- placed mplayer wrappers over mplayer (closes: 29068)

* Thu Apr 18 2013 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- updated priorities

* Mon Apr 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- refreshed priorities

* Wed Nov 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- mplayer priority is raised.

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- updated to fresh Sisyphus

* Tue Jun 19 2012 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- added %_datadir/kde4/applications/kde4/mimeapps.list

* Mon Oct 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- added font viewers

* Mon Oct 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2
- packaged lost gnome defaults

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- fixed dolphin priorities

* Sat Jul 30 2011 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- inode/directory priorities

* Tue May 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- KDE priority updates (closes: 25654)

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- priority updates

* Mon May 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- KDE priority updates (kedit, kwrite)

* Thu May 12 2011 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- priority updates

* Wed May 04 2011 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- updated text priorities

* Tue May 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- added gnome priorities defaults.list

* Tue May 03 2011 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- firefox as default http x-scheme-handler

* Wed Apr 27 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- cleaned up kde priorities 

* Tue Apr 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- added kde priorities

* Tue Apr 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- added html, text priorities

* Mon Apr 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- added piorities for a few mimetypes

* Fri Apr 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- added audio/* priorities 

* Thu Apr 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added image/* priorities

* Thu Apr 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- marked as config

* Thu Apr 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added archivers and finance priorities (by cas@)

* Thu Apr 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added jar priorities

* Wed Apr 13 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- Initial build

