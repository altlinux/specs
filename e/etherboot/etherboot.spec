%def_disable iso
%def_disable liso
%def_enable zdsk
%def_enable zlilo
%def_enable zpxe
%def_enable zrom
%def_with contrib

%define formats %{?_enable_iso: iso}%{?_enable_liso: liso}%{?_enable_zdsk: zdsk}%{?_enable_zlilo: zlilo}%{?_enable_zpxe: zpxe}%{?_enable_zrom: zrom}

%define Name Etherboot
Name: etherboot
Version: 5.4.3
Release: alt4
Summary: Boot ROM images for ethernet adapters
License: %gpl2plus
Group: Networking/Other
Url: http://%name.sourceforge.net
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: %name-%version-forcedeth.patch
Packager: Led <led@altlinux.ru>
ExclusiveArch: %ix86

BuildRequires(pre): rpm-build-licenses
%{?_enable_iso:BuildRequires: mkisofs}
%{?_enable_liso:BuildRequires: mkisofs mtools syslinux}

%description
%Name is a software package for creating ROM images that can
download code over an Ethernet network to be executed on an x86
computer. Many network adapters have a socket where a ROM chip can be
installed. %Name is code that can be put in such a ROM. %Name
is normally used for for booting PCs diskless.


%if_enabled iso
%package iso
Summary: %Name iso images
Group: Networking/Other

%description iso
%Name iso images.
%endif


%if_enabled zrom
%package zrom
Summary: %Name zrom images
Group: Networking/Other

%description zrom
%Name zrom images.
%endif


%if_with contrib
%package contrib
Summary: Some %name tools
Group: Networking/Other
AutoReq: no

%description contrib
Some programs to work with %name ROM images.
%endif


%prep
%setup
%patch0 -p1
%patch1 -p1
subst 's/\r$//' contrib/{wakeonlan/{readme.txt,wakeup.pl,mp-form*},hdload/hdload.S}
subst '1 s|^#!/perl/|#!/usr/|' contrib/wakeonlan/mp-form.pl
subst 's/-mcpu=/-mtune=/g' src/arch/i386/Config


%build
%define _optlevel s
%add_optflags -fno-stack-protector
echo CFLAGS+="%optflags" >> src/Config
# we don't use custom optimizations here because it can cause problems;
# parallel make not SMP-friendly
for f in %formats; do
    # can compile undi.c ONLY with -O1 (on gcc 4.3)
    %make -C src UNDIFLAGS="-O1" all${f}s
done
ln -s {index,about}.html
bzip2 --best --keep --force LOG


%install
install -d -m 0755 %buildroot%_libexecdir/%name
install -m 0755 src/util/*rom.pl %buildroot%_libexecdir/%name
for f in %formats; do
    install -d -m 0755 %buildroot%_datadir/%name/$f
    install -m 0644 src/bin/*.$f %buildroot%_datadir/%name/$f/
done

%if_with contrib
find contrib -type f \! -name '.*' -print |
while read F; do
    if [ -x "$F" -o $(basename "$F") != $(basename "$F" .pl) -o $(basename "$F") != $(basename "$F" .sh) ]; then
	install -pD -m 0755 "$F" %buildroot%_datadir/%name/"$F"
    else
	install -pD -m 0644 "$F" %buildroot%_datadir/%name/"$F"
    fi
done
%endif


%files
%doc Copyrights LOG.* RELNOTES about.html eb.png style.css
%_libexecdir/%name
%dir %_datadir/%name
%{?_enable_zdsk:%_datadir/%name/zdsk}
%{?_enable_zlilo:%_datadir/%name/zlilo}
%{?_enable_zpxe:%_datadir/%name/zpxe}
%exclude %_datadir/%name/contrib


%if %enabled iso || %enabled liso
%files iso
%dir %_datadir/%name
%{?_enable_iso:%_datadir/%name/iso}
%{?_enable_liso:%_datadir/%name/liso}
%endif


%if_enabled zrom
%files zrom
%dir %_datadir/%name
%_datadir/%name/zrom
%endif


%if_with contrib
%files contrib
%dir %_datadir/%name
%_datadir/%name/contrib
%endif


%changelog
* Tue Nov 11 2008 Led <led@altlinux.ru> 5.4.3-alt4
- fixed build with gcc 4.3

* Mon Oct 27 2008 Led <led@altlinux.ru> 5.4.3-alt3
- fixed build

* Mon Oct 27 2008 Led <led@altlinux.ru> 5.4.3-alt2.1
- add Packager
- fixed License

* Tue Aug 07 2007 Led <led@altlinux.ru> 5.4.3-alt2
- fixed License
- removed %name-doc package (build separately)
- moved contrib from %_docdir/%name-%version/contrib to
  %_datadir/%name/contrib
- cleaned up spec
- build zroms
- cleaned up BuildRequires
- added %name-5.4.3-forcedeth.patch
- added %name-5.4.3-genliso.patch

* Tue Mar 06 2007 Grigory Milev <week@altlinux.ru> 5.4.3-alt1
- update to last version
- clean up specfile
- remove unneeded pathces.

* Sat Oct 14 2006 Michael Shigorin <mike@altlinux.org> 5.4.2-alt1
- fix build with SSP-enabled gcc4.1 (well link should be fixed
  properly but I feel it won't matter much for this package)

* Wed Apr 26 2006 Michael Shigorin <mike@altlinux.org> 5.4.2-alt0.2
- added ExclusiveArch since fixing x86_64 build is 
  out of question for a moment

* Thu Apr 20 2006 Michael Shigorin <mike@altlinux.org> 5.4.2-alt0.1
- 5.4.2 (NMU)

* Mon Mar 20 2006 Michael Shigorin <mike@altlinux.org> 5.4.1-alt0.1
- 5.4.1 (NMU)
  + fix build with recent gcc
- peek inside current Mandriva package
  + borrow gcc4 patch
  + rearrange %%install
  + re-clean-up resulting stuff
- separate doc subpackage
  + use common docdir
  + compress LOG
  + include gzipped PostScript docs
- updated buildrequires

* Tue Feb 24 2004 Grigory Milev <week@altlinux.ru> 5.3.6-alt1
- new version released

* Fri Oct  3 2003 Grigory Milev <week@altlinux.ru> 5.3.2-alt1
- new version released
- fix buildrequires

* Wed Oct 23 2002 Grigory Milev <week@altlinux.ru> 5.0.7-alt1
- new version released
- correct buildrequires
- remover perl from build requires

* Thu Jan  3 2002 Grigory Milev <week@altlinux.ru> 5.0.5-alt1
- new version released

* Thu Sep 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 5.0.4-alt2
- Minor specfile cleanup.
- Changed BuildArch.
- Updated requires and buildrequires.

* Tue Sep 25 2001 Grigory Milev <week@altlinux.ru> 5.0.4-alt1
- New version released

* Fri Jul 13 2001 Grigory Milev <week@altlinux.ru> 5.0.2-alt1
- First build for Sisyphus

