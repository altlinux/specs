Summary: Scientific Python Development Environment
Name: spyder
Version: 2.3.8
Release: alt1
Source0: http://spyderlib.googlecode.com/files/%name-%version.zip
Source1: %name.desktop
License: MIT
Group: Development/Python
Url: http://spyderlib.googlecode.com/

%setup_python_module spyderlib
%add_python_req_skip _winreg

BuildArch: noarch
Requires: python-module-matplotlib-qt4
Requires: python-module-%name-plugins
# IPython bug
Requires: python-module-zmq

# Automatically added by buildreq on Sun Jul 29 2012
# optimized out: python-base python-devel python-module-BeautifulSoup python-module-Pygments python-module-docutils python-module-jinja2 python-module-setuptools python-module-simplejson python-modules python-modules-compiler python-modules-email python-modules-encodings
BuildRequires: python-module-jinja2-tests python-module-sphinx unzip

%description
Spyder is a Python development environment with tons of features:

* Editor - Multi-language editor with function/class browser, code
  analysis (pyflakes and pylint are currently supported),
  horizontal/vertical splitting, etc.

* Documentation viewer - Automatically show documentation (if
  available, or source code otherwise) for any class instantiation or
  function call made in a Python shell (interactive/external console,
  see below).

* Interactive console - Python shell with workspace support (variable
  explorer with GUI based editors: dictionary editor, array editor,
  ...) and matplotlib figures integration.

* External console (separate process) - Run Python scripts
  (interactive, debugging or normal mode) or open a Python interpreter
  with variable explorer and documentation viewer support (a basic
  terminal window may also be opened with the external console)

* File/directories explorer

* Find in files feature - Supports regular expressions and mercurial
  repositories

* History log

Spyder may also be used as a PyQt4 extension library (module 'spyderlib').
For example, the Python interactive shell widget used in Spyder may be
embedded in your own PyQt4 application.

%package -n %packagename
Group: Development/Python
Summary: Supplemental python module for %name
%description -n %packagename
Supplemental python module for %name

%package -n python-module-%name-plugins
Group: Development/Python
Summary: Plugins module for %name
Requires: pylint, python-module-rope
%description -n python-module-%name-plugins
Plugins module for %name

%prep
%setup -n %name-%version

%build
%python_build

%install
%python_install

install -d -m755 %buildroot%_datadir/applications
install -d -m755 %buildroot%_datadir/pixmaps

install -D -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
# TODO png
install -D -m644 spyderlib/images/spyder.svg %buildroot%_iconsdir/hires/scalable/apps/%name.svg

