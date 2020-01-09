%define _unpackaged_files_terminate_build 1

%define _pseudouser_user     _geekotest
%define _pseudouser_group    _geekotest
%define _pseudouser_home     %_localstatedir/_geekotest

%define _psworker_user     _openqa-worker
%define _psworker_group    _openqa-worker
%define _psworker_home     %_localstatedir/_openqa-worker

%add_perl_lib_path %_datadir/openqa/lib
%if %{undefined tmpfiles_create}
%define tmpfiles_create() \
/sbin/systemd-tmpfiles --create %{?*} >/dev/null 2>&1 || :
%nil
%endif

%define t_requires perl(DBD/Pg.pm) perl(Mojolicious/Plugin/RenderFile.pm) perl(DBIx/Class/Schema/Config.pm) perl(DBIx/Class/OptimisticLocking.pm) perl(Config/IniFiles.pm) perl(SQL/Translator.pm) perl(Date/Format.pm) perl(File/Copy/Recursive.pm) perl(DateTime/Format/Pg.pm) perl(Net/OpenID/Consumer.pm) perl(aliased.pm) perl(Config/Tiny.pm) perl(DBIx/Class/DynamicDefault.pm) perl(DBIx/Class/Storage/Statistics.pm) perl(IO/Socket/SSL.pm) perl(Data/Dump.pm) perl(Text/Markdown.pm) perl(Net/DBus.pm) perl(IPC/Run.pm) perl(Archive/Extract.pm) perl(CSS/Minifier/XS.pm) perl(JavaScript/Minifier/XS.pm) perl(Time/ParseDate.pm) perl(Time/Piece.pm) perl(Time/Seconds.pm) perl(Sort/Versions.pm) perl(BSD/Resource.pm) perl(Cpanel/JSON/XS.pm) perl(YAML/XS.pm) perl(IPC/Run.pm) perl(CommonMark.pm)

Name: openqa
Version: 4.5.1528009330.e68ebe2b
Release: alt8
Summary: OS-level automated testing framework
License: GPLv2+
Group: Development/Tools
Url: https://github.com/os-autoinst/openQA
Source0: %name-%version.tar
# pre-generated cached assets, build with update-cache.sh. We could
# install without these and let openQA generate them at run time, but
# we don't for two reasons: we don't want to let a webapp rewrite
# itself if avoidable (it's a security risk), and the tests don't work
# without the asset cache present. This should be re-generated any
# time Source0 changes.
Source1: cache.tar
#Please check $ git grep geekotest
Patch0: addpseudouser.patch
Patch1: rmservices.patch
BuildArch: noarch

BuildRequires: %t_requires
BuildRequires: perl(DBIx/Class.pm)
BuildRequires: perl-Package-Generator
BuildRequires: perl(Mojo/SQLite.pm)
BuildRequires: spectool
BuildRequires: postgresql10-server
BuildRequires: systemd
BuildRequires: ruby-sass
BuildRequires: ruby-rb-inotify
BuildRequires: ruby-sass-listen
BuildRequires: perl(Mojolicious.pm)
BuildRequires: perl(Mojolicious/Plugin/AssetPack.pm)
BuildRequires: perl(Mojo/IOLoop/ReadWriteProcess.pm)
BuildRequires: perl(Minion.pm)
BuildRequires: perl(Minion/Backend/SQLite.pm)
BuildRequires: git-core
BuildRequires: os-autoinst
BuildRequires: osc
BuildRequires: perl(Test/Compile.pm)
BuildRequires: perl(Test/Fatal.pm)
BuildRequires: perl(Test/MockModule.pm)
BuildRequires: perl(Test/MockObject.pm)
BuildRequires: perl(Test/Mojo.pm)
BuildRequires: perl(Test/Output.pm)
BuildRequires: perl(Test/Pod.pm)
BuildRequires: perl(Test/Warnings.pm)
BuildRequires: perl(Perl/Critic.pm)
BuildRequires: perl(DBD/SQLite.pm)
BuildRequires: perl(DBIx/Class/DeploymentHandler.pm)
BuildRequires: perl(SQL/SplitStatement.pm)
BuildRequires: perl(IPC/Cmd.pm)
BuildRequires: perl(Module/Load/Conditional.pm)
BuildRequires: perl(CPAN/Meta/YAML.pm)
BuildRequires: perl(JSON/Validator.pm)
BuildRequires: perl(Test/Exception.pm)
BuildRequires: perl(Text/Diff.pm)
BuildRequires: perl(Test/Strict.pm)
BuildRequires: perl(Mojo/RabbitMQ/Client.pm)
BuildRequires: python3-devel
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-requests
BuildRequires: python3-module-future

