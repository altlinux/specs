Name: dictd
Version: 1.12.1
Release: alt4
Serial: 1

Url: http://www.dict.org/
License: GPL

Source: %name-%version.tar.gz
Source2: dictd.init
Source3: dictdconfig
Source4: dictd.conf
Source5: dict.conf
Source6: dictd-control
Source7: dictd-README.ALT-ru_RU.UTF-8
Source8: dictd.service
Source9: dictd.filetrigger

Patch: %name-1.12.1-natspec.patch

Patch10: dict-1.9.15-alt-utf8.patch
Patch11: dict-1.9.11-alt-fix_utf.patch
Patch12: dictl-alt-params.path

# -------  dictd package description ----- #

Summary: dict server that serves dictionaries for clients
Summary(ru_RU.UTF-8): Сервер словарей, обслуживающий клиентов по протоколу dict
Group: System/Servers

# Automatically added by buildreq on Thu Sep 22 2005
BuildRequires: flex groff-base tetex-core tetex-dvips tetex-latex transfig zlib-devel
BuildRequires: libnatspec-devel >= 0.2.3
BuildRequires: libmaa-devel

%description
This package contains dictionary server that supports DICT clients
(Dictionary Server Protocol). There are many console and graphical DICT
clients. Here are some of them that are supported by ALT Linux
distributions:
* dict
* kdict
* gdict

%description -l ru_RU.UTF-8 -n dictd
Данный пакет содержит сервер словарей, поддерживающий DICT-клиентов
(Dictionary Server Protocol -- протокол сервера словарей). Существует много
консольных и графических DICT-клиентов. Вот некоторые из входящих в дистрибутивы
ALT Linux:
* dict
* kdict
* gdict

# -------- dict-tools description ------- #

%package -n dict-tools
# Name: dictd
Summary: tools for making dictionary files for dictd server
Summary(ru_RU.UTF-8): Средства для создания словарных файлов для сервера dictd
Group: Development/Other

%description -n dict-tools
This package contains various tools for creating and working with
dictionaries in dictd server format:
* dictzip(1) is a compression program which creates compressed files
  in the gzip format (see RFC 1952).
* dictfmt is program for making binary dictionaries from plain format

%description -n dict-tools -l ru_RU.UTF-8
Этот пакет содержит различные средства для создания словарей в формате
dictd и работы с ними:
* dictzip -- программа для сжатия словарей (см. RFC 1952).
* dictfmt -- программа для создание словарей в формате DICT из текстовых файлов.

# -------- dict-devel description ------- #
%package -n dict-devel
Summary: Headers for dictd server plugins
Summary(ru_RU.UTF-8): Заголовочные файлы для сборки модулей к серверу dictd
Group: Development/Other

%description -n dict-devel
This package contains header files for dictd server plugins

%description -n dict-devel -l ru_RU.UTF-8
Данный пакет содержит заголовочные файлы для сборки модулей к серверу dictd
# ------- dict description ------ #
%package -n dict
# Name: dictd
Summary: dict client
Summary(ru_RU.UTF-8): Консольный клиент для dictd-сервера
Group: Text tools

%description -n dict
This package contains console client for DICT server. It is light and
easy to use.

%description -n dict -l ru_RU.UTF-8
Данный пакет содержит консольный клиент для DICT-сервера. Он лёгок и
прост в работе.
# --------------- real part ----------------  #

%prep
%setup
%patch -p2
#%patch10 -p0
#%patch11 -p1
#%patch12 -p1
cp %SOURCE7 README.ALT-ru_RU.UTF-8

%build
%autoreconf
%configure --without-local-zlib --with-natspec
# FIXME: non-SMP-safe build as of 1.12.1
#make_build
make
%make -C doc/ rfc.txt

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_initdir
%makeinstall man1_prefix=%buildroot%_man1dir man8_prefix=%buildroot%_man8dir
install -p -m644 dict.1 %buildroot%_man1dir

install -p -m755 %SOURCE2 %buildroot%_initdir/%name
install -p -m755 -D %SOURCE3 %buildroot%_sbindir/dictdconfig
install -p -m644 -D %SOURCE4 %buildroot%_sysconfdir/%name.conf
install -p -m644 -D %SOURCE5 %buildroot%_sysconfdir/dict.conf
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_datadir/%name

# Dictionary default order
cat >%buildroot%_sysconfdir/dictd.order <<EOF
# You can arrange dictionaries' priority here
wn
engcom
foldoc
vera
web1913
jargon
elements
easton
hitchcock
gazetteer
%_datadir/%name/
EOF

mkdir -p %buildroot%_sysconfdir/sysconfig/
# Default configuration
cat >%buildroot%_sysconfdir/sysconfig/dictd <<EOF
# See %_sysconfdir/dictd.conf for additional restrictions
LISTENTO="--listen-to 127.0.0.1"
EXTRAOPTIONS="--locale ru_RU.UTF-8 \$LISTENTO"
EOF

install -D -m 755 %SOURCE6 %buildroot%_controldir/dictd
install -D %SOURCE8 %buildroot%_unitdir/dictd.service
install -D -m 755 %SOURCE9 %buildroot%_rpmlibdir/dictd.filetrigger

%pre
%_sbindir/groupadd -r dictd &>/dev/null ||:
%_sbindir/useradd -r -n -M -g dictd -d %_localstatedir/%name -s /dev/null dictd  &>/dev/null ||:

%post
if [ "$1" = "1" ]; then
	%_sbindir/dictdconfig -w
fi
%post_service %name

%preun
%preun_service %name

