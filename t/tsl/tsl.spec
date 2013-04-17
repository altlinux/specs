%define _name tsl

Name: %_name
Version: 0.1.1a
Release: alt1.qa1

Summary: Telnet Scripting Language
License: GPL
Group: Networking/Remote access
Url: http://sourceforge.net/projects/tsl

Source0: %name-%version.tar.gz

%description
Telnet Scripting Language (TSL) allows for the full automation of Telnet,
SMTP, and other TCP protocols using a simple interpreted language.

%prep
%setup -q -n %_name-%version

%build
%make_build

%install
%__mkdir_p %buildroot%_bindir
%__install -m 755 %_name %buildroot%_bindir/%_name

%files 
%_bindir/%name
%doc AUTHORS ChangeLog COPYING README

%changelog
* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1.1a-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Jul 20 2006 Grigorij Mogaev <zcrendel@altlinux.ru> 0.1.1a-alt1
- initial rpm.
