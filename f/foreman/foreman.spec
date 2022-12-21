Name:          foreman
Version:       3.5.1
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
Source10:      public.tar
Source11:      foreman-jobs.service
Source12:      foreman-jobs.sysconfig
Patch6:        rails_6.patch
Patch5:        asciidoctor-doc.patch
Patch4:        puppet_enc_script.patch
Patch3:        invalid_premission.patch
Patch1:        gemfile.patch
Patch:         alt.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-macros-webserver-common
%if_with check
BuildRequires: elfutils
BuildRequires: glibc-core
BuildRequires: libX11-devel
BuildRequires: libnss-devel
BuildRequires: libnspr-devel
BuildRequires: fontconfig
BuildRequires: libfreetype-devel
BuildRequires: gem(rails) >= 6.1.3.2 gem(rails) < 7
BuildRequires: gem(rest-client) >= 2.0.0 gem(rest-client) < 3
BuildRequires: gem(audited) >= 4.9.0 gem(audited) < 6
BuildRequires: gem(will_paginate) >= 3.1.7 gem(will_paginate) < 4
BuildRequires: gem(ancestry) >= 3.0.7 gem(ancestry) < 5
BuildRequires: gem(scoped_search) >= 4.1.10 gem(scoped_search) < 5
BuildRequires: gem(ldap_fluff) >= 0.5.0 gem(ldap_fluff) < 1.0
BuildRequires: gem(apipie-rails) >= 0.5.17 gem(apipie-rails) < 1
BuildRequires: gem(apipie-dsl) >= 2.2.6
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rabl) >= 0.15.0 gem(rabl) < 1
BuildRequires: gem(oauth) >= 1.0 gem(oauth) < 2
BuildRequires: gem(deep_cloneable) >= 3 gem(deep_cloneable) < 4
BuildRequires: gem(validates_lengths_from_database) >= 0.5 gem(validates_lengths_from_database) < 1
BuildRequires: gem(friendly_id) >= 5.4.1 gem(friendly_id) < 6
BuildRequires: gem(secure_headers) >= 6.3 gem(secure_headers) < 7
BuildRequires: gem(safemode) >= 1.3.5 gem(safemode) < 2
BuildRequires: gem(fast_gettext) >= 1.4 gem(fast_gettext) < 2
BuildRequires: gem(gettext_i18n_rails) >= 1.8 gem(gettext_i18n_rails) < 2
BuildRequires: gem(rails-i18n) >= 7.0 gem(rails-i18n) < 8
BuildRequires: gem(i18n) >= 1.1 gem(i18n) < 2
BuildRequires: gem(logging) >= 1.8.0 gem(logging) < 3.0.0
BuildRequires: gem(fog-core) >= 2.1 gem(fog-core) < 3
BuildRequires: gem(net-scp) >= 0
BuildRequires: gem(net-ssh) >= 0
BuildRequires: gem(net-ldap) >= 0.16.0
BuildRequires: gem(net-ping) >= 0
BuildRequires: gem(activerecord-session_store) >= 2.0.0 gem(activerecord-session_store) < 3
BuildRequires: gem(sprockets) >= 4.0 gem(sprockets) < 5
BuildRequires: gem(sprockets-rails) >= 3.0 gem(sprockets-rails) < 4
BuildRequires: gem(responders) >= 3.0 gem(responders) < 4
BuildRequires: gem(roadie-rails) >= 3.0 gem(roadie-rails) < 4
BuildRequires: gem(deacon) >= 1.0 gem(deacon) < 2
BuildRequires: gem(webpack-rails) >= 0.9.8 gem(webpack-rails) < 0.10
BuildRequires: gem(mail) >= 2.7 gem(mail) < 3
BuildRequires: gem(sshkey) >= 2.0 gem(sshkey) < 3
BuildRequires: gem(dynflow) >= 1.6.5 gem(dynflow) < 2.0.0
BuildRequires: gem(daemons) >= 0
BuildRequires: gem(bcrypt) >= 3.1 gem(bcrypt) < 4
BuildRequires: gem(get_process_mem) >= 0
BuildRequires: gem(rack-cors) >= 1.0.2 gem(rack-cors) < 3
BuildRequires: gem(jwt) >= 2.2.1 gem(jwt) < 3
BuildRequires: gem(graphql) >= 1.8.0 gem(graphql) < 2
BuildRequires: gem(graphql-batch) >= 0
BuildRequires: gem(jquery-ui-rails) >= 6.0 gem(jquery-ui-rails) < 7
BuildRequires: gem(patternfly-sass) >= 3.59.4 gem(patternfly-sass) < 4
BuildRequires: gem(gettext_i18n_rails_js) >= 1.3.1 gem(gettext_i18n_rails_js) < 1.4
BuildRequires: gem(execjs) >= 1.4.0 gem(execjs) < 3.0
BuildRequires: gem(uglifier) >= 1.0.3
BuildRequires: gem(sass-rails) >= 6.0 gem(sass-rails) < 7
BuildRequires: gem(coffee-rails) >= 5.0.0 gem(coffee-rails) < 5.1
BuildRequires: gem(wirb) >= 1.0 gem(wirb) < 3.0
BuildRequires: gem(amazing_print) >= 1.1 gem(amazing_print) < 2
BuildRequires: gem(maruku) >= 0.7 gem(maruku) < 1
BuildRequires: gem(gettext) >= 3.2.1 gem(gettext) < 4.0.0
BuildRequires: gem(immigrant) >= 0.1 gem(immigrant) < 1
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-rails) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(pry-doc) >= 0
BuildRequires: gem(pry-stack_explorer) >= 0
BuildRequires: gem(pry-remote) >= 0
BuildRequires: gem(rainbow) >= 2.2.1
BuildRequires: gem(bullet) >= 6.1.0
BuildRequires: gem(parallel_tests) >= 0
BuildRequires: gem(spring) >= 1.0 gem(spring) < 3
BuildRequires: gem(benchmark-ips) >= 2.8.2
BuildRequires: gem(bootsnap) >= 0
BuildRequires: gem(graphiql-rails) >= 1.7 gem(graphiql-rails) < 2
BuildRequires: gem(sidekiq) >= 5.0 gem(sidekiq) < 7
BuildRequires: gem(gitlab-sidekiq-fetcher) >= 0
BuildRequires: gem(sd_notify) >= 0.1 gem(sd_notify) < 1
BuildRequires: gem(fog-aws) >= 3.6.2 gem(fog-aws) < 4
BuildRequires: gem(facter) >= 0
BuildRequires: gem(fog-google) >= 1.13.0 gem(fog-google) < 2
BuildRequires: gem(faraday) >= 1.0
BuildRequires: gem(logging-journald) >= 2.0 gem(logging-journald) < 3
BuildRequires: gem(rack-jsonp) >= 0
BuildRequires: gem(fog-libvirt) >= 0.9.0
BuildRequires: gem(ruby-libvirt) >= 0.5 gem(ruby-libvirt) < 1
BuildRequires: gem(activerecord-nulldb-adapter) >= 0
BuildRequires: gem(rack-openid) >= 1.3 gem(rack-openid) < 2
BuildRequires: gem(fog-openstack) >= 1.0.8 gem(fog-openstack) < 2.0.0
BuildRequires: gem(fog-ovirt) >= 2.0.1 gem(fog-ovirt) < 3
BuildRequires: gem(pg) >= 0.18 gem(pg) < 2.0
BuildRequires: gem(redis) >= 4.0 gem(redis) < 5
BuildRequires: gem(puma) >= 5.1 gem(puma) < 6
BuildRequires: gem(prometheus-client) >= 1.0 gem(prometheus-client) < 5
BuildRequires: gem(statsd-instrument) >= 2.0
BuildRequires: gem(mocha) >= 1.11 gem(mocha) < 2
BuildRequires: gem(single_test) >= 0.6 gem(single_test) < 1
BuildRequires: gem(minitest) >= 5.1 gem(minitest) < 6
BuildRequires: gem(minitest-reporters) >= 1.4 gem(minitest-reporters) < 2
BuildRequires: gem(minitest-retry) >= 0.0 gem(minitest-retry) < 1
BuildRequires: gem(minitest-spec-rails) >= 6.0 gem(minitest-spec-rails) < 7
BuildRequires: gem(capybara) >= 3.33 gem(capybara) < 4
BuildRequires: gem(show_me_the_cookies) >= 6.0 gem(show_me_the_cookies) < 7
BuildRequires: gem(database_cleaner) >= 1.3 gem(database_cleaner) < 3
BuildRequires: gem(launchy) >= 2.4 gem(launchy) < 3
BuildRequires: gem(facterdb) >= 1.7 gem(facterdb) < 2
BuildRequires: gem(factory_bot_rails) >= 5.0 gem(factory_bot_rails) < 7
BuildRequires: gem(selenium-webdriver) >= 0
BuildRequires: gem(shoulda-matchers) >= 4.0 gem(shoulda-matchers) < 5
BuildRequires: gem(shoulda-context) >= 1.2 gem(shoulda-context) < 3
BuildRequires: gem(as_deprecation_tracker) >= 1.4 gem(as_deprecation_tracker) < 2
BuildRequires: gem(rails-controller-testing) >= 1.0 gem(rails-controller-testing) < 2
BuildRequires: gem(rfauxfactory) >= 0.1.5 gem(rfauxfactory) < 1
BuildRequires: gem(robottelo_reporter) >= 0.1 gem(robottelo_reporter) < 1
BuildRequires: gem(theforeman-rubocop) >= 0.0.6 gem(theforeman-rubocop) < 0.1
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(fog-vsphere) >= 3.5.0 gem(fog-vsphere) < 4.0
BuildRequires: gem(rbvmomi) >= 2.0 gem(rbvmomi) < 4
%endif
Autoprov:      yes,nopython3,nopython,noshell
Autoreq:       yes,nopython3,nopython,noshell

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack-cors >= 1.1.1,rack-cors < 2
%ruby_use_gem_dependency sidekiq >= 6.1.1,sidekiq < 7
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency jwt >= 2.2.1,jwt < 3
%ruby_use_gem_dependency audited >= 5.0.1,audited < 6
%ruby_use_gem_dependency rails >= 6.1.3.2,rails < 7
%ruby_use_gem_dependency prometheus-client >= 2.0.0,prometheus-client < 5
%ruby_use_gem_dependency graphql >= 1.9.6,graphql < 2
%ruby_use_gem_dependency patternfly-sass >= 3.59.5,patternfly-sass < 4
%ruby_use_gem_dependency ancestry >= 4.0.0,ancestry < 5
%ruby_use_gem_dependency friendly_id >= 5.4.1,friendly_id < 6
%ruby_use_gem_dependency fog-google >= 1.13.0,fog-google < 2
%ruby_use_gem_dependency database_cleaner >= 2.0.1,database_cleaner < 3
%ruby_use_gem_dependency factory_bot_rails >= 6.2.0,factory_bot_rails < 7
%ruby_use_gem_dependency shoulda-matchers >= 4.5.1,shoulda-matchers < 5
%ruby_use_gem_dependency shoulda-context >= 2.0.0,shoulda-context < 3
%ruby_use_gem_dependency rbvmomi >= 3.0,rbvmomi < 4
Requires:      gem(rails) >= 6.1.3.2
Requires:      gem(rest-client) >= 2.0.0 gem(rest-client) < 3
Requires:      gem(audited) >= 4.9.0 gem(audited) < 6
Requires:      gem(will_paginate) >= 3.1.7 gem(will_paginate) < 4
Requires:      gem(ancestry) >= 3.0.7 gem(ancestry) < 5
Requires:      gem(scoped_search) >= 4.1.10 gem(scoped_search) < 5
Requires:      gem(ldap_fluff) >= 0.5.0 gem(ldap_fluff) < 1.0
Requires:      gem(apipie-rails) >= 0.5.17 gem(apipie-rails) < 1
Requires:      gem(apipie-dsl) >= 2.2.6
Requires:      gem(rdoc) < 7
Requires:      gem(rabl) >= 0.15.0 gem(rabl) < 1
Requires:      gem(oauth) >= 1.0 gem(oauth) < 2
Requires:      gem(deep_cloneable) >= 3 gem(deep_cloneable) < 4
Requires:      gem(validates_lengths_from_database) >= 0.5 gem(validates_lengths_from_database) < 1
Requires:      gem(friendly_id) >= 5.4.1 gem(friendly_id) < 6
Requires:      gem(secure_headers) >= 6.3 gem(secure_headers) < 7
Requires:      gem(safemode) >= 1.3.5 gem(safemode) < 2
Requires:      gem(fast_gettext) >= 1.4 gem(fast_gettext) < 2
Requires:      gem(gettext_i18n_rails) >= 1.8 gem(gettext_i18n_rails) < 2
Requires:      gem(rails-i18n) >= 7.0 gem(rails-i18n) < 8
Requires:      gem(i18n) >= 1.1 gem(i18n) < 2
Requires:      gem(logging) >= 1.8.0 gem(logging) < 3.0.0
Requires:      gem(fog-core) >= 2.1 gem(fog-core) < 3
Requires:      gem(net-scp) >= 0
Requires:      gem(net-ssh) >= 0
Requires:      gem(net-smtp) >= 0
Requires:      gem(net-pop) >= 0
Requires:      gem(net-imap) >= 0
Requires:      gem(net-ldap) >= 0.16.0
Requires:      gem(net-ping) >= 0
Requires:      gem(activerecord-session_store) >= 2.0.0 gem(activerecord-session_store) < 3
Requires:      gem(sprockets) >= 4.0 gem(sprockets) < 5
Requires:      gem(sprockets-rails) >= 3.0 gem(sprockets-rails) < 4
Requires:      gem(responders) >= 3.0 gem(responders) < 4
Requires:      gem(roadie-rails) >= 3.0 gem(roadie-rails) < 4
Requires:      gem(deacon) >= 1.0 gem(deacon) < 2
Requires:      gem(webpack-rails) >= 0.9.8 gem(webpack-rails) < 0.10
Requires:      gem(mail) >= 2.7 gem(mail) < 3
Requires:      gem(sshkey) >= 2.0 gem(sshkey) < 3
Requires:      gem(dynflow) >= 1.6.5 gem(dynflow) < 2.0.0
Requires:      gem(daemons) >= 0
Requires:      gem(bcrypt) >= 3.1 gem(bcrypt) < 4
Requires:      gem(get_process_mem) >= 0
Requires:      gem(rack-cors) >= 1.0.2 gem(rack-cors) < 3
Requires:      gem(jwt) >= 2.2.1 gem(jwt) < 3
Requires:      gem(graphql) >= 1.8.0 gem(graphql) < 2
Requires:      gem(graphql-batch) >= 0
Requires:      gem(jquery-ui-rails) >= 6.0 gem(jquery-ui-rails) < 7
Requires:      gem(patternfly-sass) >= 3.59.4 gem(patternfly-sass) < 4
Requires:      gem(gettext_i18n_rails_js) >= 1.3.1 gem(gettext_i18n_rails_js) < 1.4
Requires:      gem(execjs) >= 1.4.0 gem(execjs) < 3.0
Requires:      gem(uglifier) >= 1.0.3
Requires:      gem(sass-rails) >= 6.0 gem(sass-rails) < 7
Requires:      gem(coffee-rails) >= 5.0.0 gem(coffee-rails) < 5.1
Requires:      gem(wirb) >= 1.0 gem(wirb) < 3.0
Requires:      gem(amazing_print) >= 1.1 gem(amazing_print) < 2
Requires:      gem(maruku) >= 0.7 gem(maruku) < 1
Requires:      gem(gettext) >= 3.2.1 gem(gettext) < 4.0.0
Requires:      gem(immigrant) >= 0.1 gem(immigrant) < 1
Requires:      gem(byebug) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-rails) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(pry-doc) >= 0
Requires:      gem(pry-stack_explorer) >= 0
Requires:      gem(pry-remote) >= 0
Requires:      gem(rainbow) >= 2.2.1
Requires:      gem(bullet) >= 6.1.0
Requires:      gem(parallel_tests) >= 0
Requires:      gem(spring) >= 1.0 gem(spring) < 3
Requires:      gem(benchmark-ips) >= 2.8.2
Requires:      gem(bootsnap) >= 0
Requires:      gem(graphiql-rails) >= 1.7 gem(graphiql-rails) < 2
Requires:      gem(sidekiq) >= 5.0 gem(sidekiq) < 7
Requires:      gem(gitlab-sidekiq-fetcher) >= 0
Requires:      gem(sd_notify) >= 0.1 gem(sd_notify) < 1
Requires:      gem(fog-aws) >= 3.6.2 gem(fog-aws) < 4
Requires:      gem(facter) >= 0
Requires:      gem(fog-google) >= 1.13.0 gem(fog-google) < 2
Requires:      gem(faraday) >= 1.0
Requires:      gem(logging-journald) >= 2.0 gem(logging-journald) < 3
Requires:      gem(rack-jsonp) >= 0
Requires:      gem(fog-libvirt) >= 0.9.0
Requires:      gem(ruby-libvirt) >= 0.5 gem(ruby-libvirt) < 1
Requires:      gem(activerecord-nulldb-adapter) >= 0
Requires:      gem(rack-openid) >= 1.3 gem(rack-openid) < 2
Requires:      gem(fog-openstack) >= 1.0.8 gem(fog-openstack) < 2.0.0
Requires:      gem(fog-ovirt) >= 2.0.1 gem(fog-ovirt) < 3
Requires:      gem(pg) >= 0.18 gem(pg) < 2.0
Requires:      gem(redis) >= 4.0 gem(redis) < 5
Requires:      gem(puma) >= 5.1 gem(puma) < 6
Requires:      gem(prometheus-client) >= 1.0 gem(prometheus-client) < 5
Requires:      gem(statsd-instrument) >= 2.0
Requires:      gem(mocha) >= 1.11 gem(mocha) < 2
Requires:      gem(single_test) >= 0.6 gem(single_test) < 1
Requires:      gem(minitest) >= 5.1 gem(minitest) < 6
Requires:      gem(minitest-reporters) >= 1.4 gem(minitest-reporters) < 2
Requires:      gem(minitest-retry) >= 0.0 gem(minitest-retry) < 1
Requires:      gem(minitest-spec-rails) >= 6.0 gem(minitest-spec-rails) < 7
Requires:      gem(capybara) >= 3.33 gem(capybara) < 4
Requires:      gem(show_me_the_cookies) >= 6.0 gem(show_me_the_cookies) < 7
Requires:      gem(database_cleaner) >= 1.3 gem(database_cleaner) < 3
Requires:      gem(launchy) >= 2.4 gem(launchy) < 3
Requires:      gem(facterdb) >= 1.7 gem(facterdb) < 2
Requires:      gem(factory_bot_rails) >= 5.0 gem(factory_bot_rails) < 7
Requires:      gem(selenium-webdriver) >= 0
Requires:      gem(shoulda-matchers) >= 4.0 gem(shoulda-matchers) < 5
Requires:      gem(shoulda-context) >= 1.2 gem(shoulda-context) < 3
Requires:      gem(as_deprecation_tracker) >= 1.4 gem(as_deprecation_tracker) < 2
Requires:      gem(rails-controller-testing) >= 1.0 gem(rails-controller-testing) < 2
Requires:      gem(rfauxfactory) >= 0.1.5 gem(rfauxfactory) < 1
Requires:      gem(robottelo_reporter) >= 0.1 gem(robottelo_reporter) < 1
Requires:      gem(theforeman-rubocop) >= 0.0.6 gem(theforeman-rubocop) < 0.1
Requires:      gem(webmock) >= 0
Requires:      gem(fog-vsphere) >= 3.5.0 gem(fog-vsphere) < 4.0
Requires:      gem(rbvmomi) >= 2.0 gem(rbvmomi) < 4
Requires:      gem(foreman_templates) >= 9.3.0
Requires:      gem(foreman_remote_execution) >= 8.0.0
Requires:      gem(foreman_discovery) >= 21.0.3
Requires:      gem(foreman_ansible) >= 10.0.0
Requires:      gem(foreman-tasks) >= 7.0.0
Requires:      gem(foreman_default_hostgroup) >= 6.0.0
Requires:      gem(foreman_puppet) >= 4.0.3
Requires:      gem(foreman_setup) >= 8.0.1
Requires:      gem(foreman_maintain) >= 1.1.6
Requires:      gem(foreman_chef) >= 0.10.0
Requires:      gem(foreman_hooks) >= 0.3.17
Requires:      gem(foreman_api_client) >= 1.0.2
Requires:      gem(foreman_monitoring) >= 2.1.0
Requires:      gem(foreman_webhooks) >= 3.0.5
Requires:      gem(oauth) >= 0
Requires:      gem(rss) >= 0
Requires:      gem(gridster-rails) >= 0
Requires:      gem(spice-html5-rails) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rack-protection) >= 0
Requires:      gem(rubocop-packaging) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(concurrent-ruby-edge) >= 0
Requires:      gem(ruby_engine) >= 0
Requires:      wget
Requires:      vixie-cron
Requires:      postgresql-server
Requires:      dynflow
Requires:      node
Requires:      nginx
Provides:      ruby-foreman
Conflicts:     foreman-addons
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


