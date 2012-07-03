Name: imapsync
Summary: Tool to migrate email between IMAP servers
Version: 1.337
Release: alt1.1
License: GPLv2
Group: Networking/Mail
Url: http://freshmeat.net/projects/imapsync/
Packager: Boris Savelev <boris@altlinux.org>
#Source: http://www.linux-france.org/prj/imapsync/dist/%name-%version.tgz
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: perl-Mail-Box
BuildRequires: perl-devel
BuildRequires: perl-Mail-IMAPClient
BuildRequires: perl-Date-Manip
BuildRequires: perl-podlators

%description
imapsync is a tool for facilitating incremental recursive IMAP
transfers from one mailbox to another. It is useful for mailbox migration,
and reduces the amount of data transferred by only copying messages that
are not present on both servers. Read, unread, and deleted flags are preserved,
and the process can be stopped and resumed. The original messages can
optionally be deleted after a successful transfer.

%prep
%setup

%build
%install
%makeinstall_std

%files
%doc ChangeLog CREDITS INSTALL TODO README FAQ
%_bindir/%name
%_man1dir/%name.*

%changelog
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
