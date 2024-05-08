%define _unpackaged_files_terminate_build 1

# build without man pages: no mandoc in Sisyphus
%def_without man

Name: pesign
Version: 116
Release: alt3

Summary: Signing tool for PE-COFF binaries
License: GPLv3
Group: Development/Other

Url: https://github.com/rhboot/pesign
Source: %name-%version-%release.tar

BuildRequires: libnss-devel
BuildRequires: libpopt-devel
BuildRequires: libefivar-devel
BuildRequires: libuuid-devel

%if_with man
#BuildRequires: mandoc
%endif

%description
This package contains the pesign utility for signing UEFI binaries
as well as other associated tools.

%prep
%setup -n %name-%version-%release

%if_without man
# disable mandoc
sed -i 's/mandoc/true/' Make.rules
%endif

# fix error: "_FORTIFY_SOURCE" redefined
sed -i -e 's/-D_FORTIFY_SOURCE=2//' Make.defaults

# fcf-protection works for i686 processor or newer
%ifarch i386 i486 i586
sed -i -e '/-fcf-protection/ s/full/none/' Make.defaults
%endif

%ifarch %e2k
# lcc 1.23.20 doesn't do that
sed -i 's,-fshort-wchar,,g' Make.defaults util/Makefile
%endif

# fix gcc10 issue:
#password.c:316:32: error: unknown option after '#pragma GCC diagnostic'
#  316 | #pragma GCC diagnostic ignored "-Wanalyzer-mismatching-deallocation"
#      |                                ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
%add_optflags -Wno-error=pragmas

%build
%make_build \
	OPTFLAGS='%optflags' \
	libexecdir=%_libexecdir \
	rundir=%_runtimedir

%install
%makeinstall_std \
	MACROS_DIR=%_rpmmacrosdir \
	libdir=%_libdir \
	libexecdir=%_libexecdir \
	rundir=%_runtimedir

mv %buildroot%_rpmmacrosdir/{macros.,}pesign

%makeinstall_std -C src install_systemd install_sysvinit \
	libexecdir=%_libexecdir \
	INIT_DIR=%_initdir \
	UNIT_DIR=%_unitdir \
	TMPFILES_DIR=%_tmpfilesdir \
	rundir=%_runtimedir

mkdir -pv %buildroot%_runtimedir/pesign/socketdir/
mksock -m666 %buildroot%_runtimedir/pesign/socketdir/socket
touch %buildroot%_runtimedir/pesign.pid

mkdir -pv %buildroot%_sysconfdir/sysconfig
cat > %buildroot%_sysconfdir/sysconfig/pesign <<EOF
# This is the environment file for pesign daemon.

EXTRAOPTIONS=
EOF

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
%doc README.md COPYING
%_bindir/pesign
%_bindir/pesign-client
%_bindir/pesum
%_bindir/efikeygen
%_bindir/authvar
%_bindir/pesigcheck
%dir %_libexecdir/pesign
%_libexecdir/pesign/pesign-authorize
%_libexecdir/pesign/pesign-rpmbuild-helper
%dir %_sysconfdir/pesign
%config(noreplace) %_sysconfdir/popt.d/pesign.popt
%config(noreplace) %_sysconfdir/pesign/groups
%config(noreplace) %_sysconfdir/pesign/users
%config(noreplace) %_sysconfdir/sysconfig/pesign
%_rpmmacrosdir/pesign
%if_with man
%_mandir/man?/*
%endif
%_tmpfilesdir/pesign.conf
%_initdir/pesign
%_unitdir/pesign.service
%dir %attr(750,root,pesign) %_runtimedir/pesign/
%dir %_runtimedir/pesign/socketdir/
%ghost %_runtimedir/pesign/socketdir/socket
%ghost %_runtimedir/pesign.pid

%changelog
* Wed May 08 2024 Egor Ignatov <egori@altlinux.org> 116-alt3
- pesign-client: fix 'could not access socket' error

* Tue Apr 02 2024 Egor Ignatov <egori@altlinux.org> 116-alt2
- efikeygen: Add support for RSA3072 and RSA4096
- pesign: Fix signature removal
- pesign: Fix not asking for token's password

* Thu Jul 13 2023 Egor Ignatov <egori@altlinux.org> 116-alt1
- new version 116 (Fixes: CVE-2022-3560)
  + rebase ALT commits
  + remove obsolete patches

* Tue Jan 19 2021 Nikolai Kostrigin <nickel@altlinux.org> 113-alt3
- Fix FTBFS with gcc10
  + add upstream-pesigcheck-remove-superfluous-type-settings patch

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
