Name: samefile
Version: 2.13
Release: alt1
Summary: Command-line utility to find identical files on the file system

Group: File tools
License: BSD
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://www.schweikhardt.net/samefile/
Source0: http://www.schweikhardt.net/%name-%version.tar.gz

BuildRequires: gcc gcc-c++

%description
The samefile utility finds files with identical contents, independent of file
name. This program is for you if you are notoriously low on disk space, keep
exceeding your disk quota, pay for your storage by the megabyte, run any kind
of file server, need to reduce the size of your backups, or just want to get
a feeling for how much redundant files are there on your system.

%prep
%setup

%build
%configure
make %{?_smp_mflags}

%check
make test

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc README ChangeLog
%_bindir/%name
%_mandir/man1/%name.1*

%changelog
* Tue Apr 10 2012 Ilya Mashkin <oddity@altlinux.ru> 2.13-alt1
- 2.13

* Fri Sep 5 2008 Vivek Shah <boni.vivek at gmail.com> 2.12-3
- Fixed SOURCE0 URL

* Mon Aug 25 2008 Vivek Shah <boni.vivek at gmail.com> 2.12-2
- Added self check and ChangeLog file

* Thu Aug 21 2008 Vivek Shah <boni.vivek at gmail.com> 2.12-1
- Initial Package
