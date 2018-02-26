Name: dnstracer
Version: 1.9
Release: alt1

Summary: A tool to trace DNS queries
License: BSD
Group: Networking/Other
Url: http://www.mavetju.org/unix/general.php

Packager: Evgenii Terechkov <evg@altlinux.ru>

Source: http://www.mavetju.org/download/dnstracer-%version.tar.gz

%description
dnstracer determines where a given Domain Name Server (DNS) gets its
information from, and follows the chain of DNS servers back to the
servers which know the data.

%prep
%setup

%build
%configure
%make

%install
%makeinstall

%files
%doc CHANGES CONTACT LICENSE README
%doc %_man8dir/*
%_bindir/*

%changelog
* Tue Sep  9 2008 Terechkov Evgenii <evg@altlinux.ru> 1.9-alt1
- 1.9

* Fri Dec 03 2004 Andrei Bulava <abulava@altlinux.ru> 1.8-alt1
- initial build for ALT Linux; based on specfile by Dag Wieers

