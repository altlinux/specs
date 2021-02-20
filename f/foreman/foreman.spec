Name:          foreman
Version:       1.24.3.2
Release:       alt4
Summary:       An application that automates the lifecycle of servers
License:       GPLv3
Group:         System/Servers
Url:           https://theforeman.org
Vcs:           https://github.com/theforeman/foreman.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       database.yml
Source2:       %name.sysconfig
Source3:       %name.logrotate
Source4:       %name.cron.d
Source5:       %name.tmpfiles
Source6:       %name.service
Source7:       settings.yml
Source9:       manifest.js
Source10:      %name-production-%version.tar
Source11:      %name-jobs.service
Source12:      %name-jobs.sysconfig
Patch:         patch.patch
Patch1:        sass.patch
Patch2:        1.22.2.patch
Patch3:        1.22.3.1.patch

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
BuildRequires: node-sass

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
# explicit TODO then remove
Requires:      gem-sshkey
Requires:      gem-ldap-fluff
Requires:      gem-little-plugger
Requires:      gem-http-cookie
Requires:      gem-apipie-params
Requires:      gem-arel
Requires:      gem-secure-headers >= 6.3.0
Requires:      gem-ovirt-engine-sdk
Requires:      gem-rails-dom-testing
Requires:      gem-spice-html5-rails >= 0.1.5-alt1
Requires:      gem-gridster-rails >= 0.5.6.1-alt1
Requires:      dynflow

%gem_replace_version rails ~> 5.2
%gem_replace_version graphql ~> 1.9
%gem_replace_version jquery-ui-rails ~> 6.0
%gem_replace_version patternfly-sass ~> 3.38
%gem_replace_version fog-core ~> 2.1
%gem_replace_version prometheus-client ~> 2.0
%gem_replace_version sprockets ~> 4.0
%gem_replace_version sass-rails ~> 6.0
%gem_replace_version net-ssh ~> 6.0
%add_findreq_skiplist *.pyc
%add_findreq_skiplist *.pyo
%add_findreq_skiplist *.erb
%add_findreq_skiplist %_libexecdir/%name/**/*

# npmjs
%add_verify_elf_skiplist %_libexecdir/%name/**/*
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
%setup -a 10
%patch -p1
# TODO remove when patternfly-sass gem will be upgraded to new font-awesome-sass v5
%patch1 -p1
%patch2
%patch3
sed -e "s/a2x/asciidoctor/" -e "s/-f/-b/" -i Rakefile.dist # NOTE patching a2x to asciidoctor
sed "s,gem 'turbolinks'.*,gem 'gitlab-turbolinks-classic'," -i Gemfile
rm -rf ./node_modules/node-sass/ ./node_modules/.bin/node-sass
install -Dm0755 %SOURCE9 app/assets/config/manifest.js

%build
%ruby_build --ignore=font-awesome-sass --use=foreman --join=lib:bin --srcexedirs= --srcconfdirs= --srclibdirs=
# Build man pages
# rake -f Rakefile.dist build PREFIX=%_prefix SBINDIR=%_sbindir SYSCONFDIR=%_sysconfdir
# Build locale files
make -C locale all-mo

%install
# public www TODO
mkdir -p %buildroot%webserver_datadir \
         %buildroot%_sbindir \
         %buildroot/run/%name \
         %buildroot%_spooldir/%name/tmp \
         %buildroot%_cachedir/%name/_ \
         %buildroot%_localstatedir/%name \
         %buildroot%_cachedir/%name/openid-store \
         %buildroot%_sysconfdir/%name/plugins
mv config/foreman-debug.conf %buildroot%_sysconfdir/%name/foreman-debug.conf

%ruby_install
rm -rf %buildroot%_libexecdir/%name/extras/{jumpstart,spec}

# Create VERSION file
install -pm0644 VERSION %buildroot%_libexecdir/%name/VERSION
cp -r node_modules/.bin %buildroot%_libexecdir/%name/node_modules/

install -Dm0755 %SOURCE1 %buildroot%_sysconfdir/%name/database.yml
install -Dm0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -Dm0644 %SOURCE3 %buildroot%_logrotatedir/%name
install -Dm0644 %SOURCE4 %buildroot%_sysconfdir/cron.d/%name
install -Dm0644 %SOURCE5 %buildroot%_tmpfilesdir/%name.conf
install -Dm0755 %SOURCE6 %buildroot%_unitdir/%name.service
install -Dm0755 %SOURCE7 %buildroot%_sysconfdir/%name/settings.yml
install -Dm0640 /dev/null %buildroot%_sysconfdir/%name/encryption_key.rb
install -Dm0640 /dev/null %buildroot%_sysconfdir/%name/local_secret_token.rb
install -Dm0644 %SOURCE11 %buildroot%_unitdir/%{name}-jobs.service
install -Dm0644 %SOURCE12 %buildroot%_sysconfdir/sysconfig/%{name}-jobs


