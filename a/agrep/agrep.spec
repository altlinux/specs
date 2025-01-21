Name: agrep
Version: 3.41.5
Release: alt1

Summary: Approximate grep
License: ISC
Group: Text tools
URL: https://github.com/Wikinaut/agrep/
Vcs: https://github.com/Wikinaut/agrep.git

# NB: we have permission to redistribute agrep package
# with boxed distributions -- mike

Source: %name-%version.tar

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
%setup

%build
%make_build CFLAGS="%optflags -Wno-error=implicit-function-declaration -Wno-error=implicit-int -Wno-error=int-conversion -D__APPLE__ -DHAVE_DIRENT_H"

%install
install -pD -m755 agrep %buildroot%_bindir/agrep
install -pD -m644 agrep.1 %buildroot%_man1dir/agrep.1

%files
%doc COPYRIGHT README.md agrep.algorithms agrep.chronicle contribution.list
%_bindir/*
%_man1dir/*

%changelog
* Tue Jan 21 2025 Andrew A. Vasilyev <andy@altlinux.org> 3.41.5-alt1
- new version
- change building scheme

* Sun Feb 18 2018 Igor Vlasenko <viy@altlinux.ru> 2.04-alt1.qa2
- added URL: http://webglimpse.net (for distromap)

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.04-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Jun 08 2003 Michael Shigorin <mike@altlinux.ru> 2.04-alt1
- built for ALT Linux
- based on PLD spec;
  All persons listed below can be reached at <cvs_login>@pld.org.pl
  qboosh
  - which was in turn taken from some -contrib
  - based on spec by W.L.Estes <wlestes@hamlet.uncg.edu>
    and Peter Soos <sp@osb.hu>

