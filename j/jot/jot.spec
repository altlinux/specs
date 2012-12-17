Name: jot
Version: 1.43
Release: alt1
Source: jot-1.43.tar
Patch: %name-urandom.patch
Url: http://www.freebsd.org/cgi/cvsweb.cgi/src/usr.bin/jot
Summary: jot is a simple tool that prints random or sequential data
Summary (ru_RU.UTF-8): Выводит данные по возрастанию, убыванию по одному элементу на строку
License: BSD
Group: Text tools

%description
Jot prints numbers, in arithmetic sequence or according to some simple
random generators.

%description -l ru_RU.UTF-8
Athena jot (или просто jot) выводит данные, обычно числа, по
возрастанию, убыванию, произвольные или повторяющиеся, по одному
элементу на строку.

%prep
%setup
%patch -p1

%build
cc -D'__FBSDID(x)=' -D'arc4random()=random()' -O2 %name.c -o %name

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir
install -s -m755 %name %buildroot%_bindir/
install %name.1 %buildroot%_man1dir/

%files
%_bindir/%name
%_man1dir/%name.*

%changelog
* Thu Dec 13 2012 Fr. Br. George <george@altlinux.ru> 1.43-alt1
- Autobuild version bump to 1.43 (no code changed, just version up)
- Recode spec from koi8-r to utf8

* Wed Jul 27 2011 Fr. Br. George <george@altlinux.ru> 1.42-alt2
- Using autobuild scheme

* Tue May 10 2011 Fr. Br. George <george@altlinux.ru> 1.42-alt1
- Version up

* Sun Sep 05 2010 Fr. Br. George <george@altlinux.ru> 1.41-alt1
- Version up

* Thu Nov 08 2007 Fr. Br. George <george@altlinux.ru> 1.37-alt1
- Initial build for ALT

