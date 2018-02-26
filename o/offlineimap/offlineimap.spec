Name: offlineimap
Version: 6.0.0
Release: alt1.1.1
Summary: Powerful IMAP/Maildir synchronization and reader support

License: GPLv2+
Group: Networking/Mail
Url: http://software.complete.org/offlineimap/
Source0: %version/%{name}_%version.tar.gz
Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch

# Automatically added by buildreq on Sun May 11 2008
BuildRequires: docbook-utils python-devel

%description
OfflineIMAP is a tool to simplify your e-mail reading. With OfflineIMAP,
you can read the same mailbox from multiple computers.  You get a
current copy of your messages on each computer, and changes you make one
place will be visible on all other systems. For instance, you can delete
a message on your home computer, and it will appear deleted on your work
computer as well. OfflineIMAP is also useful if you want to use a mail
reader that does not have IMAP support, has poor IMAP support, or does
not provide disconnected operation.

%prep
%setup -n %name

%build
python setup.py build
cp -p debian/changelog ChangeLog
docbook2man %name.sgml

%install
python setup.py install --root=%buildroot --prefix=%prefix
mkdir -p %buildroot/%_man1dir
install -p %name.1 %buildroot/%_man1dir/

%files
%_bindir/%name
%python_sitelibdir/%name/
%python_sitelibdir/%name-%version-py*.egg-info
%_man1dir/%name.1.*

%doc README COPY* UPGRADING %name.conf* FAQ.html ChangeLog

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 6.0.0-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.0.0-alt1.1
- Rebuilt with python 2.6

* Sat Jul 19 2008 Terechkov Evgenii <evg@altlinux.ru> 6.0.0-alt1
- 6.0.0

* Sun May 11 2008 Terechkov Evgenii <evg@altlinux.ru> 5.99.14-alt1
- 5.99.14
- Initial build for ALT Linux Sisyphus (Thanks to Fedora for initial spec)

* Sun May 11 2008 Evgenii Terechkov <evg@altlinux.ru> 5.99.7-1
- spec macro abuse cleanup

* Tue Mar 04 2008 Till Maas <opensource till name> - 5.99.7-1
- Update to latest version

* Tue Mar 04 2008 Till Maas <opensource till name> - 5.99.6-1
- Update to latest version

* Mon Jan 07 2008 Till Maas <opensource till name> - 5.99.4-2
- add egg-info to %%files

* Sun Oct 21 2007 Till Maas <opensource till name> - 5.99.4-1
- update to new version

* Tue Sep 04 2007 Till Maas <opensource till name> - 5.99.2-1
- update to new version
- update license Tag
- add unclosed listitem in offlineimap.sgml
- add missing BR: docbook-utils
- build manpage
- remove todo and manual files from %%doc

* Sat Dec 09 2006 Till Maas <opensource till name> - 4.0.16-3
- rebuild for python2.5
- added BR: python-devel, which is needed now

* Mon Dec 04 2006 Till Maas <opensource till name> - 4.0.16-2
- added -p to cp to preserve timestamp of ChangeLog

* Sun Dec 03 2006 Till Maas <opensource till name> - 4.0.16-1
- version bump
- added one more %%{version} to Source0
- added FAQ.html, todo to %%doc
- added debian/changelog as ChangeLog to %%doc

* Sat Dec 02 2006 Till Maas <opensource till name> - 4.0.15-1
- added %%{?dist} tag
- made Source0 a valid URL
- rearranged tag order and changed whitespace
- added -q -n %%name to %%setup
- removed ChangeLog* from %%doc (not in archive)
- added offlineimap.conf* to %%doc
- Use %%{_bindir} and %%{python_sitelib}
- removed directory docs from %%doc
- added BuildArch: noarch
- added manpage

* Tue May 16 2006 Adam Spiers <adam@spiers.net> 4.0.13-3
- Force prefix to /usr

* Mon May 15 2006 Adam Spiers <adam@spiers.net> 4.0.13-2
- Finally get savemessage_searchforheader right?

* Sun May 14 2006 Adam Spiers <adam@spiers.net> 4.0.13-1
- Updated for 4.0.13

* Sat Apr 29 2006 Adam Spiers <offlineimap@adamspiers.org> 4.0.11-2
- Add patch for Groupwise IMAP servers.

* Fri Apr 28 2006 Adam Spiers <offlineimap@adamspiers.org> 4.0.11-1
- Initial build.