%files
%doc doc/rfc.txt README README.ALT-ru_RU.UTF-8
%config(noreplace) %_sysconfdir/dictd.conf
%config(noreplace) %_sysconfdir/dictd.order
%config(noreplace) %_sysconfdir/sysconfig/dictd
%_controldir/dictd
%_sbindir/dictd
%_sbindir/dictdconfig
%_man8dir/*
%_initdir/%name
%_datadir/%name
%_localstatedir/%name
%_unitdir/dictd.service
%_rpmlibdir/dictd.filetrigger

%files -n dict-tools
%_bindir/dict_lookup
%_bindir/dictfmt
%_bindir/dictunformat
%_bindir/dictzip
%_bindir/dictfmt_index2suffix
%_bindir/dictfmt_index2word
%_man1dir/dict_lookup.1*
%_man1dir/dictfmt.1*
%_man1dir/dictunformat.1*
%_man1dir/dictzip.1*
%_man1dir/dictfmt_index2suffix.1*
%_man1dir/dictfmt_index2word.1*

%files -n dict-devel
%_includedir/dictdplugin.h
%_bindir/dictdplugin-config

%files -n dict
%doc README
%config(noreplace) %_sysconfdir/dict.conf
%exclude %_bindir/dictl
%exclude %_man1dir/dictl.*
%_bindir/dict
%_bindir/colorit
%_man1dir/dict.1*
%_man1dir/colorit.1*

%changelog
* Mon Jan 01 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:1.12.1-alt4
- NMU: built actual dictd 1.12.1

* Mon Jan 09 2017 Michael Shigorin <mike@altlinux.org> 1:1.12.1-alt3
- NMU:
  + fixed FTBFS by turning the rest of manpage paths to globs
  + converted spec to UTF-8
  + disabled parallel build to be safe

* Wed Feb 04 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.12.1-alt2
- add dictd.filetrigger

* Thu Apr 18 2013 Fr. Br. George <george@altlinux.ru> 1:1.12.1-alt1
- Autobuild version bump to 1.12.1
- Add systemd service file

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1:1.9.15-alt5.qa1
- NMU: rebuilt for debuginfo.

* Sat Jan 12 2008 Vitaly Lipatov <lav@altlinux.ru> 1:1.9.15-alt5
- disable recode dependens: do not install dictl script and man
  (we already have transiterable recoding in dict)
- enable SMP build

* Wed Jan 24 2007 Vitaly Lipatov <lav@altlinux.ru> 1:1.9.15-alt4
- remove Obsoletes: dict
- add README.ALT
- add comments about listen ports to config

* Tue Jun 27 2006 Vitaly Lipatov <lav@altlinux.ru> 1:1.9.15-alt3
- NMU: fix bug #9720 (listen only 127.0.0.1 by default)
- move options for server to sysconfig/dictd
- add control facility for switch between local/server

* Mon Mar 13 2006 Vitaly Lipatov <lav@altlinux.ru> 1:1.9.15-alt2
- NMU: fix bug #9233 (use natspec patch instead iconv)
- cleanup spec (remove commented dictfmt, rearranged doc preparing)

* Tue Mar 07 2006 Vitaly Lipatov <lav@altlinux.ru> 1:1.9.15-alt1
- NMU: new version
- spec cleanup by rpmcs utils (use %%buildroot anywhere)
- fix path to dicts in dict.order (fix bug #6176 again, #8859)
- ALT's utf8 patch updated

* Thu Sep 22 2005 Vitaly Lipatov <lav@altlinux.ru> 1:1.9.11-alt2
- NMU: fix bugs #2651, #4123, #8000
- add dict.order (fix bug #6176)
- change /etc/ to %%_sysconfdir
- remove COPYING (it is GPL)

* Thu Jan 29 2004 Alexey Dyachenko <alexd@altlinux.ru> 1:1.9.11-alt1
- new version
- dict-devel subpackage
- dictunformat, dictfmt_index2suffix, dictfmt_index2word to dict-tools added
- dictl script added

* Fri Jun 20 2003 Alexey Dyachenko <alexd@altlinux.ru> 1:1.9.7-alt1
- new version
- add translation for german umlauts
- init script by aen
- fixed bug #0002612: missing full codepage in spec
- fixed bug #0002651: %_sysconfdir/dictd.conf isn't marked as %%config

* Thu Jan 30 2003 Alexey Dyachenko <alexd@altlinux.ru> 1:1.9.1-alt2
- build with standard dictfmt

* Tue Jan 21 2003 Alexey Dyachenko <alexd@altlinux.ru> 1:1.9.1-alt1
- new version
- fixed bug #0001704: service dictd condreload should be available
- start daemon with ru_RU.UTF-8 locale by default

* Mon Oct 14 2002 Alexey Dyachenko <alexd@altlinux.ru> 1:1.8.0-alt1
- new version with plug-in support
- map wrong characters to '?'
- fixed bug #0001279:  service dictd reload crush
- close feature request #0000843:  output not converted to locale charset (CP1251)

* Tue Sep 24 2002 Alexey Dyachenko <alexd@altlinux.ru> 1:1.7.1-alt1
- new version
- utf-8 patches for dictd from  Alexey Cheusov
- translation patch from utf8 to current encoding
- spec cleanup by Stanislav Ievlev

* Sun Mar 17 2002 Peter 'Nidd' Novodvorsky <nidd@alt-linux.org> 1.5.5-alt1
- fixed bug #625:  dictd server runs as a user with no name

* Sun Feb  6 2001 Peter 'Nidd' Novodvorsky <petya@logic.ru> 1.5.5-ipl2
- fixed bug in init script. Not supports chkconfig.

* Sun Feb  4 2001 Peter 'Nidd' Novodvorsky <petya@logic.ru> 1.5.5-ipl1
- initial release

