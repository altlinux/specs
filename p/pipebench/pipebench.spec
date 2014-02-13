Name: pipebench
Version: 0.40
Release: alt3

Summary: Measures the speed of STDIN/STDOUT communication

License: GPLv2+
Group: Other
Url: http://www.habets.pp.se/synscan/programs.php?prog=%name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.habets.pp.se/synscan/files/%name-%version.tar

Source44: import.info

%description
Measures the speed of a pipe, by sitting in the middle passing the data along
to the next process. See the included README for example usage.

%prep
%setup

## Fix the Makefile; taken from the Gentoo ebuild and modified slightly.
sed -i Makefile \
	-e 's:CFLAGS=-Wall:CFLAGS+= -Wall:' \
	-e 's:$(CFLAGS) -o:$(LDFLAGS) &:g' \
	-e 's:/usr/local/bin/:$(DESTDIR)%_bindir:' \
	-e 's:/usr/local/man/man1/:$(DESTDIR)%_man1dir:'

%build
%make_build

%install
## Create the necessary filesystem skeleton.
mkdir -m 755 -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
%makeinstall_std

%files
%doc README
%_bindir/%name
%_man1dir/%name.*

%changelog
* Thu Feb 13 2014 Vitaly Lipatov <lav@altlinux.ru> 0.40-alt3
- cleanup spec
- initial update for ALT Linux Sisyphus

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1_9
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1_8
- initial fc import

