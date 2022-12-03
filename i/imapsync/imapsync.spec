Name: imapsync
Version: 2.229
Release: alt1

Summary: Tool to migrate email between IMAP servers

License: NOLIMIT Public License
Group:   Networking/Mail
Url:     http://imapsync.lamiral.info/
#Url:     https://github.com/imapsync/imapsync

Packager: Boris Savelev <boris@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Patch1:  %name-1.977-alt-no_cpanminus.patch

BuildArch: noarch

# Manual Requires:
Requires: perl(IO/Socket/INET6.pm)

# Build requires:
BuildRequires:  perl(Data/Dumper.pm) perl(Data/Uniqid.pm)
BuildRequires:  perl(Digest/HMAC.pm) perl(Digest/HMAC_SHA1.pm) perl(Digest/MD5.pm)
BuildRequires:  perl(File/Copy/Recursive.pm)
BuildRequires:  perl(IO/Socket/SSL.pm) perl(IO/Socket/INET6.pm)
BuildRequires:  perl(IO/Tee.pm) perl(IPC/Open3.pm)
BuildRequires:  perl(JSON/WebToken.pm) perl(LWP/UserAgent.pm)
BuildRequires:  perl(Mail/IMAPClient.pm) perl(Sys/MemInfo.pm)
BuildRequires:  perl(Parse/RecDescent.pm) perl(Net/Ping.pm)
BuildRequires:  perl(Readonly.pm) perl(Term/ReadKey.pm)
BuildRequires:  perl(Test/MockObject.pm) perl(Test/More.pm) perl(Test/Pod.pm)
BuildRequires:  perl(Test/Fatal.pm) perl(Pod/Usage.pm) perl(Test/Requires.pm)
BuildRequires:  perl(Dist/CheckConflicts.pm) perl(Test/Mock/Guard.pm)
BuildRequires:  perl(URI/Escape.pm) perl(Unicode/String.pm)
BuildRequires:  perl(PAR/Packer.pm) perl(Class/Load.pm)
BuildRequires:  perl(CGI.pm) perl(Regexp/Common.pm) perl(Try/Tiny.pm)
BuildRequires:  perl(Unicode/String.pm) perl(URI/Escape.pm)
BuildRequires:  perl(Test/NoWarnings.pm) perl(Test/Deep.pm) perl(Test/Warn.pm)
BuildRequires:  perl(File/Tail.pm) perl(Encode/IMAPUTF7.pm)
Buildrequires:  perl(Proc/ProcessTable.pm)

%description
imapsync is a tool for facilitating incremental recursive IMAP
transfers from one mailbox to another. It is useful for mailbox migration,
and reduces the amount of data transferred by only copying messages that
are not present on both servers. Read, unread, and deleted flags are preserved,
and the process can be stopped and resumed. The original messages can
optionally be deleted after a successful transfer.

%prep
%setup
%patch0 -p1

%patch1

%install
mkdir W
%makeinstall_std

%files
%doc ChangeLog LICENSE CREDITS TODO README FAQ
%_bindir/%name
%_man1dir/%name.*

%changelog
* Sat Dec 03 2022 Nikolay A. Fetisov <naf@altlinux.org> 2.229-alt1
- New version

* Sun Aug 08 2021 Nikolay A. Fetisov <naf@altlinux.org> 2.140-alt1
- New version

* Tue Jun 15 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.977-alt1
- New version

* Sun Aug 04 2019 Nikolay A. Fetisov <naf@altlinux.org> 1.945-alt1
- New version

* Sat May 12 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.882-alt1
- New version

* Tue Mar 13 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.836-alt1
- New version

* Mon May 08 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.727-alt1
- New version
- Cleanup spec file
- Fix license

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
