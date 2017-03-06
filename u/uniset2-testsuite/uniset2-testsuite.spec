%def_enable doc

Name: uniset2-testsuite
Version: 2.5
Release: alt7
Summary: UniSet test suite
Group: Development/Python
License: LGPL
Url: http://github.com/Etersoft/uniset2-testsuite
Source: %name-%version.tar
# Automatically added by buildreq on Wed Jan 18 2017
# optimized out: pkg-config python-base python-modules python3 python3-base
BuildRequires: doxygen python-devel python-dev
BuildRequires: python-module-uniset2 >= 2.6-alt10

Requires: python-module-uniset2 >= 2.6-alt10
Provides: python2.7(UTestInterface)
Provides: python2.7(TestSuiteGlobal)
BuildArch: noarch

%if_enabled doc
BuildRequires: doxygen
%endif

%description
%summary

%package gui
Summary: GUI interface of uniset2-testsuite
Group: Development/Python
Requires: %name = %version-%release 
Requires: python-module-pygtk
AutoReq: no
%description gui
GUI (gtk) interface of uniset2-testsuite

%package doc
Summary: docs for uniset2-testsuite
Group: Development/Python
BuildArch: noarch
# Requires: %name = %version-%release 
%description doc
Documentation for uniset2-testsuite

%package snmp
Summary: SNMP plugin for uniset2-testsuite
Group: Development/Python
Requires: %name = %version-%release 
Requires: net-snmp-clients
%description snmp
SNMP Plugin for uniset2-testsuite

%prep
%setup

%build
%autoreconf
%configure %{subst_enable docs}
%make

%install
%make_install install DESTDIR=%buildroot

