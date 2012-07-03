%define tarname autocompleteusersplugin
Name: python-module-trac-autocompleteusersplugin
%define r_minor r9433
Version: 0.11
Release: alt1.%r_minor.1

Summary: This plugin allow complete the owner field for the ticket text input for known users

Group: Development/Python
# FIXME: unknown?
License: http://www.opensource.org/licenses/mit-license.php
Url: http://trac-hacks.org/wiki/AutocompleteUsersPlugin

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Source: %{tarname}-%r_minor.zip

BuildArch: noarch

# manually removed: python-module-Pyrex python-module-Rabbyt python-module-lxml
# Automatically added by buildreq on Sun Jan 06 2008
BuildRequires: python-module-MySQLdb python-module-ruledispatch python-module-setuptools unzip

%description
This plugin allow the configuration of the svnauthz file from the web inferface

%prep
%setup -q -n %tarname/%version

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot

#Fix rights for template
chmod -R a+r %buildroot%python_sitelibdir/autocompleteusers/htdocs

%files
%doc
%python_sitelibdir/*

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11-alt1.r9433.1
- Rebuild with Python-2.7

* Tue Nov 16 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.11-alt1.r9433
- Build for ALT

