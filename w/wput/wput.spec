%define _unpackaged_files_terminate_build 1

Summary: A utility for putting files using the FTP protocol from the command line
Name: wput
Version: 0.6.1
Release: alt2
License: GPL
Group: Networking/WWW
URL: http://wput.sourceforge.net

Source: %name-%version.tar

Patch1: %name-%version-alt-fno-common.patch

%description
wput is a tiny program that looks like wget and is designed to upload files
or whole directories to remote ftp-servers.

%prep
%setup
%patch1 -p2

%build
%configure --prefix=%buildroot%prefix --disable-g-switch
%make

%install
install -d -m 0755 %buildroot%_bindir
install -d -m 0755 %buildroot%_man1dir
%makeinstall
gunzip -c %buildroot%_mandir/wput.1.gz > %buildroot%_man1dir/wput.1
rm -f %buildroot%_mandir/wput.1.gz

%find_lang %name

%files -f %name.lang
%doc ChangeLog COPYING INSTALL TODO doc
%_man1dir/*
%_bindir/%name

%changelog
* Mon Dec 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt2
- Fixed build with -fno-common.

* Mon Sep 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt1
- Updated to upstream version 0.6.1.

* Fri Sep 29 2006 Mikhail Pokidko <pma@altlinux.ru> 0.6-alt1
- Initial build

