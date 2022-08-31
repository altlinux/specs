Name: offlineimap
Version: 8.0.0
Release: alt1

Summary: Powerful IMAP/Maildir synchronization and reader support

License: GPLv2+
Group: Networking/Mail
Url: http://offlineimap.org/

BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: asciidoc-a2x
BuildRequires: python3-module-distro
BuildRequires: python3-module-setuptools
BuildRequires: python3-modules-sqlite3

# this is not a python module
AutoProv: no

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
%setup
%patch -p1

%build
%python3_build
make -C docs man SPHINXBUILD='sphinx-build-3'

%install
%python3_install --prefix=%prefix
%python3_prune

mkdir -p %buildroot/%_man1dir
install -p docs/%name.1 %buildroot/%_man1dir/

%check
./offlineimap.py -V

%files
%doc COPYING %name.conf*
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%name-%version-py*.egg-info
%_man1dir/%name.1.*

%changelog 
* Wed Aug 31 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 8.0.0-alt1
- Revived offlineimap, version 8.0.0 (Closes: #42236, #39793, #33735)
