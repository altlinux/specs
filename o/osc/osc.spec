#
# spec file for package osc
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define altlinux 1

Name:           osc
Version:        0.134.1
Release:        alt1
License:        GPLv2+
Summary:        openSUSE Build Service Commander
Url:            http://www.gitorious.org/opensuse/osc
Group:          Development/Tools
Source:         %{name}-%{version}.tar.gz
Packager: Denis Pynkin <dans@altlinux.org>

%if !0%{?altlinux}
%if 0%{?mandriva_version} < 02010
BuildRequires:  python-urlgrabber
Requires:       python-urlgrabber
%endif
%endif
BuildRequires:  python-devel
%if 0%{?mandriva_version}
BuildRequires:  python-rpm
Requires:       python-rpm
%else
BuildRequires:  rpm-python
Requires:       rpm-python
%endif
#
%if 0%{?suse_version}
%if 0%{?suse_version} < 1020
BuildRequires:  python-elementtree
Requires:       python-elementtree
%else
BuildRequires:  python-xml
Requires:       python-xml
%endif
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif
%if 0%{?suse_version} > 1000
Recommends:     build >= 2010.05.04
# These packages are needed for "osc add $URL"
Recommends:     obs-service-recompress
Recommends:     obs-service-set_version
Recommends:     obs-service-tar_scm
Recommends:     obs-service-verify_file
Recommends:     obs-service-download_files
Recommends:     obs-service-format_spec_file
Recommends:     obs-service-source_validator
%endif
%endif
%if 0%{?rhel_version} && 0%{?rhel_version} < 600
BuildRequires:  python-elementtree
Requires:       python-elementtree
%endif
%if 0%{?centos_version} && 0%{?centos_version} < 600
BuildRequires:  python-elementtree
Requires:       python-elementtree
%endif

%if !0%{?altlinux}
%if 0%{?suse_version}%{?mandriva_version}
BuildRequires:  python-m2crypto
Requires:       python-m2crypto > 0.19
%else
BuildRequires:  m2crypto
Requires:       m2crypto > 0.19
%endif
%endif

%if 0%{?altlinux}
BuildArch:      noarch
BuildRequires: python-module-m2crypto
BuildRequires: python-module-elementtree
BuildRequires: python-module-urlgrabber
BuildRequires: python-module-rpm
BuildRequires: rpm-build-python
%endif

