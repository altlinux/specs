%global release_name icehouse
%global milestone ...

Name:             openstack-swift
Version:          1.13.1
Release:          alt1
Summary:          OpenStack Object Storage (Swift)

Group:            System/Servers
License:          ASL 2.0
URL:              http://launchpad.net/swift
Source0:          %{name}-%{version}.tar

Source2:          %{name}-account.service
Source21:         %{name}-account@.service
Source22:         account-server.conf
Source23:         %{name}-account-replicator.service
Source24:         %{name}-account-replicator@.service
Source25:         %{name}-account-auditor.service
Source26:         %{name}-account-auditor@.service
Source27:         %{name}-account-reaper.service
Source28:         %{name}-account-reaper@.service
Source4:          %{name}-container.service
Source41:         %{name}-container@.service
Source42:         container-server.conf
Source43:         %{name}-container-replicator.service
Source44:         %{name}-container-replicator@.service
Source45:         %{name}-container-auditor.service
Source46:         %{name}-container-auditor@.service
Source47:         %{name}-container-updater.service
Source48:         %{name}-container-updater@.service
Source5:          %{name}-object.service
Source51:         %{name}-object@.service
Source52:         object-server.conf
Source53:         %{name}-object-replicator.service
Source54:         %{name}-object-replicator@.service
Source55:         %{name}-object-auditor.service
Source56:         %{name}-object-auditor@.service
Source57:         %{name}-object-updater.service
Source58:         %{name}-object-updater@.service
Source59:         %{name}-object-expirer.service
# Is it possible to supply an instance-style expirer unit for single-node?
Source6:          %{name}-proxy.service
Source61:         proxy-server.conf
Source62:         object-expirer.conf
Source20:         %{name}.tmpfs
Source7:          swift.conf

#
# patches_base=1.13.1
#
Patch0001: 0001-remove-runtime-requirement-on-pbr.patch
Patch0002: 0002-Add-fixes-for-building-the-doc-package.patch
Patch0003: 0003-Set-permissions-on-generated-ring-files.patch
Patch0004: 0004-properly-quote-www-authenticate-header-value.patch

BuildArch:        noarch
BuildRequires:    python-devel
BuildRequires:    python-module-setuptools
BuildRequires:    python-module-pbr
Requires:         python-module-configobj
Requires:         python-module-eventlet >= 0.9.15
Requires:         python-module-greenlet >= 0.3.1
Requires:         python-module-PasteDeploy
Requires:         python-module-simplejson
Requires:         python-module-pyxattr
Requires:         python-module-setuptools
Requires:         python-module-netifaces

Requires(pre):    shadow-utils

%description
OpenStack Object Storage (Swift) aggregates commodity servers to work together
in clusters for reliable, redundant, and large-scale storage of static objects.
Objects are written to multiple hardware devices in the data center, with the
OpenStack software responsible for ensuring data replication and integrity
across the cluster. Storage clusters can scale horizontally by adding new nodes,
which are automatically configured. Should a node fail, OpenStack works to
replicate its content from other active nodes. Because OpenStack uses software
logic to ensure data replication and distribution across different devices,
inexpensive commodity hard drives and servers can be used in lieu of more
expensive equipment.

%package          account
Summary:          Account services for Swift
Group:            System/Servers

Requires:         %{name} = %{version}-%{release}

%description      account
OpenStack Object Storage (Swift) aggregates commodity servers to work together
in clusters for reliable, redundant, and large-scale storage of static objects.

This package contains the %{name} account server.

%package          container
Summary:          Container services for Swift
Group:            System/Servers

Requires:         %{name} = %{version}-%{release}

%description      container
OpenStack Object Storage (Swift) aggregates commodity servers to work together
in clusters for reliable, redundant, and large-scale storage of static objects.

This package contains the %{name} container server.

%package          object
Summary:          Object services for Swift
Group:            System/Servers

Requires:         %{name} = %{version}-%{release}
Requires:         rsync >= 3.0

%description      object
OpenStack Object Storage (Swift) aggregates commodity servers to work together
in clusters for reliable, redundant, and large-scale storage of static objects.

This package contains the %{name} object server.

%package          proxy
Summary:          A proxy server for Swift
Group:            System/Servers

