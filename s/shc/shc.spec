Name: shc
Version: 3.8.6
Release: alt1

Summary: Generic shell script compiler
License: GPL
Group: Development/Other
URL: http://www.datsi.fi.upm.es/~frosal/
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source0: %name-%version.tgz

Patch0: %name-3.7-makefile.patch

Requires: gcc

%description
A generic shell script compiler. shc takes a script, which is
specified on the command line and produces C source code. The
generated source code is then compiled and linked to produce a
stripped binary executable. Use with care.

%prep
%setup -q -n %name-%version
%patch0

%build
%make

%install
%__mkdir_p $RPM_BUILD_ROOT{%_bindir,%_man1dir}
%makeinstall

%files
%_bindir/*
%doc CHANGES Copying shc.README shc.html
%_mandir/man?/*

%changelog
* Wed Oct 22 2008 Ilya Mashkin <oddity@altlinux.ru> 3.8.6-alt1
- 3.8.6

* Mon Jul 18 2005 Alex Yustasov <yust@altlinux.ru> 3.8.3-alt1
- 3.8.3

* Wed Jan 26 2005 Alex Yustasov <yust@altlinux.ru> 3.7-alt1
- initial release
