Summary: Network traffic analyzer
Name:    darkstat
Version: 3.0.721
Release: alt1
License: GPLv2
Group:   Monitoring
Url: https://unix4lyfe.org/darkstat/

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: http://dmr.ath.cx/net/darkstat/darkstat-%version.tar.gz
Source1:       %{name}.service
Source2:       %{name}.sysconfig


# Automatically added by buildreq on Wed Apr 02 2008
BuildRequires: libpcap-devel zlib-devel

Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
BuildRequires:    systemd
BuildRequires: make

%description
darkstat is a network traffic analyzer. It's basically a packet sniffer
which runs as a background process on a cable/DSL router and gathers
all sorts of useless but interesting statistics.

%prep
%setup
%autoreconf

%build
#configure
%configure --disable-silent-rules
%make_build

%install
%makeinstall
install -Dp -m 0644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service
install -Dp -m 0644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}

%pre
getent passwd %{name} >/dev/null || useradd -r -s /sbin/nologin -c "Network traffic analyzer" %{name}
exit 0

%post
%post_service %{name}.service

%preun
%preun_service %{name}.service


%files
%doc AUTHORS COPYING* INSTALL LICENSE NEWS README.git *.txt
%_man8dir/darkstat.8*
%_sbindir/darkstat
%attr(0600,%{name},root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service


%changelog
* Fri Jan 14 2022 Ilya Mashkin <oddity@altlinux.ru> 3.0.721-alt1
- 3.0.721
- Update url

* Sat Mar 13 2021 Ilya Mashkin <oddity@altlinux.ru> 3.0.719-alt1
- 3.0.719

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.0.707-alt1.qa1
- NMU: rebuilt for debuginfo.

* Wed Apr 02 2008 Nick S. Grechukh <gns@altlinux.org> 3.0.707-alt1
- first build to sisyphus. TODO: steal nice initscript from debian

* Tue Oct 02 2007 Dag Wieers <dag@wieers.com> - 3.0.707-1
- Updated to release 3.0.707.

* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 3.0.619-1
- Updated to release 3.0.619.

* Mon Aug 07 2006 Dag Wieers <dag@wieers.com> - 3.0.540-1
- Updated to release 3.0.540.

* Tue Jun 20 2006 Dag Wieers <dag@wieers.com> - 3.0.471-1
- Updated to release 3.0.471.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 2.6-1
- Initial package. (using DAR)
