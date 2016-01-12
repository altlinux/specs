
Name: rkward
Version: 0.6.3
Release: alt8
Summary: Graphical frontend for R language
Summary(fr):    Interface graphique pour le langage R
Summary(ru_RU.UTF-8):    Интерфейс к языку программирования R
License: GPL-2.0
Group: Sciences/Mathematics

Url: http://rkward.sourceforge.net/
Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: %name-%version.tar.gz
Patch: altlinux-path-libr.so.patch

BuildRequires: R-base
BuildRequires: R-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc-fortran
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: qt4-devel
BuildRequires: libqt4-devel
BuildRequires: kde4libs-devel
BuildRequires: rpm-macros-kde-common-devel
BuildRequires: qt4-designer
Requires: R-base
Requires: kde4base-runtime

%description
RKWard aims to provide an easily extensible, easy to use IDE/GUI for the
R-project. RKWard tries to combine the power of the R-language with the
(relative) ease of use of commercial statistics tools. Long term plans
include integration with office suites

%description -l fr
RKWard fournis un environnement de développement graphique intégré
aisément extensible et simple d'utilisation. RKWard tente de
combiner la puissance du langage R et la (relative) simplicité d'utilisation
des outils statistiques commerciaux. L'objectif à long terme est de voir son
intégration dans les suites bureautiques.

%description -l ru_RU.UTF-8
RKWard интерфейс для языка R-rpoject. Предоставляет функционал IDE/GUI для 
удобной работы с данными. Является приложением KDE4

%prep
%setup
%patch0 -p1

%build
%K4build

%install
%K4install

