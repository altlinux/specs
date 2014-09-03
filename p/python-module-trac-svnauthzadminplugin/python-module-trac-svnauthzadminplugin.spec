%define tarname svnauthzadminplugin
Name: python-module-trac-svnauthzadminplugin
%define r_minor r13892
Epoch: 1
Version: 0.2
Release: alt1.%r_minor

Summary: This plugin allow the configuration of the svnauthz file from the web inferface

Group: Development/Python
# FIXME: unknown?
License: http://www.opensource.org/licenses/mit-license.php
Url: http://trac-hacks.org/wiki/SvnAuthzAdminPlugin

Source: %{tarname}-%r_minor.zip

BuildArch: noarch

# manually removed: python-module-Pyrex python-module-Rabbyt python-module-lxml
# Automatically added by buildreq on Sun Jan 06 2008
BuildRequires: python-module-MySQLdb python-module-ruledispatch python-module-setuptools unzip

%description
This plugin allow the configuration of the svnauthz file from the web inferface

%prep
%setup -n %tarname

%build
%python_build

%install
%python_install

chmod -R a+r %buildroot%python_sitelibdir/svnauthz/templates

%files
%doc
%python_sitelibdir/*

%changelog
* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.2-alt1.r13892
- Version 0.2

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11-alt1.r9433.1
- Rebuild with Python-2.7

* Tue Nov 16 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.11-alt1.r9433
- New version

* Mon Oct 04 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.11-alt1.r9250
- Build for ALT