%files
%doc README.md
%_desktopdir/*.desktop
%_iconsdir/hires/*/apps/*
%_pixmapsdir/spyder.png
%_bindir/*
%python_sitelibdir/%name-*egg-info

%files -n %packagename
# TODO strange place for documentation
#python_sitelibdir/spyderlib/doc
%python_sitelibdir/spyderlib

%files -n python-module-%name-plugins
%python_sitelibdir/spyderplugins

%changelog
* Thu Dec 24 2015 Fr. Br. George <george@altlinux.ru> 2.3.8-alt1
- Autobuild version bump to 2.3.8

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 2.3.7-alt1
- Autobuild version bump to 2.3.7

* Mon Sep 14 2015 Fr. Br. George <george@altlinux.ru> 2.3.6-alt1
- Autobuild version bump to 2.3.6

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 2.3.5.2-alt1
- Autobuild version bump to 2.3.5.2

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 2.3.4-alt1
- Autobuild version bump to 2.3.4

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 2.3.2-alt1
- Autobuild version bump to 2.3.2

* Sat Sep 27 2014 Fr. Br. George <george@altlinux.ru> 2.3.1-alt1
- Autobuild version bump to 2.3.1

* Tue Aug 26 2014 Fr. Br. George <george@altlinux.ru> 2.3.0-alt1
- Autobuild version bump to 2.3.0
- Fix build

* Mon Oct 14 2013 Fr. Br. George <george@altlinux.ru> 2.2.5-alt1
- Autobuild version bump to 2.2.5

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 2.2.3-alt1
- Autobuild version bump to 2.2.3

* Mon May 20 2013 Fr. Br. George <george@altlinux.ru> 2.2.0-alt1
- Autobuild version bump to 2.2.0
- Skip _winreg module dependency

* Sun Mar 31 2013 Fr. Br. George <george@altlinux.ru> 2.1.13.1-alt1
- Autobuild version bump to 2.1.13.1

* Thu Jan 10 2013 Fr. Br. George <george@altlinux.ru> 2.1.13-alt1
- Autobuild version bump to 2.1.13

* Sun Jul 29 2012 Fr. Br. George <george@altlinux.ru> 2.1.11-alt1
- Autobuild version bump to 2.1.11

* Sun Jul 29 2012 Fr. Br. George <george@altlinux.ru> 2.1.10-alt1
- Initial build from Mandriva

* Tue Apr 17 2012 Cristobal Lopez Silla <tobal@mandriva.org> 2.1.9-2mdv2011.0
+ Revision: 791525
- added a launcher for the program

* Tue Apr 03 2012 Lev Givon <lev@mandriva.org> 2.1.9-1
+ Revision: 788902
- Update to 2.1.9.

* Wed Mar 07 2012 Lev Givon <lev@mandriva.org> 2.1.8-1
+ Revision: 782571
- Update to 2.1.8.

* Sun Jan 15 2012 Lev Givon <lev@mandriva.org> 2.1.7-1
+ Revision: 760894
- Update to 2.1.7.

* Tue Dec 20 2011 Lev Givon <lev@mandriva.org> 2.1.6-1
+ Revision: 743963
- Update to 2.1.6

* Sun Dec 18 2011 Lev Givon <lev@mandriva.org> 2.1.5-1
+ Revision: 743400
- Update to 2.1.5.

* Wed Nov 30 2011 Lev Givon <lev@mandriva.org> 2.1.4-1
+ Revision: 735740
- Update to 2.1.4.

* Mon Nov 28 2011 Lev Givon <lev@mandriva.org> 2.1.3-1
+ Revision: 735142
- Update to 2.1.3.

* Fri Nov 18 2011 Lev Givon <lev@mandriva.org> 2.1.2-1
+ Revision: 731618
- Update to 2.1.2.

* Mon Nov 07 2011 Lev Givon <lev@mandriva.org> 2.1.1-1
+ Revision: 727181
- Update to 2.1.1.

* Thu Nov 03 2011 Lev Givon <lev@mandriva.org> 2.1.0-1
+ Revision: 714294
- Update to 2.1.0.

* Sun Jun 12 2011 Lev Givon <lev@mandriva.org> 2.0.12-1
+ Revision: 684339
- Update to 2.0.12.

* Sun May 01 2011 Lev Givon <lev@mandriva.org> 2.0.11-1
+ Revision: 661302
- Update to 2.0.11.

* Wed Apr 06 2011 Lev Givon <lev@mandriva.org> 2.0.10-1
+ Revision: 651052
- Update to 2.0.10.

* Mon Apr 04 2011 Lev Givon <lev@mandriva.org> 2.0.9-1
+ Revision: 650109
- Update to 2.0.9.

* Sun Feb 27 2011 Lev Givon <lev@mandriva.org> 2.0.8-1
+ Revision: 640670
- Update to 2.0.8.

* Mon Jan 10 2011 Lev Givon <lev@mandriva.org> 2.0.6-1
+ Revision: 630834
- Update to 2.0.6.

* Thu Dec 16 2010 Lev Givon <lev@mandriva.org> 2.0.5-1mdv2011.0
+ Revision: 622222
- Update to 2.0.5.

* Mon Dec 13 2010 Lev Givon <lev@mandriva.org> 2.0.4-1mdv2011.0
+ Revision: 620685
- Update to 2.0.4.

* Tue Dec 07 2010 Lev Givon <lev@mandriva.org> 2.0.3-1mdv2011.0
+ Revision: 614423
- Update to 2.0.3.

* Wed Dec 01 2010 Lev Givon <lev@mandriva.org> 2.0.2-1mdv2011.0
+ Revision: 604554
- Update to 2.0.2.

* Tue Nov 30 2010 Lev Givon <lev@mandriva.org> 2.0.1-1mdv2011.0
+ Revision: 603777
- Update to 2.0.1.

* Tue Nov 30 2010 Lev Givon <lev@mandriva.org> 2.0.0-1mdv2011.0
+ Revision: 603750
- import spyder

