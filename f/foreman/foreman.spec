%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel

Name:          foreman
Version:       3.18.1
Release:       alt1
Summary:       An application that automates the lifecycle of servers
License:       MIT
Group:         System/Servers
Url:           https://theforeman.org
Vcs:           https://github.com/theforeman/foreman.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       database.yml
Source2:       foreman.sysconfig
Source3:       foreman.logrotate
Source4:       foreman.cron.d
Source5:       foreman.tmpfiles
Source6:       foreman.service
Source7:       settings.yml
Source8:       foreman.conf
Source9:       foreman.po
Source10:      public.tar
Source11:      foreman-jobs.service
Source12:      foreman-jobs.sysconfig
Patch7:        rails7.1.patch
Patch6:        rails_6.patch
Patch5:        asciidoctor-doc.patch
Patch3:        invalid_premission.patch
Patch2:        fast_gettext-2.3.0.patch
Patch1:        alt.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(activerecord-nulldb-adapter) >= 0
BuildRequires: gem(activerecord-session_store) >= 2.0.0
BuildRequires: gem(amazing_print) >= 2.0
BuildRequires: gem(ancestry) >= 4.0
BuildRequires: gem(apipie-dsl) >= 2.6.2
BuildRequires: gem(apipie-rails) >= 0.8.0
BuildRequires: gem(as_deprecation_tracker) >= 1.6
BuildRequires: gem(audited) > 5.1.0
BuildRequires: gem(bcrypt) >= 3.1
BuildRequires: gem(benchmark-ips) >= 2.8.2
BuildRequires: gem(bootsnap) >= 0
BuildRequires: gem(bullet) >= 6.1.0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(capybara) >= 3.33
BuildRequires: gem(daemons) >= 0
BuildRequires: gem(database_cleaner) >= 1.3
BuildRequires: gem(deacon) >= 1.0
BuildRequires: gem(deep_cloneable) >= 3
BuildRequires: gem(dynflow) >= 1.6.5
BuildRequires: gem(facterdb) >= 1.7
BuildRequires: gem(factory_bot_rails) >= 5.0
BuildRequires: gem(fast_gettext) >= 2.1
BuildRequires: gem(fog-core) >= 2.1
BuildRequires: gem(friendly_id) >= 5.4.1
BuildRequires: gem(get_process_mem) >= 0
BuildRequires: gem(gettext) >= 3.2.1
BuildRequires: gem(gettext_i18n_rails) >= 1.8
BuildRequires: gem(graphiql-rails) >= 1.7
BuildRequires: gem(graphql) >= 1.9.6
BuildRequires: gem(graphql-batch) >= 0
BuildRequires: gem(immigrant) >= 0.1
BuildRequires: gem(jwt) >= 2.2.1
BuildRequires: gem(launchy) >= 2.4
BuildRequires: gem(ldap_fluff) >= 0.9.0
BuildRequires: gem(logging) >= 1.8.0
BuildRequires: gem(mail) >= 2.7
BuildRequires: gem(maruku) >= 0.7
BuildRequires: gem(minitest) >= 5.1
BuildRequires: gem(minitest-reporters) >= 1.4
BuildRequires: gem(minitest-retry) >= 0.0
BuildRequires: gem(minitest-spec-rails) >= 7.1
BuildRequires: gem(minitest_reporters_github) >= 1.0
BuildRequires: gem(mocha) >= 2.1
BuildRequires: gem(net-ldap) >= 0.16.0
BuildRequires: gem(net-ping) >= 0
BuildRequires: gem(net-scp) >= 0
BuildRequires: gem(net-ssh) >= 0
BuildRequires: gem(oauth) >= 1.0
BuildRequires: gem(parallel_tests) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-doc) >= 0
BuildRequires: gem(pry-rails) >= 0
BuildRequires: gem(pry-remote) >= 0
BuildRequires: gem(pry-stack_explorer) >= 0
BuildRequires: gem(puma) >= 5.1
BuildRequires: gem(rabl) >= 0.15.0
BuildRequires: gem(rack-cors) >= 1.1
BuildRequires: gem(rails) >= 7.0.3
BuildRequires: gem(rails-controller-testing) >= 1.0
BuildRequires: gem(rails-i18n) >= 7.0
BuildRequires: gem(rainbow) >= 2.2.1
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(responders) >= 3.0
BuildRequires: gem(rest-client) >= 2.0.0
BuildRequires: gem(rfauxfactory) >= 0.1.5
BuildRequires: gem(roadie-rails) >= 3.0
BuildRequires: gem(robottelo_reporter) >= 0.1
BuildRequires: gem(rss) >= 0
BuildRequires: gem(safemode) >= 1.4
BuildRequires: gem(scoped_search) >= 4.1.9
BuildRequires: gem(secure_headers) >= 6.3
BuildRequires: gem(selenium-webdriver) >= 0
BuildRequires: gem(shoulda-context) >= 1.2
BuildRequires: gem(shoulda-matchers) >= 5.0
BuildRequires: gem(show_me_the_cookies) >= 6.0
BuildRequires: gem(spring) = 4.2.1
BuildRequires: gem(sprockets) >= 4.0
BuildRequires: gem(sprockets-rails) >= 3.0
BuildRequires: gem(sshkey) >= 2.0
BuildRequires: gem(statsd-instrument) >= 3.0
BuildRequires: gem(theforeman-rubocop) >= 0.1.2
BuildRequires: gem(validates_lengths_from_database) >= 0.5
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(will_paginate) >= 3.3
BuildConflicts: gem(activerecord-session_store) >= 3
BuildConflicts: gem(ancestry) >= 5
BuildConflicts: gem(apipie-rails) >= 2
BuildConflicts: gem(as_deprecation_tracker) >= 2
BuildConflicts: gem(bcrypt) >= 4
BuildConflicts: gem(capybara) >= 4
BuildConflicts: gem(database_cleaner) >= 3
BuildConflicts: gem(deacon) >= 2
BuildConflicts: gem(deep_cloneable) >= 4
BuildConflicts: gem(dynflow) >= 3.0.0
BuildConflicts: gem(facterdb) >= 2
BuildConflicts: gem(factory_bot_rails) >= 7
BuildConflicts: gem(fast_gettext) >= 3
BuildConflicts: gem(fog-core) >= 3
BuildConflicts: gem(friendly_id) >= 6
BuildConflicts: gem(gettext) >= 4.0.0
BuildConflicts: gem(gettext_i18n_rails) >= 2
BuildConflicts: gem(graphiql-rails) >= 2
BuildConflicts: gem(graphql) >= 2
BuildConflicts: gem(immigrant) >= 1
BuildConflicts: gem(jwt) >= 3
BuildConflicts: gem(launchy) >= 3
BuildConflicts: gem(ldap_fluff) >= 1.0
BuildConflicts: gem(logging) >= 3.0.0
BuildConflicts: gem(mail) >= 3
BuildConflicts: gem(maruku) >= 1
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(minitest-reporters) >= 2
BuildConflicts: gem(minitest-retry) >= 1
BuildConflicts: gem(minitest-spec-rails) >= 8
BuildConflicts: gem(minitest_reporters_github) >= 2
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(oauth) >= 2
BuildConflicts: gem(puma) >= 7
BuildConflicts: gem(rabl) >= 1
BuildConflicts: gem(rack-cors) >= 4
BuildConflicts: gem(rails) >= 8
BuildConflicts: gem(rails-controller-testing) >= 2
BuildConflicts: gem(rails-i18n) >= 8
BuildConflicts: gem(responders) >= 4
BuildConflicts: gem(rest-client) >= 3
BuildConflicts: gem(rfauxfactory) >= 1
BuildConflicts: gem(roadie-rails) >= 4
BuildConflicts: gem(robottelo_reporter) >= 1
BuildConflicts: gem(safemode) >= 2
BuildConflicts: gem(scoped_search) >= 5
BuildConflicts: gem(secure_headers) >= 8
BuildConflicts: gem(shoulda-context) >= 3
BuildConflicts: gem(shoulda-matchers) >= 7
BuildConflicts: gem(show_me_the_cookies) >= 7
BuildConflicts: gem(sprockets) >= 5
BuildConflicts: gem(sprockets-rails) >= 4
BuildConflicts: gem(sshkey) >= 3
BuildConflicts: gem(theforeman-rubocop) >= 1
BuildConflicts: gem(validates_lengths_from_database) >= 1
BuildConflicts: gem(will_paginate) >= 5
%endif

