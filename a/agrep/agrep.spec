Name: agrep
Version: 2.04
Release: alt1

Summary: Approximate grep
License: distributable not for profit, free use
Group: Text tools

# NB: we have permission to redistribute agrep package
# with boxed distributions -- mike

Source0: ftp://ftp.cs.arizona.edu/agrep/%name-%version.tar.Z
Source1: %name-README.ALT

Summary(ru_RU.KOI8-R): "Нечеткий" grep
Summary(uk_UA.KOI8-U): "Неч╕ткий" grep
Summary(pl): Wersja grep dopuszczaj╠ca bЁЙdy

%description
Tool for fast text searching allowing errors. It's similar to egrep
(or grep or fgrep), but it is much more general and usually faster.

%description -l ru_RU.KOI8-R
Утилита семейства grep, позволяющая выполнять поиск по нечетко заданному
шаблону, приближенно напоминающему искомый результат.

%description -l uk_UA.KOI8-U
Утил╕та на кшталт grep, що дозволя╓ виконувати пошук за неч╕тко заданим
шаблоном, що дещо нагаду╓ результат, який потр╕бен.

%description -l pl
agrep jest narzЙdziem podobnym do grep, ale umo©liwia przeszukiwanie
przybli©one.

%prep
%setup -q

%build
%make_build CFLAGS="%optflags"

%install
install -pD -m755 agrep %buildroot%_bindir/agrep
install -pD -m644 agrep.1 %buildroot%_man1dir/agrep.1
install -pD -m644 %SOURCE1 $RPM_BUILD_DIR/%name-%version/README.ALT

%files
%doc COPYRIGHT README agrep.algorithms agrep.chronicle contribution.list
%doc README.ALT
%_bindir/*
%_mandir/man1/*

%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)
%changelog
* Sun Jun 08 2003 Michael Shigorin <mike@altlinux.ru> 2.04-alt1
- built for ALT Linux
- based on PLD spec; 
  All persons listed below can be reached at <cvs_login>@pld.org.pl
  qboosh
  - which was in turn taken from some -contrib
  - based on spec by W.L.Estes <wlestes@hamlet.uncg.edu>
    and Peter Soos <sp@osb.hu>

