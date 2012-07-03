%define _unpackaged_files_terminate_build 1

Name: cyrus2dovecot
Version: 1.2
Release: alt1

Summary: Cyrus to dovecot migration tool
License: GPL or Artistic
Group: Networking/Mail
Url: http://www.cyrus2dovecot.sw.fu-berlin.de/
BuildArch: noarch

Packager: Maxim Ivanov <redbaron@altlinux.org>

Source0: cyrus2dovecot-1.2.tar

%description
Cyrus2Dovecot is a full-featured command line tool for converting the e-mails
of one or more users from Cyrus format to Dovecot Maildir++  folders. It
allows for performing a server transition which is fully transparent to both
POP and IMAP users. 

For details, see perldoc documentation (just run perldoc %name).

%prep
%setup 

%install
install -m755 -D  %name %buildroot%_bindir/%name

%files 
%_bindir/*

%changelog
* Sun May 17 2009 Maxim Ivanov <redbaron at altlinux.org> 1.2-alt1
- Initial build for Sisyphus 