Autoprov:      yes,nopython3,nopython,noshell
Autoreq:       yes,nopython3,nopython,noshell
%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency amazing_print >= 2.0.0,amazing_print < 3
%ruby_use_gem_dependency statsd-instrument >= 3.0.0,statsd-instrument < 4
%ruby_use_gem_dependency rack-cors >= 3.0.0,rack-cors < 4
%ruby_use_gem_dependency will_paginate >= 4.0.0,will_paginate < 5
%ruby_use_gem_dependency sidekiq >= 7.3.8,sidekiq < 8
%ruby_use_gem_dependency redis >= 6.0.0,redis < 7
%ruby_use_gem_dependency jwt >= 2.2.1,jwt < 3
%ruby_use_gem_dependency audited >= 5.0.1,audited < 6
%ruby_use_gem_dependency rails >= 7.1,rails < 8
%ruby_use_gem_dependency graphql >= 1.9.6,graphql < 2
%ruby_use_gem_dependency patternfly-sass >= 3.59.5,patternfly-sass < 4
%ruby_use_gem_dependency scoped_search >= 4.1.9,scoped_search < 5
%ruby_use_gem_dependency friendly_id >= 5.4.1,friendly_id < 6
%ruby_use_gem_dependency database_cleaner >= 2.0.1,database_cleaner < 3
%ruby_use_gem_dependency factory_bot_rails >= 6.2.0,factory_bot_rails < 7
%ruby_use_gem_dependency shoulda-matchers >= 6.4.0,shoulda-matchers < 7
%ruby_use_gem_dependency shoulda-context >= 2.0.0,shoulda-context < 3
%ruby_use_gem_dependency theforeman-rubocop >= 0.1.2,theforeman-rubocop < 1
Requires:      rake
Requires:      wget
Requires:      vixie-cron
Requires:      postgresql-server
Requires:      dynflow
Requires:      node
Requires:      nginx
Requires:      railsctl >= 1.0.1-alt1
Requires:      ruby >= 3.1.2
Requires:      gem(activerecord-nulldb-adapter) >= 0
Requires:      gem(activerecord-session_store) >= 2.0.0
Requires:      gem(amazing_print) >= 2.0
Requires:      gem(ancestry) >= 4.0
Requires:      gem(apipie-dsl) >= 2.6.2
Requires:      gem(apipie-rails) >= 0.8.0
Requires:      gem(as_deprecation_tracker) >= 1.6
Requires:      gem(audited) > 5.1.0
Requires:      gem(bcrypt) >= 3.1
Requires:      gem(benchmark-ips) >= 2.8.2
Requires:      gem(bootsnap) >= 0
Requires:      gem(bullet) >= 6.1.0
Requires:      gem(byebug) >= 0
Requires:      gem(capybara) >= 3.33
Requires:      gem(daemons) >= 0
Requires:      gem(database_cleaner) >= 1.3
Requires:      gem(deacon) >= 1.0
Requires:      gem(deep_cloneable) >= 3
Requires:      gem(dynflow) >= 1.6.5
Requires:      gem(facterdb) >= 1.7
Requires:      gem(factory_bot_rails) >= 5.0
Requires:      gem(fast_gettext) >= 2.1
Requires:      gem(fog-core) >= 2.1
Requires:      gem(friendly_id) >= 5.4.1
Requires:      gem(get_process_mem) >= 0
Requires:      gem(gettext) >= 3.2.1
Requires:      gem(gettext_i18n_rails) >= 1.8
Requires:      gem(graphiql-rails) >= 1.7
Requires:      gem(graphql) >= 1.9.6
Requires:      gem(graphql-batch) >= 0
Requires:      gem(immigrant) >= 0.1
Requires:      gem(jwt) >= 2.2.1
Requires:      gem(launchy) >= 2.4
Requires:      gem(ldap_fluff) >= 0.9.0
Requires:      gem(logging) >= 1.8.0
Requires:      gem(mail) >= 2.7
Requires:      gem(maruku) >= 0.7
Requires:      gem(minitest) >= 5.1
Requires:      gem(minitest-reporters) >= 1.4
Requires:      gem(minitest-retry) >= 0.0
Requires:      gem(minitest-spec-rails) >= 7.1
Requires:      gem(minitest_reporters_github) >= 1.0
Requires:      gem(mocha) >= 2.1
Requires:      gem(net-ldap) >= 0.16.0
Requires:      gem(net-ping) >= 0
Requires:      gem(net-scp) >= 0
Requires:      gem(net-ssh) >= 0
Requires:      gem(oauth) >= 1.0
Requires:      gem(parallel_tests) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-doc) >= 0
Requires:      gem(pry-rails) >= 0
Requires:      gem(pry-remote) >= 0
Requires:      gem(pry-stack_explorer) >= 0
Requires:      gem(puma) >= 5.1
Requires:      gem(rabl) >= 0.15.0
Requires:      gem(rack-cors) >= 1.1
Requires:      gem(rails) >= 7.0.3
Requires:      gem(rails-controller-testing) >= 1.0
Requires:      gem(rails-i18n) >= 7.0
Requires:      gem(rainbow) >= 2.2.1
Requires:      gem(rdoc) >= 0
Requires:      gem(responders) >= 3.0
Requires:      gem(rest-client) >= 2.0.0
Requires:      gem(rfauxfactory) >= 0.1.5
Requires:      gem(roadie-rails) >= 3.0
Requires:      gem(robottelo_reporter) >= 0.1
Requires:      gem(rss) >= 0
Requires:      gem(safemode) >= 1.4
Requires:      gem(scoped_search) >= 4.1.9
Requires:      gem(secure_headers) >= 6.3
Requires:      gem(selenium-webdriver) >= 0
Requires:      gem(shoulda-context) >= 1.2
Requires:      gem(shoulda-matchers) >= 5.0
Requires:      gem(show_me_the_cookies) >= 6.0
Requires:      gem(spring) = 4.2.1
Requires:      gem(sprockets) >= 4.0
Requires:      gem(sprockets-rails) >= 3.0
Requires:      gem(sshkey) >= 2.0
Requires:      gem(statsd-instrument) >= 3.0
Requires:      gem(theforeman-rubocop) >= 0.1.2
Requires:      gem(validates_lengths_from_database) >= 0.5
Requires:      gem(webmock) >= 0
Requires:      gem(will_paginate) >= 3.3
Requires:      gem(gridster-rails) >= 0
Requires:      gem(spice-html5-rails) >= 0
Requires:      gem(font-awesome-rails) >= 0
Requires:      gem(foreman_templates) >= 0
Requires:      gem(foreman_remote_execution) >= 0
Requires:      gem(foreman_discovery) >= 0
Requires:      gem(foreman_ansible) >= 0
Requires:      gem(foreman_default_hostgroup) >= 0
Requires:      gem(foreman_puppet) >= 0
Requires:      gem(foreman_setup) >= 0
Requires:      gem(foreman_maintain) >= 0
Requires:      gem(foreman_chef) >= 0
Requires:      gem(foreman_hooks) >= 0
Requires:      gem(foreman_api_client) >= 0
Requires:      gem(foreman_monitoring) >= 0
Requires:      gem(foreman_cert_revoke_host) >= 0
Requires:      gem(foreman_webhooks) >= 0
Requires:      gem(rbvmomi) >= 0
Requires:      gem(font-awesome-sass) >= 0
Requires:      gem(patternfly-sass) >= 0
Requires:      gem(gettext_i18n_rails_js) >= 0
Requires:      gem(terser) >= 0
Requires:      gem(sass-rails) >= 0
Requires:      gem(wirb) >= 0
Requires:      gem(sidekiq) >= 0
Requires:      gem(gitlab-sidekiq-fetcher) >= 0
Requires:      gem(fog-aws) >= 0
Requires:      gem(logging-journald) >= 0
Requires:      gem(rack-jsonp) >= 0
Requires:      gem(fog-libvirt) >= 0
Requires:      gem(rack-openid) >= 0
Requires:      gem(fog-openstack) >= 0
Requires:      gem(pg) >= 0
Requires:      gem(redis) >= 0
Requires:      gem(sd_notify) >= 0
Requires:      gem(prometheus-client) >= 0
Requires:      gem(fog-vsphere) >= 0
Requires:      gem(ruby_engine) >= 2.0.0.3
Conflicts:     gem(activerecord-session_store) >= 3
Conflicts:     gem(ancestry) >= 5
Conflicts:     gem(apipie-rails) >= 2
Conflicts:     gem(as_deprecation_tracker) >= 2
Conflicts:     gem(bcrypt) >= 4
Conflicts:     gem(capybara) >= 4
Conflicts:     gem(database_cleaner) >= 3
Conflicts:     gem(deacon) >= 2
Conflicts:     gem(deep_cloneable) >= 4
Conflicts:     gem(dynflow) >= 3.0.0
Conflicts:     gem(facterdb) >= 2
Conflicts:     gem(factory_bot_rails) >= 7
Conflicts:     gem(fast_gettext) >= 3
Conflicts:     gem(fog-core) >= 3
Conflicts:     gem(friendly_id) >= 6
Conflicts:     gem(gettext) >= 4.0.0
Conflicts:     gem(gettext_i18n_rails) >= 2
Conflicts:     gem(graphiql-rails) >= 2
Conflicts:     gem(graphql) >= 2
Conflicts:     gem(immigrant) >= 1
Conflicts:     gem(jwt) >= 3
Conflicts:     gem(launchy) >= 3
Conflicts:     gem(ldap_fluff) >= 1.0
Conflicts:     gem(logging) >= 3.0.0
Conflicts:     gem(mail) >= 3
Conflicts:     gem(maruku) >= 1
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-reporters) >= 2
Conflicts:     gem(minitest-retry) >= 1
Conflicts:     gem(minitest-spec-rails) >= 8
Conflicts:     gem(minitest_reporters_github) >= 2
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(oauth) >= 2
Conflicts:     gem(puma) >= 7
Conflicts:     gem(rabl) >= 1
Conflicts:     gem(rack-cors) >= 4
Conflicts:     gem(rails) >= 8
Conflicts:     gem(rails-controller-testing) >= 2
Conflicts:     gem(rails-i18n) >= 8
Conflicts:     gem(responders) >= 4
Conflicts:     gem(rest-client) >= 3
Conflicts:     gem(rfauxfactory) >= 1
Conflicts:     gem(roadie-rails) >= 4
Conflicts:     gem(robottelo_reporter) >= 1
Conflicts:     gem(safemode) >= 2
Conflicts:     gem(scoped_search) >= 5
Conflicts:     gem(secure_headers) >= 8
Conflicts:     gem(shoulda-context) >= 3
Conflicts:     gem(shoulda-matchers) >= 7
Conflicts:     gem(show_me_the_cookies) >= 7
Conflicts:     gem(sprockets) >= 5
Conflicts:     gem(sprockets-rails) >= 4
Conflicts:     gem(sshkey) >= 3
Conflicts:     gem(theforeman-rubocop) >= 1
Conflicts:     gem(validates_lengths_from_database) >= 1
Conflicts:     gem(will_paginate) >= 5
Conflicts:     foreman-addons
Obsoletes:     foreman-addons < %EVR

