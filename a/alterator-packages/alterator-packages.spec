%define _altdata_dir %_datadir/alterator

Name: alterator-packages
Version: 0.5.4
Release: alt10

Summary: Alterator module for packages installation/removal
License: GPL
Group: System/Configuration/Other

Source0: %name.tar

BuildArch: noarch
BuildRequires: alterator >= 3.1-alt1

Requires: gawk >= 3.1.4-alt2
Requires: apt >= 0.5.15lorg2-alt4
Requires: alterator >= 3.1-alt1

%description
%name is a Alterator's module for packages installation/removal

%prep
%setup -c

%build
make

%install
%makeinstall DESTDIR=%buildroot

%find_lang %name

%files -f %name.lang
%_alterator_backend3dir/*
%_altdata_dir/images/packages
%_altdata_dir/ui/packages
%_altdata_dir/applications/packages.desktop

%changelog
* Fri Sep 30 2011 Lenar Shakirov <snejok@altlinux.ru> 0.5.4-alt10
- quote the backslash symbol, really fix the (ALT: #26199)

* Tue Sep 20 2011 Andrey Cherepanov <cas@altlinux.org> 0.5.4-alt9
- Disable description and changelog of package process (closes: #26199)

* Thu Jan 20 2011 Lenar Shakirov <snejok@altlinux.ru> 0.5.4-alt8
- info-update: check for value of minor-id listbox (closes: #22219)

* Mon Jan 17 2011 Andrey Cherepanov <cas@altlinux.org> 0.5.4-alt7
- Add Ukrainian module name translation (thanks Roman Savochenko)

* Mon Jul 19 2010 Andrey Cherepanov <cas@altlinux.org> 0.5.4-alt6
- use translation database from specspo package (closes: #23787)

* Sun Jan 24 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.4-alt5
- obsolete update/clean_menus macros removed

* Mon Sep 28 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.4-alt4
- redundant width/height popup attributes removed (#21680)
- incomplete search results fixed (#21682)
- made search keyword group unsorted (#21683)
- allow package state change by `enter' hit (#21755)

* Tue Feb 17 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.4-alt3
- backend updated for guile 1.8

* Wed Apr 30 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.4-alt2
- move module to proper category (#15508)

* Tue Apr  8 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.4-alt1
- obsolete widget attributes removed

* Fri Feb 22 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.3-alt1
- rewrote for backend3, ui cleaned up

* Fri Jan 25 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.2-alt14
- rebuilt with recent alterator

* Sun Aug 12 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.2-alt13
- added missing reqs and alterator-specific desktop file, closes \#12483

* Wed May  2 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.2-alt12
- ukrainian translation updated (Serhii Hlodin)

* Mon Apr 16 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.2-alt11
- adopted for use with consolehelper, closes \#11231

* Mon Apr 16 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.2-alt10
- fixed empty sources.list.d handling
- fixed desktop entry

* Fri Mar 23 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.2-alt8
- redo REs in apt-pipe status parsing, closes \#11197

* Thu Mar 22 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.2-alt7
- fixed quoting for a-mailbox-send, closes \#10930

* Thu Jan 11 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.2-alt6
- dbus replaced with alterator's own message sender, everywhere
- get rid of obsolete woo-extract-name
- ui tweaks

* Fri Dec 29 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.2-alt5
- dbus replaced with alterator's own message sender

* Fri Dec 22 2006 Stanislav Ievlev <inger@altlinux.org> 0.5.2-alt4
- replace obsoleted woo-read-names with woo-list-names

* Fri Dec 22 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.2-alt3
- fixed build with recent alterator

* Fri Dec  1 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.2-alt2
- fixed tree breakage on empty content
- ensure to shut up apt-pipe when leaving

* Thu Nov 30 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.2-alt1
- sync'd with recent alterator

* Tue Nov 21 2006 Stanislav Ievlev <inger@altlinux.org> 0.5.1-alt3
- replace string-starts-with? with string-prefix?
- replace sure-string with ->string

* Tue Nov 07 2006 Stanislav Ievlev <inger@altlinux.org> 0.5.1-alt2
- update for new alterator, minor code improvements

* Wed Jun 14 2006 Anton Farygin <rider@altlinux.ru> 0.5.1-alt1
- updated for new alterator

* Fri May 26 2006 Anton Farygin <rider@altlinux.ru> 0.5-alt1
- updated for new alterator

* Tue Mar 14 2006 Stanislav Ievlev <inger@altlinux.org> 0.5-alt0.1
- first test build for new alterator

* Fri Oct 21 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt4
- search mode fixes

* Thu Oct 20 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt3
- icons added

* Fri Oct 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt2
- trnslations fixed

* Wed Oct 12 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4-alt1
- packages sources tab added

* Fri Sep  2 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt6
- help updated (kirill@)
- ui tweaks

* Tue Aug 30 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt5
- ui improvements (zerg@)
- fixed backend bug with harmful `dbus-send' buffering

* Fri Aug 19 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt4
- ukrainian translation added

* Mon Aug  8 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt3
- sync'd with recent (2.0-alt0.1) alterator's core
- hide 'profile' view when no profile data exists
- splash screens during slow operations added

* Tue Aug  2 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt2
- ui tweaks

* Mon Aug  1 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3-alt1
- search added

* Tue Jul 19 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt4
- sync'd with recent (1.99-alt47) alterator's core

* Mon Jul 18 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt3
- added 'update' command & ui
- help updated

* Thu Jul 14 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt2
- help added

* Wed Jul 13 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt1
- standalone version
- full profile group removal, #7284

* Thu Jul  7 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.9
- sync'd with recent (1.99-alt41) alterator's core: 
  + layout fixed to use relative size quantifiers
  + some hacks adopted to new version (inger@)
  + fixed map (inger@)

* Fri Jul  1 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.8
- installation of predefined set of packages added

* Thu Jun 30 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.7
- undo/redo functions added

* Mon Jun 27 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.6
- 'upgradable' group added
- 'error' dialog added
- 'install progress' dialog unified
- 'legend' area extended

* Wed Jun 22 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.5
- bugs fixed:
  + cdrom identity
  + shut down apt-pipe at exit

* Mon Jun 20 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.4
- backend improvements
- added 'Insert CDROM...' dialog

* Tue Jun  7 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.3
- added mininstall for use from other modules
- sync'd with recent alterator
 
* Fri Jun  3 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.2
- added 'pending changes' view
- ui layout changes

* Tue May 31 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt0.1
- sync'd with alterator's changes

* Thu May 26 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.3
- progress substep merged into main step

* Mon May 23 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.2
- fixed: #6867, #6897
- required/freed disk space indication fixed
- russian translation added, incomplete

* Mon May 16 2005 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt0.1
- Initial build.
