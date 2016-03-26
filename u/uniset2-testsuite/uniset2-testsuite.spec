%def_enable doc

Name: uniset2-testsuite
Version: 2.2
Release: alt4
Summary: UniSet test suite
Group: Development/Python
License: GPL
Url: http://wiki.office.etersoft.ru/asu/
Source: %name-%version.tar
# Automatically added by buildreq on Thu Oct 02 2014
# optimized out: pkg-config python-base python-devel python-modules
BuildRequires: python-module-distribute

BuildRequires: python-module-uniset2 >= 2.0-alt6.M70P.7.Build1

Requires: python-module-uniset2 >= 2.0-alt6.M70P.7.Build1

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
Requires: %name = %version-%release 
%description doc
Documentation for uniset2-testsuite

%prep
%setup

%build
%autoreconf
%if_enabled doc
%configure
%else
%configure --disable-docs
%endif
%configure
#%make_build
%make

%install
%make_install install DESTDIR=%buildroot

mkdir -p %buildroot%python_sitelibdir/%name
mv -f %buildroot%python_sitelibdir/*.py %buildroot%python_sitelibdir/%name/

mkdir -p %buildroot/%_bindir/
ln -s %python_sitelibdir/%name/TestSuiteXMLPlayer.py %buildroot/%_bindir/uniset2-testsuite-xmlplayer
ln -s %python_sitelibdir/%name/guiTestSuitePlayer-gtk.py %buildroot/%_bindir/uniset2-testsuite-gtkplayer
ln -s %python_sitelibdir/%name/%name-conv.py %buildroot/%_bindir/uniset2-testsuite-conv

#%if_enabled doc
#  mkdir -p %buildroot/%_docdir/%name
#  mv %buildroot/%_docdir/%name/html/* %buildroot/%_docdir/%name/
#  rmdir %buildroot/%_docdir/%name/html
#%endif

%files
%dir %python_sitelibdir/%name
%python_sitelibdir/*
%_bindir/uniset2-testsuite-xmlplayer
%_bindir/uniset2-testsuite-conv
%python_sitelibdir/%name/*
%exclude %python_sitelibdir/%name/gui*Player*
%exclude %python_sitelibdir/%name/Gtk*
%exclude %python_sitelibdir/%name/ScenarioParamEditor*
%exclude %python_sitelibdir/%name/dlg*

%files gui
%python_sitelibdir/%name/guiTestSuitePlayer-gtk.py
%python_sitelibdir/%name/GtkProcessMonitor.py
%python_sitelibdir/%name/ScenarioParamEditor*
%python_sitelibdir/%name/dlg*
%_bindir/uniset2-testsuite-gtkplayer
%dir %_datadir/%name/player/
%dir %_datadir/%name/player/editors
%_datadir/%name/player/*.ui
%_datadir/%name/player/editors
%dir %_datadir/%name/player/images
%_datadir/%name/player/images/*

%if_enabled doc
%files doc
%_docdir/%name
%endif

%changelog
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