Requires: openqa-common = %EVR
Requires: openqa-client = %EVR
Requires: perl(URI.pm)
Requires: perl(LWP/Protocol/https.pm)
Requires: optipng
Requires: dbus
Requires: perl(YAML/XS.pm)

%description
openQA is a testing framework that allows you to test GUI applications on one
hand and bootloader and kernel on the other. In both cases, it is difficult to
script tests and verify the output. Output can be a popup window or it can be
an error in early boot even before init is executed.

openQA is an automated test tool that makes it possible to test the whole
installation process of an operating system. It uses virtual machines to
reproduce the process, check the output (both serial console and screen) in
every step and send the necessary keystrokes and commands to proceed to the
next. openQA can check whether the system can be installed, whether it works
properly in 'live' mode, whether applications work or whether the system
responds as expected to different installation options and commands.

Even more importantly, openQA can run several combinations of tests for every
revision of the operating system, reporting the errors detected for each
combination of hardware configuration, installation options and variant of the
operating system.

%package common
Summary: Common components for openQA server and workers
Group: Development/Tools

Requires: perl(DBD/Pg.pm) perl(Mojolicious/Plugin/RenderFile.pm) perl(DBIx/Class/Schema/Config.pm) perl(DBIx/Class/OptimisticLocking.pm) perl(SQL/Translator.pm) perl(File/Copy/Recursive.pm) perl(aliased.pm) perl(Config/Tiny.pm) perl(DBIx/Class/DynamicDefault.pm) perl(IO/Socket/SSL.pm) perl(Data/Dump.pm) perl(CSS/Minifier/XS.pm) perl(JavaScript/Minifier/XS.pm) perl(Cpanel/JSON/XS.pm) perl(Mojo/SQLite.pm)
Requires: perl(Mojolicious/Plugin/AssetPack.pm) >= 2.01

%description common
This package contains shared resources for the openQA server and
openQA workers.

%package worker
Summary: The openQA worker
Group: Development/Tools
Requires: openqa-common = %EVR
Requires: os-autoinst < 5
Requires: os-autoinst-openvswitch
Requires: openqa-client = %EVR
Requires: perl(DBD/SQLite.pm)
Requires: perl(SQL/SplitStatement.pm)
Requires: perl(Mojo/SQLite.pm)
Requires(post): coreutils
Requires(post): os-autoinst >= 4.4
PreReq: qemu-common

%description worker
The openQA worker manages the os-autoinst test engine. A system with
openqa-worker installed can run an arbitrary number of openQA workers
(as many as its hardware can support), each of which will run a single
openQA test job at a time, as long as appropriate jobs for the worker
are available from the server it is configured to work for.

%package httpd
Summary: openQA httpd (Apache) integration
Group: Development/Tools
Requires: apache2
Obsoletes: openqa < 4.3-7

%description httpd
This package contains httpd (Apache2) configuration for the openQA
automated testing framework. openQA runs as a self-contained http
server which is expected to be reverse-proxied by a public-facing http
server (rather than being accessed directly). The config snippets in
this package help you configure openQA to be reverse proxied by httpd.

%package client
Summary: Client tools for remote openQA management
Group: Development/Tools
Requires: perl(Config/IniFiles.pm)
Requires: perl(Mojolicious.pm)

%description client
This package contains the openQA client script, along with several
other useful tools and support files. The client script is a convenient
helper for interacting with the openQA REST API.

%package local-db
Summary: Helper package to ease setup of postgresql DB
Group: Development/Tools
Requires: postgresql10-server

%description local-db
You only need this package if you have a local postgresql server
next to the webui.

%package doc
Summary: The openQA documentation
Group: Development/Tools
%description doc
Documentation material covering installation, configuration, basic test
writing, etc., covering both openQA and the os-autoinst test engine.

