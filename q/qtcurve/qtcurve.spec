%def_enable qt4

Name: qtcurve
Version: 1.6.3
Release: alt1.1
Serial: 1

Summary: QtCurve (KDE and GTK2 style)
License: GPLv2
Group: Graphical desktop/Other
Url: http://www.kde-look.org/content/show.php?content=40492

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source: %name-%version.tar
Patch1: QtCurve-Gtk2-1.0.0-alt-qtrc.patch
Patch2: QtCurve-Gtk2-0.62.4-alt-icons.patch
Patch3: QtCurve-KDE3-1.0.2-alt-link-fixes.patch
Patch4: qtcurve-1.6.3-alt-glib2.patch

BuildRequires(pre): kde-common-devel rpm-macros-qt3 rpm-macros-qt4
BuildPreReq: gcc-c++ libgtk+2-devel libqt3-devel kde4libs-devel
BuildPreReq: kde4base-workspace-devel

%description
This is a set of widget styles for KDE and GTK2 based apps.
The underlying code is based upon Blue/FreeCurve - however,
*extensive* modifications have been made.

%package -n kde4-styles-%name
Group: Graphical desktop/KDE
Summary: QtCurve style for KDE 4

%description -n kde4-styles-%name
This is a set of widget styles for KDE 4

%package -n qt4-styles-%name
Group: Graphical desktop/KDE
Summary: QtCurve style for Qt4
Conflicts: kde4-styles-%name

%description -n qt4-styles-%name
This is a set of widget styles for Qt4

%package -n qt3-styles-%name
Group: Graphical desktop/KDE
Summary: QtCurve style for Qt3
Obsoletes: kde-styles-%name < 1.1.0-alt1
Provides: kde-styles-%name = %version-%release

%description -n qt3-styles-%name
This is a set of widget styles for Qt3

%package -n gtk2-themes-%name
Summary: The QtCurve engine for GTK2
Group: Graphical desktop/GNOME
Provides: gtk-engines-%name
Obsoletes: gtk-engines-%name < %version-%release gtk1-themes-%name < %version-%release

%description -n gtk2-themes-%name
The QtCurve engine for GTK2

%prep
%setup
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1

%build
pushd QtCurve-KDE4
%if_enabled qt4
# Qt4
%K4cmake -DQTC_QT_ONLY:BOOL=1
%K4make
mv BUILD-%_target_platform{,-qt}
%endif
# KDE4
%K4build
popd

mkdir QtCurve-KDE3/build
pushd QtCurve-KDE3/build
# Qt3
cmake .. \
        -DCMAKE_C_FLAGS:STRING="%optflags" \
        -DCMAKE_CXX_FLAGS:STRING="%optflags"
%make_build VERBOSE=1
popd

mkdir QtCurve-Gtk2/build
pushd QtCurve-Gtk2/build
# Gtk2
cmake .. \
        -DCMAKE_C_FLAGS:STRING="%optflags"
%make_build VERBOSE=1
popd

%install
%makeinstall_std -C QtCurve-KDE4/BUILD-%_target_platform/
%makeinstall_std -C QtCurve-KDE3/build/
%makeinstall_std -C QtCurve-Gtk2/build/

%if_enabled qt4
install -pD -m644 QtCurve-KDE4/BUILD-%_target_platform-qt/style/%name.so %buildroot%_qt4dir/plugins/styles/%name.so
%endif

