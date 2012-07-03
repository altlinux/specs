Summary: A utility for putting files using the FTP protocol from the command line
Name: wput
Version: 0.6
Release: alt1
License: GPL
Group: Networking/WWW
URL: http://wput.sourceforge.net
Packager: Mikhail Pokidko <pma@altlinux.org>
Source: %name-%version.tgz

%description
wput is a tiny program that looks like wget and is designed to upload files
or whole directories to remote ftp-servers.

%prep
#setup -q -n %name
%setup -q

%build
%configure --prefix=%buildroot%prefix --disable-g-switch
%make

%install
install -d -m 0755 %buildroot%_bindir
install -d -m 0755 %buildroot%_man1dir
%makeinstall
mv %buildroot%_mandir/wput.1.gz %buildroot%_man1dir/
strip %buildroot%_bindir/%name

%files
%doc ChangeLog COPYING INSTALL TODO doc
%_man1dir/*.bz2
#prefix/share/locale/*
%_bindir/%name


%changelog
* Fri Sep 29 2006 Mikhail Pokidko <pma@altlinux.ru> 0.6-alt1
- Initial build

