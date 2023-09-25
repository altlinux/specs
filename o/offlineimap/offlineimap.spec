%define _unpackaged_files_terminate_build 1

%define _userunitdir %_prefix/lib/systemd/user

Name: offlineimap
Version: 8.0.0
Release: alt2

Summary: Powerful IMAP/Maildir synchronization and reader support

License: GPLv2+
Group: Networking/Mail
Url: http://offlineimap.org/

BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: asciidoc-a2x
BuildRequires: python3-module-distro
BuildRequires: python3-modules-sqlite3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

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

# fix setuptools deprecation warning
sed -i -e "s/description-file =/long_description = file:/" setup.cfg

%build
%pyproject_build
make -C docs man SPHINXBUILD='sphinx-build-3'

%install
%pyproject_install

mkdir -p %buildroot/%_man1dir
install -p docs/%name.1 %buildroot/%_man1dir/

mkdir -p %buildroot/%_userunitdir
install -p contrib/systemd/*.service contrib/systemd/*.timer -t %buildroot/%_userunitdir

%check
./offlineimap.py -V

%files
%doc COPYING %name.conf*
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}
%_userunitdir/*
%_man1dir/%name.1.*

%changelog
* Thu Sep 07 2023 Egor Ignatov <egori@altlinux.org> 8.0.0-alt2
- Migrate to pyproject macros
- Backport python3.11 compatibility patch
- Package systemd unit files

* Wed Aug 31 2022 Alexey Sheplyakov <asheplyakov@altlinux.org> 8.0.0-alt1
- Revived offlineimap, version 8.0.0 (Closes: #42236, #39793, #33735)