%{!?python_sitelib: %define python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%description
Commandline client for the openSUSE Build Service.

See http://en.opensuse.org/openSUSE:OSC , as well as
http://en.opensuse.org/openSUSE:Build_Service_Tutorial for a general
introduction.

%prep
cp %SOURCE0 /tmp/
%setup

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
ln -s osc-wrapper.py %{buildroot}/%{_bindir}/osc
mkdir -p %{buildroot}%{_localstatedir}/lib/osc-plugins
install -Dm0644 dist/complete.csh %{buildroot}%{_sysconfdir}/profile.d/osc.csh
install -Dm0644 dist/complete.sh %{buildroot}%{_sysconfdir}/profile.d/osc.sh

%if 0%{?altlinux}
install -Dm0755 dist/osc.complete %{buildroot}%{_datadir}/osc/complete
%else
%if 0%{?suse_version} > 1110
install -Dm0755 dist/osc.complete %{buildroot}%{_prefix}/lib/osc/complete
%else
install -Dm0755 dist/osc.complete %{buildroot}%{_libdir}/osc/complete
%endif
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS README TODO NEWS
%{_bindir}/osc*
%{python_sitelib}/*
%config %{_sysconfdir}/profile.d/osc.csh
%config %{_sysconfdir}/profile.d/osc.sh
%dir %{_localstatedir}/lib/osc-plugins
%{_mandir}/man1/osc.*

%if 0%{?altlinux}
%{_datadir}/osc
%else
%if 0%{?suse_version} > 1110
%{_prefix}/lib/osc
%else
%{_libdir}/osc
%endif
%endif

%changelog
* Mon Apr 02 2012 Denis Pynkin <dans@altlinux.org> 0.134.1-alt1
- New version

* Fri Jan 20 2012 Denis Pynkin <dans@altlinux.org> 0.133.1-alt1
- New version

* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.132.6-alt1.1
- Rebuild with Python-2.7

* Sat Oct 29 2011 Denis Pynkin <dans@altlinux.org> 0.132.6-alt1
- initial build for ALTLinux

* Thu Aug 25 2011 adrian@suse.de
- update to 0.132.6
  * fix crash on removal of local _service file
  * handle both old OBS versions before 2.3
  * fix pgp pubkey parsing
  * show created incident project
* Tue Aug 16 2011 idonmez@novell.com
- Add osc-pubkey-parsing.patch, fix PGP pubkey parsing: base64
  checksum shouldn't be in the key data, upstream commit
  f707e9a22e185098bbea923b7ff8971f19a87991
* Thu Jul  7 2011 adrian@suse.de
- update to 0.132.5
  * fix detection of project wide source service only
  * crash fix on incident creation
* Thu Jun 16 2011 saschpe@suse.de
- spec file cleanup:
  * run spec-cleaner
  * simplified some shell commands
- recommend obs-service-download_files,
  obs-service-format_spec_file, obs-service-source_validator
- remove recommends for osc-source_validator
* Wed Jun 15 2011 adrian@suse.de
- update to 0.132.4
  - fix local package build
* Fri Jun 10 2011 adrian@suse.de
- update to 0.132.3
  - fix a possible crash after commit
* Thu Jun  9 2011 adrian@suse.de
- update to 0.132.2
  - fix broken update after commit with service run
  - fix up -S on unexpanded checkouts
* Wed Jun  8 2011 adrian@suse.de
- update to 0.132.1
  - fix backward compatibility with OBS 2.1 and before
  - meta files and content can be listed now
* Tue Jun  7 2011 adrian@suse.de
- update to 0.132.0
  - rdelete and undelete command requesting now a comment
  - add 'requestbugownership' command for setting the bugowner via request
  [#]
  [#] Features which requires OBS 2.3
  [#]
  - new command "createincident" to create maintenance incidents without a request
  - support to create hidden project on "branch" and "createincident" commands
  - osc waits and updates package after checkin when a source service is used
  - support for the new service file mode for "update" and "checkout" command when
    downloading server side generated files
  - integration for local source services, they will replace the source_validator mechanism
* Fri Apr 29 2011 adrian@suse.de
- update to 0.131.1
  - fixes runtime complaining about missing apiurl config.
- fix wrong links in package description (bnc #690636)
* Wed Apr 27 2011 adrian@suse.de
- update to 0.131
  - new command 'develproject' to print the devel project from the package meta.
  - add blt and rblt commands, aka "buildlogtail" and "remotebuildlogtail" to show
    just the end of a build log (for getting the fail reason faster).
    CHANGE: the --start parameter is now called --offset
  - add "createrequest -a add_group" option to create a group request
  - add "createrequest -a add_me" shortcut
  - add "less" command, doing the same as "osc cat" but with pager
  - fallback to unexpanded diff mode on "osc diff" on merge error.
  - support viewing the commit history of deleted packages
  - show review states on "review list"
  - new source service commands "localrun" and "disabledrun" to generate files without _service: prefix
  - add "request supersede" and "review supersede" to supersede with existing request
  - make it possible to run single source services, even when not specified in _service file.
    (For example for doing a version update without creating a _service file: osc service lr update_source)
  - protect rebuild and abortbuild commands with required "--all" option to mass failures by accident (similar to wipebinaries)
  - "review accept/decline" is trying to change all reviews of a requests, if a specific one is not specified by user
  [#]
  [#] Features which requires OBS 2.3
  [#]
  - "my requests" is doing faster and complete server side lookup now if available
  - "review" command has been extended to handle reviews by project or by package maintainers
  - support for new source service modes: disabled, trylocal and localonly
  - support project wide source services
  - support for armv7hl architecuture. used to denote armv7 + hardfloat binaries
  - add force option to accept requests in review state.
  - add "maintenancerequest" command to request a maintenance incident from maintenance team
  - add "releaserequest" command run a maintenance update release process (for maintenance team only)
  - allow to force the storage of project meta data (to ignore depending repositories for example)
  - "my requests" is showing requests with open reviews also now
* Fri Mar 18 2011 bwiedemann@novell.com
- add Requires: rpm-python (bnc#680986)
* Sat Dec 18 2010 suse-tux@gmx.de
- update to 0.130.1 (bugfix release):
  - don't crash if a file marked as 'A' does not exist (bnc#658664)
  - fixed proxy handling (bnc#657958)
  - fixed repairwc (bnc#657838)
  - fixed build for python2.4
* Mon Dec  6 2010 suse-tux@gmx.de
- update to 0.130
  - new "revert" command to restore the original working copy file (without
    downloading it)
  - rewrote "diff" logic
  - added new "--http-full-debug" option, "--http-debug" filters the
    "Authentication" and "Set-Cookie" header
  - added new "--disabled-cpio-bulk-download" option: disable downloading
    packages as cpio archive from api
  - added new "repairwc" command which tries to repair an inconsistent working
    copy
  - workaround for broken urllib2 in python 2.6.5: wrong credentials lead to an
    infinite recursion
  - support --interactive-review option when running "osc rq list <project>"
  - improved "osc rq show <id> --interactive-review"
  - do_config: added new options --stdin, --prompt, --no-echo:
  - -stdin: read value from stdin
  - -prompt: prompt for a value
  - -no-echo: prompt for a value but don't echo entered characters (for
    instance to enter a passwd)
  - added template support for a submitrequest accept/decline message
  - lots of internal rewrites (new working copy handling etc.)
  - support added for osc search 'perl(Foo::Bar)'
  - New "service" command to run source services locally or trigger a re-run on the server.
  - setlinkrev is setting now the revision to xsrcmd5 by default to avoid later breakage on indirect links by default.
  [#]
  [#] Feature which requires OBS 2.1
  [#]
  - support reliable diff for an accepted request
- osc might fail with the following error:
  Your working copy '.' is in an inconsistent state.
  Please run 'osc repairwc .' (Note this might _remove_
  files from the .osc/ dir). Please check the state
  of the working copy afterwards (via 'osc status .')
  Simply run "osc repairwc" (see README for more information)
* Wed Dec  1 2010 adrian@suse.de
- Add Recommends for osc add $URL functionality
* Mon Aug 30 2010 suse-tux@gmx.de
- release 0.129
* Fri Aug 27 2010 suse-tux@gmx.de
- recommend build >= 2010.05.04
- update to 0.129
  - "dists" command to show the configured default base repos from the server.
  - "review list" command to list open review requests
  - "review add" command to add another reviewer for a request (either user or group)
  - add "buildinfo --prefer-pkgs <dir>" option
  - add "prjresults --hide-disabled" option to hide packages which are disabled/excluded
    in all repos and repos which have only disabled/excluded packages
  - harmonize "api"'s options with curl's options
  - use builtin signature check by default (instead of verifying the signature with "rpm -K...")
  - add "status --show-excluded"  to show all files (except the store dir)
  - new "osc reqmaintainership" command which is a shortcut for
    "osc creq -a add_role USER maintainer PROJECT PACKAGE"
  [#]
  [#] Feature which requires OBS 2.1
  [#]
  - add "osc aggregate --nosources" option
  - add "request clone" command to clone all packages from a given request
  - fixed references into en.opensuse.org to honor the new Wiki structure
* Fri Jul 16 2010 adrian@suse.de
- update to 0.128
  - better default commands selection for editor/pager
  - support "osc rq reopen" to set a request in new state again
  - "osc repos" and "wipebinaries" is checking for local project now
  - "osc getbinaries" works in project dir now
  - support added for SPARC builds
  - support build --oldpackages
  - introduced the "trusted projects"
  - Fixes for default editor, api check on deleterequest call, tempfile leaks, getbinaries source package handling, results command
  [#]
  [#] Feature which require either OBS 2.1 or 2.0.4
  [#]
  - add osc signkey --extend for extending the expiration date of the gpg public key
* Wed Jun  9 2010 adrian@suse.de
- update to 0.127
  - add size limit mode, files can be ignored on checkout or update given a certain size limit.
  - --csv/--format options for results command - using format user can explicitly specify what he wants print
  - osc branch reads project/package in package directory
  - fix creation of package link, when target project has the package via linked project
  - add "osc rq approvenew $PROJECT" command to show and accept all request in new state.
    This makes sense esp. for projects which work with default reviewers before.
  - support external source validator scripts before commiting
  - support request creation with multiple actions
  [#]
  [#] Features which require OBS 2.0 server
  [#]
  - support "osc add http://...", this uses obs source service for downloading a file and verify it via sha256 verifier service
  - add support for CBpreinstall/CBinstall
  - support branch --force to override target
  - support for "unresolvable" state of OBS 2.0
  - support undelete of project or package
  - support for package meta data checkout
* Mon Apr 19 2010 suse-tux@gmx.de
- update to 0.126 (final):
  - added VM autosetup to osc. This requires appropriate OBS version and build script version.
  - enhanced QEMU cross build support with 'armv4l' 'armv5el' 'armv6el' 'armv7el' 'armv8el' 'mips' 'mips64' 'ppc' 'ppc64' 'sh4' arch strings now supported on x86 host
  - suggest git, svn, ... if indicated, after oscerr.NoWorkingCopy
  - "osc cat" & "osc ls" now auto-expands through link.
  - fixed "osc add" after "osc delete".
  - fix "osc patchinfo" command (crashed before)
  - fixed SSL proxy support
  - fixed meta attribute create and set calls
  - osc remotebuildlog supports a buildlogurl
  - Allow --prefer-pkgs to parse repodata
  - new "osc build --no-service" option to skip source service update
  - fix linktobranch apiurl usage
  - "maintained package" search is telling relevant projects now
  * requires OBS 1.7.2 or 2.0
  - added "osc chroot" command
  - fixed #547005 ("osc co could show download progress")
  - added "--interactive" option to "osc request"
  - store commit message so it doesn't get lost on failure
  - added "--cpio-bulk-download" and "--download-api-only" options to "osc build"
  - added "osc localbuildlog" command
  - added "--build-uid uid:gid|caller" option to "osc build" to specify abuild id in chroot
  - verify files using rpm bindings and keys supplied by buildservice
  - added "--exclude-target-project <prj>" option to "osc rq list"
  - added "--message" option to "osc branch"
  - added "osc config" command to set/get/delete a config option
  - added "--binary" and "--baseproject" options to "osc search"
  - added "-o/--offline" and "-l/--preload" options to osc build
  * osc build -l standard i586 foo.spec (to cache all dependencies)
  * osc build -o standard i586 foo.spec (to build without contacting the api)
* Wed Apr  7 2010 suse-tux@gmx.de
- use rpm macros
- mark files in %%%%{_sysconfdir}/profile.d/ as %%%%config
* Sun Mar 21 2010 suse-tux@gmx.de
- fixed rpmlint warning
* Sun Mar 21 2010 suse-tux@gmx.de
- -update to version 0.126 (unstable)
  - suggest git, svn, ... if indicated, after oscerr.NoWorkingCopy
  - "osc cat" & "osc ls" now auto-expands through link.
  - fixed "osc add" after "osc delete".
  - fix "osc patchinfo" command (crashed before)
  - fixed SSL proxy support
  - fixed meta attribute create and set calls
  - osc remotebuildlog supports a buildlogurl
  - Allow --prefer-pkgs to parse repodata
  - new "osc build --no-service" option to skip source service update
  - fix linktobranch apiurl usage
  - "maintained package" search is telling relevant projects now
  * requires OBS 1.7.2 or 2.0
  - added "osc chroot" command
  - fixed #547005 ("osc co could show download progress")
  - added "--interactive" option to "osc request"
  - store commit message so it doesn't get lost on failure
  - added "--cpio-bulk-download" and "--download-api-only" options to "osc build"
  - added "osc localbuildlog" command
  - added "--build-uid uid:gid|caller" option to "osc build" to specify abuild id in chroot
  - verify files using rpm bindings and keys supplied by buildservice
  - added "--exclude-target-project <prj>" option to "osc rq list"
  - added "--message" option to "osc branch"
  - added "osc config" command to set/get/delete a config option
  - added "--binary" and "--baseproject" options to "osc search"
* Mon Feb  1 2010 adrian@suse.de
- update to version 0.125.5
  - rdiff happens against baserev now
  - fixed "osc build --local-package
  - detect a kiwi file on build
  - improved _service file handling
* Wed Jan 27 2010 adrian@suse.de
- update to 0.125.4
  - fix patchinfo command
* Thu Jan 21 2010 adrian@suse.de
- update to 0.125.3
  - fixed attribute handling for final OBS 1.7 api
* Wed Jan 20 2010 adrian@suse.de
- update to osc 0.125.2
  * include ssl proxy fix from Ludwig
* Thu Jan 14 2010 adrian@suse.de
- osc 0.125.1 final
  * when a broken link is encountered automatically switch to last working
  version. use 'osc pull' to repair the broken link.
  * osc my request is showing now also requests from other people target to
  myself
  * new config option 'submitrequest_on_accept_action' to specify a default action
  if a submitrequest has been accepted
  * show scheduler state for each repo with "results" and "prjresults"
* Mon Jan 11 2010 adrian@suse.de
- version 0.125 beta 1
  * the new commands are "pull" and "linktobranch"
  * proxy support via SSL
* Thu Dec 10 2009 adrian@suse.de
- make version 0.124 final. (commit 13d900a64838fb577527d520fa0cf31c09af4cf6)
  Full changelog is inside the NEWS file.
* Wed Dec  9 2009 adrian@suse.de
- first package from git repo (osc 0.124 RC1)
  * fixing product building
* Wed Dec  2 2009 adrian@suse.de
- update to current svn trunk (r9348, osc 0.124 beta 2)
  * build --release option added by Ludwig
* Fri Nov 13 2009 adrian@suse.de
- update to current svn trunk (osc 0.124 beta 1)
  * osc submitrequest is working on project level
  * patchinfo support
* Mon Nov  2 2009 adrian@suse.de
- update to current svn trunk (osc 0.124 alpha 1)
  * Juergens incompatible changes are back, may get removed again for release
  * For maintenance work:
  - new "osc maintained $PACKAGE" command
  - new "osc mbranch $PACKAGE" command
* Fri Oct 16 2009 adrian@suse.de
- update to version 0.123
  - IMPORTANT: ssl certificate checks are actually performed now to
    prevent man-in-the-middle-attacks. python-m2crypto is needed to
    make this work. Certificate checks can be turned off per server
    via 'sslcertck = 0' in .oscrc.
  - 'osc list' option -D now only limits non-'new' requests. In state 'new' all are shown.
  - suggest 'osc list' --bugowner option. Not implemented.
  - implemented 'osc ls .' to take proj/pack name from current directory.
  * Incompatible change: 'osc ls' now defaults to 'osc ls .',
  * Use 'osc ls /' if you really want to list all projects.
  * This is meant as a proof of concept. I intend to generalize this usage of '.'
    for all osc commands. Feedback welcome.
  - 'osc in' to be done. Its usage just prints a suggested zypper command line.
  - Incompatible change: osc se now prints Project Package, instead of Package Project
    for easier copy&paste.
  - fix checkout of packages, which contain not committed files (but uploaded)
  - add signing key management command (osc signkey)
  * shows public part of project key
  * allows (re)creation of a project key
  * allows deletion of a project key
  - support 100%% offline build with "osc build --noinit ...."
* Thu Oct  8 2009 adrian@suse.de
- update to 0.123 svn snapshot
  * new dependency to python-m2crypto for SSL certification check
* Thu Sep 17 2009 suse-tux@gmx.de
- removed "Recommends: rpm-python" which isn't needed anymore
* Tue Sep  8 2009 adrian@suse.de
- update to 0.122
  * added missing code for 'osc sr -l [ID]'
  * allow osc cat with one parameter, if it is a url.
  * make osc getpac really get the package (instead of branch only)!
  * expanded several tabs to spaces.
  * added default project to new getpac and bco subcommand. .oscrc:getpac_default_project = OpenSUSE:Factory
    (not added to branch subcommand, to not interfere with its syntax.)
  * add support for generic python-keyring lib, supports KWallet, Gnome keyring, MacOS and Windows.
  * make buildhist command usable without checked out package
  * rename old "platform/s" names to "repository/ies" (internal cleanup only)
  * fixed osc diff -c N, it failed with int and string concatenation
  * made osc diff and rdiff more similar: added -p, -c to rdiff, removed -u from rdiff.
    made -u default for both, renamed --pretty to --plain as it is the opposite of -u
  [#]
  [#] Features which require OBS 1.7
  [#]
  * option to download server side generated _service:* files on update
  * support for running source services locally. Happens by default on source update
    and build.
  * support modification flages on creation of submit request
    (for auto update or clean up packages or to avoid it, when submit request got accepted)
  * show request ids from package source logs
  * added support to require local packages which don't exist in the obs for a local build. This
    fixes #377021, #481193
* Fri Sep  4 2009 adrian@suse.de
- update to version 0.122 pre 1
* Fri Sep  4 2009 lv@lekv.de
- Add switch to installation in debian/rules to correctly install on debian-based systems
* Thu Sep  3 2009 adrian@suse.de
- switch to noarch package for > 11.1
* Tue Sep  1 2009 adrian@suse.de
- update to version 0.121.1
  * fix creation of new .osrc (#535919)
  * fix "osc my request"
* Thu Aug 27 2009 adrian@suse.de
- update to r7948 (version 0.121 candidate)
* Wed Aug 19 2009 alexandre@exatati.com.br
- Fix on spec file for x64 system bash auto-complete (bnc#528088).
* Thu Jun 18 2009 adrian@suse.de
- use completion script from tar ball
- update to r7560 (version 0.120)
  - support "setlinkrev" for whole projects
  - add "setlinkrev --unset" for removing revision references
  - add "osc request list -t <type>" to list only submit, delete or develchange requests
  - add shell completion scripts
  - fix support of listing requests with multiple actions
  - "osc maintainer" is following to the development project / package now
  - "osc maintainer" list maintainer and bugowner roles now
* Thu Jun 18 2009 adrian@suse.de
- update to version 0.119.1
  * fixing listing of requests, when a delete request exists
* Wed Jun 10 2009 werner@suse.de
- Add completion support for both tcsh and bash
* Wed Jun  3 2009 adrian@suse.de
- update to r7528 (version 0.119)
  - Support new request types
  - "submitreq" command has a new syntax (incompatible !)
  - new "deleterequest" command
  - new "changedevelrequest" command
  - new "request" command for showing/modifing requests
  - Multiple actions in one request is not yet supported by osc
  - The new commands require an OBS 1.7 server, submitreq is still working with
    older servers.
  - support of added .changes in commit message template
  - make submit request listing fast by server side filtering
  - allow pulling of conflicting changes via "osc repairlink"
  - delete commands consolidated:
  * deleteprj and deletepac are obsolete.
  * delete and rdelete take over
  - enable package tracking by default
  - bugfix: templates in edit commit message causes an empty commit logs
  - osc submitrequest consumes DESTPRJ [DESTPKG] arguments only
  - osc build now also tested on native arm targets where uname -m reports a string
    like armv{4l,5el,6l,7el,7l}
  - osc rlog now works with srcmd5 also
  - plugins now should be placed in /usr/lib/osc-plugins to match FHS (the /var path
    is still supported though)
  - osc now includes automatically generated man page
  - osc can now store credentials in Gnome keyring if it is available
  - new support for osc linkpac to specify cicount attribute
  - new log/rlog output formats (CSV and XML)
  - new jobhistory/buildhistory/search output format (CSV)
  - new option to fetch buildlogs starting at given offset
  - new option for copypac
  * -r to specify source revision
  * -m to specify a comment (and send default comment if not specified)
  - new option to results(r), and rresults:
  * -r|--repo to specify a repository(repositories)
  * -a|--arch to specify a architexure(s)
  * --xml for xml output (makes results_meta obsolete)
  - request list -M shows open SRs created by the user.
  - Fixed build support for images, only refered packages from buildinfo get used. (#485047)
  - "req" command got renamed to "api" to avoid clash with "request" command
  - osc build has a smarter default platform selection - it checks the
    availibility config value, 'standard' and 'opensuse_Factory' in platforms list and in case
    of fail it uses the last entry from that list
  - new osc linkpac -f to allow to override existing _link files
  - rename "rebuildpac" to "rebuild", but keep "rebuildpac" as alias
* Wed Apr 22 2009 adrian@suse.de
- update to r7162 (version 0.117)
  - new repairlink command for repairing a broken source link (requires server version 1.6)
  - new vc command for editing the changes files (requires build.rpm 2009.04.17 or newest)
  - support checkout of single package via "osc co PACKAGE" when local dir is project
  - allow to specify target project and package on osc branch (requires server version 1.6)
  - add option to automatic checkout a branched package
  - support "osc getbinaries" in checkout packages
  - '-b|--brief' option for osc submitreq show subcommand
  - use "latest" commited revision on checkout, not "upload" (#441783)
* Thu Apr 16 2009 adrian@suse.de
- update to r7093 (version 0.116)
  - support listings of older revisions with "osc ls -R"
  - add --current parameter for linkpac to use current revision of source package fixed.
  - add osc setlinkrev to add or update revision number in links easily
  - fix streaming of binary files via "cat" (#493325)
* Tue Mar 17 2009 adrian@suse.de
- update to r6820 (version 0.115)
  - optional transfer of devel project during copy_pac and link_pac is fixing
    opertation with remote build service instance
  - "osc ci" fails uploading large files to Provo BuildService
  - fixed support for accessing download repositories (worked only for download.o.o so far)
* Tue Mar  3 2009 poeml@suse.de
- update to r6667 (version 0.114):
  - the .oscrc config handling has been cleaned up:
  * use "apiurl" for everything now (== <protocol>://<host>)
  * added aliases support for [apiurl] sections in the ~/.oscrc.
    Example:
    [http(s)://foobar]
    ...
    aliases = foo, bar
    => "osc -A foo <cmd>" will do the same as "osc -A http(s)://foobar ls"
  * "scheme" and "apisrv" are deprecated and will produce a warning
  * when writing a new ~/.oscrc, store the apiurl in the conffile (bnc#478054)
  * fixed bug that made osc ask for credentials when -A was used (bnc#478054)
  * fixed crash upon password entry (first startup) (bnc#478052)
  - osc build:
  * make product builds work
  * speed up by using a cookie when fetching the binaries (bnc#477690)
  * support for VM (kvm or xen) builds
  * obsolete the need to configure download server, get it from the build
    service instance instead.
  * be a bit more verbose if the linked package isn't expanded (bnc#470948)
  - osc branch:
  * --develproject option fixed (the API calls it 'ignoredevel' instead of 'nodevelproject')
  * --revision option added
  - osc jobhistory: new command to see build job history of a project or a package
  - osc results/rresults: option -l, --last-build added (show last build results)
  - osc linkpac: fix failure when -A<url> is used (bnc#479156)
  - osc commit: don't scare users if they want to commit a nonexistent file (bnc#469167)
  - osc diff: bugfix to make --pretty option work
  - 11.1 added to the osc project template
* Thu Jan 22 2009 poeml@suse.de
- update to r6097 (version 0.113):
  - osc diff -rX:Y: the default is to return an unified diff (to get a pretty
    diff use the --pretty option)
  - osc rdiff: the default is to return a pretty diff (to get an unified diff use the --unified option)
  - osc sr show --diff: the default is to return a pretty diff (to get an unified diff use the --unified option)
  - osc getbinaries: optionally also download source rpms
  - osc importsrcpkg: set the url in the package meta (bnc#458083)
  - osc wipebinaries: added --expansion option
  - added support for format strings like "%%(project)s" and "%%(package)s" which
    can be used in the build-root config option.  For example one could use a new
    chroot for each package.
  - osc updatepacmetafromspec: fix failure if %%description is starting with newline (bnc#462869)
  - catch OSError exceptions which might be raised by the subprocess module
  - don't use a hardcoded path for the rpm binary otherwise it fails on
    distributions like debian
  - osc meta: be more verbose in case of failure (bnc#459292)
  - osc mkpac: add info how to enable the package tracking feature (bnc#459288)
* Fri Dec 12 2008 poeml@suse.de
- update to r5880 (version 0.112):
  important bugfix:
  - osc deletepac: prevent recursive deletion of a whole project [bnc#458535]
  - osc build: support more options: --icecream, --ccache, --with, --without
  - osc build: --keep-pkgs also saves the src.rpm now
  - osc build: small fix in debuginfo handling
  - osc build: new armv7el arch for all binaries for up to ARMv7 EABI with VFP
* Fri Nov 28 2008 poeml@suse.de
- update to r5751 (version 0.111):
  - fix accidental truncation of .oscrc to 0 bytes
  - fix osc's ignorance of the revision option (-r) for expanded links
  - osc build: handle kiwi builds (local image build)
  - osc build: cross build support
  - osc build: support for ARMv5 EABI little endian arch added
  - osc build: fixed detection of the build type (rpm or deb),
    after change in the buildinfo
  - osc build: build debuginfo packages if enabled in the
    project/package meta (this partly fixes [bnc#421390])
* Fri Oct 24 2008 poeml@suse.de
- update to r5425 (version 0.110):
  - osc build: no working copy needed anymore when building a local
    package [bnc#431434]
  - osc checkout: when checking out a project, and a linkerror
    occurs for one of the packages, do a checkout in unexpanded
    form and continue checking out the rest of the project
    [bnc#428303]
  - osc deletepac, osc branch: allow slash notation for the
    project/package arguments
  - fix deprecation warnings on Factory (which uses Python 2.6)
  - fix to avoid (internal) stale Package objects [bnc#436932]
* Tue Sep 30 2008 poeml@suse.de
- update to r5219 (version 0.109):
  With changes from Marcus_H, myself, dmueller, tpatzig:
  - osc getbinaries: new command to download binaries directly from
    the api server
  - pass the --debug option to the build script which will take
    care of creating debuginfo packages
  - add link to plugin API to osc help output
  - Don't try to catch rpm-python errors if rpm-python isn't installed.
    Thus we can avoid a hard dependency on having rpm-python.
  - added command 'rlog', to show commit logs of remote packages
  - fixed depracation warnings with Python 2.6 [bnc#426612]
  - fix streaming of unfinished logfiles again
  - fixed regression of .oscrc template [bnc#427118]
* Tue Sep 16 2008 poeml@suse.de
- update to r5032 (version 0.108):
  - osc submitreq: has two aliases now: "osc sr" and "osc submitrequest"
  - osc sr create: prompt to revoke existing requests
  - osc sr revoke: new command for to get rid of requests to projects one can't write to
  - osc sr list: allow showing requests in a state other than "new"
  - osc sr show: show the current state's comment
  - osc sr log: new command to show the history of a given id
  - osc sr: enable requests for submitting new packages
  - osc build: implement --no-checks
  - osc build: be less strict on the arguments, and guess what's needed. For instance:
  * osc build PLATFORM ARCH BUILD_DESCR
  * osc build PLATFORM (ARCH = hostarch, BUILD_DESCR guessed)
  * osc build ARCH (PLATFORM = build_platform (config option), BUILD_DESCR guessed)
  * osc build BUILD_DESCR (PLATFORM = build_platform (config option), ARCH = hostarch)
  * osc build (PLATFORM = build_platform (config option), ARCH = hostarch, BUILD_DESCR guessed)
  - osc build: download after the target architecture check
  - osc addremove: bugfixes, --recursive option
  - osc init: added support to initialize a project dir
  - osc metafromspec: new alias for 'updatepacmetafromspec' which is hard to remember
  - osc updatepacmetafromspec: also update URL
  - osc buildlog: do not download entire log to memory
  - new http_headers option to add arbitrary headers to HTTP requests
  - bugfix to make osc work on Gentoo
  - enhance/update the package and project template
  - .netrc heritage from previous commandline client has been removed
  - osc asks for password now, when used with -A
* Wed Jul 16 2008 poeml@suse.de
- update to r4461 (version 0.107):
  - osc update / checkout: *important bugfix* don't check out a
    working copy, or update an existing one, when a source link
    cannot be applied [bnc#409373]
  - osc build: the --extra-pkgs option is now a configurable
    setting in .oscrc.  Default is "extra-pkgs = vim gdb strace"
* Fri Jul 11 2008 poeml@suse.de
- update to r4428 (version 0.106):
  - osc rdiff / osc submitreq show: diff the _expanded_ sources [bnc#408267]
  - osc submitreq list: show author's name
  - osc submitreq: shortcut alias 'sr' added
* Wed Jul  9 2008 poeml@suse.de
- update to r4401: (version 0.105):
  - osc submitreq list:
  - can now be called without parameters, applying to the working copy then.
  - calling it in a project directory is also possible now.
  - output was improved. Newest requests are listed first.
  - osc submitreq delete: a new action which has been added
  - osc submitreq list/create: use api URL from the working copy
  - osc meta: editing returns the API error description instead of a plain HTTP
    error if available
  - osc copypac: use the correct userid when copying to another api host
  - osc importsrcpkg: disable signature check when getting data from a rpm file
  - osc linkpac: --revision option added.
  - osc search: added option -i|--involved, to show in which projects/packages
    a developer is involved
  - osc build: double check the buildinfo for local builds. Refuse to build for
    architectures that are not supported by the host
  - osc buildhist: change the output into a format which better matches actual
    RPM filenames.
  - osc commit: give commit message tempfiles a ".diff" suffix, so syntax
    highlighting automatically works in capable editors
  - other bug fixes:
  - don't expand/unexpand if the working copy has local modifications - this is
    an ugly workaround for bnc#399247 but this way the working copy isn't screwed up
  - work around a bug which causes packages to be cached locally under the
    "None" architecture (and therefore causing issues when building for more
    than one architecture via osc build).
  - don't create _linkerror files in working copies
  - better error handling (mostly printing more details) in a number of cases
  - show error messages from the API also for type 500 errors
* Wed Jun 11 2008 poeml@suse.de
- update to r4164 (version 0.104):
  - osc update: after update, reset the revision when updating
    multiple package. Fixes "404: Not Found" type errors when
    updating an entire project. [bnc#399177]
  - more/better error messages in some error scenarios
  - osc wipebinaries: add missing check for commandline arguments,
    which could cause a PACKAGE argument to be ignored
  - fixed make_diff in order to avoid errors when committing a new
    package (created with mkpac)
* Fri Jun  6 2008 poeml@suse.de
- update to r4120 (version 0.103):
  - osc submitreq create: simplify by make osc guess needed
    parameters, if there is a working copy and it is a source link.
  - osc submitreq create: don't stop on packages that have a devel
    project defined, if the submit actually comes from that
    project.
  - osc checkout: checkout of source links is now done in expanded
    form per default. The new option --unexpand-link can be used to
    get the raw link file.
  - show the API's error message for HTTP 403 (Forbidden) replies.
* Tue Jun  3 2008 poeml@suse.de
- update to r4089 (version 0.102)
  - osc branch: Show the actually created branch project name, not
    a guessed one.  Add --nodevelproject.
  - osc submitreq: look up the develproject of the target, and if
    there is one, don't create the request, unless forced with
  - -nodevelproject.
  - when -d (global, for debug) was used, save the body because it can't be read twice
* Tue May 27 2008 poeml@suse.de
- update to r4030:
  - version 0.101
  - add osc branch command, using the branch API call to branch a package to
    home:poeml:branches:PRJ/PKG
  - osc commit now opens $EDITOR for commit message
  - improved error handling, when API returns HTTP status code 400 (bad request)
  - osc status: implement -q/--quiet switch
  - osc info: slightly more verbose
  - osc deletepac: allow deletion of multiple packages at once
  - make "osc meta prjconf <project> -e" work again (probably caused by r3702)
* Tue May 20 2008 poeml@suse.de
- update to r4002:
  - osc maintainer: new -D/--devel-project switch
  - osc rprjresults/rresults: small fixes
  - facilitate correct syntax highlighting when editing metadata
* Mon May 19 2008 poeml@suse.de
- update to r3995:
  - version 0.100
  - improved error handling (babysitter.py wrapper, oscerr.py exception classes)
    Tracebacks are mostly suppressed now. To enable them, use
    |    -t, --traceback    print call trace in case of errors
    or set traceback=1 in .oscrc.
  - other new global options for debugging:
    |    --debugger         jump into the debugger before executing anything
    |    --post-mortem      jump into the debugger in case of errors
    |    -d, --debug        print info useful for debugging
  - make way for more seamless osc version updates (the .osc directory in working copies
    will have its own versioning in the future)
  - osc rprjresults and osc rresults: new commands to show remote build results
  - osc build: added --baselibs and --jobs options
  - osc copypac: added --keep-maintainers switch
  - BUILD_DIST environment variable will be ignored (bnc#359846)
    The following environment variables can still be used:
  * OSC_SU_WRAPPER overrides the setting of su-wrapper.
  * OSC_BUILD_ROOT overrides the setting of build-root.
  * OSC_PACKAGECACHEDIR overrides the setting of packagecachedir.
  - a few bug fixes.
* Mon Apr 21 2008 poeml@suse.de
- remove the patch added by Adrian (bnc#378421)
* Sat Apr 12 2008 adrian@suse.de
- add patch from abauer to fix cookie handling (bnc#378421)
* Wed Apr  2 2008 poeml@suse.de
- update to r3614:
  - osc commit: implement committing with keeping links (to commit
    changes to expanded links)
  - osc copypac: make the server-side copy the default. But do a
    client-side copy if source and target are not on the same
    buildservice instance
* Tue Apr  1 2008 poeml@suse.de
- update to r3598:
  New features:
  - new link handling:
    add support for handling linked packages in expanded form. They
    can be checked out, updated (expanding or unexpanding them),
    and built locally.
    Missing: commit support.
    Newly introduced options are:
  * osc checkout: --expand-link
  * osc update: --expand-link and --unexpand-link
  - osc build: add --debuginfo switch (Thanks, Juergen!) [bnc#368524]
  - osc req: add option -a / --add-header to inject arbitrary
    request headers
  - osc addremove (and others): ignore _all_ dot files (the
    buildservice doesn't handle them) [bnc#370476]
  - copypac: do a server-side copy (via a single api call) when
    used with -s / --server-side.
  - prjresults: csv export uses ';' as default (Pavol)
  - osc update/checkout: enable to use md5sum as revision id
  - osc info: make it show info about expanded and non-expanded links
  - osc submitreq:
  - implement an 'accept' action, resulting in the respective
    state change
  - when requesting a submit, save the source package's revision
    id (looking up what it currently is)
  - give the user a way to override it, to submit an older
    revision
  - when using show --diff, take the actual old revision into
    account. Thus, the diff is against the source revision of the
    time of request creation.
  Bug fixes:
  - osc mkpac only works when 'do_package_tracking' is enabled
  - do_repos() should work in a project dir too
  - handle mmap failure on filesystems like NTFS, which may not
    support memory mapping when mounted under Linux
  - submitreq show: if the target package doesn't exist, a diff
    cannot be produced.
  - fixed username issues when creating a new package (the problem was
    that the username for the default host was used and not the one for
    that specific apiurl)
  Internal changes:
  - enhance osc.core.makeurl(). This function accepts a query
    parameter in form of a list. The query can now also be given as a
    dictionary, and in that case it will be automatically urlencoded.
    The behaviour for a list is unchanged for the reason of backward
    compatibility.
  - add Linkinfo class to osc.core
  - Package class:
  - add linkinfo when reading in package data via update_datastructs()
  - add islink() and isexpanded() methods
  - added 3 new methods:
  * createPackageDir(): creates and initializes a new package dir in
    the given project.
  * get_apiurl_usr(): returns the username for a certain apiurl
  * get_configParser(): returns an ConfigParser() object which can be
    used for parsing the ~/.oscrc file
  - new show_upstream_xsrcmd5() method which returns the xsrcmd5 (if a
    linkinfo element exists)
  - all necessary auth-information are available in the 'auth_dict'
    (so there's no need to fool around with the ConfigParser...)
  - if there are no credentials for the apisrv in use (which may be
    specified with -A on the commandline), don't try to set up
    config['user'] with credentials.
* Mon Mar 10 2008 poeml@suse.de
- update to r3492:
  - new feature: package tracking. It's not enabled by default and
  needs to be switched on with do_package_tracking=1 in .oscrc.
  before using. See
  http://lists.opensuse.org/opensuse-buildservice/2008-03/msg00114.html
  for more info.
  - new command submitreq, to handle "submit requests" (next
  generation build service feature). Its functionality isn't
  complete yet. So far it can create, list and show requests.
  - define bugowner when creating new projects or packages
* Tue Mar  4 2008 poeml@suse.de
- update to r3403:
  - fixes from Marcus and Michal Marek:
  - fix importsrcpkg when $projectdir/.osc/_apiurl is an
    alternative apiurl
  - added optional apiurl parameter to the following methods:
    meta_exists, make_meta_url, checkRevision if no apiurl
    parameter is specified the global value (conf.config['apiurl'])
    will be used. This should fix bug #361764
  - some small apiurl fixes in the make_diff method (the
    package_tracking branch already has this fix)
  - added option --csv to 'osc prjresults' to output a CSV table
  - small fixes testsuite for the testsuite
* Thu Jan 24 2008 poeml@suse.de
- update to r3046:
  - build:
  - add --no-verify
  - add --local-package to build a package which doesn't exist on the server
  - add --alternative-project to specify a project, if the current one doesn't
    exist on the server
  - use api url from .osc/_apiurl [#355144]
  - new command remotebuildlog
  - diff: fix #347377 (diffing too many files)
  - checkout: check for project existance beforehand
* Fri Jan 11 2008 adrian@suse.de
- add Recommends: build > 2007.09.14
* Mon Dec 10 2007 poeml@suse.de
- update to r2778:
  - bugfix in build: in order to verify package signatures, run the
    external rpm command with en_EN locale, because the output is
    being parsed
  - cat: simplify the code a bit; don't print header and footer lines
* Fri Nov 30 2007 poeml@suse.de
- update to r2688:
  - fixed bug in osc cat
* Fri Nov 30 2007 poeml@suse.de
- update to r2685:
  - rdiff: new command for server-side diffs between arbitrary
    packages
  - cat: new command to print a file on the standard output
  - diff: reworked functionality to show newly added files, and
    behaving more like svn when doing diff against a certain
    revision
  - bugfix in {link,aggregate,copy}_pac (<person> elements). Patch
    from Michal Marek.
  - checkout an empty project instead of doing nothing
  - fix prjresults for newly added packages, where build status is
    missing
  - internal changes:
  - copied init_project_dir() method from the
    osc-package-tracking branch (just removed the
    do_package_tracking stuff)
  - changed the storedir attribut of the Package() class to an
    absolute filename - normally this shouldn't have any impact
    on existing methods, functionality etc.
* Tue Oct 30 2007 poeml@suse.de
- update to r2467. Most work done by Marcus Huewe.
  - version 0.99
  - aggregatepac: new command, similar to linkpac. Patch from Pavol
    Rusnak.
  - wipebinaries: added --build-failed and --broken [#335498]
  - deleteprj: enabled this command, as the backend now supports it
  - maintainer:
  - added --verbose option
  - added functionality to add/remove users from a project/package
  - print the list of URL to try, when in HTTP debug mode
  - build: allow to use lbuild, a compatible replacement for build
  - do not create dirs for non-existing packages during checkout
    [#259711]
* Mon Sep  3 2007 poeml@suse.de
- update to r2075:
  - new 'maintainer' command, to list the maintainers of a project
    or package
  - make osc call build with --changelog option, by default [#298436]
  - make osc library simpler to use from external scripts, by
    simply calling conf.get_config(), with possibility to override
    conf file, http debugging, api server). It is no longer
    required to set up the api url in the config dict, and call
    conf.init_basicauth().
  - allow to specify a different config file via the environmental
    variable OSC_CONFIG, or via -c|--config on the commandline
* Fri Aug 17 2007 poeml@suse.de
- update to r2001:
  - contributions from James Oakley and Marcus Huewe
  - ls: add -b option to list binaries
  - req: show error response for 404 responses
  - core: add get_binarylist(); works per project and per package
  - core: add get_binarylist_published(); works per project
  - core: add get_binary_file()
  - build: "osc build" if $BUILD_DIST is set
* Tue Aug 14 2007 poeml@suse.de
- update to r1974:
  - version 0.98
  - commit: use the documented commit method by default now
  - build: add --changelog option to force update of the package
    changelog from a changes file
* Thu Aug  9 2007 poeml@suse.de
- update to r1961:
  - meta: remove notion of non-implemented --create switch. give
    example for meta pkg usage
  - search: add --repos-baseurl option
* Wed Aug  8 2007 poeml@suse.de
- update to r1947:
  - commit: fixed possible "UnboundLocalError" with -m. Thanks to
    judas_iscariote for spotting this issue, and Marcus for fixing
    it.
* Wed Aug  8 2007 poeml@suse.de
- update to r1946:
  - avoid warning/error with unsupported HTTPS_PROXY [#214983][#298378]
  - importsrcpkg:
  * changed default behaviour - the files will not be committed by
    default. To commit them use the --commit switch.
  * added --delete-old-files option switch to delete old files from
    the server.
  * allow to import source rpms by specifying an URL
  * use rpm-python
  - fix for "osc prjconf <project> -e".
  - add Recommends: rpm-python
* Wed Jul 25 2007 poeml@suse.de
- update to r1884:
  - added new importfromsrcpkg command, to import a package src.rpm
    (we owe this to Marcus)
  - added new req command, to issue arbitrary requests to the API
  - append missing newline if do_commits=False [#293672]
  - make delete_package() and delete_project() more userfriendly
    (added trivial exception handling..)
  - expand ~ to users home for packagecachedir in .oscrc [#293675]
* Thu Jul 19 2007 poeml@suse.de
- update to r1871:
  - meta: allow for editing patterns
  - small fixes:
  - fix error message which osc issues if build package is too old
  - results: result code can be empty when package has just been created
  - fix name of 10.2 product in the template for new projects
* Wed Jul 18 2007 poeml@suse.de
- update to r1861:
  - commit (using the currently documented way):
  - do DELETEs _before_ generating an "upload" revision with
    PUTs. The DELETEs would be invalidated by the commit.
  - switch to new commit mode also if the -F switch is used
  - flush stdout, so that the progress dots are seen directly
    when being written
* Mon Jul 16 2007 poeml@suse.de
- update to r1846:
  - added initial search support (some ideas are taken from the webclient):
  * when searching a package/project it
    is also possible to search for the search term
    in the <title /> and <description /> elements of
    a package/project.
  * show only exact matches
  - new meta command, replacing editmeta, editprj, createprj,
    editpac, createpac, edituser. Can either show existing meta, or
    edit it (--edit), or upload content (--file). Fix metadata
    change detection, which no longer relies on the timestamp of
    the temporary file.
  - log:
  - renamed previous "log" command to "buildlog" (short: bl)
  - implementing a log command to review the commit log
  - commit:
  - commit: implemented -m and -F option for the commit message.
    NOTE: if -m is used, osc uses a different mode of uploading
    files and commit them, namely the way which is currently
    documented in the api. So far, osc was uploading each file
    separately through the old backward compatible way. This way
    of committing can also be forced with do_commits = 1 in
    .oscrc.
  - other changes:
  - api now sends HTTP/1.1 400 Bad Request for invalid xml. Thus,
    show the reply body because it contains helpful info.
  - if PUT on metadata fails with a 500, and http_debug is True,
    print out the body of the server reply
  - improved exception handling in some places
  - updatepacmetafromspec: read spec files in utf-8, or whatever
    the preferred encoding is in the locale
* Wed Jul 11 2007 poeml@suse.de
- update to r1825:
  - version 0.97
  - added initial revision handling:
  - extended "osc co prj pac" to checkout a specific revision of pac
  - extended "osc up" to update to a specific revision
  - extended "osc diff" to diff the working copy against a
    specific revision on the server. NOTE: comparing two
    server-side revisions (osc diff -r 11:12) is currently
    not supported!
  - addremove: ignore foo.rXX, foo.mine for files which are in 'C' state
  - wipebinaries: allow to wipe all binaries of packages for which
    the build is disabled
  - updatepacmetafromspec scans for spec files automatically; also,
    added a --specfile option.
  - load subcommands from /var/lib/osc-plugins/ or ~/.osc-plugins/
* Fri Jun 29 2007 poeml@suse.de
- add /var/lib/osc-plugins to the filelist
* Fri Jun 29 2007 poeml@suse.de
- update to r1794:
  - rm: don't allow to mark files as deleted which are not under
    version control
* Thu Jun 28 2007 poeml@suse.de
- update to r1792:
  - linkpac: make this osc subcommand work again: sync metadata if
    edit_meta() is called with change_is_required=False.
  - log: fail gracefully if logfile can't be found
  - handle empty prjresults (e.g. when no repositories are defined)
* Tue Jun 26 2007 poeml@suse.de
- update to r1783:
  - build: don't stumble over an empty list of packages when trying to verify packages
  - ls: add verbose option to print extra information for packages
  - for ls, co, meta, editmeta, linkpac, copypac, rebuildpac, and wipebinaries
    (basically all the server-side commands), allow arguments "foo/bar" instead
    of "foo bar"
* Fri Jun 22 2007 poeml@suse.de
- update to r1769:
  fix return values in metafile.sync() which I broke whey I applied
  Marcus Huewe's patch...
* Thu Jun 21 2007 poeml@suse.de
- update to r1763:
  - set correct Content-Type header on PUT requests
    (application/octet-stream). Rails 1.2 seems to be more strict
    in this regard. Patch from Marcus Rueckert.
  - init: make usage (and usage info) info more precise
* Thu Jun 14 2007 poeml@suse.de
- update to r1733:
  New features kindly implemented by Marcus Huewe:
  - added wipebinaries command
  - added abortbuild command
  - improved handling of metadata editing if the server doesn't accept it
* Thu Jun 14 2007 poeml@suse.de
- update to r1731:
  - adjust for change in build.rpm, where /usr/lib/build/debsort
    was removed.  Look for debtransform program instead in order to
    determine if build.rpm is new enough.
  - update cmdln.py to planned 1.0 version. The main changes are
    related to points that were raised during employment in osc:
    [#] v0.8.3
  - Fix a bug where errors with passing an incorrect number of args to
    functions in do_foo() implementations would be masked.
    [#] v1.0.0
  - [backward incompat] `Cmdln.main()` no longer takes an `optparser`
    argument. Top-level option parsing has been changed so that top-level
    options for a `Cmdln` subclass can more naturally be defined and
    handled on the class definition. Changes:
  - `Cmdln.main()` calls `self.get_optparser` to get an option handler.
    Subclasses should overload this method for custom top-level options.
  - After option parsing, but before sub-command handling, the
    `self.postoptparse()` hook is called.
  - Add a `version` attribute on `Cmdln` subclasses. If set, the default
    top-level option parser will have a `--version` attribute.
  - [backward incompat] Simplify the StopProcessing/opts.stop handling for
    option handling in subcommands. The "opts" argument to "do_*"
    sub-command functions will no longer have a "stop" value.
    StopProcessing is now called StopOptionProcessing. This shouldn't
    affect simple usage of cmdln.py.
  - adjust osc.commandline for these changes.
  - make startdir a module global
  - add info about usage with the 'nosetests' test discovery tool
  - add tests for commandline options
  - results: remove obsolete code handling commandline arguments
* Mon May 14 2007 poeml@suse.de
- update to r1657:
  - rebuildpac: fix mistyped repository parameter
  - build: add --userootforbuild option
* Sat May 12 2007 poeml@suse.de
- update to r1655:
  - build: fix bug introduced with r1652: for the buildinfo, POST
    the specfile's content, not its name...
* Thu May 10 2007 poeml@suse.de
- update to r1652:
- build: implement -x/--extra-pkgs option (passed to backend and
  included in buildinfo result)
- make filling out of username in templates work again
* Tue May  8 2007 poeml@suse.de
- update to r1644:
  - don't allow to delete projects, as long it is not implemented in
    the backend
  - use new API route for downloading binaries also in configured URLs
  - make deletepac work again
* Fri May  4 2007 poeml@suse.de
- update to r1635:
  - version 0.96
  - following suggestions by Christian Boltz and Michal Marek, osc
    now memorizes where a working copy was checked out from, saving
    the api server url to .osc/_apiurl.
  - implement 'info' subcommand
  - buildhistory works again
  - copypac: implement package copy from one buildservice instance to another
    (--to-apiurl option)
  - build:
  - rename --prefer-pacs option to --prefer-pkgs
  - implement --keep-pkgs option
  - call rpm command for preferred rpms with --nosignature --nodigest
  - improve key import instructions after suggestion by Michael Wolf
  - the results subcommand now handles multiple <working copy> arguments
  - use the new api routes in all places
* Wed May  2 2007 poeml@suse.de
- update to r1626:
  - build: implement --prefer-pacs option
  - apply patch from Michael Marek, fixing all places where error
    messages were printed to stdout instead of stderr. [#239404]
* Wed Apr 25 2007 poeml@suse.de
- update to r1608:
  - version 0.95
  - osc is now easier to work with when using alternative API servers. The
    configured server can be overriden with -A <url> on the commandline.
    "apisrv" in the config takes a URL now, so the variable "scheme" which was
    needed in addition before becomes obsolete. For backward compatibility, a
    hostname (and scheme variable) are accepted like before. Likewise, the auth
    sections in the config take a URL now, or a hostname:port to keep old config
    working. HTTP or HTTPS scheme is determined from the URL. Credentials must be
    configured in .oscrc.
  - build: use actual api server in urllist for downloading, instead of hardcoded
    api.opensuse.org [#265211].
  - finally, global option -H enables HTTP traffic debugging
  - implement "rebuild all failed packages", via --failed option in rebuildpac
    subcommand
  - status -v shows all files, including unmodified ones
  - suppress the legend in prjresults by default (show with -l)
  - --version shows the program version number
  - fix the commit subcommand's argument handling. The following works correctly
    now: osc ci ../test/onlyinwc `pwd` fstab ../test/f2
  - fix the download progress meter to work with small terminals [#266989]
* Fri Apr 20 2007 poeml@suse.de
- update to r1594:
  - save and reuse HTTP server cookies, speeding HTTP requests up
    about 5 times (in our iChain setup anyway...)
  - rewrite the HTTP handling
  - adding http_GET/POST/PUT/DELETE() functions, which dispatch to
    http_request(), and use them everywhere
  - removing othermethods.py
  - keeping urlopen(), in case it is used from externally, but have it print out
    a "depracated" message
  - finally, implementing a global HTTP debug mode
  - if data to be sent is large, mmap it instead of reading at once
  - build: remove debug print of tempfile name
  - README: add info about dependencies of osc python module
  - further the osc buildroot configuration example
* Thu Mar 29 2007 poeml@suse.de
- update to r1551:
- update: when updating multiple packages, print each package name
- build:
  - use <bdep> preinstall attribute instead of obsolete <pdep> element
  - use <bdep> runscripts attribute and hand it over to build in the buildinfo
- results: quote parameter in the new URL
- prjresults: sort package names
- run build with --norootforbuild, thereby defaulting to build as
  abuild user
- when updating, don't delete files with local modifications
- add testcase
- update osc tests for small api changes
- use new api ['build', prj, '_result'] for prjresults subcommand
* Mon Mar 12 2007 poeml@suse.de
- update to r1427:
- apply fix from Christoph Thiel to use cElementTree from Python 2.5
- let the diff subcommand return 1 if differences were found
- make 'results' subcommand many times faster, by making only a
  single request on _result?view=status&package=%%s (new api)
* Fri Mar  9 2007 poeml@suse.de
- build the debian package in the new way
* Tue Jan 23 2007 poeml@suse.de
- update to r1093:
- fix important bug, which could lead to overwriting local
  modifications when upstream changes are merged in
- if a merge fails, the store copy must be updated neverthelesss
- sort output of 'status' (unknown files first, filenames
  alphabetically)
* Tue Jan 23 2007 poeml@suse.de
- remove unused (and possibly disturbing, because unfunctional) rpm
  define of py_sitedir
* Fri Jan 12 2007 poeml@suse.de
- update to r1047:
- core: added class "metadata" (merge from Susannes
  /branches/froh/reponator/)
  - added command alias 'stat' for 'status', like in svn
  - improved documentation/examples (Lars + Susanne)
  - print usage info if 'co' is called without arguments
* Fri Oct 13 2006 poeml@suse.de
- set scheme=https in the default configuration, to work around
  issue with new server
* Thu Oct 12 2006 poeml@suse.de
- update to 0.9 (r761):
- "iChain-ready" (works with API server now using iChain
  authentication)
- add runtime check for build.rpm version, so the rpm package
  dependency is no longer required
- add 'edituser' command for editing the metadata of a user
  account. It tries to create a user if it doesn't exist yet. A new
  command 'usermeta' replaces 'id' respectively 'userid'.
- rewrite configuration handling. Now the API server can be set in
  .oscrc
- ignore '.gitignore', '.pc', '*~' (now using filename matching
  [#208969]
- fix 'status' to work with project directories as arguments
- fix 'status <filename>'
* Fri Sep 29 2006 poeml@suse.de
- update to r753:
- 'rebuildpac' now accepts additional repo and arch argument. Note:
  the syntax has changed.
- add 'prjresults' command to display aggregated build status over
  an entire project
- add 'deleteprj' command (the API server doesn't seem to support
  it yet, though)
- change 'buildhistory' to display human-readable text
- 'log': print usage info if called with missing arguments
- 'ci': handle upload errors
- fix filelist for python >= 2.5
* Thu Sep 21 2006 poeml@suse.de
- update to r744:
- add 'copypac' subcommand, to copy a complete package to a new package,
  possibly cross-project
- don't die if user tries to 'add' a file which is already versioned
- don't die if 'addremove' encounters directories
- urlopen(): for server return code 500, print out the reply body
- be fair, and also mention dsc files in some help texts
* Fri Sep 15 2006 poeml@suse.de
- update to r735:
- build: use configuration from *local* specfile (e.g. BuildRequires)
- build: let envvars OSC_SU_WRAPPER and OSC_BUILD_ROOT override config
- build: allow 'dynamical' build-root setting by using %%(repo)s and %%(arch)s
- add 'createpac/editpac' and 'createprj/editprj' subcommands which
  are similar to 'editmeta' but should be more logical to find
- added 'deletepac' subcommand
- added 'buildhistory' subcommand (formerly 'history'). This only
  gives out raw xml at this time
- added ".git" to the excluded files
* Mon Aug  7 2006 poeml@suse.de
- update to svn r635:
- added 'linkpac' subcommand
- adapt to API changes
* Thu Jul 20 2006 poeml@suse.de
- fixed issue with uploading files when an intercepting web proxy
  was in between osc and the api server
- fixed creation of new packages/projects
* Mon Jul 17 2006 poeml@suse.de
- update to 0.7 (r599)
- initial support for local builds (subcommand 'build')
- new subcommands buildconfig, buildinfo, repos
- better error handling
* Sun Jun 25 2006 poeml@suse.de
- update to svn r534
- fix 'rebuildpac' command to not show raw xml
- editmeta:
  - add examples for <disable> tags to the package template
  - add examples for build targets to the project template
- fix updatepacmetafromspec to cope with subpackages during parsing
- code cleanup
- remove requirement on pyxml package
* Wed Jun 21 2006 poeml@suse.de
- update to svn r528:
- add support for streaming build log (thanks to Christoph Thiel)
- don't try to merge binary files
- set mtime on files that have been fetched during merge
* Wed Jun  7 2006 poeml@suse.de
- update to svn r481:
- fix handling of filenames with '+' signs [#153725, #181593]
- before committing, make sure that the working copy is up to date
- don't diff binary files
- add 'rebuildpac' command, which triggers a rebuild for all
  repositories/architectures of the package
- fix merge on 'update', if osc is called from another directory
- don't fail on 'resolve' when the working copy is in a newer rev already
- add 'commit' as command alias for 'ci/checkin'
* Mon Jun  5 2006 poeml@suse.de
- update to svn r469:
- work around ruby on rails issue, which swallows '+' signs in filenames in PUT
  requests [#153725, 181593]
- before committing, make sure that the working copy is up to date (added
  show_rev() function)
- add 'commit' as subcommand alias for 'ci/checkin'
* Fri Jun  2 2006 poeml@suse.de
- update to svn r466:
- add 'repourls' subcommand
- display reason for new build status is 'broken'
- add a tentative 'updatepacmetafromspec' subcommand, which takes package
  metadata from a specfile
- handle some error conditions
- fix the profiling wrapper script
- make 'resolved' more robust
- set a User-agent
* Mon May 29 2006 poeml@suse.de
- update to 0.6:
- diff bugfix: sometimes displayed diff against obsolete files
- update bugfixes: fix update of working copy when adding a file from upstream
  which is missing locally; fix update in directory with unmodified files:
  don't try to merge if upstream file wasn't changed at all
- add: make it faster
* Mon May 22 2006 poeml@suse.de
- update to 0.5:
- help :-)
- fix status letter for files merged on update (in analogy to svn , it is
  either G or U)
- if an old _files listing without any metadata is found, don't bother the user
  with it
- make all subcommands properly importable functions
- bug in 'resolved' command fixed, which wouldn't clear the conflict state of a file
- fix update in directory with unmodified files: don't try to merge if upstream
  file wasn't changed at all
* Sun May 21 2006 poeml@suse.de
- don't fail on undeleting non-existing _to_be_deleted file
* Sun May 21 2006 poeml@suse.de
- update to 0.4:
- allow 'up' inside a project directory (will automatically pull in all new
  packages). (For past checkouts, you may need to put the project name into
  $prjdir/.osc/_project yourself).
- checkout: preserve mtimes
- add diff3 merge support. Locally modified files are merged with upstream changes
  if possible, and go into Conflict state if that fails.
- add 'resolved' command to be used after manual merging.
* Thu May 18 2006 poeml@suse.de
- update to 0.3:
- use the new file metadata, which provides checksum, size and mtime
- faster 'status', 'update', 'diff'
- improve argument handling, now e.g. 'osc up *' is possible
- on first usage, ask for username and password and store them in .oscrc
  (.netrc can still be used)
* Sun May 14 2006 poeml@suse.de
- this package is not noarch
* Thu May 11 2006 poeml@suse.de
- don't use --record-rpm option on setup.py, only SUSE has it
- define py_sitelib macro
* Tue May  9 2006 poeml@suse.de
- created package (version 0.2)
