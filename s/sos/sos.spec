%define _localedir %_datadir/locale

Summary: A set of tools to gather troubleshooting information from a system
Name: sos
Version: 4.4
Release: alt2
Packager: Evgeny Sinelnikov <sin@altlinux.ru>

Source: %name-%version.tar
License: GPL-2.0+
Group: System/Configuration/Other

BuildArch: noarch
Url: http://github.com/sosreport/sos

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-sphinx-sphinx-build-symlink
BuildRequires: python3-module-wheel
Requires: libxml2-python
Provides: sysreport = 1.3.15-8

Patch: %name-%version-alt.patch

%filter_from_requires /setuptools._vendor.packaging/d
%py3_requires setuptools

%description
Sos is a set of tools that gathers information about system
hardware and configuration. The information can then be used for
diagnostic purposes and debugging. Sos is commonly used to help
support technicians and developers.

%prep
%setup -q -n %name-%version
%patch -p1

%build
%pyproject_build

%install
%pyproject_install
mkdir -p %buildroot%_sysconfdir/sos/{cleaner,presets.d,extras.d,groups.d}
mkdir -p %buildroot%_sbindir
mv %buildroot%_bindir/* %buildroot%_sbindir
mv %buildroot%_prefix/config/sos.conf %buildroot%_sysconfdir/sos/sos.conf
rm -f %buildroot%_defaultdocdir/%name/{AUTHORS,README.md}
rm -f %buildroot%_datadir/licenses/sos/LICENSE
%find_lang %name

%files -f %name.lang
%doc AUTHORS README.md docs/*
%config(noreplace) %_sysconfdir/sos/sos.conf
%_sbindir/sos
%_sbindir/sosreport
%_sbindir/sos-collector
%dir %_sysconfdir/sos/cleaner
%dir %_sysconfdir/sos/presets.d
%dir %_sysconfdir/sos/extras.d
%dir %_sysconfdir/sos/groups.d
%python3_sitelibdir/sos
%python3_sitelibdir/%{pyproject_distinfo sos}
%_man1dir/sos*.1*
%_man5dir/sos.conf.5*

%changelog
* Thu Jan 19 2023 Andrey Cherepanov <cas@altlinux.org> 4.4-alt2
- Added python3-module-setuptools to requirements.

* Wed Jan 18 2023 Andrey Cherepanov <cas@altlinux.org> 4.4-alt1
- New version (ALT #40681).

* Thu Aug 05 2021 Vitaly Lipatov <lav@altlinux.ru> 3.5-alt9.2
- use python3 sphinx

* Tue Jul 06 2021 Andrey Cherepanov <cas@altlinux.org> 3.5-alt9.1
- FTBFS: fix install using %%__python.

* Fri Nov 22 2019 Dmitry Terekhin <jqt4@altlinux.org> 3.5-alt9
- Replaced Python with Python 2.7 to prepare for
- the transition to Python 3 by default

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 3.5-alt8
- NMU: remove rpm-build-ubt from BR:

* Fri Nov 30 2018 Dmitry Terekhin <jqt4@altlinux.org> 3.5-alt7
- Wrong command "automount -m" changed to "df -a -t autofs"
- and "mount -t autofs" (closes: #35577)

* Thu Jul 05 2018 Dmitry Terekhin <jqt4@altlinux.org> 3.5-alt6
- Do not create special nodes in archive
- Do not change path in symlinks to special nodes to relative

* Fri Jun 08 2018 Dmitry Terekhin <jqt4@altlinux.org> 3.5-alt5
- Change group of result files to wheel and add reading permissions

* Wed Jun 06 2018 Dmitry Terekhin <jqt4@altlinux.org> 3.5-alt4
- Add pam plugin to samba-ad profile

* Fri May 25 2018 Dmitry Terekhin <jqt4@altlinux.org> 3.5-alt3
- Add additional functionality to samba-ad profile

* Tue May 22 2018 Evgeny Sinelnikov <sin@altlinux.org> 3.5-alt2
- Add samba-ad profile
- Fix build scheme from sources

* Fri Apr 13 2018 Dmitry Terekhin <jqt4@altlinux.org> 3.5-alt1
- Update to latest release

* Fri Apr 14 2017 Evgeny Sinelnikov <sin@altlinux.ru> 3.4-alt1
- Update to latest release with unified build tag (aka ubt macros)

* Tue Dec 06 2016 Evgeny Sinelnikov <sin@altlinux.ru> 3.3-alt1
- Update to latest release

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.7.9.1-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.9.1-alt1.1
- Rebuilt with python 2.6

* Thu Feb 14 2008 Denis Medvedev <nbr@altlinux.ru> 1.7.9.1-alt1
 - Initial ALT release, import from RedHat srpms

* Thu Aug 16 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-9.1
- sysreport calls sysreport.legacy if stdin is not a terminal
- backported minor fixes from trunk

* Thu Aug 16 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-9
- corrected a problem causing sometimes exceptions not to be catched when triggered within a thread

* Mon Aug 13 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-8
- added README.rh-upload-core

* Mon Aug 13 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-7
- Resolves: bz251927 SOS errata needs to be respin to match 4.6 code base
- added extras/rh-upload-core script from David Mair <dmair@redhat.com>

* Thu Aug  9 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-6
- more language fixes
- added arabic, italian and french
- package prepared for release
- included sysreport as sysreport.legacy

* Thu Aug  9 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-5
- package obsoletes sysreport and creates a link pointing to sosreport
- added some commands in cluster and process plugins
- fixed html output (wrong links to cmds, thanks streeter)
- process: back down sleep if D state doesn't change
- Resolves: bz241277 Yum Plugin for sos
- Resolves: bz247520 Spelling mistake in sosreport output
- Resolves: bz247531 Feature: plugin to gather initial ramdisk scripts
- Resolves: bz248252 sos to support language localization
- Resolves: bz241282 Make SOS for RHEL 4

* Wed Aug  1 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-4
- catch KeyboardInterrupt when entering sosreport name
- added color output for increased readability
- list was sorted twice, removing latter .sort()

* Tue Jul 31 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-3
- added preliminary problem diagnosis support
- better i18n initialization
- better user messages
- more progressbar fixes
- catch and log python exceptions in report
- use python native commands to create symlinks
- limit concurrent running threads

* Sat Jul 28 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-2
- initial language localization support
- added italian translation

* Mon Jul 16 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-1
- split up command outputs in sub-directories (sos_command/plugin/command instead of sos_command/plugin.command)
- fixed doExitCode() calling thread.wait() instead of join()
- curses menu is disabled by default
- multithreading is enabled by default
- major progressbar changes (now has ETA)
- multithreading fixes
- plugins class descriptions shortened to fix better in --list-plugins
- rpm -Va in plugins/rpm.py sets eta_weight to 200 (plugin 200 longer than other plugins, for ETA calculation)
- beautified command output filenames in makeCommandFilename()

* Thu Jul 12 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.7-0
- curses menu disabled by default (enable with -c)
- sosreport output friendlier to the user (and similar to sysreport)
- smarter plugin listing which also shows options and disable/enabled plugins
- require root permissions only for actual sosreport generation
- fix in -k where option value was treated as string instead of int
- made progressbar wider (60 chars)
- selinux plugin is enabled only if selinux is also enabled on the system
- made some errors less verbose to the user
- made sosreport not copy files pointed by symbolic links (same as sysreport, we don't need %_bindir/X or /sbin/ifup)
- copy links as links (cp -P)
- added plugin get_description() that returns a short decription for the plugin
- guess sosreport name from system's name

* Thu Jul  5 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.6-5
- Yet more fixes to make package Fedora compliant.

* Thu Jul  5 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.6-4
- More fixes to make package Fedora compliant.

* Mon Jul  2 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.6-3
- Other fixes to make package Fedora compliant.

* Mon Jul  2 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.6-2
- Minor fixes.

* Mon Jul  2 2007 Navid Sheikhol-Eslami <navid at redhat dot com> - 1.6-1
- Beautified output of --list-plugins.
- GPL licence is now included in the package.
- added python-devel requirement for building package
- Resolves: bz241282 fixed incompatibility with python from RHEL4

* Fri May 25 2007 Steve Conklin <sconklin at redhat dot com> - 1.5-1
- Bumped version

* Fri May 25 2007 Steve Conklin <sconklin at redhat dot com> - 1.4-2
- Fixed a backtrace on nonexistent file in kernel plugin (thanks, David Robinson)

* Mon Apr 30 2007 Steve Conklin <sconklin at redhat dot com> - 1.4-1
- Fixed an error in option handling
- Forced the file generated by traceroute to not end in .com
- Fixed a problem with manpage
- Added optional traceroute collection to networking plugin
- Added clalance's patch to gather iptables info.
- Fixes to the device-mapper plugin
- Fixed a problem with installation of man page

* Mon Apr 16 2007 Steve Conklin <sconklin at redhat dot com> - 1.3-3
- including patches to fix the following:
- Resolves: bz219745 sosreport needs a man page
- Resolves: bz219667 sosreport does not terminate cleanly on ^C
- Resolves: bz233375 Make SOS flag the situation when running on a fully virtu...
- Resolves: bz234873 rhel5 sos needs to include rpm-va by default
- Resolves: bz219669 sosreport multi-threaded option sometimes fails
- Resolves: bz219671 RFE for sosreport - allow specification of plugins to be run
- Resolves: bz219672 RFE - show progress while sosreport is running
- Resolves: bz219673 Add xen information gathering to sosreport
- Resolves: bz219675 Collect information related to the new driver update model
- Resolves: bz219877 'Cancel' button during option selection only cancels sele...

* Tue Feb 20 2007 John Berninger <jwb at redhat dot com> - 1.3-2
- Add man page

* Fri Dec 15 2006 Steve Conklin <sconklin at redhat dot com> - 1.3-1
- really fixed bz_219654

* Fri Dec 15 2006 Steve Conklin <sconklin at redhat dot com> - 1.2-1
- fixed a build problem

* Fri Dec 15 2006 Steve Conklin <sconklin at redhat dot com> - 1.1-1
- Tighten permissions of tmp directory so only readable by creator bz_219657
- Don't print message 'Problem at path ...'  bz_219654
- Removed useless message bz_219670
- Preserve file modification times bz_219674
- Removed unneeded message about files on copyProhibitedList bz_219712

* Wed Aug 30 2006 Steve Conklin <sconklin at redhat dot com> - 1.0-1
- Seperated upstream and RPM versioning

* Mon Aug 21 2006 Steve Conklin <sconklin at redhat dot com> - 0.1-11
- Code cleanup, fixed a regression in threading

* Mon Aug 14 2006 Steve Conklin <sconklin at redhat dot com> - 0.1-10
- minor bugfixes, added miltithreading option, setup now quiet

* Mon Jul 17 2006 Steve Conklin <sconklin at redhat dot com> - 0.1-9
- migrated to svn on 108.redhat.com, fixed a problem with command output linking in report

* Mon Jun 19 2006 Steve Conklin <sconklin at redhat dot com> - 0.1-6
- Added LICENSE file containing GPL

* Wed May 31 2006 Steve Conklin <sconklin at redhat dot com> - 0.1-5
- Added fixes to network plugin and prepped for Fedora submission

* Wed May 31 2006 John Berninger <jwb at redhat dot com> - 0.1-4
- Reconsolidated subpackages into one package per discussion with sconklin

* Mon May 22 2006 John Berninger <jwb at redhat dot com> - 0.1-3
- Added ftp, ldap, mail, named, samba, squid SOS plugins
- Fixed various errors in kernel and hardware plugins

* Mon May 22 2006 John Benringer <jwb at redhat dot com> - 0.1-2
- split off cluster plugin into subpackage
- correct file payload lists

* Mon May 22 2006 John Berninger <jwb at redhat dot com> - 0.1-1
- initial package build
