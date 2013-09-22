%define bname clex
%define Name CLEX
Name: %bname-doc
Version: 4.6.6
Release: alt1
Summary: HTML documentation for %Name file manager
License: GPLv2+
Group: Documentation
URL: http://www.%bname.sk
Source: %url/download/%bname-html-help-%version.tar
Provides: %bname-html-help = %version-%release
BuildArch: noarch

%description
%Name (pronounced KLEKS) is a file manager with a full-screen user
interface. It displays directory contents including the file status
details and provides features like command history, filename insertion,
or name completion in order to help users to create commands to be
executed by the shell.
This package contains HTML documentation for %Name file manager.


%prep
%setup -n %bname-html-help-%version


%install
install -d -m 0755 %buildroot%_docdir/%bname-%version/html
install -m 0644 *.{css,html,png} %buildroot%_docdir/%bname-%version/html/


%files
%dir %_docdir/%bname-%version
%doc %_docdir/%bname-%version/html


%changelog
* Sun Sep 22 2013 Led <led@altlinux.ru> 4.6.6-alt1
- 4.6.6

* Tue Apr 07 2009 Led <led@altlinux.ru> 4.4-alt1
- 4.4

* Sun Mar 15 2009 Led <led@altlinux.ru> 4.2-alt1
- 4.2

* Sun Mar 15 2009 Led <led@altlinux.ru> 4.1-alt1
- 4.1

* Sat Dec 27 2008 Led <led@altlinux.ru> 4.0-alt1
- initial build