%prep
%setup -n %name-%version
tar xf %SOURCE1 -C assets
%patch0 -p1
%patch1 -p1
sed -i -e 's|../webfonts/|https://use.fontawesome.com/releases/v5.0.10/webfonts/|g' assets/cache/use.fontawesome.com/releases/v5.0.10/css/all.css
sed -i -e 's|/usr/lib/systemd/|/lib/systemd/|'  systemd/systemd-openqa-generator
sed -i -e 's|/usr/lib/systemd/|/lib/systemd/|' -e 's|/usr/lib/tmpfiles.d|/lib/tmpfiles.d|'  Makefile
sed -i -e 's|https://|cache/|' -e 's|http://|cache/|' assets/assetpack.def
sed -i -e 's,apache2\.service,httpd2\.service,g' systemd/*.service
sed -i -e 's,"$(DESTDIR)"/etc/apache2/vhosts.d,"$(DESTDIR)"%_sysconfdir/httpd2/conf/sites-available,g' Makefile
sed -i -e 's,/etc/apache2/vhosts.d,%_sysconfdir/httpd2/conf/sites-available,g' etc/apache2/vhosts.d/*
sed -i -e 's,/etc/apache2/ssl.crt,%_sysconfdir/pki/tls/certs,g' etc/apache2/vhosts.d/*
sed -i -e 's,/etc/apache2/ssl.key,%_sysconfdir/pki/tls/private,g' etc/apache2/vhosts.d/*
sed -i -e 's,/usr/bin/systemd-tmpfiles --create /etc/tmpfiles.d/openqa.conf,/sbin/systemd-tmpfiles --create /lib/tmpfiles.d/openqa.conf,g' systemd/systemd-openqa-generator
#These services are not used.
rm -rf systemd/openqa-vde_switch.service
rm -rf systemd/openqa-slirpvde.service

%build
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_datadir/openqa/etc/openqa
ln -s %_sysconfdir/openqa/openqa.ini %buildroot%_datadir/openqa/etc/openqa/openqa.ini
ln -s %_sysconfdir/openqa/database.ini %buildroot%_datadir/openqa/etc/openqa/database.ini
mkdir -p %buildroot%_bindir
ln -s %_datadir/openqa/script/client %buildroot%_bindir/openqa-client
ln -s %_datadir/openqa/script/clone_job.pl %buildroot%_bindir/openqa-clone-job
ln -s %_datadir/openqa/script/dump_templates %buildroot%_bindir/openqa-dump-templates
ln -s %_datadir/openqa/script/load_templates %buildroot%_bindir/openqa-load-templates

#These files are not needed
rm -f %buildroot%_datadir/openqa/script/openqa-bootstrap
rm -f %buildroot%_datadir/openqa/script/openqa-bootstrap-container

cd %buildroot
grep -rl %_bindir/env . | while read file; do
  sed -e 's,%_bindir/env perl,%_bindir/perl,' -i $file
done

mkdir -p %buildroot%_datadir/openqa/packed
mkdir -p %buildroot%_localstatedir/openqa/cache
mkdir -p %buildroot%_localstatedir/openqa/pool
mkdir -p %buildroot%_localstatedir/openqa/webui/cache

# We don't do AppArmor
rm -rf %buildroot%_sysconfdir/apparmor.d
mkdir -p %buildroot%_datadir/openqa/lib/OpenQA/WebAPI/Plugin/

%check
rm -f t/24-worker-overall.t
rm -f t/40-script_openqa-clone-custom-git-refspec.t
rm -f t/42-screenshots.t
# we don't really need the tidy test
rm -f t/00-tidy.t

rm -rf %buildroot/DB
export LC_ALL=en_US.UTF-8
./t/test_postgresql %buildroot/DB
export TEST_PG="DBI:Pg:dbname=openqa_test;host=%buildroot/DB"
OBS_RUN=1 prove -l -r
pg_ctl -D %buildroot/DB stop
rm -rf %buildroot/DB

%pre
/usr/sbin/groupadd -r -f %_pseudouser_group ||:
/usr/sbin/useradd -g %_pseudouser_group \
        -d %_pseudouser_home -s /dev/null -r %_pseudouser_user >/dev/null 2>&1 ||:


%pre worker
/usr/sbin/groupadd -r -f %_psworker_group ||:
/usr/sbin/useradd -g %_psworker_group -G vmusers \
        -d %_psworker_home -s /dev/null -r %_psworker_user >/dev/null 2>&1 ||:

%post worker
%tmpfiles_create %_tmpfilesdir/openqa.conf

%post httpd
if [ $1 -eq 1 ]; then
        echo "### copy and edit /etc/httpd2/conf/sites-available/openqa.conf.template!"
fi

if [ $1 -eq 0 ]; then
   rm -rf %_datadir/openqa/public/packed
fi

%files
%doc README.asciidoc
%dir %_sysconfdir/openqa
%config(noreplace) %_sysconfdir/openqa/openqa.ini
%config(noreplace) %attr(-,root,_geekotest) %_sysconfdir/openqa/database.ini
%dir %_datadir/openqa
%dir %_datadir/openqa/etc
%dir %_datadir/openqa/etc/openqa
%_datadir/openqa/etc/openqa/openqa.ini
%_datadir/openqa/etc/openqa/database.ini
%config %_sysconfdir/logrotate.d/*
%dir
%_unitdir/openqa-webui.service
%_unitdir/openqa-gru.service
%_unitdir/openqa-scheduler.service
%_unitdir/openqa-websockets.service
%_unitdir/openqa-livehandler.service
%_unitdir/openqa-worker-cacheservice-minion.service
%_unitdir/openqa-worker-cacheservice.service
%_unitdir/openqa-enqueue-audit-event-cleanup.service
%_unitdir/openqa-enqueue-audit-event-cleanup.timer
%_unitdir/openqa-enqueue-asset-and-result-cleanup.service
%_unitdir/openqa-enqueue-asset-and-result-cleanup.timer
# web libs
%_datadir/openqa/templates
%_datadir/openqa/public
%_datadir/openqa/dbicdh
%_datadir/openqa/assets
%dir %_datadir/openqa/script
%_datadir/openqa/script/check_dependencies
%_datadir/openqa/script/create_admin
%_datadir/openqa/script/fetchneedles
%_datadir/openqa/script/initdb
%_datadir/openqa/script/openqa
%_datadir/openqa/script/openqa-scheduler
%_datadir/openqa/script/openqa-websockets
%_datadir/openqa/script/upgradedb
%_datadir/openqa/script/modify_needle
%_datadir/openqa/script/openqa-livehandler
%_datadir/openqa/script/openqa-workercache
%_datadir/openqa/script/openqa-clone-custom-git-refspec
%_datadir/openqa/script/openqa-label-all
%dir %_localstatedir/openqa/share
%defattr(-,_geekotest,root)
%dir %_localstatedir/openqa/db
%dir %_localstatedir/openqa/images
%dir %_localstatedir/openqa/share/factory
%dir %_localstatedir/openqa/share/tests
%_localstatedir/openqa/testresults
%ghost %attr(0640,_geekotest,root) %_localstatedir/openqa/db/db.sqlite

%files common
%doc COPYING
%dir %_datadir/openqa
%ghost %dir %_datadir/openqa/packed
%_datadir/openqa/lib
%dir %_datadir/openqa/script
%exclude %_datadir/openqa/lib/OpenQA/Client.pm
%dir %_localstatedir/openqa
%_localstatedir/openqa/factory
%_localstatedir/openqa/tests
%_localstatedir/openqa/script

%files worker
%config(noreplace) %_sysconfdir/openqa/workers.ini
%config(noreplace) %attr(0600,_openqa-worker,root) %_sysconfdir/openqa/client.conf
%dir %_unitdir
/lib/systemd/system-generators/systemd-openqa-generator
%_unitdir/openqa-worker.target
%_unitdir/openqa-worker@.service
%_unitdir/openqa-worker-no-cleanup@.service
%_tmpfilesdir/openqa.conf
%_datadir/openqa/script/worker
%dir %_localstatedir/openqa/pool
%defattr(-,_geekotest,root)
%dir %_localstatedir/openqa/cache
%dir %_localstatedir/openqa/webui/cache

%files httpd
%doc COPYING
# apache vhost
%config %_sysconfdir/httpd2/conf/sites-available/openqa.conf.template
%config %_sysconfdir/httpd2/conf/sites-available/openqa-common.inc
%config %_sysconfdir/httpd2/conf/sites-available/openqa-ssl.conf.template

%files client
%_datadir/openqa/script/client
%_datadir/openqa/script/clone_job.pl
%_datadir/openqa/script/dump_templates
%_datadir/openqa/script/load_templates
%_datadir/openqa/lib/OpenQA/Client.pm
%_datadir/openqa/script/configure-web-proxy
%_datadir/openqa/script/openqa-clone-job
%_bindir/openqa-client
%_bindir/openqa-clone-job
%_bindir/openqa-dump-templates
%_bindir/openqa-load-templates

%files doc
%doc docs/*

%files local-db
%_unitdir/openqa-setup-db.service

%changelog
* Mon Dec 30 2019 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt8
- update to current version

* Tue Oct 29 2019 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt7
- update to current version

* Tue Oct 01 2019 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt6
- update to current version

* Wed Jul 31 2019 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt5
- update to current version

* Fri Jul 5 2019 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt4
- update to current version

* Fri Apr 5 2019 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt3
- update to current version

* Tue Feb 5 2019 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt2
- update to current version

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt1
- initial build for ALT
