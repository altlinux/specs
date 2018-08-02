%define _unpackaged_files_terminate_build 1

Name:       puppetserver
Version:    5.3.4
Release:    alt1%ubt

Summary:    Server automation framework and application
License:    Apache-2.0
Group:      Other

Url:        https://github.com/puppetlabs/puppetserver

BuildArch:  noarch

Source: %name-%version.tar
Patch0: alt_adapt.patch

BuildPreReq: /proc
BuildPreReq: rpm-build-java
BuildPreReq: rpm-build-ruby
BuildPreReq: rpm-build-ubt

Requires: clojure
Requires: puppet


%description
Puppet Server is the next-generation application for managing Puppet agents.
This platform implements Puppet's server-side components in a more distributed,
service-oriented architecture. We've built Puppet Server on top of the same
technologies that make PuppetDB successful, and which allow us to greatly
improve performance, scalability, advanced metrics collection, and fine-grained
control over the Ruby runtime.

%prep
%setup
%patch0 -p1

%install
## Docs
install -d -m 0755 mkdir %buildroot%_datadir/%name
cp -fR LICENSE.md README.md docs %buildroot%_datadir/%name

## Requires
mkdir -p %buildroot%_sysconfdir/sysconfig
touch %buildroot%_sysconfdir/sysconfig/%name
install -D default %buildroot%_sysconfdir/default/%name

## Install dirs
install -d -m 0755 %buildroot%_sysconfdir/%name/conf.d
install -d -m 0755 %buildroot%_sysconfdir/%name/services.d
install -d -m 0755 %buildroot%_javadir/%name/cli
install -d -m 0755 %buildroot%_javadir/%name/cli/apps
install -d -m 0755 %buildroot%_logdir/%name
install -d -m 0755 %buildroot%_localstatedir/%name

## Install files
# bin
install -Dm 0755 %name %buildroot%_bindir/%name
# jar
install -D %name.jar %buildroot%_javadir/%name/%name.jar
install -D jruby-9k.jar %buildroot%_javadir/%name/jruby-9k.jar
install -D jruby-1_7.jar %buildroot%_javadir/%name/jruby-1_7.jar
# service & init
install -D %name.service %buildroot%_unitdir/%name.service
install -D %name.init %buildroot%_initdir/%name
mkdir -p %buildroot%_sysconfdir/tmpfiles.d
cat > %buildroot%_sysconfdir/tmpfiles.d/%name.conf <<EOF
d /var/run/puppetserver 0775 puppet puppet -
EOF
mkdir -p %buildroot%_runtimedir/%name
# configs
install ca.cfg %buildroot%_sysconfdir/%name/services.d/ca.cfg
install puppetserver.conf %buildroot%_sysconfdir/%name/conf.d/puppetserver.conf
install global.conf %buildroot%_sysconfdir/%name/conf.d/global.conf
install web-routes.conf %buildroot%_sysconfdir/%name/conf.d/web-routes.conf
install auth.conf %buildroot%_sysconfdir/%name/conf.d/auth.conf
install metrics.conf %buildroot%_sysconfdir/%name/conf.d/metrics.conf
install webserver.conf %buildroot%_sysconfdir/%name/conf.d/webserver.conf
install bootstrap.cfg %buildroot%_sysconfdir/%name/bootstrap.cfg
install request-logging.xml %buildroot%_sysconfdir/%name/request-logging.xml
install logback.xml %buildroot%_sysconfdir/%name/logback.xml
# cli
install -m 0755 cli/reload %buildroot%_javadir/%name/cli/apps/reload
install -m 0755 cli/stop %buildroot%_javadir/%name/cli/apps/stop
install -m 0755 cli/gem %buildroot%_javadir/%name/cli/apps/gem
install -m 0755 cli/irb %buildroot%_javadir/%name/cli/apps/irb
install -m 0755 cli/foreground %buildroot%_javadir/%name/cli/apps/foreground
install -m 0755 cli/ruby %buildroot%_javadir/%name/cli/apps/ruby
install -m 0755 cli/start %buildroot%_javadir/%name/cli/apps/start
install -m 0755 cli-defaults.sh %buildroot%_javadir/%name/cli/cli-defaults.sh
# ezbake
install -m 0755 ezbake-functions.sh %buildroot/%_javadir/%name/ezbake-functions.sh
install -m 0644 ezbake.manifest %buildroot/%_javadir/%name/ezbake.manifest

