%define tarname worklogplugin
Name: python-module-trac-worklogplugin
%define r_minor r9436
Version: 0.1
Release: alt1.%r_minor.1

Summary: Plugin to manage the which tickets users are currently working on

Group: Development/Python
License: http://www.opensource.org/licenses/mit-license.php
Url: http://trac-hacks.org/wiki/

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Source: %{tarname}-%r_minor.zip

BuildArch: noarch

BuildRequires: python-module-setuptools unzip

%description
This is a plugin that adds a Work Log capability to Trac. Basically, it allows you to register the fact
you have started work on a ticket which effectively allows you to clock on and clock off. It uses 
javascript to add a button to the ticket page to allow you to start/stop working on a given ticket. If the 
TimingAndEstimationPlugin is installed then when you clock off, the time spent on the ticket will be recorded.

%prep
%setup -q -n %tarname/0.11

%build
%__python setup.py build

%install
%__python setup.py install --root %buildroot

#Fix rights
chmod -R a+r %buildroot%python_sitelibdir/worklog/htdocs
chmod -R a+r %buildroot%python_sitelibdir/worklog/templates

%files
%doc
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.r9436.1
- Rebuild with Python-2.7

* Wed Nov 17 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1-alt1.r9436
- Build for ALT
