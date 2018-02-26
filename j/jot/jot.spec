Name: jot
# wget -qO- 'http://www.freebsd.org/cgi/cvsweb.cgi/~checkout~/src/usr.bin/jot/jot.c' | sed -n '\@src/usr.bin/jot/jot.c,v @s@.*,v \([0-9.]*\).*@\1@p'
Version: 1.42
Release: alt1
# svn checkout svn://svn.freebsd.org/base/head/usr.bin/jot
Source: %name-%version.tar
Patch: %name-urandom.patch
URL: http://www.freebsd.org/cgi/cvsweb.cgi/src/usr.bin/%name
Packager: Fr. Br. George <george@altlinux.ru>
Summary: jot is a simple tool that prints random or sequential data
Summary (ru_RU.KOI8-R): Выводит данные по возрастанию, убыванию по одному элементу на строку
License: BSD
Group: Text tools

%description
Jot prints numbers, in arithmetic sequence or according to some simple
random generators.

%description -l ru_RU.KOI8-R
Athena jot (или просто jot) выводит данные, обычно числа, по возрастанию, убыванию, произвольные или повторяющиеся, по одному элементу на строку.

Эта крошечная программа, написанная на С, очень полезна в сценариях.

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
* Tue May 10 2011 Fr. Br. George <george@altlinux.ru> 1.42-alt1
- Version up

* Sun Sep 05 2010 Fr. Br. George <george@altlinux.ru> 1.41-alt1
- Version up

* Thu Nov 08 2007 Fr. Br. George <george@altlinux.ru> 1.37-alt1
- Initial build for ALT

