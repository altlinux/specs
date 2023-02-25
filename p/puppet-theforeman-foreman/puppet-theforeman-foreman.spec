# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname theforeman-foreman

Name:          puppet-%pkgname
Version:       22.1.2
Release:       alt1
Summary:       Foreman server configuration
License:       GPLv3
Group:         Development/Ruby
Url:           https://github.com/theforeman/puppet-foreman
Vcs:           https://github.com/theforeman/puppet-foreman.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         sssd.patch
Patch1:        ruby.patch
BuildRequires(pre): rpm-build-ruby

Requires:      puppet

%description
Puppet module for managing Foreman

Installs and configures Foreman, part of the Foreman installer or to be used as
a Puppet module.

Many Foreman plugins can be installed by adding additional foreman::plugin::*
classes, extra compute resource support via foreman::compute::* classes and
the Hammer CLI can be installed by adding foreman::cli.

By default, it configures Foreman to run as a standalone service fronted by
Apache as a reverse proxy with a PostgreSQL database.

The web interface is configured to use Puppet's SSL certificates by default,
so ensure they're present first, reconfigure server_ssl_* or disable the ssl
parameter. When used with the 'puppet' module, it will generate a new CA and
the required certificate.

Lots of parameters are supplied to tune the default installation, which may be
found in the class documentation at the top of each manifest.

Other modules may be used in combination with this one: puppet for managing
a Puppet master and agent, and foreman_proxy to configure Foreman's Smart Proxy
and related services.


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install
mkdir -p %buildroot%_libexecdir/puppet-modules/
mv %buildroot%_libexecdir/%name %buildroot%_libexecdir/puppet-modules/%pkgname
rm -f %buildroot%_libexecdir/puppet-modules/%pkgname/lib
mv %buildroot%ruby_sitelibdir %buildroot%_libexecdir/puppet-modules/%pkgname/lib

%check
%ruby_test

%files
%doc README*
%_libexecdir/puppet-modules/%pkgname


%changelog
* Thu Feb 09 2023 Pavel Skrylev <majioa@altlinux.org> 22.1.2-alt1
- ^ 19.1.1 -> 22.1.2

* Mon Jan 31 2022 Pavel Skrylev <majioa@altlinux.org> 19.1.1-alt1
- ^ 16.0.0 -> 19.1.1
- !fixed require sssd.rb in facter when it absents

* Wed Dec 23 2020 Pavel Skrylev <majioa@altlinux.org> 16.0.0-alt1.2
- ! placement for the puppet modules

* Wed Dec 23 2020 Pavel Skrylev <majioa@altlinux.org> 16.0.0-alt1.1
- + requires to puppet
- * to enable execution of embedded scripts

* Tue Dec 08 2020 Pavel Skrylev <majioa@altlinux.org> 16.0.0-alt1
- + packaged puppet module with usage Ruby Policy 2.0