Requires:         %{name} = %{version}-%{release}
Requires:         python-module-keystoneclient
Requires:         python-module-swift-plugin-swift3

%description      proxy
OpenStack Object Storage (Swift) aggregates commodity servers to work together
in clusters for reliable, redundant, and large-scale storage of static objects.

This package contains the %{name} proxy server.

%package doc
Summary:          Documentation for %{name}
Group:            Documentation

BuildRequires:    python-module-sphinx >= 1.0
# Required for generating docs (otherwise py-modindex.html is missing)
BuildRequires:    python-module-eventlet
BuildRequires:    python-module-pyxattr

%description      doc
OpenStack Object Storage (Swift) aggregates commodity servers to work together
in clusters for reliable, redundant, and large-scale storage of static objects.

This package contains documentation files for %{name}.

%prep
%setup

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1

#sed -i 's/%{version}.%{milestone}/%{version}/' PKG-INFO

# Remove bundled egg-info
rm -rf swift.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

# Remove dependency on pbr and set version as per rpm
###sed -i 's/%%RPMVERSION%%/%%{version}/; s/%%RPMRELEASE%%/%%{release}/' swift/__init__.py

%build
%python_build
# Fails unless we create the build directory
mkdir -p doc/build
# Build docs
%{__python} setup.py build_sphinx

# Fix hidden-file-or-dir warning
#rm doc/build/html/.buildinfo

%install
%python_install
# systemd units
install -p -D -m 755 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}-account.service
install -p -D -m 755 %{SOURCE21} %{buildroot}%{_unitdir}/%{name}-account@.service
install -p -D -m 755 %{SOURCE23} %{buildroot}%{_unitdir}/%{name}-account-replicator.service
install -p -D -m 755 %{SOURCE24} %{buildroot}%{_unitdir}/%{name}-account-replicator@.service
install -p -D -m 755 %{SOURCE25} %{buildroot}%{_unitdir}/%{name}-account-auditor.service
install -p -D -m 755 %{SOURCE26} %{buildroot}%{_unitdir}/%{name}-account-auditor@.service
install -p -D -m 755 %{SOURCE27} %{buildroot}%{_unitdir}/%{name}-account-reaper.service
install -p -D -m 755 %{SOURCE28} %{buildroot}%{_unitdir}/%{name}-account-reaper@.service
install -p -D -m 755 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}-container.service
install -p -D -m 755 %{SOURCE41} %{buildroot}%{_unitdir}/%{name}-container@.service
install -p -D -m 755 %{SOURCE43} %{buildroot}%{_unitdir}/%{name}-container-replicator.service
install -p -D -m 755 %{SOURCE44} %{buildroot}%{_unitdir}/%{name}-container-replicator@.service
install -p -D -m 755 %{SOURCE45} %{buildroot}%{_unitdir}/%{name}-container-auditor.service
install -p -D -m 755 %{SOURCE46} %{buildroot}%{_unitdir}/%{name}-container-auditor@.service
install -p -D -m 755 %{SOURCE47} %{buildroot}%{_unitdir}/%{name}-container-updater.service
install -p -D -m 755 %{SOURCE48} %{buildroot}%{_unitdir}/%{name}-container-updater@.service
install -p -D -m 755 %{SOURCE5} %{buildroot}%{_unitdir}/%{name}-object.service
install -p -D -m 755 %{SOURCE51} %{buildroot}%{_unitdir}/%{name}-object@.service
install -p -D -m 755 %{SOURCE53} %{buildroot}%{_unitdir}/%{name}-object-replicator.service
install -p -D -m 755 %{SOURCE54} %{buildroot}%{_unitdir}/%{name}-object-replicator@.service
install -p -D -m 755 %{SOURCE55} %{buildroot}%{_unitdir}/%{name}-object-auditor.service
install -p -D -m 755 %{SOURCE56} %{buildroot}%{_unitdir}/%{name}-object-auditor@.service
install -p -D -m 755 %{SOURCE57} %{buildroot}%{_unitdir}/%{name}-object-updater.service
install -p -D -m 755 %{SOURCE58} %{buildroot}%{_unitdir}/%{name}-object-updater@.service
install -p -D -m 755 %{SOURCE59} %{buildroot}%{_unitdir}/%{name}-object-expirer.service
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
install -p -D -m 660 %{SOURCE62} %{buildroot}%{_sysconfdir}/swift/object-expirer.conf
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
# Install recon directory
install -d -m 755 %{buildroot}%{_localstatedir}/cache/swift
# Install home directory
install -d -m 755 %{buildroot}%{_sharedstatedir}/swift
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
%post_service %{name}-account
%post_service %{name}-account-replicator
%post_service %{name}-account-auditor
%post_service %{name}-account-reaper