%files -n kde4-styles-%name
%_K4lib/*.so
%_K4plug/styles/*.so
%_K4apps/QtCurve
%_K4apps/kstyle/themes/*.themerc
%_K4apps/color-schemes/*.colors
%_K4apps/kwin/*.desktop
%doc QtCurve-KDE4/AUTHORS QtCurve-KDE4/ChangeLog QtCurve-KDE4/README QtCurve-KDE4/TODO

%if_enabled qt4
%files -n qt4-styles-%name
%dir %_qt4dir/plugins/styles/
%_qt4dir/plugins/styles/%name.so
%doc QtCurve-KDE4/AUTHORS QtCurve-KDE4/ChangeLog QtCurve-KDE4/README QtCurve-KDE4/TODO
%endif

%files -n qt3-styles-%name
%dir %_qt3dir/plugins/styles/
%_qt3dir/plugins/styles/%name.so
%doc QtCurve-KDE3/AUTHORS QtCurve-KDE3/ChangeLog QtCurve-KDE3/README QtCurve-KDE3/TODO

%files -n gtk2-themes-%name
%_libdir/gtk-2.0/*/engines/lib%name.so*
%dir %_datadir/themes/QtCurve
%_datadir/themes/QtCurve/gtk-2.0
%dir %_datadir/themes/QtCurve/mozilla
%_datadir/themes/QtCurve/mozilla/preferences-rev.xml
%_datadir/themes/QtCurve/mozilla/QtCurve.css
%_datadir/themes/QtCurve/mozilla/QtCurve-KDEButtonOrder.css
%doc QtCurve-Gtk2/AUTHORS QtCurve-Gtk2/ChangeLog QtCurve-Gtk2/README QtCurve-Gtk2/TODO


%changelog
* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.6.3-alt1.1
- Fixed build

* Sun Sep 26 2010 Andrey Rahmatullin <wrar@altlinux.org> 1:1.6.3-alt1
- 1.6.3 (KDE4 & Gtk2), 1.6.2 (KDE3)

* Fri Sep 24 2010 Andrey Rahmatullin <wrar@altlinux.org> 1:1.6.2-alt1
- 1.6.2 (KDE4 & Gtk2), 1.6.1 (KDE3)

* Wed Sep 15 2010 Andrey Rahmatullin <wrar@altlinux.org> 1:1.6.1-alt1
- 1.6.1 (KDE4 & Gtk2), 1.6.0 (KDE3)

* Mon Sep 13 2010 Andrey Rahmatullin <wrar@altlinux.org> 1:1.6.0-alt1
- 1.6.0

* Wed Jul 21 2010 Andrey Rahmatullin <wrar@altlinux.org> 1:1.5.2-alt1
- 1.5.2 (KDE4 & Gtk2), 1.5.0 (KDE3)

* Mon Jul 12 2010 Andrey Rahmatullin <wrar@altlinux.org> 1:1.5.1-alt1
- 1.5.1 (KDE4 & Gtk2), 1.5.0 (KDE3)

* Tue Jun 29 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.5.0-alt1
- 1.5.0

* Thu May 27 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.4.2-alt1
- 1.4.2 (KDE4), 1.4.1 (KDE3 & Gtk2)

* Sat May 15 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.4.0-alt1
- 1.4.0

* Tue Apr 13 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.3.0-alt1
- 1.3.0

* Fri Mar 19 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.2.0-alt1
- 1.2.0

* Thu Feb 25 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.1.0-alt1
- 1.1.0

* Fri Feb 05 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.0.2-alt2
- link the kde3 style plugin with -lkdecore
- add qt3-only subpackage

* Mon Feb 01 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.0.2-alt1
- 1.0.2 (KDE4 & Gtk2), 1.0.1 (KDE3)

* Wed Jan 13 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.0.1-alt1
- 1.0.1 (KDE4 & Gtk2), 1.0.0 (KDE3)

* Mon Oct 19 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.69.2-alt1
- 0.69.2 (KDE4 & Gtk2), 0.69.1 (KDE3)
- re-enable qt4-only subpackage

