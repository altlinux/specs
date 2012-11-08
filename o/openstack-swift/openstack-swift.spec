Name:		openstack-swift
Version:	1.7.0
Release:	alt1
Summary:	OpenStack Object Storage (swift)

Group:		System/Servers
License:	ASL 2.0
URL:		http://launchpad.net/swift
Source0:	%{name}-%{version}.tar.gz
Source2:	%{name}-account.service
Source21:	%{name}-account@.service
Source22:	account-server.conf
Source4:	%{name}-container.service
Source41:	%{name}-container@.service
Source42:	container-server.conf
Source5:	%{name}-object.service
Source51:	%{name}-object@.service
Source52:	object-server.conf
Source6:	%{name}-proxy.service
Source61:	proxy-server.conf
Source20:	%{name}.tmpfs
Source7:	swift.conf

BuildArch:	noarch
BuildRequires:	dos2unix
BuildRequires:	python-devel
BuildRequires:	python-module-distribute
BuildRequires:	python-module-netifaces
BuildRequires:	python-module-PasteDeploy

Requires(post):		systemd-units
Requires(preun):	systemd-units
Requires(postun):	systemd-units
#Requires(post):		systemd-sysv
Requires(pre):		shadow-utils

Obsoletes:	openstack-swift-auth

# swift3 was split off in 1.5.0
#Requires:	python-module-swift-plugin-swift3

# swiftclient was split offf in 1.6.0
Requires:	python-module-swiftclient
Requires:	python-module-swift = %{version}-%{release}

%description
OpenStack Object Storage (swift) aggregates commodity servers to work
together in clusters for reliable, redundant, and large-scale storage of
static objects. Objects are written to multiple hardware devices in the
data center, with the OpenStack software responsible for ensuring data
replication and integrity across the cluster. Storage clusters can scale
horizontally by adding new nodes, which are automatically configured.
Should a node fail, OpenStack works to replicate its content from other
active nodes. Because OpenStack uses software logic to ensure data
replication and distribution across different devices, inexpensive
commodity hard drives and servers can be used in lieu of more expensive
equipment.

%package -n python-module-swift
Summary:	Swift Python libraries
Group:		Development/Python

Requires:	python-module-configobj
Requires:	python-module-eventlet >= 0.9.8
Requires:	python-module-greenlet >= 0.3.1
Requires:	python-module-PasteDeploy
Requires:	python-module-simplejson
Requires:	python-module-webob >= 0.9.8
Requires:	python-module-pyxattr
Requires:	python-module-distribute
Requires:	python-module-netifaces

