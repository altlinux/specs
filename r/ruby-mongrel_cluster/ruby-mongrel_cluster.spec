# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname mongrel_cluster

Name: ruby-%pkgname
Version: 1.0.5
Release: alt6

Summary: Mongrel Cluster Plugin
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/mongrel/

Requires: %_datadir/gem_plugin

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Tue Nov 03 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-setup

%description
Tool to help start/stop/restart multiple mongrel servers to use behind
a load balancer like Apache 2.2 (mod_proxy_balancer), Lighttpd, Pound,
Pen or Balance. This plugin adds an option to specify a number of
Mongrel servers to launch, a range of ports, and a configuration file
for the cluster.

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

mv lib/%pkgname/init.rb .
rm -f resources/mongrel_cluster

%build
%ruby_config
%ruby_build

%install
%ruby_install

mkdir -p %buildroot{%_sysconfdir/%pkgname/sites-{available,enabled},%_logdir/%pkgname}

chmod +x %buildroot%_initdir/%pkgname
chmod +x %buildroot%_bindir/*

mkdir -p %buildroot%_datadir/gem_plugin/%pkgname
cp -vrp init.rb resources %buildroot%_datadir/gem_plugin/%pkgname

cat <<EOF >%buildroot%_datadir/gem_plugin/%pkgname/dependencies.yaml
---
- gem_plugin
- mongrel
EOF

%pre
/usr/sbin/groupadd -r -f _mongrel
/usr/sbin/useradd -r -n -g _mongrel -d /var/empty -s /dev/null -c 'Mongrel' _mongrel >/dev/null 2>&1 ||:

%post
%post_service %pkgname

%preun
%preun_service %pkgname

%files
%doc README README.ALT
%_initdir/%pkgname
%config(noreplace) %_logrotatedir/%pkgname
%_sysconfdir/%pkgname
%_bindir/*
%ruby_sitelibdir/*
%_datadir/gem_plugin/%pkgname
%attr(1777,root,root) %dir %_logdir/%pkgname

%changelog
* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.0.5-alt6
- Rebuild

* Fri Jul 23 2010 Alexey I. Froloff <raorn@altlinux.org> 1.0.5-alt5
- Fixed usage output to match expected arguments (closes: #23799)
- Fixed debug option processing (closes: #23800)

* Sun Nov 29 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.5-alt4
- Fix log path in logrotate script

* Tue Nov 17 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.5-alt3
- Fix log file name

* Wed Nov 11 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.5-alt2
- init.d/mongrel_cluster: pass --clean to mongrel_cluster_ctl
- mongrel_cluster: when loading foo.yml, source foo.env if available

* Tue Nov 03 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.5-alt1
- Built for Sisyphus

