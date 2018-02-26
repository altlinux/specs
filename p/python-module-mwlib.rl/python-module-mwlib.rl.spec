%define modulename mwlib.rl

Name: python-module-%modulename
Version: 0.12.4
Release: alt1.1
BuildArch: noarch
Summary: Python library for writing PDF documents from MediaWiki articles 
%setup_python_module %modulename

Group: Development/Python
License: BSD
Url: http://code.pediapress.com/
Packager: Michael A. Kangin <prividen@altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools python-module-docutils gettext-tools-python
BuildPreReq: python-module-mwlib >= 0.12.10
Requires: fonts-ttf-freefont python-module-mwlib >= 0.12.10 python-module-Reportlab >= 2.3

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
%exclude %python_sitelibdir/mwlib/tests
%python_sitelibdir/*.egg-info
%python_sitelibdir/*.pth
%doc README.* example-mwlib.config


%files tests
%python_sitelibdir/mwlib/tests/


%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.4-alt1.1
- Rebuild with Python-2.7

* Wed Jun 30 2010 Michael A. Kangin <prividen@altlinux.org> 0.12.4-alt1
- Initial build for Sisyphus
