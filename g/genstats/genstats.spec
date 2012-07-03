Summary: Generate statistics on any textfile
Name: genstats
Version: 1.0.0
Release: alt1
License: GPL2
Group: Text tools
Source0: http://www.vanheusden.com/genstats/%name-%version.tgz
Url: http://www.vanheusden.com/genstats/

BuildRequires: gcc-c++

%description
Generates statistics on any textfile. With commandline parameters
which are very similar to those of the 'cut'-command, one can select
what part of the lines in a textfile should be counted. Genstats then
generates a table with the frequency of occurence of each string
together with the interval.

%prep
%setup
%build
make

%install
mkdir -p %buildroot{%_bindir,%_man1dir}
install -m 755 %name %buildroot%_bindir/%name
install -m 644 %name.1 %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Sat Sep  4 2010 Terechkov Evgenii <evg@altlinux.org> 1.0.0-alt1
- Initial build for ALT Linux Sisyphus