%package       -n foreman-doc
Version:       3.5.1
Release:       alt1
Summary:       An application that automates the lifecycle of servers documentation files
Group:         Development/Documentation
BuildArch:     noarch

Requires:      foreman = 3.5.1

%description   -n foreman-doc
An application that automates the lifecycle of servers documentation files.

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


%prep
%setup
%setup -a 10
%autopatch -p1

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
mkdir -p %buildroot%_datadir/%name \
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
install -Dm0755 %SOURCE6 %buildroot%_unitdir/%name.service
install -Dm0644 %SOURCE7 %buildroot%_sysconfdir/%name/settings.yml
install -Dm0755 %SOURCE8 %buildroot%_sysconfdir/nginx/sites-available.d/%name.conf
install -Dm0640 /dev/null %buildroot%_sysconfdir/%name/encryption_key.rb
install -Dm0640 /dev/null %buildroot%_sysconfdir/%name/local_secret_token.rb
install -Dm0644 %SOURCE11 %buildroot%_unitdir/%{name}-jobs.service
install -Dm0644 %SOURCE12 %buildroot%_sysconfdir/sysconfig/%{name}-jobs
install -Dm0644 config.ru %buildroot%_libexecdir/%name/config.ru
touch %buildroot%_cachedir/%name/Gemfile.lock