mv %buildroot%_libexecdir/%name/public %buildroot%webserver_datadir/%name
ln -svr %webserver_datadir/%name %buildroot%_libexecdir/%name/public
ln -svr %_sysconfdir/%name/plugins %buildroot%_libexecdir/%name/config/settings.plugins.d
ln -svr %_sysconfdir/%name/settings.yml %buildroot%_libexecdir/%name/config/settings.yaml
ln -svr %_sysconfdir/%name/database.yml %buildroot%_libexecdir/%name/config/database.yml
ln -svr %_sysconfdir/%name/foreman-debug.conf %buildroot%_libexecdir/%name/config/foreman-debug.conf
ln -svr %_sysconfdir/%name/encryption_key.rb %buildroot%_libexecdir/%name/config/initializers/encryption_key.rb
ln -svr %_sysconfdir/%name/local_secret_token.rb %buildroot%_libexecdir/%name/config/initializers/local_secret_token.rb
ln -svr %_spooldir/%name/tmp %buildroot%_libexecdir/%name/tmp
ln -svr %_cachedir/%name/_ %buildroot%_spooldir/%name/tmp/cache
ln -svr %_cachedir/%name/openid-store %buildroot%_libexecdir/%name/db/openid-store
ln -svr %_libexecdir/%name/script/foreman-rake %buildroot%_sbindir/foreman-rake
install -d %buildroot%_logdir/%name

%pre
# Add the "foreman" user and group
getent group foreman >/dev/null || %_sbindir/groupadd -r foreman
getent passwd _foreman >/dev/null || \
   %_sbindir/useradd -r -g foreman -G foreman -d %_localstatedir/%name -s /bin/bash -c "Foreman" _foreman
getent group puppet >/dev/null || \
   %_sbindir/usermod -a -G puppet _foreman
rm -rf %_libexecdir/%name/db/openid-store
exit 0

%post
%post_service foreman
%post_service foreman-jobs

%preun
railsctl cleanup %name
%preun_service foreman
%preun_service foreman-jobs


%files
%doc README* CONTRIBUTING.md LICENSE
%_sbindir/*
%_libexecdir/%name
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %_sysconfdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/sysconfig/%name-jobs
%config(noreplace) %_sysconfdir/%name/plugins
%config(noreplace) %_sysconfdir/%name/settings.yml
%config(noreplace) %_sysconfdir/%name/database.yml
%config(noreplace) %_sysconfdir/%name/foreman-debug.conf
%attr(640,_foreman,foreman) %config(noreplace) %_sysconfdir/%name/encryption_key.rb
%attr(640,_foreman,foreman) %config(noreplace) %_sysconfdir/%name/local_secret_token.rb
%attr(770,_foreman,foreman) %_sysconfdir/cron.d/%name
%_tmpfilesdir/%name.conf
%_unitdir/*
%attr(770,_foreman,foreman) %webserver_datadir/%name
%attr(770,_foreman,foreman) %_spooldir/%name/tmp
%attr(770,_foreman,foreman) %_cachedir/%name
%dir %attr(770,_foreman,foreman) %_cachedir/%name/openid-store
%dir %attr(770,_foreman,foreman) %_cachedir/%name/_
%dir %attr(770,_foreman,foreman) /run/%name
%dir %attr(770,_foreman,foreman) %_logdir/%name
%dir %attr(770,_foreman,foreman) %_localstatedir/%name
%dir %attr(770,_foreman,foreman) %_spooldir/%name
# %_man8dir/*.8*

%files         doc
%ruby_ridir/*

%changelog
* Sun Feb 14 2021 Pavel Skrylev <majioa@altlinux.org> 1.24.3.2-alt4
- ! spec folders to include
- ! default database config
- + foreman-jobs sysconfig and service

* Fri Jan 22 2021 Pavel Skrylev <majioa@altlinux.org> 1.24.3.2-alt3
- + deps to 4 module gems
- * right for some folders
- + _dynflow user to foreman group
- + foreman config

* Thu Dec 17 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.3.2-alt2
- ! to add modules

* Tue Dec 08 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.3.2-alt1
- ^ 1.24.3[1] -> 1.24.3[2]
- * updated embedded node packages
- ! path to images for some views
- ! scss files to conform new sprockets and sassc

* Thu Dec 03 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.3.1-alt1
- ^ 1.24.2 -> 1.24.3[1]

* Fri Jul 17 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt6.3
- > post services for foreman
- * moving user _foreman's home to /var/lib/foreman

* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt6.2
- ! spec dep replace for net-ssh gem to 6.x
- ! spec post script
- + external manifest.js

* Wed Jun 10 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt6.1
- ! gems dep for sprockets to 4.0, and sass-rails to 6.0

* Fri May 19 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt6
- * tmpfiles.d file

* Fri May 15 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt5
- ! patches and requires

* Fri May 08 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt4
- + explicit require deps to gem-secure-headers
- - post call to railsctl on install
- ! service name call to railsctl in .service

* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt3
- - post exec in spec
- * with service run using 'railsctl'
- ! gem rails deps to ~> 5.2

* Mon Mar 30 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt2
- * moving code from %%_libdir -> %%_libexecdir

* Mon Mar 02 2020 Pavel Skrylev <majioa@altlinux.org> 1.24.2-alt1
- updated (^) 1.22.2 -> 1.24.2
- updated (^) node modules
- fixed (!) systemd service file, and spec deps

* Wed Feb 26 2020 Pavel Skrylev <majioa@altlinux.org> 1.22.2-alt1
- updated (^) 1.22.0 -> 1.22.2
- added (+) post script condition to initialize the foreman after the db is
  initialized and started
- fixed (!) rails db/migration
- fixed (!) post-install code

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
