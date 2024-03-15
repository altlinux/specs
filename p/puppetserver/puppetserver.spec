%define _unpackaged_files_terminate_build 1

Name:       puppetserver
Version:    8.4.0
Release:    alt1
Summary:    Server automation framework and application
License:    Apache-2.0
Group:      Other
Url:        https://github.com/puppetlabs/puppetserver

BuildArch: noarch

Source: %name-%version.tar
Source1: repository.tar
Source2: puppetserver.init
Source3: jruby-gem-home.tar
Source4: ext.tar
Source5: %name.service
Source6: %name.conf

Patch1: puppetserver-alt-fix.patch
Patch2: puppetserver-alt-set-logback.xml.patch

BuildRequires(pre): rpm-build-java
BuildRequires(pre): procps
BuildRequires: leiningen
BuildRequires: java-11-openjdk-devel

Requires: java
Requires: clojure
Requires: facter
Requires: puppet
Requires: puppetserver-ca
Requires: gem-multi-json
Requires: gem-deep-merge
Requires: gem-text
Requires: gem-locale
Requires: gem-fast-gettext
Requires: gem-gettext
Requires: gem-semantic-puppet
Requires: gem-concurrent-ruby >= 1.1.6-alt1.1

%description
Puppet Server is the next-generation application for managing Puppet agents.
This platform implements Puppet's server-side components in a more distributed,
service-oriented architecture. We've built Puppet Server on top of the same
technologies that make PuppetDB successful, and which allow us to greatly
improve performance, scalability, advanced metrics collection, and fine-grained
control over the Ruby runtime.

%prep
%setup
%patch1 -p1
%patch2 -p1
tar xf %SOURCE1 -C ~
tar xf %SOURCE3
tar xf %SOURCE4
sed "s|gem-path: \\[.*\\]|gem-path: [$(echo $(ls /usr/lib/ruby/gems | \
   sed -e "s,^,/usr/lib/ruby/gems/,") | sed "s/ \\+/, /")]|" \
   -i resources/ext/config/conf.d/puppetserver.conf
subst 's|/var/log/puppetlabs|/var/log|' $(find -name '*.xml')
sed '/name.*environments/a \
        }, \
        { \
            match-request: { \
                path: "/puppet/v3/environment_classes" \
                type: path \
                method: get \
            } \
            allow: "*" \
            sort-order: 500 \
            name: "puppetlabs environment_classes"' \
      -i ezbake/config/conf.d/auth.conf

# Set correct version
subst 's/8\.4\.0/%version/' ext/bin/puppetserver ext/ezbake.manifest

%build
lein uberjar

%install
install -d -m 0755 %buildroot%_datadir/%name
install -d -m 0770 %buildroot%_localstatedir/%name
install -Dpm 0644 target/puppet-server-release.jar  %buildroot%_datadir/%name/puppet-server-release.jar
install -m 0755 ext/ezbake-functions.sh %buildroot%_datadir/%name
install -m 0644 ext/ezbake.manifest %buildroot%_datadir/%name
install -d -m 0755 %buildroot%_sysconfdir/%name
install -d -m 0755 %buildroot%_sysconfdir/%name/conf.d

install -d -m 0755 %buildroot%_sysconfdir/%name/services.d

install -m 0644 ezbake/system-config/services.d/bootstrap.cfg %buildroot%_sysconfdir/%name/bootstrap.cfg
install -m 0640 %SOURCE6 %buildroot%_sysconfdir/%name/conf.d/%name.conf
install -m 0644 resources/ext/config/request-logging.xml %buildroot%_sysconfdir/%name/request-logging.xml

install -m 0644 ezbake/config/logback.xml %buildroot%_sysconfdir/%name/logback.xml
install -m 0644 ezbake/config/conf.d/global.conf %buildroot%_sysconfdir/%name/conf.d/global.conf
install -m 0644 ezbake/config/conf.d/web-routes.conf %buildroot%_sysconfdir/%name/conf.d/web-routes.conf
install -m 0644 ezbake/config/conf.d/auth.conf %buildroot%_sysconfdir/%name/conf.d/auth.conf
install -m 0644 ezbake/config/conf.d/metrics.conf %buildroot%_sysconfdir/%name/conf.d/metrics.conf
install -m 0644 ezbake/config/conf.d/webserver.conf %buildroot%_sysconfdir/%name/conf.d/webserver.conf
install -m 0644 ezbake/config/services.d/ca.cfg %buildroot%_sysconfdir/%name/services.d/ca.cfg
install -m 0644 ezbake/system-config/services.d/bootstrap.cfg %buildroot%_sysconfdir/%name/services.d/bootstrap.cfg

