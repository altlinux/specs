%define _unpackaged_files_terminate_build 1
Name: pesign
Version: 113
Release: alt2

Summary: Signing tool for PE-COFF binaries
License: GPLv3
Group: Development/Other

Url: https://github.com/vathpela/pesign
# git://git.altlinux.org/gears/p/pesign.git
Source: %name-%version-%release.tar
Patch1: pesign-fix-build-with-nss3.44.patch

BuildRequires: libnss-devel
BuildRequires: libpopt-devel
BuildRequires: libefivar-devel
BuildRequires: libuuid-devel

%description
This package contains the pesign utility for signing UEFI binaries
as well as other associated tools.

%prep
%setup -n %name-%version-%release
%patch1 -p1
sed -i '/^libexecdir/s/)libexec/)lib/' Make.defaults
%ifarch %e2k
# lcc 1.23.20 doesn't do that
sed -i 's,-fshort-wchar,,g' Make.defaults util/Makefile
%endif

%build
%make_build OPTFLAGS='%optflags'

%install
%makeinstall_std libdir=%_libdir MACROS_DIR=%_rpmmacrosdir
mv %buildroot%_rpmmacrosdir/{macros.,}pesign
%makeinstall_std -C src install_systemd install_sysvinit \
	INIT_DIR=%_initdir \
	UNIT_DIR=%_unitdir \
	TMPFILES_DIR=%_tmpfilesdir \
	#

mksock -m666 %buildroot%_runtimedir/pesign/socketdir/socket
touch %buildroot%_runtimedir/pesign.pid

#cleanup
rm -f %buildroot/etc/rpm/macros.pesign

%pre
getent group pesign >/dev/null || groupadd -r pesign
getent passwd pesign >/dev/null ||
	useradd -r -g pesign -d /var/empty -s /dev/null \
		-c 'PE-COFF signing service' pesign

%preun
%preun_service %name

%post
%post_service %name
# handle hasher
if [ $1 = 1 -a -d /.host -a -d /.in -a -d /.out ]; then
	chmod a+rX %_runtimedir/pesign/
fi

%files
%doc README COPYING
%_bindir/pesign
%_bindir/pesign-client
%_bindir/efikeygen
%_bindir/authvar
%_bindir/efisiglist
%_bindir/pesigcheck
%_libexecdir/pesign/pesign-authorize
%config(noreplace) %_sysconfdir/popt.d/pesign.popt
%config(noreplace) %_sysconfdir/pesign/groups
%config(noreplace) %_sysconfdir/pesign/users
%_rpmmacrosdir/pesign
%_mandir/man?/*
%_tmpfilesdir/pesign.conf
%_initdir/pesign
%_unitdir/pesign.service
%dir %attr(750,root,pesign) %_runtimedir/pesign/
%dir %_runtimedir/pesign/socketdir/
%ghost %_runtimedir/pesign/socketdir/socket
%ghost %_runtimedir/pesign.pid

%changelog
* Mon Jul 27 2020 Nikolai Kostrigin <nickel@altlinux.org> 113-alt2
- macros.pesign: remove strings duplicates

* Fri Apr 24 2020 Nikolai Kostrigin <nickel@altlinux.org> 113-alt1
- new version
  + rediff ALT patches
  + remove obsolete warnings patch
  + change license GPLv2 -> GPLv3

* Fri Nov 22 2019 Michael Shigorin <mike@altlinux.org> 0.109-alt7
- E2K: avoid lcc-unsupported option

* Tue Sep 10 2019 Andrey Cherepanov <cas@altlinux.org> 0.109-alt6
- Use upstream fix for build with nss >= 3.44.

* Tue Jun 13 2017 Sergey Novikov <sotor@altlinux.org> 0.109-alt5
- Commented KeyIdTemplate to fix warnings

* Mon Dec 16 2013 Michael Shigorin <mike@altlinux.org> 0.109-alt4
- macros.pesign: implement in-place signing

* Mon Dec 16 2013 Dmitry V. Levin <ldv@altlinux.org> 0.109-alt3
- %%post: removed redundant systemd-tmpfiles invocation.

* Mon Dec 16 2013 Michael Shigorin <mike@altlinux.org> 0.109-alt2
- Fixed my typo in macro file

* Mon Dec 02 2013 Dmitry V. Levin <ldv@altlinux.org> 0.109-alt1
- Initial revision, based on specs from mike@ and Fedora.
