%define _unpackaged_files_terminate_build 1
%def_without xenstore

Name: vhostmd
Version: 1.1
Release: alt1
Summary: Virtualization Host Metrics Daemon
License: GPLv2+
Group: System/Servers
Url: https://github.com/vhostmd/vhostmd

Source: %name-%version.tar
Source1: vhostmd.conf
Patch: %name-%version.patch

BuildRequires: libxml2-devel
BuildRequires: libvirt-devel
%{?_with_xenstore:BuildRequires: libxen-devel}

%description
Daemon vhostmd provides a "metrics communication channel" between a host and
its hosted virtual machines, allowing limited introspection of host
resource usage from within virtual machines.

%package -n vm-dump-metrics
Summary: Virtualization Host Metrics Dump
Group: Monitoring

%description -n vm-dump-metrics
Executable to dump all available virtualization host metrics to stdout
or alternativly an argumented file.

%package -n libmetrics
Summary: Virtualization Host Metrics Dump library
Group: System/Libraries

%description -n libmetrics
%summary

%package -n libmetrics-devel
Summary: Virtualization Host Metrics Dump development
Group: Development/C
Requires: libmetrics = %EVR

%description -n libmetrics-devel
Header and libraries necessary for metrics gathering development

%prep
%setup
%patch -p1
%build
%autoreconf
%configure \
	%{subst_with xenstore} \
	--with-init-script=systemd \
	--enable-shared \
	--disable-static
%make_build

%install
%makeinstall_std

# Remove docdir - we'll make a proper one ourselves.
rm -r %buildroot%_docdir/vhostmd

# Remove metric.dtd from /etc.
rm %buildroot%_sysconfdir/vhostmd/metric.dtd

rm %buildroot%_sysconfdir/vhostmd/vhostmd.conf
install -p -m 0644  %SOURCE1 %buildroot%_sysconfdir/vhostmd/vhostmd.conf

# Remove Perl scrip
rm %buildroot%_datadir/vhostmd/scripts/pagerate.pl

%pre
# UID:GID 112:112 reserved
groupadd -r -f -g 112 %name  >/dev/null 2>&1 ||:
useradd -u 112 -r -g %name -d %_localstatedir/vhostmd -s /sbin/nologin \
	-c "Virtual Host Metrics Daemon" %name >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS README
%doc mdisk.xml metric.dtd vhostmd.dtd vhostmd.xml scripts/pagerate.pl scripts/vif-stats.py
%_sbindir/%name
%_man8dir/%name.*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf
%config %_sysconfdir/%name/%name.dtd
%_unitdir/%name.service
%_datadir/%name

%files -n vm-dump-metrics
%_sbindir/vm-dump-metrics
%_man1dir/vm-dump-metrics.*

%files -n libmetrics
%_libdir/*.so.*

%files -n libmetrics-devel
%_libdir/*.so
%_includedir/*

%changelog
* Mon Aug 09 2021 Alexey Shabalin <shaba@altlinux.org> 1.1-alt1
- Initial build.