%ruby_on_build_rake_tasks build

%description
Foreman is a free open source project that gives you the power to easily
automate repetitive tasks, quickly deploy applications, and proactively manage
your servers lifecyle, on-premises or in the cloud. From provisioning and
configuration to orchestration and monitoring, Foreman integrates with your
existing infrastructure to make operations easier. Using Puppet, Ansible, Chef,
Salt and Foreman's smart proxy architecture, you can easily automate repetitive
tasks, quickly deploy applications, and proactively manage change, both
on-premise with VMs and bare-metal or in the cloud. Foreman provides
comprehensive, interaction facilities including a web frontend, CLI and RESTful
API which enables you to build higher level business logic on top of a solid
foundation.


%if_enabled    doc
%package       -n foreman-doc
Version:       3.18.1
Release:       alt1
Summary:       An application that automates the lifecycle of servers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      foreman = 3.18.1-alt1

%description   -n foreman-doc
An application that automates the lifecycle of servers documentation
files.

Foreman is a free open source project that gives you the power to easily
automate repetitive tasks, quickly deploy applications, and proactively manage
your servers lifecyle, on-premises or in the cloud. From provisioning and
configuration to orchestration and monitoring, Foreman integrates with your
existing infrastructure to make operations easier. Using Puppet, Ansible, Chef,
Salt and Foreman's smart proxy architecture, you can easily automate repetitive
tasks, quickly deploy applications, and proactively manage change, both
on-premise with VMs and bare-metal or in the cloud. Foreman provides
comprehensive, interaction facilities including a web frontend, CLI and RESTful
API which enables you to build higher level business logic on top of a solid
foundation.
%endif


