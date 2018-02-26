Name: python-module-trac-gitplugin
Version: 0.11
Release: alt4.1

Summary: Plugin for Trac 0.10/0.11 which enables GIT to be used instead of Subversion

Group: Development/Python
License: GPL
Url: http://trac-hacks.org/wiki/GitPlugin

Packager: Eugene Prokopiev <enp@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-module-setuptools

%description
This is yet another plugin for Trac 0.10/0.11 which enables GIT to be used instead of Subversion
Features:

    * Browsing source code in a Git repository via the TracBrowser
    * Viewing the change history of a file or directory using TracRevisionLog
    * Performing diffs between any two files or two directories
    * Displaying submitted changes in the TracTimeline (0.11)
    * (Optionally) caching TracChangeset information in Trac's database (0.11)
    * Caching Git commit relation graph in memory (0.11)
    * Using the TracSearch page to search change descriptions (0.11)
    * Annotation support, also known as "blame" operation (0.11)
    * Interpretation of 40-character wide hex-strings as sha1 commit checksums
    * ...

%prep
%setup

%build
cd gitplugin/%version
subst "/namespace_packages/d" setup.py
%__python setup.py build

%install
cd gitplugin/%version
%__python setup.py install --root %buildroot

%files
%doc gitplugin/%version/README gitplugin/%version/COPYING
%python_sitelibdir/tracext/
# need for discover by trac as plugin
%python_sitelibdir/TracGit-0.11.0.1-py%__python_version.egg-info/

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11-alt4.1
- Rebuild with Python-2.7

* Mon Dec 28 2009 Eugene Prokopiev <enp@altlinux.ru> 0.11-alt4
- closes #22437

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt3.1
- Rebuilt with python 2.6

* Tue Mar 17 2009 Eugene Prokopiev <enp@altlinux.ru> 0.11-alt3
- fix python modules packaging policy violation

* Wed Jan 28 2009 Eugene Prokopiev <enp@altlinux.ru> 0.11-alt2
- fix install problems (thanks to peet@)

* Tue Jan 27 2009 Eugene Prokopiev <enp@altlinux.ru> 0.11-alt1
- first build for Sisyphus

