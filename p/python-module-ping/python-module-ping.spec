%define module_name ping

Name: python-module-ping
Version: 0.2
Release: alt1
Group: Development/Python
License: GPLv2
Summary: implementation of the standard ICMP ping in pure Python
URL: http://pypi.python.org/pypi/ping
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: http://bitbucket.org/delroth/python-ping/downloads/python-%module_name-%version.tar.gz

BuildArch: noarch

BuildRequires: python-module-distribute

%description
This library is a fork of George Notaras' python-ping library, which is
an implementation of the standard ICMP ping in pure Python

%prep
%setup -n python-%module_name-%version

%build
%python_build

%install
%python_install


%files
%python_sitelibdir_noarch/*

%changelog
* Thu Jan 03 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2-alt1
- build for ALT