#it is a same file like in kde4-kate-core
rm %buildroot/%_kde4_prefix/apps/katepart/syntax/r.xml

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/kde4/*.desktop
%_libdir/R/library/*
%_iconsdir/hicolor/*/apps/*
%_K4exec/%name.*
%_K4apps/katepart/syntax/%name.xml
%_K4apps/%name/*
%_K4doc/en/%name/*
%_K4doc/en/rkwardplugins/*
%_K4srv/%name.protocol
%_man1dir/%name.1.*
%_datadir/mime/packages/vnd.%name.r.xml
# missed by find_lang
%_K4datadir/locale/x-test/LC_MESSAGES/rkward.mo

%changelog
* Tue Jan 12 2016 Konstantin Artyushkin <akv@altlinux.org> 0.6.3-alt8
- escaping rpm-mcaroses in chengelog

* Mon Jan 11 2016 Konstantin Artyushkin <akv@altlinux.org> 0.6.3-alt7
- add russian summary and description

* Sun Jan 10 2016 Konstantin Artyushkin <akv@altlinux.org> 0.6.3-alt6
- repack to _kde4_prefix with %%K4build and %%K4install macrosses

* Sat Sep 12 2015 Konstantin Artyushkin <akv@altlinux.org> 0.6.3-alt5
-  rebuild with altlinux qt4 policy 

* Wed Aug 19 2015 Konstantin Artyushkin <akv@altlinux.org> 0.6.3-alt4
-  rebuild with %%find_lang macro 

* Tue Aug 18 2015 Konstantin Artyushkin <akv@altlinux.org> 0.6.3-alt3
-  clean spec 

* Mon Aug 17 2015 Konstantin Artyushkin <akv@altlinux.org> 0.6.3-alt2
- initial build for ALT Linux Sisyphus

* Fri Mar 13 2015 detlef.steuer@gmx.de
- upstream release 0.6.3
- Most important changes:
- New features and improvements
  New element <i18n> for use in plugins' logic section: Provides a translatable string property
  New element <label> for use in plugin help pages: Copies the label-attribute of the given element into the text
  New string property modifier "quoted" to make it easier to quote dynamic strings inside plugins
  Reworked distribution calculator plugins
  Added power analysis plugin (already existed as separate plugin)
  Assume plugin .js files to be in utf-8 encoding; this allows using non-ascii characters in the generated code
  <matrix> element gains options min_rows and min_columns, and the details of fixed_width="true" have been improved
  Add R function rk.set.plugin.status() to allow further customization of loaded plugins (hiding of individual menu entries)
  Pluginmap-management was reworked, partially, and moved to Settings->Manage R packages and plugins
  Provide more detailed information on loaded plugins in rk.list.plugins()
  Allow to override plugins from a different pluginmap (the plugin with the highest specified version is used)
  When the RKWard installation has moved on disk, try to adjust stored .pluginmaps paths, accordingly
  Allow opening RKWard's plugin files (with correct highlighting), and other text files
  More robust control over placement of plugins within a menu
  Restructure layout of CSV-import dialog
  Allow to open (any number of) R script files and rkward://-urls from the command line
  Add command line option --reuse for reusing an existing instance of RKWard
  Be slightly(!) smarter about when (not) to ask for saving workspace on workspace load (e.g. not directly after workspace has been saved)
  Change default in Workspace browser to showing only .GlobalEnv, initially
  Support automatically generating a printable header parameter from most plugin elements
  New Object based convience method for printing headers from plugins
  Implement polyPath()-drawing in RK() device
  Pre-compile the common js code included in every plugin (only when compiled with Qt >= 4.7)
  Improve crash recovery dialog to not prompt again for the same files
  Plugins and in-application help pages can now be fully translated
- Fixes
  Fixed: Hang when trying to select existing directories in file selectors on Windows
  Fixed: <valueslot>s were quirky with respect to showing as invalid
  Fix a hang-on-exit issue
  Fixed: Error when using fix() or trace(...edit=TRUE) with default settings on some systems
  Fixed: Freezes when using RKWard-functionality (such as the RK()-device) from tcl/tk (e.g. Rcmdr)
  Fix several issues of excessive printing of digits in plugins' output
  Fixed potential crash while the "RKWard Debug Messages" window is visible
  Fixed display of file paths containing non-ascii characters in the title bar and startup dialog
  Fixed some erroneous plugin debug messages
* Tue Nov 11 2014 detlef.steuer@gmx.de
- upstream release 0.6.2
- Most important changes:
- In data editor, indicate NAs, explicitly
- Import Stata plugin gains option to convert character encoding.
- New embeddable (minimal) plugin "multi_input" to combine different input elements
- Fixed: Problems starting from paths with spaces in the file name on Windows
- Added command line option --r-executable for switching between several installations of R
- Use a binary wrapper, instead of wrapper shell script for startup on all platforms
- Linear regression plugin gains option to save predicted values
- Fixed some compilation problems
- Add basic support to export plots using tikzDevice
- Fixed: cbind-value of <matrix> element was missing commas
- Fixed: Give a label to an unlabelled toolbar
- Fixed: Adjust to (re-?)named parameters for options("pager")
- Allow plugin UI script code to query R for information
- Fixed: potential crash when a previously installed pluginmap is not longer readable
- Allow to connect <varslot>/<valueslot> source to any property, not just <varselectors>
- New plugin elements <valueselector> and <select>
- New plugin element <valueslot> for selecting arbitrary string values (otherwise almost identical to <varslot>)
- <varslots> can be set to accept the same object several times. Used in scatterplot plugin.
- New R function rk.embed.device() for manually embedding graphics devices in RKWard
- Fixed: R backend would exit immediately, without meaningful error message, if there is an error in .Rprofile (or Rprofile.site)
- Fixed: Installing suggested packages from the package installation dialog was broken
- Fixed: Selecting a mirror via the "R packages" settings page would not work when prompted for package installation form the backend
- Remove support for compiling RKWard in a single process (threaded) variant. This was not used / tested since RKWard 0.5.5
- Shortcuts for the "Run ..." actions have been changed for better cross-platform compatibility
- The script editor's "Run line" and "Run selection" actions have been merged
- Add UI for configuring default graphics device, and embedding of standard graphics devices.
- New RKWard native on-screen device (RK()). This is the default on-screen device in RKWard, now.
- New R function rk.without.plot.history() for turning off plot history, temporarily
- Add command line option --backend-debugger
* Mon Apr  8 2013 detlef.steuer@gmx.de
- Update to R-3.0.0. Note: it works with R-3.0.0 only if compiled against.
  If compiled against an older version, i.e. against 2.15.2 as in 12.3 it
  won't work with a newer version and must be recompiled.
- Update notes from upstream:
--- Version 0.6.1 - Apr-02-2013
- Add option to force-close a graphics window
- Add plugin for subsetting data.frames by rows or columns
- On the Windows platform, add an new (experimental) binary startup wrapper (rkward.exe)
- Revert to building R packages form source on Mac OS X by default (controllable via compile-time option)
- Fixed: lattice plots would not be added to the plot history, correctly, for some versions of lattice
- Fix crash when trying to print, and neither okular, nor kpdf are available
- Added support for loaded namespaces that are not attached to a loaded package
- Pluginmaps can specify their "priority". Pluginmaps with low priority will not be added automatically, when found.
- Pluginmaps can <require> other pluginmaps based on their id (for cross-package inclusion)
- Added new element <dependency_check> for dynamic version checks within a plugin (R and RKWard versions, only, so far)
- Add guard against accidental usage of the standard distributed pluginmaps in a later version of RKWard (installed in parallel)
- Easier (de-)activation of RKWard plugin maps using checkboxes (Settings->Configure RKWard->Plugins)
- Broken or quirky .pluginmap files are reported to the user, completely broken maps are disabled, automatically
- Implement basic dependency handling for plugins / pluginmaps
- Added support for the upcoming R 3.0.0                        TODO: Check for any more regressions, before release
- Added <switch> logic element to switch between several target properties (or fixed values) based on the value of a condition property
- Sort plugin gains option to sort data.frames by more than one column at a time, and options for type conversion
- Add in-application debug message viewer (targetted at (plugin) developers)
- Add setting to customize initial working directory
- Windows only: Add UI-checkbox for R's "internet2"-option
- New functions getString(), getList() and getBoolean() for fetching data in plugin scripts
- Boolean properties now return a numeric, not labelled representation of their value, by default. <checkbox>es should be unaffected.   TODO: when announcing release, link to explanation mail.
- Added <optionset> GUI element for entering a set of options for an arbitrary number of items
- Reduce CPU usage of pluings while idle
- Fix conversion from Numeric to Factor in the data editor
- In the data.frame editor, columns containing invalid values are now highlighted in red
- Fixed: If none of the previous plugin maps could be found on startup, re-add the default
- Added <matrix> GUI element for entering matrix or vector data in plugins
- Improve key handling while editing factor levels in a data.frame
- Added utiltity function rk.flush.output()
- RKWard is now categorized as Science/Math/Numerical Analysis in its .desktop file
- Fixed: Yet another fix for hard-to-read function argument hints
- Fixed: Device history was not working with more recent versions of ggplot2
- Fixed: Option to include suggested packages in install was mis-labelled "install dependencies"
- rk.set.output.html.file() gains argument to allow addition of custom content to the html header
* Fri Nov  2 2012 detlef.steuer@gmx.de
- aj asked for details why a user should update.
- Note: I'm only the packager, not even using this software
- myself. But if you ask: here is upstream's list of improvements:
  New features and improvements
    Preview device windows will display some status information (most importantly, warnings or errors)
    Most plot plugins gain options to control margins and tick label orientation
    Added option for installing packages from source (implicitly enabled on Unixoid platforms)
    Omit comments on missing function calls in dialog code windows (e.g., if prepare() is unused, there's no "## Prepare" in the output either)
    Output markup is now more XHTML compliant and easier to parse
    Also save cursor position, folding, etc. for scripts. Note: Implementation details may be subject to change.
    New function rk.list.labels() to retrieve column labels in a data.frame
    rk.get.label() will now return an empty string ("") instead of NULL, in case no label is assigned
    Do not offer to restore individual removed columns of a data.frame opened for editing
    combined all Wilcoxon/Mann-Whitney-tests in one plugin (from previously two separate plugins)
    Added polyserial/polychoric correlations to correlation matrix plugin
    Added more compression options to the "Save objects as R code" plugin
    Added MacPorts support, see README.MacPorts and bundle build script in the macports folder
    Added dynamically generated table-of-contents menu to output document
    Allow some markup inside <text> elements in plugins, and auto-add breaks only for duplicate newlines.
    Reorganized t-test plugin, and add support for single sample t-tests
    Box plot plugin gains more options for adding means
    Improve keypress handling issues in the R Console, when the cursor or a selection is outside the editable range
    Only install translations which are at least 80%% complete (not counting strings in plugins, which are not yet translatable)
    When asking for workspace file to open, use appropriate file filter
    When configured to ask for workspace to open on startup, don't prompt to save, first
    Simplified the "Sort Data" plugin, and added a help page
    Added GUI support for inspecting the call stack during debugging
    The backend executable is no longer linked against KDE libraries
    Objects, which are not acceptable in a varslot, will still be shown, there, with a warning
    Bugfixes
    Fixed: Entering "0" as propabilities (quantiles) vector in distribution plugins would cause error message
    Fixed: Wrong handling of carriage returns ('\r') in the console window
    Fixed: Spinboxes had wrong initial values
    Fixed: Changed configuration settings would not be saved for script editor
    Fixed: One character missing in R commands on lines longer than 4096 characters
    Fixed: "Next"-button in wizards would remain enabled while settings are missing on a page
    Fixed: Dynamic pages in a wizard would cause a layout bug on the first page
    Fixed: Plot history and graphical menus broken in some cases with R 2.15.0
    Fixed: If the rkward package was loaded in a plain R session, q() and quit() still work
    Fixed: Would not show output of system() commands to stderr on the console (on Unix-like systems)
    Fixed: Function argument hints for the second half of the parameter list would not be quoted, correctly
    Fixed: Failure to open workspaces with non-latin1 filenames from the command line
    Fixed: Saving / restoring workplace layout would fail when saving to directories with unusual characters
    Fixed: potential crash when clicking "Select all updates" in the package installation dialog
    Fixed: potential crash in object name completion under certain conditions
    Fixed: On Windows, detached windows would sometimes be positioned with the menubar outside the upper screen edge
* Wed Oct 31 2012 detlef.steuer@gmx.de
- upstream release 0.6.0
- from a packager view nothing changed besides version number
- details:
- http://sourceforge.net/apps/mediawiki/rkward/index.php?title=News#RKWard_0.6.0_is_available_-_also_on_the_Mac
* Thu Jan 12 2012 detlef.steuer@gmx.de
- directory ownership for rkwardplugins added
* Mon Dec 12 2011 detlef.steuer@gmx.de
- Update to upstream version 0.5.7
- Support for R-2.14.0
- Improvements for add-on handling
- many bug fixes
* Mon Aug 29 2011 detlef.steuer@gmx.de
- Fixed another directory ownership, now builds fine
* Sat Aug 27 2011 aj@suse.de
- Fix spec list by owning a directory.
* Thu Jun 30 2011 detlef.steuer@gmx.de
- Update for upstream new version 0.5.6
  Submitrequest into Factory
* Mon May  9 2011 detlef.steuer@gmx.de
- First submitrequest of rkward into Factory
  rkward  is a kde4 frontend for the statistical software R, which is part of
  11.4 and Factory.