%if_enabled    devel
%package       -n foreman-devel
Version:       3.18.1
Release:       alt1
Summary:       An application that automates the lifecycle of servers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      foreman = 3.18.1-alt1

%description   -n foreman-devel
Foreman is a free open source project that gives you the power to easily
automate repetitive tasks, quickly deploy applications, and proactively manage
your servers lifecyle, on-premises or in the cloud. From provisioning and
configuration to orchestration and monitoring, Foreman integrates with your
existing infrastructure to make operations easier. Using Puppet, Ansible, Chef,
Salt and Foreman's smart proxy architecture, you can easily automate repetitive
tasks, quickly deploy applications, and proactively manage change, both
on-premise with VMs and bare-metal or in the cloud. Foreman provides
comprehensive, interaction facilities including a web frontend, CLI and RESTful
API which enables you to build higher level business logic on top of a solid
foundation.
%endif


%prep
%setup -a 10
%autopatch -p1

rm -rf ./extras/jumpstart ./tmp/cache
install -Dm0755 %SOURCE9 ./locale/ru/foreman.po

%build
%ruby_build
make -C locale all-mo

%install
%ruby_install

rm -rf %buildroot%_libexecdir/%name/extras/{jumpstart,spec}
rm -rf %buildroot%_bindir/{bundle,rails,rake,spring}
rm -rf %buildroot%_sysconfdir/%name
rm -rf %buildroot%_libexecdir/%name/config
rm -rf %buildroot%ruby_sitelibdir
rm -rf %buildroot%_libexecdir/%name/lib
rm -rf %buildroot%_localstatedir/%name
rm -rf %buildroot%_libexecdir/%name/tmp
cp -rf config %buildroot%_libexecdir/%name/config
cp -rf lib %buildroot%_libexecdir/%name/
mkdir -p %buildroot%_datadir \
         %buildroot%_sbindir \
         %buildroot/run/%name \
         %buildroot%_spooldir/%name/tmp \
         %buildroot%_cachedir/%name/_ \
         %buildroot%_cachedir/%name/.bundle \
         %buildroot%_cachedir/%name/openid-store \
         %buildroot%_cachedir/%name/apipie-cache \
         %buildroot%_sysconfdir/%name/plugins \
         %buildroot%_localstatedir/%name

