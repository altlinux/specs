Name: python-module-xreadline
Version: 0.4.6
Release: alt2.2.1.1
Summary: eXtended readline library
Group: Development/Python
License: GPL
Packager: Eugene Prokopiev <enp@altlinux.ru>
Url: http://www.radlinux.org/connexion/wiki

Source0: %name-%version.tar

BuildRequires: gcc libncursesw-devel libreadline-devel python-devel
Requires: python-base

%description
eXtended readline library

%prep
%setup

%build

%install
%python_build_install --install-lib=%python_sitelibdir

%files
%python_sitelibdir/xreadline*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.6-alt2.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.6-alt2.2.1
- Rebuild with Python-2.7

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt2.2
- Rebuilt for debuginfo

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt2.1
- Rebuilt with python 2.6

* Sun Aug 31 2008 Eugene Prokopiev <enp@altlinux.ru> 0.4.6-alt2
- first build for Sisyphus from git


