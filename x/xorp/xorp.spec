# configure options
%define with_shared	1
%define with_optimize	1
%define prefixdir	/usr
%define snapshot	1

Name: xorp

%define baseversion 1.8.6

%if %snapshot
%define snapshotdate 20130830
Version: %baseversion
Release: alt0.%snapshotdate.1
%else
Version: %baseversion
Release: alt1
%endif

Summary:	An eXtensible Open Router Platform (XORP)
License:	%gpllgpl2only
Group:		Networking/Other
URL:		http://www.xorp.org
%if %snapshot
Source0:	%{name}-%{version}.git%{snapshotdate}-src.tar.bz2
%else
Source0:	http://www.xorp.org/releases/%{version}/%{name}-%{version}-src.tar.bz2
%endif

Source1:	xorp.altlinux
Source2:	xorp.sysconfig
Source3:	xorp.logrotate
Source4:	xorp.conf

BuildRequires:    rpm-build-licenses

# Automatically added by buildreq on Tue Apr 08 2014
# optimized out: libstdc++-devel libtinfo-devel python-base python-modules python-modules-compiler python-modules-email xz
BuildRequires:    cvs flex gcc4.5-c++ libncurses-devel libpcap-devel libpcre-devel libssl-devel scons


%description
XORP is an extensible open-source routing platform. Designed for extensibility
from the start, XORP provides a fully featured platform that implements IPv4
and IPv6 routing protocols and a unified platform to configure them. XORP's
modular architecture allows rapid introduction of new protocols, features and
functionality, including support for custom hardware and software forwarding.


%prep
%setup -q -n xorp

# build with gcc 4.7 (latest in p7/t7) fail with "internal compiler error"
# gcc 4.5 exist in branches 6/7 and Sicyphus.
%set_gcc_version 4.5


%build
[ -n "$NPROCS" ] || NPROCS='%{__nprocs}'; scons -j$NPROCS \
	DESTDIR=${RPM_BUILD_ROOT}     \
	sbindir=%{_sbindir}           \
	prefix=%{prefixdir}           \
	libexecdir=%{_libexecdir}     \
	sysconfdir=%{_sysconfdir}     \
	xorp_confdir=%{_sysconfdir}   \
	localstatedir=%{_localstatedir} \
	build=%{_configure_platform} \
	rtld_origin=false \
%if %with_shared
	shared=yes \
%endif
%if %with_optimize
	optimize=yes \
%endif


%install
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_initrddir}
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_sysconfdir}/{logrotate.d,sysconfig,xorp}
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_sbindir}
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_datadir}/xorp
%{__mkdir_p} ${RPM_BUILD_ROOT}%{_logdir}/xorp

scons \
	DESTDIR=${RPM_BUILD_ROOT}     \
	sbindir=%{_sbindir}           \
	prefix=%{prefixdir}           \
	libexecdir=%{_libexecdir}     \
	sysconfdir=%{_sysconfdir}     \
	xorp_confdir=%{_sysconfdir}   \
	localstatedir=%{_localstatedir} \
	build=%{_configure_platform} \
	rtld_origin=false \
%if %with_shared
	shared=yes \
%endif
%if %with_optimize
	optimize=yes \
%endif
	install


%{__install} -m 0755 %{SOURCE1}    ${RPM_BUILD_ROOT}%{_initrddir}/xorp
%{__install} -m 0644 %{SOURCE2}    ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/xorp
%{__install} -m 0644 %{SOURCE3}    ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/xorp
%{__install} -m 0660 %{SOURCE4}    ${RPM_BUILD_ROOT}%{_sysconfdir}/xorp


%pre
if ! getent group xorp >/dev/null 2>&1; then
	/usr/sbin/groupadd -r xorp

	# xorpsh is using group's permission for access to xorp.
	# So, root user should be in group.
	/usr/sbin/usermod -G xorp root
fi
exit 0


%post
%post_service %name


%preun
%preun_service %name


%files
%doc README RELEASE_NOTES
%doc BUGS ERRATA LICENSE*
%{_initrddir}/xorp
%config(noreplace) %{_sysconfdir}/logrotate.d/xorp
%config(noreplace) %{_sysconfdir}/sysconfig/xorp
%attr(770,root,xorp) %dir %{_sysconfdir}/xorp
%attr(660,root,xorp) %config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xorp/xorp.conf

%dir %_datadir/%name
%dir %_libexecdir/%name
%dir %_logdir/%name

%_sbindir/*
%_datadir/%name/*
%_libexecdir/%name/*

%changelog
* Thu Apr 10 2014 Sergey Y. Afonin <asy@altlinux.ru> 1.8.6-alt0.20130830.1
- Initial version for ALT Linux (20130830 git snapshot).
  SPEC file based on xorp-1.8.3-1.fc14.src.rpm,
  with some help from glebfm@altlinux