%description -n python-module-swift
Swift is a Python implementation of the OpenStack
(http://www.openstack.org) Object Storege API.

This package contains the Swift Python library.

%package account
Summary:	A swift account server
Group:		System/Servers

Requires:	%{name} = %{version}-%{release}

%description account
OpenStack Object Storage (swift) aggregates commodity servers to work
together in clusters for reliable, redundant, and large-scale storage of
static objects.

This package contains the %{name} account server.

%package container
Summary:	A swift container server
Group:		System/Servers

Requires:	%{name} = %{version}-%{release}

%description container
OpenStack Object Storage (swift) aggregates commodity servers to work
together in clusters for reliable, redundant, and large-scale storage of
static objects.

This package contains the %{name} container server.

%package object
Summary:	A swift object server
Group:		System/Servers

Requires:	%{name} = %{version}-%{release}
Requires:	rsync >= 3.0

%description object
OpenStack Object Storage (swift) aggregates commodity servers to work
together in clusters for reliable, redundant, and large-scale storage of
static objects.

This package contains the %{name} object server.

%package proxy
Summary:	A swift proxy server
Group:		System/Servers

Requires:	%{name} = %{version}-%{release}

%description proxy
OpenStack Object Storage (swift) aggregates commodity servers to work
together in clusters for reliable, redundant, and large-scale storage of
static objects.

This package contains the %{name} proxy server.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
BuildRequires:	python-module-sphinx >= 1.0
BuildRequires:	python-module-objects.inv
# Required for generating docs
BuildRequires:	python-module-eventlet
BuildRequires:	python-module-simplejson
BuildRequires:	python-module-webob
BuildRequires:	python-module-pyxattr

%description doc
OpenStack Object Storage (swift) aggregates commodity servers to work
together in clusters for reliable, redundant, and large-scale storage of
static objects.

This package contains documentation files for %{name}.

%prep
%setup -q
# Fix wrong-file-end-of-line-encoding warning
dos2unix LICENSE

%build
%{__python} setup.py build
# Fails unless we create the build directory
mkdir -p doc/build
# Build docs
%{__python} setup.py build_sphinx
# Fix hidden-file-or-dir warning
#rm doc/build/html/.buildinfo

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
# systemd units
install -p -D -m 755 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}-account.service
install -p -D -m 755 %{SOURCE21} %{buildroot}%{_unitdir}/%{name}-account@.service
install -p -D -m 755 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}-container.service
install -p -D -m 755 %{SOURCE41} %{buildroot}%{_unitdir}/%{name}-container@.service
install -p -D -m 755 %{SOURCE5} %{buildroot}%{_unitdir}/%{name}-object.service
install -p -D -m 755 %{SOURCE51} %{buildroot}%{_unitdir}/%{name}-object@.service
install -p -D -m 755 %{SOURCE6} %{buildroot}%{_unitdir}/%{name}-proxy.service
# Remove tests
rm -fr %{buildroot}/%{python_sitelibdir}/test
# Misc other
install -d -m 755 %{buildroot}%{_sysconfdir}/swift
install -d -m 755 %{buildroot}%{_sysconfdir}/swift/account-server
install -d -m 755 %{buildroot}%{_sysconfdir}/swift/container-server
install -d -m 755 %{buildroot}%{_sysconfdir}/swift/object-server
install -d -m 755 %{buildroot}%{_sysconfdir}/swift/proxy-server
# Config files
install -p -D -m 660 %{SOURCE22} %{buildroot}%{_sysconfdir}/swift/account-server.conf
install -p -D -m 660 %{SOURCE42} %{buildroot}%{_sysconfdir}/swift/container-server.conf
install -p -D -m 660 %{SOURCE52} %{buildroot}%{_sysconfdir}/swift/object-server.conf
install -p -D -m 660 %{SOURCE61} %{buildroot}%{_sysconfdir}/swift/proxy-server.conf
install -p -D -m 660 %{SOURCE7} %{buildroot}%{_sysconfdir}/swift/swift.conf
# Install pid directory
install -d -m 755 %{buildroot}%{_runtimedir}/swift
install -d -m 755 %{buildroot}%{_runtimedir}/swift/account-server
install -d -m 755 %{buildroot}%{_runtimedir}/swift/container-server
install -d -m 755 %{buildroot}%{_runtimedir}/swift/object-server
install -d -m 755 %{buildroot}%{_runtimedir}/swift/proxy-server
# Swift run directories
mkdir -p %{buildroot}%{_sysconfdir}/tmpfiles.d
install -p -m 0644 %{SOURCE20} %{buildroot}%{_sysconfdir}/tmpfiles.d/openstack-swift.conf
# man pages
install -d -m 755 %{buildroot}%{_mandir}/man5
for m in doc/manpages/*.5; do
  install -p -m 0644 $m %{buildroot}%{_mandir}/man5
done
install -d -m 755 %{buildroot}%{_mandir}/man1
for m in doc/manpages/*.1; do
  install -p -m 0644 $m %{buildroot}%{_mandir}/man1
done

%pre
getent group swift >/dev/null || groupadd -r swift -g 160
getent passwd swift >/dev/null || \
useradd -r -g swift -u 160 -d %{_sharedstatedir}/swift -s /sbin/nologin \
-c "OpenStack Swift Daemons" swift
exit 0

%post account
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun account
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable openstack-swift-account.service > /dev/null 2>&1 || :
    /bin/systemctl stop openstack-swift-account.service > /dev/null 2>&1 || :
fi

%postun account
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart openstack-swift-account.service >/dev/null 2>&1 || :
fi

%post container
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun container
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable openstack-swift-container.service > /dev/null 2>&1 || :
    /bin/systemctl stop openstack-swift-container.service > /dev/null 2>&1 || :
fi

%postun container
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart openstack-swift-container.service >/dev/null 2>&1 || :
fi

%triggerun -- openstack-swift-container < 1.4.5-1
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply openstack-swift-container
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save openstack-swift-container >/dev/null 2>&1 ||:
# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del openstack-swift-container >/dev/null 2>&1 || :
/bin/systemctl try-restart openstack-swift-container.service >/dev/null 2>&1 || :

%post object
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun object
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable openstack-swift-object.service > /dev/null 2>&1 || :
    /bin/systemctl stop openstack-swift-object.service > /dev/null 2>&1 || :
fi

%postun object
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart openstack-swift-object.service >/dev/null 2>&1 || :
fi

%post proxy
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun proxy
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable openstack-swift-proxy.service > /dev/null 2>&1 || :
    /bin/systemctl stop openstack-swift-proxy.service > /dev/null 2>&1 || :
fi

%postun proxy
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart openstack-swift-proxy.service >/dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE README
%doc etc/dispersion.conf-sample etc/drive-audit.conf-sample etc/object-expirer.conf-sample
%doc etc/swift.conf-sample
%{_mandir}/man5/dispersion.conf.5*
%{_mandir}/man1/swift-dispersion-populate.1*
%{_mandir}/man1/swift-dispersion-report.1*
%{_mandir}/man1/swift.1*
%{_mandir}/man1/swift-get-nodes.1*
%{_mandir}/man1/swift-init.1*
%{_mandir}/man1/swift-orphans.1*
%{_mandir}/man1/swift-recon.1*
%{_mandir}/man1/swift-ring-builder.1*
%config(noreplace) %{_sysconfdir}/tmpfiles.d/openstack-swift.conf
%dir %{_sysconfdir}/swift
%config(noreplace) %attr(660, root, swift) %{_sysconfdir}/swift/swift.conf
%dir %attr(0755, swift, root) %{_runtimedir}/swift
%{_bindir}/swift-account-audit
%{_bindir}/swift-bench
%{_bindir}/swift-drive-audit
%{_bindir}/swift-get-nodes
%{_bindir}/swift-init
%{_bindir}/swift-ring-builder
%{_bindir}/swift-dispersion-populate
%{_bindir}/swift-dispersion-report
%{_bindir}/swift-recon*
%{_bindir}/swift-object-expirer
%{_bindir}/swift-oldies
%{_bindir}/swift-orphans
%{_bindir}/swift-form-signature
%{_bindir}/swift-temp-url

%files -n python-module-swift
%defattr(-,root,root,-)
%doc LICENSE
%dir %{python_sitelibdir}/swift
%{python_sitelibdir}/swift/*.py*
%{python_sitelibdir}/swift/common
%{python_sitelibdir}/swift-%{version}-*.egg-info

%files account
%defattr(-,root,root,-)
%doc etc/account-server.conf-sample
%{_mandir}/man5/account-server.conf.5*
%{_mandir}/man1/swift-account-auditor.1*
%{_mandir}/man1/swift-account-reaper.1*
%{_mandir}/man1/swift-account-replicator.1*
%{_mandir}/man1/swift-account-server.1*
%dir %{_unitdir}/%{name}-account.service
%dir %{_unitdir}/%{name}-account@.service
%dir %{_sysconfdir}/swift/account-server
%config(noreplace) %attr(660, root, swift) %{_sysconfdir}/swift/account-server.conf
%dir %attr(0755, swift, root) %{_runtimedir}/swift/account-server
%{_bindir}/swift-account-auditor
%{_bindir}/swift-account-reaper
%{_bindir}/swift-account-replicator
%{_bindir}/swift-account-server
%{python_sitelibdir}/swift/account

%files container
%defattr(-,root,root,-)
%doc etc/container-server.conf-sample
%{_mandir}/man5/container-server.conf.5*
%{_mandir}/man1/swift-container-auditor.1*
%{_mandir}/man1/swift-container-replicator.1*
%{_mandir}/man1/swift-container-server.1*
%{_mandir}/man1/swift-container-sync.1*
%{_mandir}/man1/swift-container-updater.1*
%dir %{_unitdir}/%{name}-container.service
%dir %{_unitdir}/%{name}-container@.service
%dir %{_sysconfdir}/swift/container-server
%config(noreplace) %attr(660, root, swift) %{_sysconfdir}/swift/container-server.conf
%dir %attr(0755, swift, root) %{_runtimedir}/swift/container-server
%{_bindir}/swift-container-auditor
%{_bindir}/swift-container-server
%{_bindir}/swift-container-replicator
%{_bindir}/swift-container-updater
%{_bindir}/swift-container-sync
%{python_sitelibdir}/swift/container

%files object
%defattr(-,root,root,-)
%doc etc/object-server.conf-sample etc/rsyncd.conf-sample
%{_mandir}/man5/object-server.conf.5*
%{_mandir}/man5/object-expirer.conf.5*
%{_mandir}/man1/swift-object-auditor.1*
%{_mandir}/man1/swift-object-expirer.1*
%{_mandir}/man1/swift-object-info.1*
%{_mandir}/man1/swift-object-replicator.1*
%{_mandir}/man1/swift-object-server.1*
%{_mandir}/man1/swift-object-updater.1*
%dir %{_unitdir}/%{name}-object.service
%dir %{_unitdir}/%{name}-object@.service
%dir %{_sysconfdir}/swift/object-server
%config(noreplace) %attr(660, root, swift) %{_sysconfdir}/swift/object-server.conf
%dir %attr(0755, swift, root) %{_runtimedir}/swift/object-server
%{_bindir}/swift-object-auditor
%{_bindir}/swift-object-info
%{_bindir}/swift-object-replicator
%{_bindir}/swift-object-server
%{_bindir}/swift-object-updater
%{python_sitelibdir}/swift/obj

%files proxy
%defattr(-,root,root,-)
%doc etc/proxy-server.conf-sample
%{_mandir}/man5/proxy-server.conf.5*
%{_mandir}/man1/swift-proxy-server.1*
%dir %{_unitdir}/%{name}-proxy.service
%dir %{_sysconfdir}/swift/proxy-server
%config(noreplace) %attr(660, root, swift) %{_sysconfdir}/swift/proxy-server.conf
%dir %attr(0755, swift, root) %{_runtimedir}/swift/proxy-server
%{_bindir}/swift-proxy-server
%{python_sitelibdir}/swift/proxy

%files doc
%defattr(-,root,root,-)
%doc LICENSE doc/build/html

%changelog
* Thu Nov 08 2012 Pavel Shilovsky <piastry@altlinux.org> 1.7.0-alt1
- Initial release for Sisyphus (based on Fedora)
