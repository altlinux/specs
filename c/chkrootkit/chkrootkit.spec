Name: chkrootkit
Version: 0.58b
Release: alt1

Summary: Check rootkits
Summary(ru_RU.UTF-8): Поиск троянских коней и закладок в программах

License: BSD-2-Clause
Group: Monitoring
Url: http://www.chkrootkit.org/

Source: ftp://ftp.pangeia.com.br/pub/seg/pac/%name-%version.tar.gz
Patch0: chkrootkit-alt-libpath.patch

BuildRequires: glibc-devel-static

Requires: binutils coreutils findutils sed gawk grep net-tools procps crontabs
Requires: /usr/bin/ssh

%define cron_daily %_sysconfdir/cron.daily

%description
chkrootkit is a tool to locally check for signs of a rootkit.
It contains:

* chkrootkit: shell script that checks system binaries for
  rootkit modification.
* ifpromisc: checks if the network interface is in promiscuous mode.
* chklastlog: checks for lastlog deletions.
* chkwtmp: checks for wtmp deletions.
* chkproc: checks for signs of LKM trojans.
* chkdirs: checks for signs of LKM trojans.
* strings: quick and dirty strings replacement.
* chkutmp: checks for utmp deletions.

%description -l ru_RU.UTF-8
Chkrootkit является набором утилит для поиска троянских коней и закладок
по набору сигнатур в программах на локальном компьютере.

%prep
%setup
%patch0 -p2
subst 's|@CHKROOTKIT_DIR@|%_libdir/%name|' %name

%build
make sense CC="%{__cc} $RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64"

%install
install -Dpm0755 chkrootkit %buildroot%_sbindir/chkrootkit

for p in \
	check_wtmpx  \
    chkdirs  \
    chklastlog  \
    chkproc  \
    chkutmp \
    chkwtmp  \
    ifpromisc  \
    strings-static \
    ; do
	install -pD -m 755 "$p" "%buildroot%_libdir/%name/$p"
done

mkdir -p %buildroot%cron_daily
cat > %buildroot%cron_daily/%name << __EOF__
%_sbindir/%name -q
__EOF__

%files
%doc COPYRIGHT ACKNOWLEDGMENTS README README.chklastlog README.chkwtmp chkrootkit.lsm
%_sbindir/*
%_libdir/%name
%attr(700,root,root) %cron_daily/%name

%changelog
* Fri Mar 01 2024 Andrey Cherepanov <cas@altlinux.org> 0.58b-alt1
- New version.

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.50-alt1
- Version 0.50

* Sat Aug 08 2009 Slava Semushin <php-coder@altlinux.ru> 0.49-alt1
- Updated to 0.49

* Tue Oct 14 2008 Slava Semushin <php-coder@altlinux.ru> 0.48-alt2
- Added Packager tag (noted by repocop)

* Mon Mar 10 2008 Slava Semushin <php-coder@altlinux.ru> 0.48-alt1
- Updated to 0.48 (#12777)
- Fixed tools location on x86_64 architecture (#13141)
- Fixed owner and group of /etc/cron.daily/chkrootkit script
- Spec cleanup

* Mon Feb 28 2005 Ilya Evseev <evseev@altlinux.ru> 0.45-alt1
- 0.45, revisited patchset:
  + P0 changed,
  + P1 removed (already in upstream)

* Fri Sep 10 2004 Ilya Evseev <evseev@altlinux.ru> 0.44-alt3
- ifpromisc.c was incompatible with glibc-kernheaders

* Fri Sep  6 2004 Ilya Evseev <evseev@altlinux.ru> 0.44-alt2
- 0.44
- specfile changes for ALT conventions
- diet libc is now used by default, use 'rpmbuild --rebuild --with glibc ...'
  for compiling against glibc-static
- omit error messages when chfn and chsh are not installed
- add cron.daily record

* Wed Jul 28 2004 Per ц≤yvind Karlsen <peroyvind@linux-mandrake.com> 0.43-1mdk
- 0.43
- regenerate P0
- drop useless prefix

* Sat Dec  6 2003 Frederic Lepied <flepied@mandrakesoft.com> 0.42b-1mdk
- rediff patch0
- 0.42b

* Tue Jul 01 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.41-1mdk
- 0.41
- added rediffed patch by David Coe, thanks man!
- build statically against dietlibc per default (mr. lint hates this...)
- misc spec file fixes

* Sat Apr 05 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.40-1mdk
- 0.40
- use spec file magic to enable builds against dietlibc

* Fri Jan 31 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.39-1mdk
- 0.39
- rediff P0

* Mon Jan 27 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.38-2mdk
- build release

* Sun Dec 29 2002 Frederic Lepied <flepied@mandrakesoft.com> 0.38-1mdk
- new version

* Wed Sep 18 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.37-1mdk
- new version
- rediff
- misc spec file fixes

* Thu Jul  4 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.36-1mdk
- new version
- added md5 file (S1)

* Mon Jan 21 2002 Frederic Lepied <flepied@mandrakesoft.com> 0.35-1mdk
- 0.35

* Wed May  9 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.32-1mdk
- first version.

# end of file