mv %buildroot%_libexecdir/%name/public %buildroot%_datadir/%name
cp -r public/{javascripts,stylesheets,images} %buildroot%_datadir/%name/public/
ln -svr %buildroot%_datadir/%name/public %buildroot%_libexecdir/%name/public
ln -svr %buildroot%_datadir/%name/public %buildroot%_localstatedir/%name/public
#ln -svr %buildroot%webserver_datadir/%name %buildroot%_libexecdir/%name/public
ln -svr %buildroot%_sysconfdir/%name/plugins %buildroot%_libexecdir/%name/config/settings.plugins.d
ln -svr %buildroot%_sysconfdir/%name/settings.yml %buildroot%_libexecdir/%name/config/settings.yaml
ln -svr %buildroot%_sysconfdir/%name/database.yml %buildroot%_libexecdir/%name/config/database.yml
ln -svr %buildroot%_sysconfdir/%name/encryption_key.rb %buildroot%_libexecdir/%name/config/initializers/encryption_key.rb
ln -svr %buildroot%_sysconfdir/%name/local_secret_token.rb %buildroot%_libexecdir/%name/config/initializers/local_secret_token.rb
ln -svr %buildroot%_spooldir/%name/tmp %buildroot%_libexecdir/%name/tmp
#ln -svr %buildroot%_cachedir/%name/_ %buildroot%_spooldir/%name/tmp/cache
ln -svr %buildroot%_cachedir/%name/openid-store %buildroot%_libexecdir/%name/db/openid-store
ln -svr %buildroot%_cachedir/%name/apipie-cache %buildroot%_libexecdir/%name/public/apipie-cache
ln -svr %buildroot%_cachedir/%name/.bundle %buildroot%_libexecdir/%name/.bundle
ln -svr %buildroot%_libexecdir/%name/script/foreman-rake %buildroot%_sbindir/foreman-rake
ln -svr %buildroot%_cachedir/%name/Gemfile.lock %buildroot%_libexecdir/%name/Gemfile.lock
install -d %buildroot%_logdir/%name

%check
%ruby_test

%pre
# Add the "foreman" user and group
getent group foreman >/dev/null || %_sbindir/groupadd -r foreman
getent passwd _foreman >/dev/null || \
   %_sbindir/useradd -r -g foreman -G foreman -M -d %_localstatedir/%name -s /bin/bash -c "Foreman" _foreman
getent group puppet >/dev/null || \
   %_sbindir/usermod -a -G puppet _foreman
rm -rf %_libexecdir/%name/public %_libexecdir/%name/db/openid-store
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
%dir %attr(770,_foreman,foreman) %_cachedir/%name/.bundle
%dir %attr(770,_foreman,foreman) %_cachedir/%name/openid-store
%dir %attr(770,_foreman,foreman) %_cachedir/%name/apipie-cache
%dir %attr(770,_foreman,foreman) %_cachedir/%name/_
%dir %attr(770,_foreman,foreman) /run/%name
%dir %attr(770,_foreman,foreman) %_logdir/%name
%dir %attr(770,_foreman,foreman) %_spooldir/%name
# %_man8dir/*.8*

%files         -n foreman-doc
%doc README.md
%ruby_sitedocdir/foreman


%changelog
* Mon Dec 19 2022 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt1
- ^ 3.0.0 -> 3.5.1

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
