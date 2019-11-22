Name: pesign
Version: 0.109
Release: alt7

Summary: Signing tool for PE-COFF binaries
License: GPLv2
Group: Development/Other

Url: https://github.com/vathpela/pesign
# git://git.altlinux.org/gears/p/pesign.git
Source: %name-%version-%release.tar
Patch0: pesign-0.109-warnings.patch
Patch1: pesign-fix-build-with-nss3.44.patch

BuildRequires: libnss-devel libpopt-devel

%description
This package contains the pesign utility for signing UEFI binaries
as well as other associated tools.

%prep
%setup -n %name-%version-%release
%patch0 -p1
%patch1 -p1
%ifarch %e2k
# lcc 1.23.20 doesn't do that
sed -i 's,-fshort-wchar,,g' Make.defaults util/Makefile
%endif

%build
%make_build OPTFLAGS='%optflags'

%install
%makeinstall_std LIBDIR=%_libdir MACROS_DIR=%_rpmmacrosdir
mv %buildroot%_rpmmacrosdir/{macros.,}pesign
%makeinstall_std -C src install_systemd install_sysvinit \
	INIT_DIR=%_initdir \
	UNIT_DIR=%_unitdir \
	TMPFILES_DIR=%_tmpfilesdir \
	#
install -pm644 README %buildroot%_docdir/pesign/
mksock -m666 %buildroot%_runtimedir/pesign/socketdir/socket
touch %buildroot%_runtimedir/pesign.pid

# there's some stuff that's not really meant to be shipped yet
rm -r %buildroot%_includedir/libdpe
rm %buildroot%_libdir/libdpe*

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
%_docdir/pesign/
%_bindir/pesign
%_bindir/pesign-client
%_bindir/efikeygen
%config(noreplace) %_sysconfdir/popt.d/pesign.popt
%_rpmmacrosdir/pesign
%_mandir/man?/*
%_tmpfilesdir/pesign.conf
%_initdir/pesign
%_unitdir/pesign.service
%dir %attr(750,root,pesign) %_runtimedir/pesign/
%dir %_runtimedir/pesign/socketdir/
%ghost %_runtimedir/pesign/socketdir/socket
%ghost %_runtimedir/pesign.pid

# NB: pesign 0.113 moved to GPLv3+

%changelog
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
