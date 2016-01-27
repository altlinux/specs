Name: imapsync
Version: 1.670
Release: alt1

Summary: Tool to migrate email between IMAP servers

License: GPLv2
Group: Networking/Mail
Url: https://fedorahosted.org/imapsync/

Packager: Boris Savelev <boris@altlinux.org>
Source: https://fedorahosted.org/released/imapsync/%name-%version.tar
BuildArch: noarch

BuildRequires: perl-Mail-Box
BuildRequires: perl-devel
BuildRequires: perl-Mail-IMAPClient
BuildRequires: perl-Date-Manip
BuildRequires: perl-podlators
BuildRequires: perl(Data/Uniqid.pm)
BuildRequires: perl(File/Copy/Recursive.pm)
BuildRequires: perl(IO/Socket/INET6.pm)
BuildRequires: perl(IO/Tee.pm)
BuildRequires: perl(Term/ReadKey.pm)
BuildRequires: perl(Test/Pod.pm)
BuildRequires: perl(Unicode/String.pm)

%description
imapsync is a tool for facilitating incremental recursive IMAP
transfers from one mailbox to another. It is useful for mailbox migration,
and reduces the amount of data transferred by only copying messages that
are not present on both servers. Read, unread, and deleted flags are preserved,
and the process can be stopped and resumed. The original messages can
optionally be deleted after a successful transfer.

%prep
%setup

%install
%makeinstall_std

%files
%doc ChangeLog CREDITS TODO README FAQ
%_bindir/%name
%_man1dir/%name.*

%changelog
* Mon Dec 28 2015 Lenar Shakirov <snejok@altlinux.ru> 1.670-alt1
- new version

* Fri Sep 07 2012 Vitaly Lipatov <lav@altlinux.ru> 1.504-alt1
- new version 1.504 (with rpmrb script)
- cleanup spec

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 1.337-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Aug 02 2010 Boris Savelev <boris@altlinux.org> 1.337-alt1
- new version
- fix build

* Thu Nov 12 2009 Boris Savelev <boris@altlinux.org> 1.286-alt1
- new version

* Tue Nov 11 2008 Boris Savelev <boris@altlinux.org> 1.255-alt1
- build from Fedora

* Fri Aug  8 2008 Lubomir Rintel <lkundrak@v3.sk> - 1.255-3
- Attempt to patch around too new Mail::IMAPClient

* Wed Aug  6 2008 Marek Mahut <mmahut@fedoraproject.org> - 1.255-2
- Upstream release

* Tue May 27 2008 Marek Mahut <mmahut@fedoraproject.org> - 1.252-2
- Upstream release
- Dependency fix (BZ#447800)

* Thu Apr 10 2008 Marek Mahut <mmahut@fedoraproject.org> - 1.249-1
- Initial build.
