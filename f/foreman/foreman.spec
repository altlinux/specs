Name:          foreman
Version:       1.22.0
Release:       alt3
Summary:       An application that automates the lifecycle of servers
License:       GPLv3
Group:         System/Servers
Url:           https://theforeman.org
Vcs:           https://github.com/theforeman/foreman.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Source1:       database.yml
Source2:       %name.sysconfig
Source3:       %name.logrotate
Source4:       %name.cron.d
Source5:       %name.tmpfiles
# Source6:       dynflowd.sysconfig
# Source7:       dynflowd.service
Source8:       %name.service
Source9:       %name-production-%version.tar
Patch:         patch.patch
Patch1:        sass.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-macros-webserver-common
BuildRequires: ruby-gem(asciidoctor)
# npmjs
BuildRequires: elfutils
BuildRequires: glibc-core
BuildRequires: libX11-devel
#BuildRequires: libnss-devel
BuildRequires: libnspr-devel
BuildRequires: fontconfig
BuildRequires: libfreetype-devel

Requires:      wget
Requires:      vixie-cron
Requires:      postgresql-server
# npmjs
Requires:      libX11
Requires:      libnss
Requires:      libnspr
Requires:      fontconfig
Requires:      libfreetype

Requires:      node-sass
BuildRequires:      node-sass

%gem_replace_version rails ~> 5.2.2
%gem_replace_version graphql ~> 1.9
%gem_replace_version jquery-ui-rails ~> 6.0
%gem_replace_version sqlite3 ~> 1.3
%gem_replace_version patternfly-sass ~> 3.38
%gem_replace_version fog-core ~> 2.1
%gem_replace_version fog-ovirt ~> 1.1
%gem_replace_version fog-google ~> 1.8
%gem_replace_version deep_cloneable ~> 3.0
%gem_replace_version turbolinks ~> 5.2
%add_findreq_skiplist *.pyc
%add_findreq_skiplist *.pyo
%add_findreq_skiplist *.erb
%add_findreq_skiplist %_libdir/%name/**/*

# npmjs
%add_verify_elf_skiplist %_libdir/%name/**/*
# used binaries in node_modules
ExclusiveArch: x86_64

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


%package       doc
Summary:       Foreman code documentation
Group:         Development/Documentation

%description   doc
Foreman code documentation.


%prep
%setup -a 9
%patch -p1
# TODO remove when patternfly-sass gem will be upgraded to new font-awesome-sass v5
%patch1 -p1
sed -e "s/a2x/asciidoctor/" -e "s/-f/-b/" -i Rakefile.dist # NOTE patching a2x to asciidoctor
sed '$agem "coffee-script-source", "~> 1.12"' -i Gemfile

%build
%ruby_build --ignore=font-awesome-sass --use=foreman --join=lib:bin --srcexedirs= --srcconfdirs= --srclibdirs=
# Build man pages
# rake -f Rakefile.dist build PREFIX=%_prefix SBINDIR=%_sbindir SYSCONFDIR=%_sysconfdir
# Build locale files
make -C locale all-mo

%install
%ruby_install
rm -rf %buildroot%_libdir/%name/extras/{jumpstart,spec}

# Create VERSION file
install -pm0644 VERSION %buildroot%_libdir/%name/VERSION
cp -r node_modules/.bin %buildroot%_libdir/%name/node_modules/

install -Dm0755 %SOURCE1 %buildroot%_libdir/%name/config/database.yml
install -Dm0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -Dm0644 %SOURCE3 %buildroot%_logrotatedir/%name
install -Dm0644 %SOURCE4 %buildroot%_sysconfdir/cron.d/%name
install -Dm0644 %SOURCE5 %buildroot%_tmpfilesdir/%name.conf
# install -Dm0644 %%SOURCE6 %buildroot%_sysconfdir/sysconfig/dynflowd
# install -Dm0644 %%SOURCE7 %buildroot%_unitdir/dynflowd.service
install -Dm0755 %SOURCE8 %buildroot%_unitdir/%name.service

# public www TODO
mkdir -p %buildroot%webserver_datadir
mv %buildroot%_libdir/%name/public %buildroot%webserver_datadir/%name
ln -svr %webserver_datadir/%name %buildroot%_libdir/%name/public

install -d %buildroot%_logdir/%name

%pre
# Add the "foreman" user and group
getent group foreman >/dev/null || groupadd -r foreman
getent passwd _foreman >/dev/null || \
useradd -r -g foreman -d %_libdir/%name -s /bin/bash -c "Foreman" _foreman
exit 0

%post
%post_service postgresql
systemctl start postgresql

mkdir -m 750 -p %_var/tmp/%name
mkdir -m 750 -p %_cachedir/%name
ln -sf %_var/tmp/%name %_libdir/%name/tmp
ln -sf %_cachedir/%name %_var/tmp/%name/cache
chown _foreman:foreman %_var/tmp/%name
chown _foreman:foreman %_cachedir/%name

export RAILS_ENV=production

appname=%name
datadir=%_libdir
# CONFDIR=/etc
rootdir=$datadir/$appname
confdir=$rootdir/config

# alias bundle exec rake='bundle exec rake'

cd $rootdir

