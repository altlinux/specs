Name:    foreman
Version: 1.19.0
Release: alt2

Summary: An application that automates the lifecycle of servers
License: GPLv3+ with exceptions
Group:  System/Servers
Url:     https://theforeman.org

Packager:  Andrey Cherepanov <cas@altlinux.org>
BuildArch: noarch

Source:  %name-%version.tar
Source1: %name.init
Source2: %name.sysconfig
Source3: %name.logrotate
Source4: %name.cron.d
Source5: %name.tmpfiles
Source6: dynflowd.sysconfig
Source7: dynflowd.service

Patch1: alt-use-new-fog-google-gem.patch
Patch2: patch-gemfile-to-change-rails-version-to-5.2.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: asciidoc-a2x

Requires: wget
Requires: vixie-cron
Requires: %name-debug

%add_findreq_skiplist %_datadir/%name/app/views/unattended/provisioning_templates/script/grubby_default.erb
%filter_from_requires \,^ruby-gem(fog_extensions/vsphere/mini_server,d

%description
Foreman is a free open source project that gives you the power to easily
automate repetitive tasks, quickly deploy applications, and proactively
manage your servers lifecyle, on-premises or in the cloud.
From provisioning and configuration to orchestration and monitoring,
Foreman integrates with your existing infrastructure to make operations
easier.
Using Puppet, Ansible, Chef, Salt and Foreman's smart proxy
architecture, you can easily automate repetitive tasks, quickly deploy
applications, and proactively manage change, both on-premise with VMs
and bare-metal or in the cloud.
Foreman provides comprehensive, interaction facilities including a web
frontend, CLI and RESTful API which enables you to build higher level
business logic on top of a solid foundation.

%package cli
Summary: Foreman CLI
Group: System/Servers
#Requires: ruby-gem(hammer_cli_foreman)

%description cli
Meta Package to install hammer rubygems and its dependencies.

%package debug
Summary: Foreman debug utilities
Group: System/Servers
Requires: rsync

%description debug
Useful utilities for debug info collection.

%package libvirt
Summary: Foreman libvirt support
Group: System/Servers
Requires: ruby-gem(fog-libvirt)
Requires: %name = %EVR
Requires: genisoimage

%description libvirt
Meta package to install requirements for libvirt compute resource support.

%package openstack
Summary: Foreman OpenStack support
Group: System/Servers
Requires: ruby-gem(fog-openstack)
Requires: %name = %EVR

%description openstack
Meta package to install requirements for OpenStack compute resource support.

%package ovirt
Summary: Foreman oVirt support
Group: System/Servers
Requires: ruby-gem(fog-ovirt)
Requires: %name-compute = %EVR
Requires: %name = %EVR

%description ovirt
Meta package to install requirements for oVirt compute resource support.

%package compute
Summary: Foreman compute resource Fog dependencies
Group: System/Servers
Requires: ruby-gem(fog)
Requires: %name = %EVR

%description compute
Meta package to install dependencies to support some compute resources. Most
compute resources have a more specific package which should be installed in
preference to this package.

%package ec2
Summary: Foreman Amazon Web Services (AWS) EC2 support
Group: System/Servers
Requires: ruby-gem(fog-aws)
Requires: %name = %EVR

%description ec2
Meta package to install requirements for Amazon Web Services (AWS) EC2 support.

%package rackspace
Summary: Foreman Rackspace support
Group: System/Servers
Requires: ruby-gem(fog-rackspace)
Requires: %name = %EVR

%description rackspace
Meta package to install requirements for Rackspace compute resource support.

%package vmware
Summary: Foreman VMware support
Group: System/Servers
Requires: ruby-gem(fog-vsphere)
Requires: %name = %EVR

%description vmware
Meta package to install requirements for VMware compute resource support.

%package gce
Summary: Foreman Google Compute Engine (GCE) support
Group: System/Servers
Requires: ruby-gem(fog-google)
Requires: ruby-google-api
Requires: %name = %EVR

%description gce
Meta package to install requirements for Google Compute Engine (GCE) support

%package assets
Summary: Foreman asset pipeline support
Group: System/Servers
Requires: %name = %EVR
Requires: node >= 6.10
# Temporary dep on libuv until https://bugs.centos.org/view.php?id=10606
# is resolved
# TODO Requires: libuv

# TODO Requires
%description assets
Meta package to install asset pipeline support.

%package plugin
Summary: Foreman plugin support
Group: System/Servers
Requires: %name = %EVR
Requires: %name-sqlite = %EVR

%description plugin
Meta package with support for plugins.

%package console
Summary: Foreman console support
Group: System/Servers
Requires: ruby-gem(wirb)
Requires: ruby-hirb-unicode-steakknife
Requires: ruby-gem(awesome_print)
Requires: %name = %EVR

%description console
Meta Package to install requirements for console support

%package mysql2
Summary: Foreman mysql2 support
Group: System/Servers
Requires: ruby-gem(mysql2)
Requires: %name = %EVR
Obsoletes: %name-mysql < 1.4.0
Provides: %name-mysql = %version

%description mysql2
Meta Package to install requirements for mysql2 support

%package postgresql
Summary: Foreman Postgresql support
Group: System/Servers
Requires: ruby-gem(pg)
Requires: %name = %EVR

%description postgresql
Meta Package to install requirements for postgresql support

%package sqlite
Summary: Foreman sqlite support
Group: System/Servers
Requires: ruby-gem(sqlite3)
Requires: %name = %EVR

%description sqlite
Meta Package to install requirements for sqlite support

%prep
%setup -n %name-%version
%patch1 -p1
%patch2 -p1
rm -rf script/perfomance
%update_setup_rb

%build
%ruby_config
%ruby_build
# Build man pages
rake -f Rakefile.dist build PREFIX=%_prefix SBINDIR=%_sbindir SYSCONFDIR=%_sysconfdir
# Build locale files
make -C locale all-mo

%install
%ruby_install
rake -f Rakefile.dist install PREFIX=%buildroot%_prefix SBINDIR=%buildroot%_sbindir SYSCONFDIR=%buildroot%_sysconfdir

mkdir -p %buildroot%_sbindir
for i in dynflowd %name-debug %name-rake %name-tail;do
	install -Dm0755 script/$i %buildroot%_sbindir/$i
done

mkdir -p %buildroot%_datadir/%name/plugins
mkdir -p %buildroot%_sysconfdir/%name/plugins

install -d %buildroot%_datadir/%name
cp -p Gemfile %buildroot%_datadir/%name/Gemfile.in
cp -p -r app bin bundler.d config config.ru extras lib locale Rakefile script %buildroot%_datadir/%name
rm -rf %buildroot%_datadir/%name/extras/{jumpstart,spec}

# Remove unnecessary files
find %buildroot%_datadir/%name/script/%name-tail.d/* -type d |xargs rm -rf
# Remove all test units from produciton release
find %buildroot%_datadir/%name -type d -name "test" |xargs rm -rf
# Remove spring loader, depends on Bundler and only installed via development group
rm -f %buildroot%_datadir/%name/bin/spring
# Remove executables from %_bindir and asciidoc form mandir
rm -f %buildroot%_bindir/* %buildroot%_mandir/*.asciidoc

# Move config files to %_sysconfdir
mv %buildroot%_datadir/%name/config/database.yml.example %buildroot%_datadir/%name/config/database.yml
mv %buildroot%_datadir/%name/config/settings.yaml.example %buildroot%_datadir/%name/config/settings.yaml

for i in database.yml logging.yaml settings.yaml foreman-debug.conf; do
mv %buildroot%_datadir/%name/config/$i %buildroot%_sysconfdir/%name
ln -svr %buildroot%_sysconfdir/%name/$i %buildroot%_datadir/%name/config/$i
done

# Put db in %_localstatedir/%name/db
cp -pr db/migrate db/seeds.rb db/seeds.d %buildroot%_datadir/%name
mkdir -p %buildroot%_localstatedir/%name/db

ln -svr %buildroot%_localstatedir/%name/db %buildroot%_datadir/%name/db
ln -svr %buildroot%_datadir/%name/migrate %buildroot%_localstatedir/%name/db/migrate
ln -svr %buildroot%_datadir/%name/seeds.rb %buildroot%_localstatedir/%name/db/seeds.rb
ln -svr %buildroot%_datadir/%name/seeds.d %buildroot%_localstatedir/%name/db/seeds.d

# Put HTML %_localstatedir/%name/public
cp -pr public %buildroot%_localstatedir/%name/
ln -svr %buildroot%_localstatedir/%name/public %buildroot%_datadir/%name/public

# Put logs from /var/log/%name
ln -svr %buildroot%_logdir/%name %buildroot%_datadir/%name/log

# Symlink plugin settings directory to
ln -svr %buildroot%_sysconfdir/%name/plugins %buildroot%_datadir/%name/config/settings.plugins.d

# Create VERSION file
install -pm0644 VERSION %buildroot%_datadir/%name/VERSION

# Keep a copy of the schema for quick initialisation of plugin builds
# TODO cp -pr db/schema.rb %buildroot%_datadir/%name/schema_plugin.rb

install -Dm0755 %SOURCE1 %buildroot%_initdir/%name
install -Dm0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -Dm0644 %SOURCE3 %buildroot%_logrotatedir/%name
install -Dm0644 %SOURCE4 %buildroot%_sysconfdir/cron.d/%name
install -Dm0644 %SOURCE5 %buildroot%_tmpfilesdir/%name.conf
install -Dm0644 %SOURCE6 %buildroot%_sysconfdir/sysconfig/dynflowd
install -Dm0644 %SOURCE7 %buildroot%_unitdir/dynflowd.service

install -d %buildroot%_logdir/%name

%pre
# Add the "foreman" user and group
getent group foreman >/dev/null || groupadd -r foreman
getent passwd _foreman >/dev/null || \
useradd -r -g foreman -d %_datadir/%name -s /sbin/nologin -c "Foreman" _foreman
exit 0

%post
# secret token used for cookie signing etc.
if [ ! -f %_datadir/%name/config/initializers/local_secret_token.rb ]; then
  touch %_datadir/%name/config/initializers/local_secret_token.rb
  chmod 0660 %_datadir/%name/config/initializers/local_secret_token.rb
  chgrp foreman %_datadir/%name/config/initializers/local_secret_token.rb
  foreman_rake security:generate_token >/dev/null 2>&1 || :
  chmod 0640 %_datadir/%name/config/initializers/local_secret_token.rb
fi

# encryption key used to encrypt DB contents
# move the generated key file to /etc/foreman/ so users back it up, symlink to it from ~foreman
if [ ! -e %_datadir/%name/config/initializers/encryption_key.rb -a \
     ! -e %_sysconfdir/%name/encryption_key.rb ]; then
  touch %_datadir/%name/config/initializers/encryption_key.rb
  chmod 0660 %_datadir/%name/config/initializers/encryption_key.rb
  chgrp foreman %_datadir/%name/config/initializers/encryption_key.rb
  foreman_rake security:generate_encryption_key >/dev/null 2>&1 || :
  chmod 0640 %_datadir/%name/config/initializers/encryption_key.rb
  mv %_datadir/%name/config/initializers/encryption_key.rb %_sysconfdir/%name/
fi
if [ ! -e %_datadir/%name/config/initializers/encryption_key.rb -a \
     -e %_sysconfdir/%name/encryption_key.rb ]; then
  ln -s %_sysconfdir/%name/encryption_key.rb %_datadir/%name/config/initializers/
fi
%post_service foreman
%post_service dynflowd

# We need to run the db:migrate after the install transaction
# always attempt to reencrypt after update in case new fields can be encrypted
foreman_rake db:migrate db:encrypt_all >> %_localstatedir/log/%name/db_migrate.log 2>&1 || :
foreman_rake db:seed >> %_localstatedir/log/%name/db_seed.log 2>&1 || :
foreman_rake apipie:cache:index >> %_localstatedir/log/%name/apipie_cache.log 2>&1 || :
foreman_rake tmp:clear >> %_localstatedir/log/%name/tmp_clear.log 2>&1 || :
(/bin/systemctl try-restart %name.service) >/dev/null 2>&1
exit 0

%preun
%preun_service foreman
%preun_service dynflowd

%files
%doc README* CONTRIBUTING.md LICENSE
%_sbindir/%name-rake
%_sbindir/%name-tail
%_sbindir/dynflowd
%ruby_sitelibdir/*
%config(noreplace) %_sysconfdir/%name/database.yml
%config(noreplace) %_sysconfdir/%name/foreman-debug.conf
%config(noreplace) %_sysconfdir/%name/logging.yaml
%config(noreplace) %_sysconfdir/%name/settings.yaml
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/plugins
%_datadir/%name
%exclude %_datadir/%name/bundler.d/*
%exclude %_datadir/%name/script/%name-debug.d
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_logrotatedir/%name
%_sysconfdir/cron.d/%name
%_tmpfilesdir/%name.conf
%config(noreplace) %_sysconfdir/sysconfig/dynflowd
%_unitdir/dynflowd.service
%attr(750,_foreman,foreman) %_logdir/%name
%attr(750,_foreman,foreman) %_localstatedir/%name
%_man8dir/*.8*
%rubygem_specdir/*

%files cli

%files debug
%_sbindir/%name-debug
%_datadir/%name/script/%name-debug.d

%files libvirt
%_datadir/%name/bundler.d/libvirt.rb

%files openstack
%_datadir/%name/bundler.d/openstack.rb

%files ovirt
%_datadir/%name/bundler.d/ovirt.rb

%files compute
%_datadir/%name/bundler.d/fog.rb

%files ec2
%_datadir/%name/bundler.d/ec2.rb

%files rackspace
%_datadir/%name/bundler.d/rackspace.rb

%files vmware
%_datadir/%name/bundler.d/vmware.rb

%files gce
%_datadir/%name/bundler.d/gce.rb

%files assets
%_datadir/%name/bundler.d/assets.rb

%files plugin
# TODO %%_datadir/%name/schema_plugin.rb

%files console
%_datadir/%name/bundler.d/console.rb

%files mysql2
%_datadir/%name/bundler.d/mysql2.rb

%files postgresql
%_datadir/%name/bundler.d/postgresql.rb

%files sqlite
%_datadir/%name/bundler.d/sqlite.rb

%changelog
* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 1.19.0-alt2
- Bumped to 1.19 with Gemfile fix.
- Enable auto req detection.

* Fri Sep 21 2018 Andrey Cherepanov <cas@altlinux.org> 1.19.0-alt1
- New version.

* Sun Jul 15 2018 Andrey Cherepanov <cas@altlinux.org> 1.18.0-alt1
- New version.

* Fri May 18 2018 Andrey Cherepanov <cas@altlinux.org> 1.17.1-alt1
- New version.

* Thu Apr 12 2018 Andrey Cherepanov <cas@altlinux.org> 1.17.0-alt1
- Initial build in Sisyphus