# Create VERSION file
install -pm0644 VERSION %buildroot%_libexecdir/%name/VERSION
# bin folder is required for the rails run
cp -r bin %buildroot%_libexecdir/%name/bin

install -Dm0644 %SOURCE1 %buildroot%_sysconfdir/%name/database.yml
install -Dm0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -Dm0644 %SOURCE3 %buildroot%_logrotatedir/%name
install -Dm0644 %SOURCE4 %buildroot%_sysconfdir/cron.d/%name
install -Dm0644 %SOURCE5 %buildroot%_tmpfilesdir/%name.conf
install -Dm0644 %SOURCE6 %buildroot%_unitdir/%name.service
install -Dm0644 %SOURCE7 %buildroot%_sysconfdir/%name/settings.yml
install -Dm0644 %SOURCE8 %buildroot%_sysconfdir/nginx/sites-available.d/%name.conf
install -Dm0640 /dev/null %buildroot%_sysconfdir/%name/encryption_key.rb
install -Dm0640 /dev/null %buildroot%_sysconfdir/%name/local_secret_token.rb
install -Dm0644 %SOURCE11 %buildroot%_unitdir/%{name}-jobs.service
install -Dm0644 %SOURCE12 %buildroot%_sysconfdir/sysconfig/%{name}-jobs
install -Dm0644 config.ru %buildroot%_libexecdir/%name/config.ru
touch %buildroot%_cachedir/%name/Gemfile.lock

