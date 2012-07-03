%define Name CreateTorrent
Name: createtorrent
Version: 1.1.4
Release: alt1.1
Summary: Create BitTorrent files from the command line
License: %gpl2only
Group: Networking/File transfer
URL: http://www.%name.com/
Source: %url/%name-%version.tar
Patch: %name-%version-%release.patch
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: libssl-devel

%description
%Name is a small and fast command line utility for all Linux
and Unix operating systems to create BitTorrent files easily.
BitTorrent files can be created from either one file or a collection of
files that are grouped together into a directory.


%prep
%setup
%patch -p1


%build
%define _optlevel s
%autoreconf
%configure
%make_build


%install
%make_install DESTDIR=%buildroot install


%files
%doc AUTHORS ChangeLog
%_bindir/*


%changelog
* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 1.1.4-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Mar 07 2009 Led <led@altlinux.ru> 1.1.4-alt1
- initial build
