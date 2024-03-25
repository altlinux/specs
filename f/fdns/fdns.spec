%define _unpackaged_files_terminate_build 1
%def_with check

Name: fdns
Version: 0.9.72
Release: alt1

Summary: Firejail DNS-over-HTTPS Proxy Server
License: GPLv3
Group: System/Servers
Url: https://github.com/netblue30/fdns/

Source:  %name-%version.tar
Source1: %name-%version-etc-blocklists.tar
Patch0:  %name-%version-alt.patch

BuildRequires: libssl-devel
BuildRequires: libseccomp-devel
%if_with check
BuildRequires: man
BuildRequires: firejail
BuildRequires: expect
BuildRequires: /dev/pts
%endif

%description
FDNS is an encrypted DNS proxy designed for small
networks and Linux desktops. Lean and mean, it protects
your computer from some of the most common cyber threats,
while also improving privacy and the system performance.

%prep
%setup -a1
%autopatch -p1

%build
%configure
%make_build

%install
%makeinstall_std \
	SYSTEMD_DIR=%systemd_unitdir

%check
export PATH=$PATH:%buildroot%_bindir
export SHELL
export SERVER_LIST=%buildroot/etc/fdns/servers
cd test/fdns
./test-user.sh

%files
%doc COPYING README RELNOTES
%dir %_sysconfdir/fdns
%_sysconfdir/fdns/servers
%config(noreplace) %_sysconfdir/fdns/servers.local
%config(noreplace) %_sysconfdir/fdns/resolver*
%config(noreplace) %_sysconfdir/fdns/list*
%systemd_unitdir/fdns.service
%_bindir/nxdomain
%_bindir/fdns
%_docdir/fdns
%_datadir/bash-completion/completions/fdns
%_man1dir/fdns*
%_man1dir/nxdomain*

%changelog
* Tue Mar 19 2024 Ajrat Makhmutov <rauty@altlinux.org> 0.9.72-alt1
- First build for ALT.