%files
%_datadir/%name/*.*
%_bindir/%name-xmlplayer
%_bindir/%name-conv
%exclude %_datadir/%name/plugins.d/*SNMP.py

%files snmp
%_datadir/%name/plugins.d/*SNMP.py

%files gui
%_datadir/%name/gtkplayer/guiTestSuitePlayer-gtk.py
%_datadir/%name/gtkplayer/GtkProcessMonitor.py
%_datadir/%name/gtkplayer/ScenarioParamEditor*
%_datadir/%name/gtkplayer/dlg*.py
%_bindir/%name-gtkplayer
%_datadir/%name/gtkplayer/*.ui
%_datadir/%name/gtkplayer/editors/*
%_datadir/%name/gtkplayer/images/*

%if_enabled doc
%files doc
%_docdir/%name
%endif

%changelog
* Tue Mar 07 2017 Pavel Vainerman <pv@altlinux.ru> 2.5-alt7
- add bash wrapper for run
- pack files to /usr/share/uniset2-testsuite

* Mon Mar 06 2017 Pavel Vainerman <pv@altlinux.ru> 2.5-alt6.1
- minor fixes in spec

* Thu Mar 02 2017 Pavel Vainerman <pv@altlinux.ru> 2.5-alt6
- (snmp): add ignoreCheckMIB parameter

* Thu Mar 02 2017 Pavel Vainerman <pv@altlinux.ru> 2.5-alt5
- fixed bug in replace..

* Fri Jan 27 2017 Pavel Vainerman <pv@altlinux.ru> 2.5-alt4
- update version

* Fri Jan 27 2017 Pavel Vainerman <pv@altlinux.ru> 2.5-alt3.1
- (snmp): use system utility and pipe

* Thu Jan 26 2017 Pavel Vainerman <pv@altlinux.ru> 2.5-alt3
- minor fixed (gitlab.set issue #5)

* Wed Jan 25 2017 Pavel Vainerman <pv@altlinux.ru> 2.5-alt2.1
- change snmp python interface: pysnmp --> netsnmp

* Mon Jan 23 2017 Pavel Vainerman <pv@altlinux.ru> 2.5-alt2
- add 'disable_tags' property for <test> (gitlab.set issue #5)

* Wed Jan 18 2017 Pavel Vainerman <pv@altlinux.ru> 2.5-alt1
- release new version (supported plugins, add snmp interface)

* Wed Jan 18 2017 Pavel Vainerman <pv@altlinux.ru> 2.3-alt17.1
- test plugins build

* Sat Jan 14 2017 Pavel Vainerman <pv@altlinux.ru> 2.3-alt17
- fixed bug 'double replace' (gitlab.set issue #7)

* Fri Jan 13 2017 Pavel Vainerman <pv@altlinux.ru> 2.3-alt16
- fixed bug in --play-tags (gitlab.set issue #5)

* Mon Jan 09 2017 Pavel Vainerman <pv@altlinux.ru> 2.3-alt15
- fixes for new uniset
- fixed bug set gitlab issue #8 

* Mon Dec 19 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt14
- add '--show-test-tree' command (gitlab.set issue #5)
- gitlab.set issue #1 (check scripts path in scenario-mode)
- gitlab.set issue #4 (bug in holdtime)

* Wed Dec 14 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt13
- skip sleep for 'test scenario mode' (gitlab.set refs #2)

* Tue Dec 13 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt12
- doc: minor fixes
- remove require for doc package

* Wed Dec 07 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt11
- new version

* Mon Dec 05 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt10.1
- add show 'extended information' for stacktrace
- add supported 'tags' or test
- add supported --check-scenario

* Tue Oct 11 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt10
- fixed bug 'change directory' for 'outlink'

* Thu Sep 01 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt9
- added support --supplier-name 

* Fri Jul 29 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt8
- fixed bug in 2.3-alt7 

* Fri Jul 29 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt7
- add supported list of tests for --test-name prop=test1,prop2=test2,...

* Thu Jul 14 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt6
- fixed trace call format (build only 'fail trace path')

* Fri Jul 01 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt5
- fixed a critical bug  of the previous commit

* Mon Jun 27 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt4
- added support --print-calltrace-limit. Default: 20

* Sat Jun 18 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt3
- added support --print-calltrace

* Sat Mar 26 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt2
- fixed URL in spec
- GPL --> LGPL
- update README

* Sat Mar 26 2016 Pavel Vainerman <pv@altlinux.ru> 2.3-alt1
- added support 'compare' test (compare sensor1 and sensor2) 

* Sat Mar 26 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt4
- added support 'ignore' flag for 'check' and 'action'

* Mon Mar 21 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt3
- fixed bug in requires

* Thu Mar 10 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt2
- add <Success> and <Failure> section to run scripts at the end of the test

* Fri Mar 04 2016 Pavel Vainerman <pv@altlinux.ru> 2.2-alt1
- rebuild for ALTLinux (rename eter --> alt)

* Tue Mar 01 2016 Pavel Vainerman <pv@altlinux.ru> 2.1-eter12
- add 'logfile' option for <RunList> items..

* Thu Feb 04 2016 Pavel Vainerman <pv@altlinux.ru> 2.1-eter11
- minor fixes

* Mon Feb 01 2016 Pavel Vainerman <pv@altlinux.ru> 2.1-eter10
- add chdir for outlinks..
- minor fixes

* Mon Feb 01 2016 Pavel Vainerman <pv@altlinux.ru> 2.1-eter9
- show real value (ID=val) for test: >=,>,<=,<
- coloring outlinks

* Sun Jan 24 2016 Pavel Vainerman <pv@altlinux.ru> 2.1-eter8
- added coloring output

* Sun Jan 24 2016 Pavel Vainerman <pv@altlinux.ru> 2.1-eter7
- minor fixes for processing unicode

* Sat Jan 23 2016 Pavel Vainerman <pv@altlinux.ru> 2.1-eter6
- global refactoring replace mechanism

* Fri Jan 22 2016 Pavel Vainerman <pv@altlinux.ru> 2.1-eter5
- minor refactoring for replace mechanism

* Fri Jan 22 2016 Pavel Vainerman <pv@altlinux.ru> 2.1-eter4
- fixed bug in processing replace rule

* Sat Jan 16 2016 Pavel Vainerman <pv@altlinux.ru> 2.1-eter3.2
- minor fixes

* Fri Oct 16 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-eter3
- add --show-test-comment param

* Fri Oct 16 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-eter2
- fixed minor bug in uniset2-testsuite-xmlplayer

* Fri Oct 16 2015 Pavel Vainerman <pv@altlinux.ru> 2.1-eter1
- refactoring
- modify help
- add --show-comments
- add --show-test-type
- add --hide-time
- add --show-numline

* Tue Jun 30 2015 Pavel Vainerman <pv@server> 2.0-eter16
- add support '-' for value

* Wed Jun 10 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-eter15
- added support spec symbol '[',']','{','}' for replace 

* Wed Jun 10 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-eter14
- added support spec symbol '#','$','%%' for replace

* Mon Jun 08 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-eter13
- fixed bug in replace mechanism..(link='..')

* Thu May 28 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-eter12
- improve the output format

* Thu May 28 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-eter11
- add new check 'holdtime=..'
- minor fixes

* Tue May 26 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-eter10
- add test separator (--------)

* Tue Apr 28 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-eter9
- minor fixes.. (result print format)

* Thu Apr 02 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-eter8
- modify replace 'mechanism'..

* Mon Mar 16 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-eter7
- modify junit report generator

* Wed Feb 11 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-eter6
- disable 'press key event' processing

* Tue Feb 10 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-eter5
- experimental: add "text testsuite format"
- experimental: new command line argument: --junit report.xml 

* Sun Feb 01 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-eter4
- fixed bug in TestSuiteInterface (error in regular expression)
- fixed bug: import uniset (remove require uniset) (must be uniset2)

* Sun Jan 25 2015 Pavel Vainerman <pv@altlinux.ru> 2.0-eter3
- add --default-timeout and --default-check-pause parameters

* Tue Nov 04 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-eter2
- add show test filename in 'result report'
- add --show-result-only

* Fri Oct 10 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-eter1
- added key press event processing

* Thu Oct 02 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-eter0.2
- add require to python-module-uniset2

* Sun Feb 02 2014 Pavel Vainerman <pv@altlinux.ru> 2.0-eter0.1
- modify for uniset2 (uniset-2.0)

* Wed May 15 2013 Pavel Vainerman <pv@altlinux.ru> 1.3-eter2
- add new action 'script'

* Tue Mar 05 2013 Pavel Vainerman <pv@altlinux.ru> 1.3-eter0.1
- rebuild for new uniset (add support python-module-uniset) 

* Wed Feb 13 2013 Pavel Vainerman <pv@altlinux.ru> 1.2-eter7
- add "Unknown CONFIG" error message

* Mon Oct 29 2012 Pavel Vainerman <pv@altlinux.ru> 1.2-eter6
- add --ignore-nodes

* Fri Jun 01 2012 Pavel Vainerman <pv@altlinux.ru> 1.2-eter5
- (editor): added support 'timeout' and 'check_pause' for any <check>

* Wed Mar 28 2012 Pavel Vainerman <pv@altlinux.ru> 1.2-eter4
- minor fix

* Wed Mar 28 2012 Pavel Vainerman <pv@altlinux.ru> 1.2-eter3
- fixed bug in 'multicheck'

* Mon Feb 27 2012 Pavel Vainerman <pv@altlinux.ru> 1.2-eter2
- added to replace the words within words

* Wed Jan 11 2012 Pavel Vainerman <pv@altlinux.ru> 1.1-eter4
- added support "multi interface" test

* Wed Nov 02 2011 Pavel Vainerman <pv@altlinux.ru> 1.1-eter3
- fixed bug in multicheck and multiset editors

* Fri Sep 30 2011 Pavel Vainerman <pv@altlinux.ru> 1.1-eter1
- add simple editor (1)

* Sat Sep 24 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-eter2
- minor fixes

* Sat Sep 24 2011 Pavel Vainerman <pv@altlinux.ru> 1.0-eter1
- added support modbus scenarios

* Wed Jun 01 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-eter29
- add check python version (for running with python 2.5 and python 2.6)
- fixed bug in logfile.open

* Wed Apr 20 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-eter28
- fixed bug in gtkplayer. ("Event" failed)

* Tue Apr 19 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-eter27
- add catch KeyboardInterrupt exception

* Mon Apr 11 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-eter26
- fixed bug in previous commit

* Mon Apr 11 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-eter25
- fixed bug in gtkplayer (do not stop process)

* Sun Apr 10 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-eter24
- added the possibility of issuing a flag "IGNORE"

* Sun Apr 10 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-eter23
- fixed various bugs in gtkplayer

* Sun Apr 10 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-eter22
- Fixed various bugs in gtkplayer

* Thu Apr 07 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-eter21
- test build

* Thu Apr 07 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-eter20
- add "waiting" progressbar for guiTestSuitePlayer

* Wed Apr 06 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-eter19
- added support <RunList> for guiTestSuitePlayer

* Mon Mar 14 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-eter18
- added the ability to interrupt long operations in the guiTestSuitePlayer

* Wed Jan 26 2011 Pavel Vainerman <pv@altlinux.ru> 0.9-eter17
- rebuild for uniset release

* Mon Dec 06 2010 Pavel Vainerman <pv@altlinux.ru> 0.9-eter16
- add log messages for better debuging

* Wed Dec 01 2010 Pavel Vainerman <pv@altlinux.ru> 0.9-eter15
- fixed bug in ProcessMonitor

* Sat Nov 27 2010 Pavel Vainerman <pv@altlinux.ru> 0.9-eter14
- new build (minor fixes)

* Wed Nov 24 2010 Pavel Vainerman <pv@altlinux.ru> 0.9-eter13
- fixed bug for recursive replace

* Wed Nov 24 2010 Pavel Vainerman <pv@altlinux.ru> 0.9-eter12
- fixed minor bug in replace (processing of multistring property)

* Tue Nov 23 2010 Pavel Vainerman <pv@altlinux.ru> 0.9-eter11
- add waiting for complete reset value thread

* Tue Nov 23 2010 Pavel Vainerman <pv@altlinux.ru> 0.9-eter10
- fixed bug for 'ignore_runlist flag'

* Tue Nov 23 2010 Pavel Vainerman <pv@altlinux.ru> 0.9-eter9
- reaise SIGTERM if thread terminated

* Mon Nov 22 2010 Pavel Vainerman <pv@altlinux.ru> 0.9-eter8
- add --ignore-run-list

* Mon Nov 22 2010 Pavel Vainerman <pv@altlinux.ru> 0.9-eter7
- add synchonization for RunList and TestList threads

* Mon Nov 22 2010 Pavel Vainerman <pv@altlinux.ru> 0.9-eter6
- add 'silent_mode' for <RunList> items

* Mon Nov 22 2010 Pavel Vainerman <pv@altlinux.ru> 0.9-eter5
- fixed bug in after_run_pause

* Mon Nov 22 2010 Pavel Vainerman <pv@altlinux.ru> 0.9-eter4
- fixed bug in play_xml

* Mon Nov 22 2010 Pavel Vainerman <pv@altlinux.ru> 0.9-eter3
- fixed bug in <RunList> "args" - parameter
- add "after_run_pause"

* Mon Nov 22 2010 Pavel Vainerman <pv@altlinux.ru> 0.9-eter2
- add ignore_runlist flag for 'outlink'

* Mon Nov 22 2010 Pavel Vainerman <pv@altlinux.ru> 0.9-eter1
- add <RunList>

* Wed Nov 17 2010 Pavel Vainerman <pv@altlinux.ru> 0.8-eter4
- new release (add gui player to master branch)

* Sun Nov 14 2010 Pavel Vainerman <pv@altlinux.ru> 0.8-eter3
- new split packages

* Sun Nov 14 2010 Pavel Vainerman <pv@altlinux.ru> 0.8-eter2
- add gui player
- split package

* Thu Nov 11 2010 Pavel Vainerman <pv@altlinux.ru> 0.7-eter1
- added the possibility of remote call and load many configure

* Mon Nov 08 2010 Pavel Vainerman <pv@altlinux.ru> 0.6-eter1
- add 'geat' and 'less' test

* Mon Nov 08 2010 Pavel Vainerman <pv@altlinux.ru> 0.5-eter6
- fixed minor bug: for 'EVENT' use action log..

* Sat Nov 06 2010 Pavel Vainerman <pv@altlinux.ru> 0.5-eter1
- new release (extened 'replace' mechanism)

* Fri Nov 05 2010 Pavel Vainerman <pv@altlinux.ru> 0.4-eter5
- modify time format output

* Fri Nov 05 2010 Pavel Vainerman <pv@altlinux.ru> 0.4-eter4
- noexception --> ignore_failed

* Thu Nov 04 2010 Pavel Vainerman <pv@altlinux.ru> 0.4-eter3
- add 'replace' for <TestList> and <test>

* Thu Nov 04 2010 Pavel Vainerman <pv@altlinux.ru> 0.4-eter2
- add global_replace property

* Thu Nov 04 2010 Pavel Vainerman <pv@altlinux.ru> 0.4-eter1
- add 'replace' method (for 'link' and 'outlink')

* Wed Oct 27 2010 Pavel Vainerman <pv@altlinux.ru> 0.3-eter4
- new version (add outlink ::ALL::)

* Tue Oct 26 2010 Pavel Vainerman <pv@altlinux.ru> 0.3-eter3
- minor fixes

* Tue Oct 26 2010 Pavel Vainerman <pv@altlinux.ru> 0.3-eter2
- new version (add chekc="outlink")

* Tue Oct 26 2010 Pavel Vainerman <pv@altlinux.ru> 0.3-eter1
- new version (add check="link")

* Mon Oct 25 2010 Pavel Vainerman <pv@altlinux.ru> 0.2-eter1
- new version

* Mon Oct 25 2010 Pavel Vainerman <pv@altlinux.ru> 0.1-eter9
- fixed bug in result report

* Mon Oct 25 2010 Pavel Vainerman <pv@altlinux.ru> 0.1-eter8
- fixed bug in xml:findNode

* Sun Oct 24 2010 Pavel Vainerman <pv@altlinux.ru> 0.1-eter7
- new version (format logs)

* Sun Oct 24 2010 Pavel Vainerman <pv@altlinux.ru> 0.1-eter6
- new version (add 'multicheck')

* Sun Oct 24 2010 Pavel Vainerman <pv@altlinux.ru> 0.1-eter5
- new version (add --show-result-report)

* Sun Oct 24 2010 Pavel Vainerman <pv@altlinux.ru> 0.1-eter4
- new version (add --log-action-show parameter)

* Sun Oct 24 2010 Pavel Vainerman <pv@altlinux.ru> 0.1-eter3
- new build

* Sun Oct 24 2010 Pavel Vainerman <pv@altlinux.ru> 0.1-eter2
- add new actions

* Mon Oct 18 2010 Pavel Vainerman <pv@altlinux.ru> 0.1-eter1
- initial build
