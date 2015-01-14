%set_verify_elf_method relaxed
%def_disable libwrap

Name: tac_plus
Version: 4.0.4.28
Release: alt1
Epoch: 1
License: BSD
Group: System/Servers
Summary: TACACS+ server based on Cisco engineering release
Url: http://www.shrubbery.net/tac_plus/
Source:  tacacs-F%version.tar
Source1: tac_plus.conf
Source2: tac_plus.pamd
Source3: tac_plus.init
Source4: tac_plus.sysconfig
Source5: README
Source6: tac_plus.logrotate
Source7: tac_plus.service
Patch0: tacacs+-F4.0.4.28-k1.diff
Patch1: tacacs+-F4.0.4.28.diff

BuildRequires: flex gcc-c++ libpam-devel chrpath
%if_enabled libwrap
BuildRequires: libwrap-devel
%endif

%description
The base source for this TACACS+ package is Cisco's publicly available TACACS+
"developer's kit", for which we are grateful.

We needed a way to limit certain groups within the company from logging into
or getting enable access on certain devices. Access lists (ACLs) of a sort have
been added that match against the address of the device speaking with the
daemon.

Being paranoid, we also wanted to limit which hosts could connect to the
daemon. This can be done with tcp_wrappers via inetd, but this does not work if
the daemon is running standalone. So, calls to libwrap, the tcp_wrappers
library, have been added. For the source and more information about
tcp_wrappers, see Wietse Venema's site at http://www.porcupine.org/.

Along the way we have also added autoconf, expanded the manual pages,
cleaned-up various formatting and STD C nits, added PAM authentication support,
and fixed a few LP64 problems.

Of course we have also received some enchancement requests from users. One of
which was the addition of a host clause (per-host configuration). This has been
added; ported from Devrim Seral's implementation. See the documentation for
further information.

Note: this version have patch applied from http://bakacsin.ki.iif.hu/~kissg/pd/tac_plus/

%package devel
Summary: TAC Plus development files
Group: Development/C
Requires: %name = %version
%description devel
Development files for TAC Plus

%package -n libtacacs1
Summary: TACACS+ library
Group: Development/C
%description -n libtacacs1
This package contains TACACS+ library

%prep
%setup -n tacacs-F%version
%patch0 -p1 -b .k1
%patch1 -p1

%build
%configure --disable-static --enable-acls --enable-uenable --enable-maxsess --enable-debug --enable-mschap --enable-mschapdes \
%if_disabled libwrap
--without-libwrap
%endif

%make

%install
%makeinstall_std

mkdir -p %buildroot/{%_initdir,%_sysconfdir/{pam.d,sysconfig}}
install -m 640 %SOURCE1 %buildroot/%_sysconfdir/
install -m 644 %SOURCE2 %buildroot/%_sysconfdir/pam.d/%name
install -m 755 %SOURCE3 %buildroot/%_initdir/%name
install -m 644 %SOURCE4 %buildroot/%_sysconfdir/sysconfig/%name
install -m 644 %SOURCE5 .
install -pD -m644 %SOURCE6 %buildroot%_sysconfdir/logrotate.d/%name
install -pD -m644 %SOURCE7 %buildroot%_unitdir/%name.service
mkdir -p %buildroot%_logdir
touch %buildroot%_logdir/{tacwho.log,tac_plus.log,tac_plus.acct}

for i in %buildroot%_sbindir/* %buildroot%_libdir/*.so.*
do
	chrpath -d $i ||:
done

%post
%post_service %name

%preun
%preun_service %name

%files devel
%_includedir/tacacs.h
%_libdir/libtacacs.so

%files -n libtacacs1
%_libdir/libtacacs.so.*

%files
%_bindir/tac_*
%_sbindir/tac_*
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/pam.d/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/logrotate.d/%name
%_initdir/%name
%_unitdir/%name.service
%_man5dir/tac_plus.conf.5.*
%_man8dir/tac_plus.8.*
%_man8dir/tac_pwd.8.*
%attr(644,root,root) %_logdir/tac_plus.log
%attr(644,root,root) %_logdir/tac_plus.acct
%attr(600,root,root) %_logdir/tacwho.log
%doc users_guide COPYING FAQ INSTALL CHANGES README do_auth.py tac_convert

%changelog
* Tue Jan 13 2015 Terechkov Evgenii <evg@altlinux.org> 1:4.0.4.28-alt1
- 4.0.4.28

* Tue Aug 12 2014 Terechkov Evgenii <evg@altlinux.org> 1:4.0.4.27a-alt1
- Oops, seems like F5 branch is dead, rollback to F4
- Epoch tag added
- 4.0.4.27a
- Systemd unit file added

* Mon Mar  4 2013 Terechkov Evgenii <evg@altlinux.org> 5.0.0a1-alt1
- 5.0.0a1 with patch adapted

* Sun Mar  3 2013 Terechkov Evgenii <evg@altlinux.org> 4.0.4.15-alt1
- 4.0.4.15

* Sun Mar  3 2013 Terechkov Evgenii <evg@altlinux.org> 4.0.4.14-alt3
- Make build with libwrap conditional (disabled by default)

* Sun Mar  3 2013 Terechkov Evgenii <evg@altlinux.org> 4.0.4.14-alt2
- Disable libwrap

* Mon Feb 25 2013 Terechkov Evgenii <evg@altlinux.org> 4.0.4.14-alt1
- Initial build for ALT Linux Sisyphus