%pre
getent group puppet > /dev/null || groupadd -r puppet || :
useradd -r --gid puppet --home %_localstatedir/%name --shell $(which nologin) \
    --comment "puppetserver daemon"  puppet || :

%post
install --directory %_sysconfdir/puppet/ssl
install --directory %_sysconfdir/puppet/code

chown -R puppet:puppet %_sysconfdir/puppet/ssl
chown -R puppet:puppet %_sysconfdir/puppet/code

find %_sysconfdir/puppet/ssl -type d -print0 | xargs -0 chmod 770
find %_sysconfdir/puppet/code -type d -print0 | xargs -0 chmod 770

install --owner=puppet --group=puppet -d /usr/share/puppetserver/jruby-gems
/usr/bin/puppet config set --section master vardir  /var/lib/puppetserver
/usr/bin/puppet config set --section master logdir  /var/log/puppetserver
/usr/bin/puppet config set --section master rundir  /var/run/puppetserver
/usr/bin/puppet config set --section master pidfile /var/run/puppetserver/puppetserver.pid
/usr/bin/puppet config set --section master codedir /etc/puppet/code

chown puppet:puppet /var/log/puppetserver
chmod 700 /var/log/puppetserver
chown puppet:puppet /var/lib/puppetserver
chmod 770 /var/lib/puppetserver
chown puppet:puppet /etc/puppetserver
chmod 750 /etc/puppetserver
chown puppet:puppet /var/run/puppetserver
chmod 0755 /var/run/puppetserver

%files
%_javadir/%name/*
%_unitdir/%name.service
%dir %_sysconfdir/%name
%dir %attr(0770,puppet,puppet) %_localstatedir/%name
%_initdir/%name
%_sysconfdir/tmpfiles.d/%name.conf
%_runtimedir/%name
%dir %_javadir/%name
%dir %attr(0770,puppet,puppet) %_logdir/%name
%dir %_sysconfdir/%name/conf.d
%dir %_sysconfdir/%name/services.d
%dir %_datadir/%name
%dir %_javadir/%name/cli
%dir %_javadir/%name/cli/apps
%_javadir/%name/cli/apps/*
%_bindir/*
%dir %_datadir/%name
%_datadir/%name

%config(noreplace) %attr(0770,puppet,puppet) %_sysconfdir/sysconfig/%name
%config(noreplace) %attr(0770,puppet,puppet) %_sysconfdir/default/%name
%config(noreplace) %attr(0770,puppet,puppet) %_sysconfdir/%name/bootstrap.cfg
%config(noreplace) %attr(0770,puppet,puppet) %_sysconfdir/%name/request-logging.xml
%config(noreplace) %attr(0770,puppet,puppet) %_sysconfdir/%name/logback.xml
%config(noreplace) %attr(0770,puppet,puppet) %_sysconfdir/%name/conf.d/puppetserver.conf
%config(noreplace) %attr(0770,puppet,puppet) %_sysconfdir/%name/conf.d/global.conf
%config(noreplace) %attr(0770,puppet,puppet) %_sysconfdir/%name/conf.d/web-routes.conf
%config(noreplace) %attr(0770,puppet,puppet) %_sysconfdir/%name/conf.d/auth.conf
%config(noreplace) %attr(0770,puppet,puppet) %_sysconfdir/%name/conf.d/metrics.conf
%config(noreplace) %attr(0770,puppet,puppet) %_sysconfdir/%name/conf.d/webserver.conf
%config(noreplace) %attr(0770,puppet,puppet) %_sysconfdir/%name/services.d/ca.cfg


%changelog  
* Thu Aug 02 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.3.4-alt1%ubt
- Initial build in Sisyphus