if [ -z "$(psql -U postgres -tAc "SELECT 1 FROM pg_roles WHERE rolname='foreman'")" ]; then
   # create db users with postgres
   # echo "Please enter password for an admin of the foreman server: "
   createuser $appname -U postgres --createdb --createrole -w # -W
fi

# env
rm -f Gemfile.lock
bundle >/dev/null 2>&1 || :
# bundle binstubs bundler --force
# npm install

# secret token used for cookie signing etc.
if [ ! -f $datadir/$appname/config/initializers/local_secret_token.rb ]; then
   # echo "Initializing secret..."
   touch $datadir/$appname/config/initializers/local_secret_token.rb
   chmod 0660 $datadir/$appname/config/initializers/local_secret_token.rb
   chgrp foreman $datadir/$appname/config/initializers/local_secret_token.rb
   bundle exec rake security:generate_token >/dev/null 2>&1 || :
   chmod 0640 $datadir/$appname/config/initializers/local_secret_token.rb
fi

# encryption key used to encrypt DB contents
# move the generated key file to /etc/foreman/ so users back it up, symlink to it from ~foreman
if [ ! -e $datadir/$appname/config/initializers/encryption_key.rb -a \
     ! -e $confdir/encryption_key.rb ]; then
   # echo "Initializing encryption key..."
   touch $datadir/$appname/config/initializers/encryption_key.rb
   chmod 0660 $datadir/$appname/config/initializers/encryption_key.rb
   chgrp foreman $datadir/$appname/config/initializers/encryption_key.rb
   bundle exec rake security:generate_encryption_key >/dev/null 2>&1 || :
   chmod 0640 $datadir/$appname/config/initializers/encryption_key.rb
   mv $datadir/$appname/config/initializers/encryption_key.rb $confdir/
fi

if [ ! -e $datadir/$appname/config/initializers/encryption_key.rb -a \
       -e $confdir/encryption_key.rb ]; then
   # echo "Initializing link to encryption key..."
   ln -s $confdir/encryption_key.rb $datadir/$appname/config/initializers/
fi

if ! psql -U postgres -lqt | cut -d \| -f 1 | grep -qw ${appname}_${RAILS_ENV}; then
   # echo "Initializing database..."
   # We need to run the db:migrate after the install transaction
   # always attempt to reencrypt after update in case new fields can be encrypted
   bundle exec rake db:create db:migrate db:encrypt_all >> $datadir/$appname/log/db_migrate.log 2>&1 || :
   bundle exec rake db:seed >> $datadir/$appname/log/db_seed.log 2>&1 || :
   bundle exec rake apipie:cache:index >> $datadir/$appname/log/apipie_cache.log 2>&1 || :
   bundle exec rake tmp:clear >> $datadir/$appname/log/tmp_clear.log 2>&1 || :
fi

if [ -z "$(ls ./public/webpack/*js 2>/dev/null)" ]; then
   # echo "Initializing webpack frontend..."
   bundle exec rake webpack:compile >> $datadir/$appname/log/webpack_compile.log 2>&1 || :
fi

if [ -z "$(ls ./public/assets/*js 2>/dev/null)" ]; then
   # echo "Initializing assets frontend..."
   bundle exec rake assets:precompile >> $datadir/$appname/log/assets_precompile.log 2>&1 || :
fi

%post_service foreman
# %post_service dynflowd

%preun
%preun_service foreman
# %preun_service dynflowd

rm -rf %_libdir/%name/tmp %_var/tmp/%name/cache %_var/tmp/%name %_cachedir/%name %_libdir/%name/Gemfile.lock


%files
%doc README* CONTRIBUTING.md LICENSE
# %_sbindir/dynflowd
# %config(noreplace) %_sysconfdir/%name/logging.yaml
# %config(noreplace) %_sysconfdir/%name/settings.yaml
# %dir %_sysconfdir/%name/plugins
%_libdir/%name
# %exclude %_datadir/%name/bundler.d/*
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_logrotatedir/%name
%_sysconfdir/cron.d/%name
%_tmpfilesdir/%name.conf
# %config(noreplace) %_sysconfdir/sysconfig/dynflowd
# %_unitdir/dynflowd.service
%_unitdir/*
%webserver_datadir/%name
%attr(750,_foreman,foreman) %_logdir/%name
# %attr(750,_foreman,foreman) %_localstatedir/%name
# %_man8dir/*.8*

%files         doc
%ruby_ridir/*

%changelog
* Fri Jan 24 2020 Vitaly Lipatov <lav@altlinux.ru> 1.22.0-alt3
- drop libnss-devel buildreq
- update node_modules with node.js >= 13

* Mon Nov 25 2019 Pavel Skrylev <majioa@altlinux.org> 1.22.0-alt2
- changed (*) license
- fixed (!) requires and required service
- added (+) vcs tag to spec
- fixed (!) post install procedure, running the postgres server to setup users
  and db

* Thu Sep 26 2019 Pavel Skrylev <majioa@altlinux.org> 1.22.0-alt1
- updated (^) 1.20.1 -> 1.22.0
- fixed (!) run and primarily work, js is bundled in

* Mon Jan 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.20.1-alt1
- Bump to 1.20.1.

* Thu Sep 27 2018 Pavel Skrylev <majioa@altlinux.org> 1.19.0-alt5
- Patch to support 5.2 rails from master.
- Rake tasks moved to named subfolder.
- Avoid aarch64

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
