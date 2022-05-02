# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name:		burp
Version:	3.1.0
Release:	alt1
Summary:	Burp is a network-based backup and restore program
License:	AGPL-3.0 and BSD and GPLv2+ and LGPLv2+
Group:		Archiving/Backup
Url:		https://burp.grke.org/
Vcs:		https://github.com/grke/burp.git

%add_findreq_skiplist %_datadir/%name/scripts/*

Source:		%name-%version.tar
BuildRequires:  check
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  libcheck-devel
BuildRequires:  libncurses-devel
BuildRequires:  librsync-devel
BuildRequires:  libtool
BuildRequires:  libuthash-devel
BuildRequires:  libyajl-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

%description
Burp is a network backup and restore program, using client and server.
It uses librsync in order to save network traffic and to save on the
amount of space that is used by each backup.

# 2.5.4: client_protocol1_backup_phase2 test fails with lto
# and librsync >= 2.0.1
%define optflags_lto %nil

%prep
%setup

# Replace implicit root user with _burp user and readall=1.
sed -i  -e 's/# \(user\|group\)=\(nogroup\|graham\)/\1 = _burp/' \
	-e 's/# readall=1/readall = 1/' \
	-e 's/=\/home/ = \/boot/' \
	-e 's/\(exclude_comp\)=/\1 = /' \
	configs/*/burp.conf.in

%build
%define _localstatedir %_var
%add_optflags -Wno-error=unused-variable
%autoreconf
%configure \
    --sysconfdir="%_sysconfdir/burp" \
    --disable-static

%make_build

%install
%makeinstall_std install-all
install -D -p -m 0755 .gear/burp.init %buildroot%_initrddir/burp-server
install -D -p -m 0644 .gear/burp.service %buildroot%_unitdir/burp-server.service
%__subst "s,password,#password,g" %buildroot%_sysconfdir/burp/clientconfdir/testclient

%check
if ! %make_build check; then
	cat test-suite.log
	exit 1
fi
.gear/test-burp.sh

%files
%doc %_docdir/%name/
%_initrddir/burp-server
%_unitdir/burp-*.*
%dir %_datadir/%name/
%_datadir/%name/scripts/
%_bindir/vss_strip
%_sbindir/*
%_man8dir/*
%defattr(640,root,_burp,0770)
%dir %_spooldir/%name/
%defattr(640,root,_burp,3770)
%dir %_sysconfdir/burp/
%dir %_sysconfdir/burp/CA-client/
%dir %_sysconfdir/burp/clientconfdir/
%dir %_sysconfdir/burp/clientconfdir/incexc/
%config(noreplace) %_sysconfdir/burp/*.c*nf
%config(noreplace) %_sysconfdir/burp/clientconfdir/testclient
%config(noreplace) %_sysconfdir/burp/clientconfdir/incexc/example

%pre
/usr/sbin/groupadd -r -f _burp
/usr/sbin/useradd -r -g _burp -d /var/empty -s /dev/null -n -c "BURP BackUp and Restore Program" _burp >/dev/null 2>&1 ||:

%post
%post_service burp-server

%preun
%preun_service burp-server

%changelog
* Mon May 02 2022 Vitaly Chikunov <vt@altlinux.org> 3.1.0-alt1
- Update to 3.1.0 (2022-04-30).
- Remove protocol 2.

* Wed Jan 12 2022 Egor Ignatov <egori@altlinux.org> 2.5.4-alt2
- Disable LTO: client_protocol1_backup_phase2 test fails
  with librsync >= 2.0.1

* Fri Sep 03 2021 Vitaly Chikunov <vt@altlinux.org> 2.5.4-alt1
- Update to 2.5.4 (2021-08-14).

* Sat Jul 03 2021 Vitaly Chikunov <vt@altlinux.org> 2.5.2-alt1
- Update to 2.5.2 (2021-07-02).
- Make burp configs non-root by default.

* Tue May 11 2021 Vitaly Chikunov <vt@altlinux.org> 2.4.0-alt1
- Update to 2.4.0 (2021-04-01).

* Sun Nov 08 2020 Vitaly Chikunov <vt@altlinux.org> 2.3.38-alt1
- Update to 2.3.38 (2020-11-06).

* Sun Oct 18 2020 Vitaly Chikunov <vt@altlinux.org> 2.3.36-alt1
- Update to 2.3.36 (2020-09-29).

* Wed Sep 02 2020 Vitaly Chikunov <vt@altlinux.org> 2.3.34-alt1
- Update to 2.3.34 (2020-09-01).

* Fri Aug 07 2020 Vitaly Chikunov <vt@altlinux.org> 2.3.32-alt1
- Update to 2.3.32 (2020-07-31).

* Tue Jul 07 2020 Vitaly Chikunov <vt@altlinux.org> 2.3.30-alt1
- Update to 2.3.30 (2020-07-03).

* Tue May 05 2020 Vitaly Chikunov <vt@altlinux.org> 2.3.26-alt1
- Update to 2.3.26.

* Thu Feb 13 2020 Vitaly Chikunov <vt@altlinux.org> 2.3.22-alt1
- Update to 2.3.22.
- Overwrite our `readall=' support with upstream version.

* Wed Feb 12 2020 Vitaly Chikunov <vt@altlinux.org> 2.3.16-alt3
- Remove parasite dependencies from optional scripts.

* Fri Dec 06 2019 Vitaly Chikunov <vt@altlinux.org> 2.3.16-alt2
- Adjust chkconfig runlevels so that server isn't enabled by default
- Make _burp:_burp user and configs owned by root:_burp
- Fix setgid if group= is not specified
- Add small functionality test

* Mon Nov 25 2019 Vitaly Chikunov <vt@altlinux.org> 2.3.16-alt1
- New version 2.3.16
- Fix license string
- Fix compatibility with openssl-1.1.1
- Implement support of keeping readall capabilities

* Tue Oct 01 2019 Vitaly Chikunov <vt@altlinux.org> 2.3.14-alt1
- New version 2.3.14

* Wed Apr 03 2019 Vitaly Chikunov <vt@altlinux.org> 2.3.4-alt1
- New version 2.3.4

* Fri Mar 15 2019 Vitaly Chikunov <vt@altlinux.org> 2.3.2-alt1
- new version 2.3.2

* Wed Feb 20 2019 Vitaly Chikunov <vt@altlinux.org> 2.3.0-alt1
- Update to 2.3.0-12-g3d093f25

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 2.2.4-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Wed Jun 06 2018 Vitaly Chikunov <vt@altlinux.org> 2.2.4-alt1
- Update to version 2.2.4

* Thu Apr 19 2018 Vitaly Chikunov <vt@altlinux.org> 2.1.32-alt2
- Fix init script
- Secure permissions for configs that supposed to contain passwords

* Sun Apr 15 2018 Vitaly Chikunov <vt@altlinux.org> 2.1.32-alt1
- Respec for 2.1.32
- Install init scripts

* Tue Dec 05 2017 Vitaly Lipatov <lav@altlinux.ru> 2.1.24-alt1
- new version 2.1.24 (with rpmrb script)

* Wed Aug 10 2016 Vitaly Lipatov <lav@altlinux.ru> 2.0.44-alt1
- initial build for ALT Linux Sisyphus

