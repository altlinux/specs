# SPEC file for keyring-link utility: decrypt and dump PalmOS Keyring database

%define realversion 2.0-pre1

Name: keyring-link
Version: 2.0
Release: alt2.pre1.1.1.1

Summary: utility for export the Keyring for PalmOS database in text form
Summary(ru_RU.UTF-8): утилита экспорта базы Keyring для PalmOS в текстовый вид

License: GPL
Group: Communications
URL: http://gnukeyring.sourceforge.net/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%realversion.tar.gz
Patch0:  %name-2.0-pre1-alt-fix_for_pilot-link_0.12.1.patch

AutoReqProv: yes
BuildRequires: pilot-link-devel openssl-devel

%description
Keyring for PalmOS lets you securely  store secret information on
your PalmOS (PalmPilot, Visor, WorkPad)  handheld computer.  This
simple utility could be used to decrypt and dump all records from
Keyring for PalmOS ver. 1.0 and 2.0   Keys-Gtkr.pdb database into 
plain text form.

%description -l ru_RU.UTF-8
Keyring for PalmOS   позволяет хранить в безопасном виде  секретную
информацию на КПК с PalmOS (PalmPilot, Visor, WorkPad, Clie и пр.).
Данная простая  утилита может  быть использована для  расшифровки и 
вывода в текстовом виде всех записей из базы  Keys-Gtkr.pdb  версий 
Keyring for PalmOS 1.0 и 2.0.


%prep
%setup -q -n %name-%realversion
%patch0 
%__subst 's@../openssl-0.9.7@@' Makefile

%build
OPENSSL_HOME=/usr %make

%install
%__mkdir_p %buildroot%_bindir
%makeinstall DESTDIR=%buildroot 

%files 
%doc README
%_bindir/%name

%changelog
* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 2.0-alt2.pre1.1.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.0-alt2.pre1.1.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.0-alt2.pre1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Tue Dec 05 2006 Nikolay A. Fetisov <naf@altlinux.ru> 2.0-alt2.pre1
- Fix for build with pilot-link 0.12.1

* Sun Apr 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 2.0-alt1.pre1
- initial build for ALT Linux

