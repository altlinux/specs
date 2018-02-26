%define modulename jabberbot

Name: python-module-%modulename
Version: 0.8
Release: alt3.1

%setup_python_module %modulename

Summary: A simple jabber/xmpp bot framework
License: GPLv3+
Group: Development/Python

Url: http://thpinfo.com/2007/python-jabberbot
BuildArch: noarch

Source: %name-%version.tar

BuildPreReq: %py_dependencies setuptools xmpp DNS
Requires: python-module-xmpp

%description
Programming your own Jabber bot can be fun and helpful. This is
python-jabberbot, a Jabber bot framework for Python that enables you to
easily write simple Jabber bots. You can use your Jabber bots to provide
information about your running systems, to make your website interact
with your visitors or notify you about updates or changes you monitor
with your Python scripts.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc examples README AUTHORS
%python_sitelibdir/*.py*
%python_sitelibdir/*.egg-info

%changelog
* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8-alt3.1
- Rebuild with Python-2.7

* Wed Apr 21 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8-alt3
- jabberbot.py: strip resource name from jid when getting subscribtion
  for avoid bot crash when resource name contains non-ascii characters.
- Update buildreqs.

* Tue Apr 13 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8-alt2
- Package documentation.

* Tue Apr 13 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 0.8-alt1
- Initial build for Sisyphus.

