%define _unpackaged_files_terminate_build 1
%filter_from_requires /^\/usr\/bin\/mysql$/d
%filter_from_requires /^\/usr\/bin\/psql$/d

%def_without radius
%def_with mysql
%def_with pgsql

%define _localstatedir /var

Name: kea
Version: 2.4.1
Release: alt1
Summary: DHCPv4, DHCPv6 and DDNS server from ISC

License: MPL-2.0 and BSL-1.0
Group: System/Servers
Url: http://kea.isc.org
Source0: %name-%version.tar
Source1: kea-dhcp4.service
Source2: kea-dhcp6.service
Source3: kea-dhcp-ddns.service
Source4: kea-ctrl-agent.service
Patch: %name-%version.patch

Requires: lib%name = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: boost-devel boost-interprocess-devel boost-asio-devel
BuildRequires: gcc-c++ bison flex
BuildRequires: libssl-devel
BuildRequires: libkrb5-devel
BuildRequires: libmysqlclient-devel
BuildRequires: postgresql-devel
BuildRequires: liblog4cplus-devel
BuildRequires: procps
%{?_with_radius: BuildRequires: freeradius-devel}
BuildRequires: python3-devel
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme

%description
DHCP implementation from Internet Systems Consortium, Inc. that features fully
functional DHCPv4, DHCPv6 and Dynamic DNS servers.
Both DHCP servers fully support server discovery, address assignment, renewal,
rebinding and release. The DHCPv6 server supports prefix delegation. Both
servers support DNS Update mechanism, using stand-alone DDNS daemon.

%package -n lib%name-devel
Summary: Development headers and libraries for Kea DHCP server
Group: Development/Other
Requires: lib%name = %EVR
Provides: %name-devel = %EVR

%description -n lib%name-devel
Header files and API documentation.

%package hooks
Summary: Hooks libraries for kea
Group: System/Servers
Requires: lib%name = %EVR

%description hooks
Hooking mechanism allow Kea to load one or more dynamically-linked libraries
(known as "hooks libraries") and, at various points in its processing
("hook points"), call functions in them.  Those functions perform whatever
custom processing is required.

%package shell
Summary: Text client for Control Agent process
Group: System/Servers
BuildArch: noarch

%description shell
The kea-shell provides a REST client for the Kea Control Agent (CA).
It takes command as a command-line parameter that is being sent to CA
with proper JSON encapsulation. Optional arguments may be specified on
the standard input. The request it sent of HTTP and a response is
retrieved. That response is displayed out on the standard output.

%package doc
Summary: Documents for Kea dhcp
Group: Documentation
BuildArch: noarch

%description doc
Documents for Kea dhcp.

%package -n lib%name
Summary: Shared libraries used by Kea DHCP server
Group: System/Libraries
Provides: %name-libs = %EVR

%description -n lib%name
This package contains shared libraries used by Kea DHCP server.

%package -n python3-module-%name
Summary: Python3 management connector for ISC KEA DHCP server
Group: Development/Python3
BuildArch: noarch
%add_python3_path %python3_sitelibdir_noarch/%name
%allow_python3_import_path %python3_sitelibdir_noarch/%name

%description -n python3-module-%name
Python3 management connector for ISC KEA DHCP server.
KEA is an IPv4 and IPv6 DHCP server developed by Internet Systems Consortium.

This package provides Python3 connector.

%prep
%setup
%patch -p1

# to be able to build on ppc64(le)
# https://sourceforge.net/p/flex/bugs/197
# https://lists.isc.org/pipermail/kea-dev/2016-January/000599.html
sed -i -e 's|ECHO|YYECHO|g' src/lib/eval/lexer.cc

sed -i -e "s|%version-git|%version|" configure.ac

%build
%autoreconf

%configure \
    --disable-dependency-tracking \
    --disable-rpath \
    --disable-silent-rules \
    --disable-static \
    --enable-debug \
    --enable-generate-parser \
    --enable-shell \
    --enable-generate-docs \
    --enable-generate-messages \
    --enable-perfdhcp \
%if_with radius
    --with-freeradius=%_prefix \
    --with-freeradius-dictionary=%_sysconfdir/radiusclient/dictionary \
%endif
    %{subst_with mysql} \
    %{subst_with pgsql} \
    --with-gnu-ld \
    --with-log4cplus \
    --with-openssl \
    --with-gssapi \
    --with-site-packages=%python3_sitelibdir_noarch \
    runstatedir=/run

%make_build

%install
%makeinstall_std

# Get rid of .la files
find %buildroot -type f -name "*.la" -delete -print

# remove keactrl
rm %buildroot%_sysconfdir/kea/keactrl.conf
rm %buildroot%_sbindir/keactrl
rm %buildroot%_mandir/man8/keactrl.8