%preun account
%preun_service %{name}-account
%preun_service %{name}-account-replicator
%preun_service %{name}-account-auditor
%preun_service %{name}-account-reaper

%post container
%post_service %{name}-container
%post_service %{name}-container-replicator
%post_service %{name}-container-auditor
%post_service %{name}-container-updater

%preun container
%preun_service %{name}-container
%preun_service %{name}-container-replicator
%preun_service %{name}-container-auditor
%preun_service %{name}-container-updater

%post object
%post_service %{name}-object
%post_service %{name}-object-replicator
%post_service %{name}-object-auditor
%post_service %{name}-object-updater

%preun object
%preun_service %{name}-object
%preun_service %{name}-object-replicator
%preun_service %{name}-object-auditor
%preun_service %{name}-object-updater

%post proxy
%post_service %{name}-proxy
%post_service %{name}-object-expirer

%preun proxy
%preun_service %{name}-proxy
%preun_service %{name}-object-expirer

%files
%doc AUTHORS LICENSE README.md
%doc etc/dispersion.conf-sample etc/drive-audit.conf-sample etc/object-expirer.conf-sample
%doc etc/swift.conf-sample
%{_mandir}/man5/dispersion.conf.5*
%{_mandir}/man1/swift-dispersion-populate.1*
%{_mandir}/man1/swift-dispersion-report.1*
%{_mandir}/man1/swift-get-nodes.1*
%{_mandir}/man1/swift-init.1*
%{_mandir}/man1/swift-orphans.1*
%{_mandir}/man1/swift-recon.1*
%{_mandir}/man1/swift-ring-builder.1*
%config(noreplace) %{_sysconfdir}/tmpfiles.d/openstack-swift.conf
%dir %{_sysconfdir}/swift
%config(noreplace) %attr(640, root, swift) %{_sysconfdir}/swift/swift.conf
%dir %attr(0755, swift, root) %{_runtimedir}/swift
%dir %attr(0755, swift, root) %{_localstatedir}/cache/swift
%dir %attr(0755, swift, root) %{_sharedstatedir}/swift
%dir %{python_sitelibdir}/swift
%{_bindir}/swift-account-audit
%{_bindir}/swift-config
%{_bindir}/swift-drive-audit
%{_bindir}/swift-get-nodes
%{_bindir}/swift-init
%{_bindir}/swift-ring-builder
%{_bindir}/swift-dispersion-populate
%{_bindir}/swift-dispersion-report
%{_bindir}/swift-recon*
%{_bindir}/swift-oldies
%{_bindir}/swift-orphans
%{_bindir}/swift-form-signature
%{_bindir}/swift-temp-url
%{python_sitelibdir}/swift/*.py*
%{python_sitelibdir}/swift/cli
%{python_sitelibdir}/swift/common
%{python_sitelibdir}/swift/account
%{python_sitelibdir}/swift/obj
%{python_sitelibdir}/swift-%{version}*.egg-info

%files account
%doc etc/account-server.conf-sample
%{_mandir}/man5/account-server.conf.5*
%{_mandir}/man1/swift-account-auditor.1*
%{_mandir}/man1/swift-account-info.1*
%{_mandir}/man1/swift-account-reaper.1*
%{_mandir}/man1/swift-account-replicator.1*
%{_mandir}/man1/swift-account-server.1*
%{_unitdir}/%{name}-account*.service
%dir %{_sysconfdir}/swift/account-server
%config(noreplace) %attr(640, root, swift) %{_sysconfdir}/swift/account-server.conf
%dir %attr(0755, swift, root) %{_runtimedir}/swift/account-server
%{_bindir}/swift-account-auditor
%{_bindir}/swift-account-info
%{_bindir}/swift-account-reaper
%{_bindir}/swift-account-replicator
%{_bindir}/swift-account-server

%files container
%doc etc/container-server.conf-sample
%{_mandir}/man5/container-server.conf.5*
%{_mandir}/man1/swift-container-auditor.1*
%{_mandir}/man1/swift-container-info.1*
%{_mandir}/man1/swift-container-replicator.1*
%{_mandir}/man1/swift-container-server.1*
%{_mandir}/man1/swift-container-sync.1*
%{_mandir}/man1/swift-container-updater.1*
%{_unitdir}/%{name}-container*.service
%dir %{_sysconfdir}/swift/container-server
%config(noreplace) %attr(640, root, swift) %{_sysconfdir}/swift/container-server.conf
%dir %attr(0755, swift, root) %{_runtimedir}/swift/container-server
%{_bindir}/swift-container-auditor
%{_bindir}/swift-container-info
%{_bindir}/swift-container-server
%{_bindir}/swift-container-replicator
%{_bindir}/swift-container-updater
%{_bindir}/swift-container-sync
%{python_sitelibdir}/swift/container

%files object
%doc etc/object-server.conf-sample etc/rsyncd.conf-sample
%{_mandir}/man5/object-server.conf.5*
%{_mandir}/man1/swift-object-auditor.1*
%{_mandir}/man1/swift-object-info.1*
%{_mandir}/man1/swift-object-replicator.1*
%{_mandir}/man1/swift-object-server.1*
%{_mandir}/man1/swift-object-updater.1*
%{_unitdir}/%{name}-object.service
%{_unitdir}/%{name}-object@.service
%{_unitdir}/%{name}-object-auditor.service
%{_unitdir}/%{name}-object-auditor@.service
%{_unitdir}/%{name}-object-replicator.service
%{_unitdir}/%{name}-object-replicator@.service
%{_unitdir}/%{name}-object-updater.service
%{_unitdir}/%{name}-object-updater@.service
%dir %{_sysconfdir}/swift/object-server
%config(noreplace) %attr(640, root, swift) %{_sysconfdir}/swift/object-server.conf
%dir %attr(0755, swift, root) %{_runtimedir}/swift/object-server
%{_bindir}/swift-object-auditor
%{_bindir}/swift-object-info
%{_bindir}/swift-object-replicator
%{_bindir}/swift-object-server
%{_bindir}/swift-object-updater

%files proxy
%doc etc/proxy-server.conf-sample etc/object-expirer.conf-sample
%{_mandir}/man5/object-expirer.conf.5*
%{_mandir}/man5/proxy-server.conf.5*
%{_mandir}/man1/swift-object-expirer.1*
%{_mandir}/man1/swift-proxy-server.1*
%{_unitdir}/%{name}-object-expirer.service
%{_unitdir}/%{name}-proxy.service
%dir %{_sysconfdir}/swift/proxy-server
%config(noreplace) %attr(640, root, swift) %{_sysconfdir}/swift/proxy-server.conf
%config(noreplace) %attr(640, root, swift) %{_sysconfdir}/swift/object-expirer.conf
%dir %attr(0755, swift, root) %{_runtimedir}/swift/proxy-server
%{_bindir}/swift-object-expirer
%{_bindir}/swift-proxy-server
%{python_sitelibdir}/swift/proxy

%files doc
%doc LICENSE doc/build/html

%changelog
* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 1.13.1-alt1
- 1.13.1 (based on Fedora 1.13.1-5.fc21.src)

* Thu Aug 29 2013 Pavel Shilovsky <piastry@altlinux.org> 1.7.0-alt3
- Cleanup spec

* Sat Mar 30 2013 Pavel Shilovsky <piastry@altlinux.org> 1.7.0-alt2.1
- Add SysVinit support

* Wed Mar 06 2013 Pavel Shilovsky <piastry@altlinux.org> 1.7.0-alt2
- Use post/preun_service scripts in spec

* Thu Nov 08 2012 Pavel Shilovsky <piastry@altlinux.org> 1.7.0-alt1
- Initial release for Sisyphus (based on Fedora)