mv %buildroot%_libexecdir/%name/public %buildroot%_datadir/%name
ln -svr %buildroot%_datadir/%name %buildroot%_libexecdir/%name/public
ln -svr %buildroot%_datadir/%name %buildroot%_localstatedir/%name/public
ln -svr %buildroot%_sysconfdir/%name/plugins %buildroot%_libexecdir/%name/config/settings.plugins.d
ln -svr %buildroot%_sysconfdir/%name/settings.yml %buildroot%_libexecdir/%name/config/settings.yaml
ln -svr %buildroot%_sysconfdir/%name/database.yml %buildroot%_libexecdir/%name/config/database.yml
ln -svr %buildroot%_sysconfdir/%name/encryption_key.rb %buildroot%_libexecdir/%name/config/initializers/encryption_key.rb
ln -svr %buildroot%_sysconfdir/%name/local_secret_token.rb %buildroot%_libexecdir/%name/config/initializers/local_secret_token.rb
ln -svr %buildroot%_spooldir/%name/tmp %buildroot%_libexecdir/%name/tmp
ln -svr %buildroot%_cachedir/%name/_ %buildroot%_spooldir/%name/tmp/cache
ln -svr %buildroot%_cachedir/%name/openid-store %buildroot%_libexecdir/%name/db/openid-store
ln -svr %buildroot%_cachedir/%name/apipie-cache %buildroot%_libexecdir/%name/public/apipie-cache
ln -svr %buildroot%_cachedir/%name/.bundle %buildroot%_libexecdir/%name/.bundle
ln -svr %buildroot%_libexecdir/%name/script/foreman-rake %buildroot%_sbindir/foreman-rake
ln -svr %buildroot%_cachedir/%name/Gemfile.lock %buildroot%_libexecdir/%name/Gemfile.lock
install -d %buildroot%_logdir/%name