install -d -m 0755 %buildroot%_datadir/%name/cli
install -d -m 0755 %buildroot%_datadir/%name/cli/apps
install -d -m 0755 %buildroot%_bindir
install -m 0755 ext/bin/puppetserver %buildroot%_bindir/%name
install -m 0755 ext/cli/apps/reload %buildroot%_datadir/%name/cli/apps/reload
install -m 0755 ext/cli/apps/stop %buildroot%_datadir/%name/cli/apps/stop
install -m 0755 ext/cli/apps/gem %buildroot%_datadir/%name/cli/apps/gem
install -m 0755 ext/cli/apps/irb %buildroot%_datadir/%name/cli/apps/irb
install -m 0755 ext/cli/apps/foreground %buildroot%_datadir/%name/cli/apps/foreground
install -m 0755 ext/cli/apps/ruby %buildroot%_datadir/%name/cli/apps/ruby
install -m 0755 ext/cli/apps/start %buildroot%_datadir/%name/cli/apps/start
install -m 0755 ext/cli/apps/ca %buildroot%_datadir/%name/cli/apps/ca
install -m 0755 ext/cli/cli-defaults.sh %buildroot%_datadir/%name/cli/

install -d -m 0755 %buildroot%_var/run/%name
install -d -m 0700 %buildroot%_var/log/%name
install -d -m 0700 %buildroot%_localstatedir/%name/jars

install -Dpm 0644 ext/default %buildroot%_sysconfdir/sysconfig/%name

install -d -m 0755 %buildroot%_sysconfdir/init.d
install -m 0755 %SOURCE2 %buildroot%_sysconfdir/init.d/%name

install -Dpm 0644 %SOURCE5 %buildroot%_unitdir/%name.service

install -Dpm 0644 %SOURCE4 %buildroot%_sysconfdir/sysconfig/%name
install -Dpm 0644 %SOURCE5 %buildroot%_unitdir/%name.service

mkdir -p %buildroot%_tmpfilesdir
install -m 0644 ext/puppetserver.tmpfiles.conf %buildroot%_tmpfilesdir/

%pre
getent group puppet > /dev/null || \
	groupadd -r puppet || :
	if getent passwd puppet > /dev/null; then
		usermod --gid puppet --home "/var/lib/puppetserver" \
		--comment "puppetserver daemon" puppet || :
	else
		useradd -r --gid puppet --home "/var/lib/puppetserver" --shell $(which nologin) \
		--comment "puppetserver daemon"  puppet || :
	fi

%preun
%preun_service %name

%post
install --directory %_sysconfdir/puppet/ssl
install --directory %_sysconfdir/puppet/code

chown -R puppet:puppet %_sysconfdir/puppet/ssl
chown -R puppet:puppet %_sysconfdir/puppet/code

find %_sysconfdir/puppet/ssl -type d -print0 | xargs -0 chmod 0770
find %_sysconfdir/puppet/code -type d -print0 | xargs -0 chmod 0770

chown puppet:puppet /var/log/puppetserver
chmod 0700 /var/log/puppetserver
chown puppet:puppet /var/lib/puppetserver
chmod 0770 /var/lib/puppetserver
chown puppet:puppet /etc/puppetserver
chmod 0750 /etc/puppetserver
chown puppet:puppet /var/run/puppetserver
chmod 0755 /var/run/puppetserver
chown puppet:puppet /var/lib/puppetserver/jars
chmod 0700 /var/lib/puppetserver/jars

