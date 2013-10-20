%define module_name blinker

Name: python-module-%module_name
Version: 1.3
Release: alt1
Group: System/Base
License: MIT License
Summary: Fast, simple object-to-object and broadcast signaling
URL: http://discorporate.us/projects/Blinker/
Packager: Viacheslav Dubrovskyi <dubrsl@altlinux.org>
Source: %module_name-%version.tar.gz
BuildArch: noarch
BuildRequires: python-module-distribute

%description
Blinker provides a fast dispatching system that allows any number of
interested parties to subscribe to events, or "signals".

Signal receivers can subscribe to specific senders or receive signals
sent by any sender.

%prep
%setup -n %module_name-%version

%build
%python_build

%install
%python_install

%files
%doc AUTHORS CHANGES LICENSE README 
%python_sitelibdir_noarch/%{module_name}*

%changelog
* Sun Oct 20 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.3-alt1
- build for ALT
