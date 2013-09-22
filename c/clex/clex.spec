%def_disable debug

%define Name CLEX
Name: clex
Version: 4.6.6
Release: alt1
Summary: A file manager with a full-screen user interface
License: GPLv2+
Group: File tools
URL: http://www.%name.sk
Source: %url/download/%name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libncursesw-devel

%description
%Name (pronounced KLEKS) is a file manager with a full-screen user
interface. It displays directory contents including the file status
details and provides features like command history, filename insertion,
or name completion in order to help users to create commands to be
executed by the shell.
%Name is a versatile tool for system administrators and all users that
utilize the enormous power of the command line. Its unique one-panel
user interface enhances productivity and lessens the probability of
mistake. There are no built-in commands, %Name is an add-on to your
favorite shell.


%prep
%setup -q
%patch -p1


%build
%configure --enable-largefile
%make_build
gzip -9c ChangeLog > ChangeLog.gz


%install
%makeinstall_std


%files
%doc AUTHORS ChangeLog.* README
%_bindir/*
%_man1dir/*


%changelog
* Sun Sep 22 2013 Led <led@altlinux.ru> 4.6.6-alt1
- 4.6.6

* Tue Apr 07 2009 Led <led@altlinux.ru> 4.4-alt1
- 4.4

* Sun Mar 15 2009 Led <led@altlinux.ru> 4.2-alt1
- 4.2

* Sun Mar 15 2009 Led <led@altlinux.ru> 4.1-alt2
- Added xterm_title.patch from upstream

* Sun Mar 15 2009 Led <led@altlinux.ru> 4.1-alt1
- 4.1

* Sat Dec 27 2008 Led <led@altlinux.ru> 4.0-alt1
- 4.0

* Thu Jul 24 2008 Led <led@altlinux.ru> 3.18-alt1
- initial build
