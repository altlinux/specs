%define tarname worklogplugin
Name: python-module-trac-worklogplugin
%define r_minor r13835
Version: 0.4
Release: alt1.%r_minor

Summary: Plugin to manage the which tickets users are currently working on

Group: Development/Python
License: http://www.opensource.org/licenses/mit-license.php
Url: http://trac-hacks.org/wiki/WorkLogPlugin

# http://trac-hacks.org/svn/worklogplugin/trunk/
Source: %{tarname}-%r_minor.zip

BuildArch: noarch

BuildRequires: python-module-setuptools unzip

%description
This is a plugin that adds a Work Log capability to Trac. Basically, it allows you to register the fact
you have started work on a ticket which effectively allows you to clock on and clock off. It uses 
javascript to add a button to the ticket page to allow you to start/stop working on a given ticket. If the 
TimingAndEstimationPlugin is installed then when you clock off, the time spent on the ticket will be recorded.

%prep
%setup -n %tarname

%build
%python_build

%install
%python_install

#Fix rights
chmod -R a+r %buildroot%python_sitelibdir/worklog/htdocs
chmod -R a+r %buildroot%python_sitelibdir/worklog/templates

%files
%doc
%python_sitelibdir/*

%changelog
* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.r13835
- Version 0.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.r9436.1
- Rebuild with Python-2.7

* Wed Nov 17 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1-alt1.r9436
- Build for ALT