# symlinking publics
# NOTE restores required resources for production as symlynks to real ones
pushd %buildroot%_datadir/%name
find assets -type f | while read -r f
do
   if [[ "$f" =~ \.css(|.gz)$ ]]; then
      folder=stylesheets
   elif [[ "$f" =~ \.js(|.gz)$ ]]; then
      folder=javascripts
   elif [[ "$f" =~ \.(woff2?|ttf|eot)(|.gz)$ ]]; then
      folder=fonts
   else
      folder=images
   fi

   sub=$(echo "$f" |sed "s/assets\(.*\)\/[^\/]*-[a-f0-9]\{64,\}\.[^\/]*$/\1/")

   mkdir -p "$folder$sub"
   target="$folder$sub/$(echo "$f" |sed "s/.*\/\([^\/]*\)-[a-f0-9]\{64,\}/\1/")"

   if [[ ! -e "$target" ]]; then
      ln -rvs "$f" "$target"
   fi
done
popd

rm -rf %buildroot%_libexecdir/ruby

%check
%ruby_test

%pre
# Add the "foreman" user and group
getent group foreman >/dev/null || %_sbindir/groupadd -r foreman
getent passwd _foreman >/dev/null || \
   %_sbindir/useradd -r -g foreman -G foreman -M -d %_localstatedir/%name -s /bin/bash -c "Foreman" _foreman
getent group puppet >/dev/null || \
   %_sbindir/usermod -a -G puppet _foreman
