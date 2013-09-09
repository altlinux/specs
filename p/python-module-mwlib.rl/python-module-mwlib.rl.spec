%define modulename mwlib.rl

Name: python-module-%modulename
Version: 0.14.3
Release: alt1

Summary: Python library for writing PDF documents from MediaWiki articles 
%setup_python_module %modulename

Group: Development/Python
License: BSD
Url: http://code.pediapress.com/

BuildArch: noarch

Packager: Michael A. Kangin <prividen@altlinux.org>

# Source-url: https://pypi.python.org/packages/source/m/mwlib.rl/mwlib.rl-%version.zip
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools python-module-docutils gettext-tools-python

BuildPreReq: python-module-mwlib >= 0.15.11
Requires: fonts-ttf-freefont python-module-mwlib >= 0.15.11 python-module-Reportlab >= 2.5

#For math formulas:
#Requires: texvc

#For TOC:
#Requires: pdftk

%description
%modulename provides a library for writing pdf documents from mediawiki
articles which were parsed by the mwlib library.

%package tests
Summary: Tests for %modulename
Group: Development/Python
Requires: %name = %version-%release

%description tests
%modulename provides a library for writing pdf documents from mediawiki
articles which were parsed by the mwlib library.

This packages contains tests for %modulename.


%prep
%setup

%build
%python_build

%install
%python_install


%files
%python_sitelibdir/mwlib/
%python_sitelibdir/*.egg-info
%python_sitelibdir/*.pth
%doc README.* example-mwlib.config


#%files tests
#%python_sitelibdir/mwlib/tests/


%changelog
* Mon Sep 09 2013 Vitaly Lipatov <lav@altlinux.ru> 0.14.3-alt1
- new version 0.14.3 (with rpmrb script)

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.4-alt1.1
- Rebuild with Python-2.7

* Wed Jun 30 2010 Michael A. Kangin <prividen@altlinux.org> 0.12.4-alt1
- Initial build for Sisyphus