* Fri Oct 09 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.69.0-alt1
- 0.69.0 (closes: #21828)
- disable qt4-only subpackage

* Thu Sep 17 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.68.1-alt1
- 0.68.1

* Wed Sep 02 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.68.0-alt1
- 0.68.0

* Wed Aug 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.67.6-alt1
- 0.67.6 (KDE4), 0.67.5 (Gtk2), 0.67.3 (KDE3)

* Wed Aug 12 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.67.5-alt1
- 0.67.5 (KDE4), 0.67.4 (Gtk2), 0.67.2 (KDE3)

* Tue Aug 11 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.67.4-alt1
- 0.67.4 (KDE4), 0.67.3 (Gtk2), 0.67.1 (KDE3)

* Sat Jul 25 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.67.1-alt1
- 0.67.1 (KDE4 & Gtk2), 0.67.0 (KDE3)

* Tue Jul 21 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.66.1-alt1
- 0.66.1 (KDE4), 0.66.0 (KDE3 & Gtk2)

* Sun Jul 12 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.65.4-alt1
- 0.65.4 (KDE4 & KDE3), 0.65.3 (Gtk2)

* Sun Jul 05 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.65.3-alt1
- 0.65.3

* Thu Jul 02 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.65.2-alt1
- 0.65.2

* Mon Jun 29 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.65.1-alt1
- 0.65.1

* Wed Jun 24 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.65.0-alt1
- 0.65.0
- package qt4-only version

* Mon Jun 15 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.64.2-alt1
- 0.64.2
- use optflags for KDE3 & Gtk2

* Tue Jun 09 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.63.0-alt1
- 0.63.0

* Sun May 24 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:0.62.7-alt1
- 0.62.9 (KDE4), 0.62.7 (KDE3), 0.62.8 (Gtk2)
- build KDE4 window decorations
- package docs

* Tue Mar 31 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.62.6-alt1
- 0.62.6

* Mon Mar 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.62.4-alt1
- 0.62.4

* Sun Mar 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.61.4-alt1
- 0.61.4

* Wed Feb 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:0.60.0-alt1
- 0.60.0

* Thu Oct 23 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.59.7-alt2
- fixed build

* Thu Aug 21 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.59.7-alt1
- 0.59.7

* Sat Jun 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.59.4-alt1
- 0.59.4

* Sun May 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.59.1-alt1
- 0.59.1

* Thu Apr 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.59.0-alt1
- 0.59.0

* Wed Mar 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.58.0-alt1
- 0.58.0

* Fri Mar 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.57.1-alt1
- 0.57.1

* Thu Mar 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.57.0-alt1
- 0.57.0

* Tue Mar 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.56.3-alt1
- 0.56.3

* Thu Feb 28 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.56.2-alt1
- 0.56.2

* Tue Feb 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.56.1-alt1
- 0.56.1:
  + Fix crash when using corner default button indicator and no coloured mouse over
  + Fix for OpenOffice.org blanking combobox text when mouse over arrow

* Mon Feb 25 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.56.0-alt1
- 0.56.0

* Sat Feb 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.55.3-alt2
- new subpackage kde4-styles-%name

* Thu Feb 07 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.55.3-alt1
- 0.55.3

* Sat Jan 26 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.55.2-alt2
- added object-flip-horizontal, object-flip-vertical, object-rotate-left,
  object-rotate-right, x-office-presentation icons KDE3 Gtk2 substitution

* Sun Jan 20 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.55.2-alt0.M40.1
- build for branch 4.0

* Fri Jan 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:0.55.2-alt1
- 0.55.2:
  KDE3:
    1. Add ability to import qtc_*.themerc settings into config dialog.
    2. Lighten dockwidget titlebars.
  Gtk2:
    1. Fix look of disabled entry fields.
    2. Style Gtk2.12 tooltips
    3. Improve look of edit field under firefox3
    4. Fix menubar items for Firefox 3
    5. Use 32x32 as dialog icon size.
    6. Nicer tabs for Firefox 3.
    7. Better (not perfect) scrollbar types for Firefox3.

* Sat Dec 08 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.55.1-alt1
- 0.55.1:
  KDE3:
    1. Only allow coloured selected tabs if tab appearance is set to gradient.
    2. Allow triangular sliders when not rounding.
    3. Fix appearance of flat/raised disabled scrollbar buttons - more consistent with Gtk2 and KDE4
    4. Fix potential infinte loop when elliditiding title string.
    5. Also eliditude vertical titlebars.
  Gtk2:
    1. Only allow coloured selected tabs if tab appearance is set to gradient.
    2. Allow triangular sliders when not rounding.

* Fri Oct 12 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.55.0-alt2
- fixed #13106

* Thu Oct 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.55.0-alt1
- 0.55.0:
  KDE3:
    1. Ability to create custom themes. See Theme details in 'README' file.
    2. Supply a 'Klearlooks' QtCurve theme.
  Gtk2:
    1. Ability to create custom themes. See Theme details in 'README' file.
    2. Fix for 'inactiveHighlight' and KDE's apply colours to non-KDE apps.
  All:
    1. Allow 'flat' lines in scrollbar handles, toolbar handles, toolbar separators, and splitters.
    2. Option for 'X' style checkmarks.
    3. Option to have colour the selcted tab.
    4. Optional diagonal progressbar sripes.
    5. Use alternating dark/light for dashed toolbar handles.
    6. New 'split' style gradient.
    7. Option to specift slider style: plain, round (only when appearance=round), and triangular (plastik-ish)
    8. Modify default style: flat splitter lines, flat slider thumbs, no toolbar separators, triangular slider,
       diagonal progressbar stripes.

* Fri Sep 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:0.52.3-alt2
- rollback to 0.52.3

* Wed Sep 26 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.54.0-alt1
- 0.54.0:
  KDE3:
    1. Converted buildsystem to CMake.
    2. New option 'inactiveHighlight', if set then use a mix of highlight and background colour as highlight for inactive windows/elements.
    3. Set KDE3 colours from Qt4 settings if running under KDE4.
    4. Read in Qt3's inactive palette settings for highlight and highlightedText.
    5. If an inactive palette is set (e.g. via qtconfig), ensure that progress bar text is unaffected.
    6. Remove frames from source/destination labels of kio progress dialogs.
    7. Add gui to set shading option.
    8. Nicer look for selected tab highlight.
  Gtk2:
    1. Converted buildsystem to CMake.
    2. New option 'inactiveHighlight', if set then use a mix of highlight and background colour as highlight for inactive windows/elements.
    3. Fix broken 'Thinner Menuitems' option.
    4. Better code for alternate list view background.
    5. Also read in Qt's inactive palette.
    6. If read a font setting from /etc/qt3/qtrc,
       and there is not font setting in ~/.qt/qtrc - then use the setting from /etc/qt3/qtrc, as opposed to setting a default.
    7. When reading Qt4 settings, also read /etc/xdg/Trolltech.conf
    8. Nicer look for selected tab highlight.
    9. realloc() fix - thanks to 'hoodedone'	    
	   
* Wed Sep 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.53-alt2
- added map_kde_icons.pl

* Mon Sep 10 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.53-alt1
- 0.53:
  KDE3:
    1. Removed 'Shadow buttons' option, and replaced with none/shadow/etch setting - default to 'none'.
    2. Added 'passwordChar' option to set character used for password entries.
    3. Option to have frameless groupboxes - Gtk like.
    4. Add an 'Advanced' tab to config dialog.
    5. Add config item gtkButtonOrder set to 'true' to use Gtk/GNOME button order.
    6. Modified contrast settings to be more varied.
    7. Gradient background of checks and radios, if appearance is not flat/raised.
  Gtk2:
    1. Removed 'Shadow buttons' option, and replaced with none/shadow/etch setting - default to 'none'.
    2. Added 'passwordChar' option to set character used for password entries.
    3. Option to have frameless groupboxes - Gtk like.
    4. Add config item 'gtkButtonOrder' set to 'true' to use Gtk/GNOME button order.
    5. Added config item 'mapKdeIcons' to control whether to map KDE icons or not.
    6. Modified contrast settings to be more varied.
    7. Gradient background of checks and radios, if appearance is not flat/raised.
    8. Create kde-icon map on the fly - allows icon sizes to be read from kdeglobals.
    9. KDE's "apply colours to non-KDE apps" setting seems to mess up the text on progressbars, workaround this.
    10. Read alternate listview colour from KDE settings.
    11. More KDE like framed groupboxes.

* Sun Jul 15 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.52.3-alt1
- 0.52.3:
  KDE3:
    1. Don't lighten border of disabled check/radio buttons.
    2. Lighten trough of disabled slider.
    3. Modify khtml check to also check to see if widget name == "__khtml"
    4. Store khtml widgets in a map, to speed up checking.
    5. Fix shadow on comboboxes.
    6. Draw background of checked menuitem icons as per KDE4.
  Gtk2:
    1. Fix 1st stripe on vertical progress bar.
    2. Fix very small progress bar chunks.
    3. Fix blanked out widgets in tovid.
    4. Fix DeVeDe crash when 'fix parentless dialogs' is enabled.
	 
* Fri Jun 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.52.2-alt1
- 0.52.2:
  1. Fix crash when slider colour == button.

* Thu Jun 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.52.1-alt1
- 0.52.1:
  1. Draw emphasis around menus when not lightening.
  2. Use button colours to border entry fields.
  3. Dont allow scrollbars to be recoloured.
  4. Fix amarok menus.

* Tue Jun 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.52-alt1
- 0.52:
  1. Use 'dull glass' as the default gradient - previous default is now called 'Clean'.
  2. Darken slider mouse over colour if slider is not shaded.
  3. Use thinner slider mouse over sections if slider is not shaded.
  4. Improve look of small V arrows.
  5. Even duller dull glass, but much more useable.
  6. Fix setting of check/radio colour.
  7. Only highlight editable combo arrow when mouse over arrow, not over edit field - more Gtk like.
  8. Added one config file option (no gui):
     gtkScrollViews set to 'true' to have the scrollbars drawn outside of scrollviews. (However, doesn't look very good)
  9. Lighten combo list frame.
  10. Dont round MDI buttons.
  11. Fix opera's MDI buttons within menubars.
  12. Always assume PE_ButtonBevel is enabled - used for QtConfig's colour buttons.

* Mon Jun 11 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.51-alt1
- 0.51:
  1. Changed shading to use HSL colour space. This can be altered by editing
     $XDG_CONFIG_HOME/qtcurvestylerc and setting 'shading=simple' for the previous
     method, or 'shading=hsv' to use HSV.
  2. Add options:
     Border all of menu/toolbars.
     Darker borders.
     'V' arrows.
  3. Fix raised listview headers.
  4. Fix glass style menuitem appearance.
  5. Modifed look of dullglass, looks "softer"
  6. Improve look of plastik mouse-over for non coloured scrollbars.
  7. For disabled buttons, use standard fill but lighten border.
  8. Use darker colours for mouse-over and default button - helps with light colour schemes.
  9. Dont draw sunken panel around checked menuitems.
  10. If the app is a Java app, and its g_get_application_name()!="unknown", then assume
      its a SWT java app - in which case treat as a standard app. For Swing apps some
      functionality is disabled.
  11. Fix tabs in thunderbird.

* Wed May 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.50-alt4
- update QtCurve-Gtk2-0.50-alt-qtrc.patch, thanks Sergey V Turchin

* Tue May 29 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.50-alt3
- set icons size 22 for gtk-dnd and gtk-dialog

* Sun May 27 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.50-alt2
- fixed default icons path

* Fri May 25 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.50-alt1
- 0.50:
  1. Add settings for:
     Fill used slider
     Round menubar item top only
     Menuitem appearance
     Border menuitems
     Progressbar appearance
     Gradient progressbar groove
     Use standard buttons for sidebar buttons
     Check/radio colour
     Plastik style mouse-over
  2. Dont colour menubar items on mouse over if not colouring menubars.
  3. When drawing menubar borders, only draw bottom line.
  4. When drawing toolbar borders, only draw top/bottom or left/right - depending upon orientation.
  5. Draw checks/radios within listviews the same as standard.
  6. Use 'foreground' colour for menu text.

* Wed May 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.49-alt1
- 0.49

* Tue May 01 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.48.5-alt1
- 0.48.5

* Fri Apr 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.48.4-alt1
- 0.48.4

* Fri Feb 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.46.4-alt1
- 0.46.4:
  + KDE:
    1. Only draw gradients if width>0 && height>0
  + Gtk2:
    1. Only draw gradients if width>0 && height>0

* Fri Jan 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.46.3-alt1
- 0.46.3:
  + KDE:
    1. Fix look of flat/raised style menuitems and progressbars.
    2. Fix look of read-only KLineEdits.
  + Gtk2:
    1. Fix look of flat/raised style menuitems and progressbars.
    2. Use pkg-config to obtain Gtk2 libdir.

* Sat Dec 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.46.2-alt1
- 0.46.2:
  + KDE Only:
    1. Remove rgb2Hls() and hls2Rgb() unless using old style shading.
    2. Don't mouse-over disabled tabs!
    3. Fix look of flat style tabs.
  + Gtk2 Only:
    1. Remove rgb2Hls() and hls2Rgb() unless using old style shading.
    2. Use fileno() to obtain file descriptor of FILE * stream.
    3. Fix look of slider grooves for 'flat' appearance.
    4. Fix appearance of checkboxes for 'bevelled' appearance.

* Thu Dec 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.46.1-alt1
- 0.46.1

* Wed Nov 29 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.46-alt1
- 0.46

* Tue Nov 21 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.45.3-alt2
- KDE Only:
  1. Correctly place check and radio buttons.
  2. Improve drawing of very small progress.

* Thu Nov 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.45.3-alt1
- 0.45.3:
  + Gtk2 Only
    1. When determinging background of popup menu for AA'ing, use shade window colour, not button.
    2. Fix for "-1" warnings reported by some users.

* Mon Nov 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.45.2-alt1
- 0.45.2:
  + KDE Only:
    1. Make kaffeine's sidebar buttons consistent when coloured.
    2. Fix look of dvd authoring wizard buttons.
  + Gtk2 Only
    1. Fix coloured menubars.
    2. Fix firefox 2's "stack smashing detected" errors.
    3. Remove ok/Cancel button swapping from QtCurve.css, does not work for firefox 2.x
  
* Tue Oct 31 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.45.1-alt1
- 0.45.1:
  + Both:
    1. Restore pre 0.45 inactive window highlight. Option is still there to re-activate.
  + KDE Only:
    1. Fix dark text appearing on progressbars.
    2. Use KStyle to draw status bar elements - if enabled.
  + Gtk2 Only:
    1. Use listview header settings for listview headers!

* Thu Oct 26 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.45-alt1
- 0.45

* Fri Oct 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.44.3-alt1
- 0.44.3

* Fri Oct 13 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.44.2-alt1
- 0.44.2

* Wed Oct 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.44.1-alt1
- 0.44.1

* Tue Oct 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.44-alt1
- 0.44

* Sat Sep 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.43.2-alt1
- 0.43.2

* Sun Sep 24 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.43-alt1
- 0.43

* Sat Sep 09 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.42.3-alt1
- 0.42.3

* Thu Aug 24 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.42-alt1
- 0.42

* Tue Aug 15 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.41.1-alt2
- rebuild

* Sun Aug 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.41.1-alt1
- 0.41.1

* Tue Jul 25 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.40-alt1
- 0.40

* Thu Jul 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.39.1-alt1
- 0.39.1

* Fri Jun 16 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.38-alt1
- 0.38

* Thu Jun 15 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.37-alt1
- 0.37

* Thu Jun 01 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.36-alt1
- 0.36

* Sat May 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.35.1-alt3
- obsolete subpackage gtk-engines-%name
- new subpackages gtk1-themes-%name, gtk2-themes-%name

* Wed Apr 26 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.35.1-alt2
- fixed build for x86_64

* Sat Apr 22 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.35.1-alt1
- 0.35.1

* Tue Mar 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.34-alt1
- 0.34

* Thu Feb 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.33-alt1
- 0.33

* Fri Feb 10 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.31.1-alt1
- 0.31.1

* Mon Feb 06 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.29.1-alt1
- 0.29.1

* Thu Feb 02 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.28-alt1
- 0.28

* Fri Jan 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.26-alt1
- 0.26

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.25-alt1
- 0.25

* Thu Jan 12 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.24.2-alt1
- 0.24.2

* Fri May 20 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.23.1-alt1
- 0.23.1

* Fri Jan 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.22-alt1.1
- rebuild with libstdc++.so.6

* Wed May 19 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.22-alt1
- new version

* Thu May 13 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.21-alt1
- new version

* Thu Apr 22 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.20-alt1
- new version

* Thu Apr 08 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.18-alt2
- rebuild for gtk+2-2.4

* Mon Apr 05 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.18-alt1
- new version

* Tue Mar 30 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.16-alt3
- add qt3 patch

* Wed Mar 03 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.16-alt2
- rebuild

* Sat Feb 14 2004 Valery Inozemtsev <shrek@altlinux.ru> 0.16-alt1
- initial release