if [ -d /var/log/puppetlabs/puppetserver ]; then
   find /var/log/puppetlabs/puppetserver/ -name \*.log | while read -r f; do sed "s|/var/log/puppetlabs|/var/log|" -i "$f"; done
   mv -f /var/log/puppetlabs/puppetserver/* /var/log/puppetserver
   rm -rf /var/log/puppetlabs/puppetserver
fi
%post_service %name

%files
%_datadir/%name
%config(noreplace) %_sysconfdir/%name
%config %_sysconfdir/sysconfig/%name
%_unitdir/%name.service
%_var/log/%name
%_var/lib/%name
%_var/run/%name
%_bindir/%name
%_tmpfilesdir/*
%_sysconfdir/init.d/%name

%changelog
* Fri Mar 15 2024 Pavel Skrylev <majioa@altlinux.org> 8.4.0-alt1
- ^ 6.20.0 -> 8.4.0 by cas@ (ALT #38464).
- Added requires java-17-openjdk by cas@ (ALT #41623).
- Set current version in executables by cas@ (ALT #47704).
- Used bundled jruby by cas@ (ALT #47705).
- * put proper config

* Mon Mar 04 2024 Pavel Skrylev <majioa@altlinux.org> 6.20.0-alt4
- ! fixed: added proper gem_path to config (closes #49603)

* Mon Mar 04 2024 Andrey Cherepanov <cas@altlinux.org> 6.20.0-alt3
- puppetserver.service: disable autorestart and standard output type syslog
  (ALT #49602).
- Use adapted /etc/sysconfig/puppetserver.

* Wed Feb 21 2024 Andrey Cherepanov <cas@altlinux.org> 6.20.0-alt2
- Add service file.

* Wed Sep 21 2022 Pavel Skrylev <majioa@altlinux.org> 6.20.0-alt1
- ^ 6.13.0 -> 6.20.0
- - remove conflict to gem-oj
- ! fix alt patch to conform ruby new style

* Tue Feb 09 2021 Pavel Skrylev <majioa@altlinux.org> 6.13.0-alt3.1
- ! keeping sysconfig data from an old releases

* Wed Dec 23 2020 Pavel Skrylev <majioa@altlinux.org> 6.13.0-alt3
- + environment_classes to ''auth.conf''
- + replacings for the log folder, removing puppetlabs from it

* Tue Nov 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.13.0-alt2
- Updated dependencies for p9 compatibility.

* Fri Nov 06 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.13.0-alt1
- Updated to upstream version 6.13.0 (Fixes: CVE-2020-7943).

* Fri May 22 2020 Pavel Skrylev <majioa@altlinux.org> 6.5.0-alt3
- ! max memory consumption for JVM by increasing top border an config
  (closes #38519)

* Wed May 13 2020 Pavel Skrylev <majioa@altlinux.org> 6.5.0-alt2.1
- + explicit require dependencies to proper gem packages

* Tue May 12 2020 Pavel Skrylev <majioa@altlinux.org> 6.5.0-alt2
- ! gem paths config

* Mon Aug 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 6.5.0-alt1
- Version updated to 6.5.0

* Sat Jul 06 2019 Igor Vlasenko <viy@altlinux.ru> 6.3.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Tue May 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 6.3.0-alt2
- puppetserver config path fixed

* Wed May 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 6.3.0-alt1
- Version updated to 6.3.0

* Fri Mar 01 2019 Andrey Bychkov <mrdrew@altlinux.org> 6.2.1-alt1
- Version updated to 6.2.1

* Tue Dec 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 6.1.0-alt1
- version updated to 6.1.0

* Fri Dec 07 2018 Andrey Bychkov <mrdrew@altlinux.org> 6.0.2-alt3
- requires fixed

* Fri Nov 30 2018 Andrey Bychkov <mrdrew@altlinux.org> 6.0.2-alt2
- puppetserver ca added

* Mon Nov 19 2018 Andrey Bychkov <mrdrew@altlinux.org> 6.0.2-alt1
- version updated to 6.0.2

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 6.0.0-alt1.qa1
- NMU: applied repocop patch

* Fri Sep 21 2018 Andrey Bychkov <mrdrew@altlinux.org> 6.0.0-alt1
- updated version to 6.0.0 from src

* Wed Sep 12 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.3.5-alt2
- chown puppet/ssl for foreground

* Thu Aug 09 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.3.5-alt1
- Update version to 5.3.5

* Thu Aug 02 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.3.4-alt1
- Initial build in Sisyphus

