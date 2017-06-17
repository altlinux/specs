Name: msktutil
Version: 1.0
Release: alt1
Summary: Program for interoperability with Active Directory
Group: System/Base

License: GPLv2+
Url: https://sourceforge.net/p/msktutil/
Source0: %name-%version.tar

BuildRequires: openldap-devel gcc-c++ libkrb5-devel libsasl2-devel

%description
Msktutil is a program for interoperability with Active Directory that can
create a computer account in Active Directory, create a system Kerberos keytab,
add and remove principals to and from that keytab, and change the computer
account's password.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc README ChangeLog LICENSE
%_mandir/man1/*
%_sbindir/%name

%changelog
* Sat Jun 17 2017 Lenar Shakirov <snejok@altlinux.ru> 1.0-alt1
- Initial build for ALT (based on 1.0-2.fc26.src)