usermod -a -G foreman,puppet _nginx # add _nginx into foreman and puppet groups
# rm -rf %_libexecdir/%name/public %_libexecdir/%name/db/openid-store
rm -rf %_spooldir/%name/*
exit 0

%post
# ssl key generation
puppetserver ca setup --certname $(hostname) --subject-alt-names $(hostname) >> /var/log/foreman/key_generation.log 2>&1

cp -fp /etc/puppet/ssl/ca/root_key.pem /etc/foreman/rootCA.pem 2>/dev/null
cp -fp /etc/puppet/ssl/certs/$(hostname).pem /etc/foreman/ssl_cert.pem 2>/dev/null
cp -fp /etc/puppet/ssl/private_keys/$(hostname).pem /etc/foreman/ssl_key.pem 2>/dev/null

ln -sf /etc/nginx/sites-available.d/foreman.conf /etc/nginx/sites-enabled.d/ 2>/dev/null

railsctl setup foreman 2>&1 >/dev/null || true

%post_service foreman
%post_service foreman-jobs

echo 'NOTE: To complete update/install procedure, make sure you have followed manuals at https://www.altlinux.org/Связка_Puppet_и_Foreman' 1>&2

%preun
railsctl cleanup %name
%preun_service foreman
%preun_service foreman-jobs

%files
%doc README* CONTRIBUTING.md LICENSE
%_sbindir/%name-rake
%_libexecdir/%name
%_datadir/%name
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/sysconfig/%name-jobs
%config(noreplace) %_sysconfdir/%name/plugins
%config(noreplace) %_sysconfdir/%name/settings.yml
%config(noreplace) %_sysconfdir/%name/database.yml
%config(noreplace) %_sysconfdir/nginx/sites-available.d/%name.conf
%attr(640,_foreman,foreman) %config(noreplace) %_sysconfdir/%name/encryption_key.rb
%attr(640,_foreman,foreman) %config(noreplace) %_sysconfdir/%name/local_secret_token.rb
%attr(770,_foreman,foreman) %_sysconfdir/cron.d/%name
%_tmpfilesdir/%name.conf
%_unitdir/*
%attr(770,_foreman,foreman) %_spooldir/%name/tmp
%attr(770,_foreman,foreman) %_cachedir/%name/Gemfile.lock
%dir %attr(770,_foreman,foreman) %_localstatedir/%name
%dir %attr(770,_foreman,foreman) %_localstatedir/%name/public
%dir %attr(770,_foreman,foreman) %_cachedir/%name/.bundle
%dir %attr(770,_foreman,foreman) %_cachedir/%name/openid-store
%dir %attr(770,_foreman,foreman) %_cachedir/%name/apipie-cache
%dir %attr(770,_foreman,foreman) %_cachedir/%name/_
%dir %attr(770,_foreman,foreman) /run/%name
%dir %attr(770,_foreman,foreman) %_logdir/%name
%dir %attr(770,_foreman,foreman) %_spooldir/%name
# %_man8dir/*.8*

%if_enabled    doc
%files         -n foreman-doc
%doc README.md
%ruby_sitedocdir/foreman
%endif

%if_enabled    devel
%files         -n foreman-devel
%endif


%changelog
* Fri Apr 24 2026 Pavel Skrylev <majioa@altlinux.org> 3.18.1-alt1
- ^ 3.13.0 -> 3.18.1

* Wed Feb 05 2025 Pavel Skrylev <majioa@altlinux.org> 3.13.0-alt2
- * moved public to a signle level up in %%datadir

* Mon Sep 30 2024 Pavel Skrylev <majioa@altlinux.org> 3.13.0-alt1
- ^ 3.5.1 -> 3.13.0
- ! fixed CVE-2024-8553

* Tue May 14 2024 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt9
- ! fixed dep to rack server for new rack 3x

* Thu Feb 29 2024 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt8.1
- ! fixed right to service and conf files

* Thu Dec 14 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt8
- ! fixed fast-gettext patch
- ! fixed russian translation

* Mon Dec 11 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt7
- - removed ssl_dhparam from foreman.nginx.conf
- ! fixed foreman service file

* Tue Aug 01 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt6
- ! fixed fast gettext calls for 2.3.0 version

* Wed Jul 26 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt5
- + updated russion translation po
- + patch allowing set default value as a parameter for setting model instance

* Mon Apr 10 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt4
- * allowed to direct proxy pass in nginx conf with forwarding the https params
- - crop out embedded node method/resource in favor of foreman-pupper gem's one

* Thu Apr 06 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt3
- ! fixed public webpack and assets
- ! fixed spec pre section and nginx conf
- ! fixed many configs to disable direct ssl (usign via nginx only)

* Thu Mar 16 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt2
- + dep to foreman_cert_revoke_host gem
- ! default sysconfig
- ! cleanup forced requires

* Fri Mar 10 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt1.3
- ! replace conflict with obsolete foreman_addons
- + forced some requires

* Mon Feb 27 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt1.2
- ! fixes dep to rack-cors

* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt1.1
- ! fixed dep to redis

* Mon Dec 19 2022 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt1
- ^ 3.0.0 -> 3.5.1
- ! fixed CVE-2022-3874

* Tue Dec 06 2022 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1.3
- !fix deps to rbvmomi gem

* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1.2
- !fix deps to novel gems

* Fri Apr 22 2022 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1.1
- !fix deps

* Wed Oct 20 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- ^ 2.5.0 -> 3.0.0

* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt0.2
- ! require deps
- ! sitedocdir folder

* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt0.1
- ^ 1.24.3.2 -> 2.5.0(pre)

* Mon Jun 28 2021 Pavel Vasenkov <pav@altlinux.org> 1.24.3.2-alt5
- fixes #39935,#39936,#39937,#39938,#39939
- + set pyton3 declaration and correct python3 executable in shebang
- ! add record to end of scss order

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