# Install systemd units
install -Dpm 0644 %SOURCE1 %buildroot%_unitdir/kea-dhcp4.service
install -Dpm 0644 %SOURCE2 %buildroot%_unitdir/kea-dhcp6.service
install -Dpm 0644 %SOURCE3 %buildroot%_unitdir/kea-dhcp-ddns.service
install -Dpm 0644 %SOURCE4 %buildroot%_unitdir/kea-ctrl-agent.service

# Start empty lease databases
mkdir -p %buildroot%_sharedstatedir/kea/
touch %buildroot%_sharedstatedir/kea/kea-leases4.csv
touch %buildroot%_sharedstatedir/kea/kea-leases6.csv

# change log destination from /var/log/... to STDOUT and enable shortened log format
sed -i -e s/\"output\".*/\"output\":\ \"stdout\",/ -e s@\/\/\ \"pattern@\"pattern@ \
    -e s@\"socket-name\":\ \"\/tmp\/kea-@\"socket-name\":\ \"\/run\/kea\/@ \
    %buildroot%_sysconfdir/kea/kea-ctrl-agent.conf \
    %buildroot%_sysconfdir/kea/kea-dhcp6.conf \
    %buildroot%_sysconfdir/kea/kea-dhcp4.conf \
    %buildroot%_sysconfdir/kea/kea-dhcp-ddns.conf
#    %%buildroot%%_sysconfdir/kea/kea-netconf.conf  # TODO: no support for netconf/sysconf yet

%pre
%_sbindir/groupadd -r -f _kea
%_sbindir/useradd -M -r -d /var/lib/%name -s /bin/false -c "Kea DHCP User" -g _kea _kea >/dev/null 2>&1 ||:


%post
%post_service kea-dhcp4.service
%post_service kea-dhcp6.service
%post_service kea-dhcp-ddns.service
%post_service kea-ctrl-agent.service

%preun
%preun_service kea-dhcp4.service
%preun_service kea-dhcp6.service
%preun_service kea-dhcp-ddns.service
%preun_service kea-ctrl-agent.service

%files
%_bindir/*
%_sbindir/*
%exclude %_sbindir/kea-shell
%_unitdir/*.service
%dir %attr(0750, root, _kea) %_sysconfdir/%name
%config(noreplace) %attr(0640, root, _kea) %_sysconfdir/%name/*.conf
%_datadir/%name
%dir %attr(0755, _kea, _kea) %_sharedstatedir/%name
%config(noreplace) %attr(0644, _kea, _kea) %_sharedstatedir/%name/*.csv
%_man8dir/*

%files -n lib%name-devel
%_includedir/%name
%_libdir/lib%name-*.so

%files hooks
%dir %_libdir/%name
%_libdir/%name/hooks

%files shell
%_sbindir/kea-shell

%files doc
%doc %_datadir/doc/%name

%files -n lib%name
%_libdir/lib%name-*.so.*

%files -n python3-module-%name
%python3_sitelibdir_noarch/*

%changelog
* Wed Dec 06 2023 Alexey Shabalin <shaba@altlinux.org> 2.4.1-alt1
- 2.4.1

* Mon Oct 16 2023 Alexey Shabalin <shaba@altlinux.org> 2.4.0-alt2
- fixed execute kea-shell (fix define python3 site-packages path)

* Fri Aug 18 2023 Alexey Shabalin <shaba@altlinux.org> 2.4.0-alt1
- 2.4.0
- build with gssapi support

* Mon Aug 08 2022 Alexey Shabalin <shaba@altlinux.org> 2.2.0-alt1
- 2.2.0

* Mon Apr 11 2022 Alexey Shabalin <shaba@altlinux.org> 2.0.2-alt1
- 2.0.2

* Mon Oct 18 2021 Alexey Shabalin <shaba@altlinux.org> 2.0.0-alt1
- 2.0.0

* Thu Aug 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.2-alt3
- Rebuilt with boost-1.77.0.

* Fri Jun 04 2021 Alexey Shabalin <shaba@altlinux.org> 1.8.2-alt2
- fixed build docs with new sphinx

* Fri Jan 29 2021 Alexey Shabalin <shaba@altlinux.org> 1.8.2-alt1
- 1.8.2

* Tue Nov 10 2020 Alexey Shabalin <shaba@altlinux.org> 1.8.1-alt1
- 1.8.1

* Sat Mar 28 2020 Alexey Shabalin <shaba@altlinux.org> 1.6.2-alt3
- fix kea-shell package
- move docs to doc package

* Sat Mar 28 2020 Alexey Shabalin <shaba@altlinux.org> 1.6.2-alt2
- split kea-shell to separate package
- filter mysql and psql from requires
- update systemd units

* Wed Mar 18 2020 Alexey Shabalin <shaba@altlinux.org> 1.6.2-alt1
- 1.6.2

* Thu Feb 06 2020 Alexey Shabalin <shaba@altlinux.org> 1.6.1-alt1
- Initial build
