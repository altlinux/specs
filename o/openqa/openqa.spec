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

%define t_requires perl(DBD/Pg.pm) perl(Mojolicious/Plugin/RenderFile.pm) perl(DBIx/Class/Schema/Config.pm) perl(DBIx/Class/OptimisticLocking.pm) perl(Config/IniFiles.pm) perl(SQL/Translator.pm) perl(Date/Format.pm) perl(File/Copy/Recursive.pm) perl(DateTime/Format/Pg.pm) perl(Net/OpenID/Consumer.pm) perl(aliased.pm) perl(Config/Tiny.pm) perl(DBIx/Class/DynamicDefault.pm) perl(DBIx/Class/Storage/Statistics.pm) perl(IO/Socket/SSL.pm) perl(Data/Dump.pm) perl(Text/Markdown.pm) perl(Net/DBus.pm) perl(IPC/Run.pm) perl(Archive/Extract.pm) perl(CSS/Minifier/XS.pm) perl(JavaScript/Minifier/XS.pm) perl(Time/ParseDate.pm) perl(Time/Piece.pm) perl(Time/Seconds.pm) perl(Sort/Versions.pm) perl(BSD/Resource.pm) perl(Cpanel/JSON/XS.pm) perl(YAML/PP.pm) perl(YAML/XS.pm) perl(IPC/Run.pm) perl(CommonMark.pm) perl(DBIx/Class.pm) perl-Package-Generator perl(Mojo/SQLite.pm) perl(Mojolicious.pm) perl(Mojolicious/Plugin/AssetPack.pm) perl(Mojo/IOLoop/ReadWriteProcess.pm) perl(Minion.pm) perl(Minion/Backend/SQLite.pm) perl(Test/Compile.pm) perl(Test/Fatal.pm) perl(Test/MockModule.pm) perl(Test/MockObject.pm) perl(Test/Mojo.pm) perl(Test/Output.pm) perl(Test/Pod.pm) perl(Test/Warnings.pm) perl(Perl/Critic.pm) perl(DBD/SQLite.pm) perl(DBIx/Class/DeploymentHandler.pm) perl(SQL/SplitStatement.pm) perl(IPC/Cmd.pm) perl(Module/Load/Conditional.pm) perl(CPAN/Meta/YAML.pm) perl(JSON/Validator.pm) perl(Test/Exception.pm) perl(Text/Diff.pm) perl(Test/Strict.pm) perl(Mojo/RabbitMQ/Client.pm) perl(Test/Most.pm) python3-module-setuptools yamllint jq curl shellcheck perl(Test/More.pm) perl(Mojolicious/Plugin/OAuth2.pm) python3-module-jsbeautifier git-core perl(File/Map.pm) perl(Filesys/Df.pm) perl(Module/Loaded.pm)

Name: openqa
Version: 4.6
Release: alt9.1
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
Patch1: rmsysusers.patch
#BuildArch: noarch

BuildRequires: %t_requires
BuildRequires: spectool postgresql15-server systemd ruby-rb-inotify sass ruby-sass-listen os-autoinst osc
BuildRequires: python3-devel
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-requests
BuildRequires: python3-module-future

Requires: openqa-common = %EVR
Requires: openqa-client = %EVR
Requires: perl(URI.pm)
Requires: perl(LWP/Protocol/https.pm)
Requires: perl(Getopt/Long/Descriptive.pm)
Requires: optipng
Requires: dbus git-core 
Requires: perl(YAML/XS.pm)

ExclusiveArch: i586 x86_64 ppc64le aarch64

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
Requires: perl(DBD/SQLite.pm) perl(SQL/SplitStatement.pm) perl(Mojo/SQLite.pm)
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
Requires: perl(Test/More.pm)

%description client
This package contains the openQA client script, along with several
other useful tools and support files. The client script is a convenient
helper for interacting with the openQA REST API.

%package python-scripts
Summary:        Additional scripts in python
Group:          Development/Tools
Requires:       python3-module-requests python3-module-future


%description python-scripts
Additional scripts for the use of openQA in the python programming language.

%package local-db
Summary: Helper package to ease setup of postgresql DB
Group: Development/Tools
Requires: postgresql15-server

%description local-db
You only need this package if you have a local postgresql server
next to the webui.

%package single-instance
Summary:        Convenience package for a single-instance setup
Group:          Development/Tools
Requires:       %name-local-db
Requires:       %name-worker
Requires:       apache2

%description single-instance
Use this package to setup a local instance with all services provided together.

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
sed -i -e 's|../fonts/|https://cdn.jsdelivr.net/npm/fork-awesome@1.2.0/fonts/|g' assets/cache/cdn.jsdelivr.net/npm/fork-awesome@1.2.0/css/fork-awesome.min.css
sed -i -e 's|/usr/lib/systemd/|/lib/systemd/|'  systemd/systemd-openqa-generator
sed -i -e 's|/usr/lib/systemd/|/lib/systemd/|' -e 's|/usr/lib/tmpfiles.d|/lib/tmpfiles.d|'  Makefile
sed -i -e 's|https://|cache/|' -e 's|http://|cache/|' assets/assetpack.def
sed -i -e 's,apache2\.service,httpd2\.service,g' systemd/*.service
sed -i -e 's,"$(DESTDIR)"/etc/apache2/vhosts.d,"$(DESTDIR)"%_sysconfdir/httpd2/conf/sites-available,g' Makefile
sed -i -e 's,/etc/apache2/vhosts.d,%_sysconfdir/httpd2/conf/sites-available,g' etc/apache2/vhosts.d/*
sed -i -e 's,/etc/apache2/ssl.crt,%_sysconfdir/pki/tls/certs,g' etc/apache2/vhosts.d/*
sed -i -e 's,/etc/apache2/ssl.key,%_sysconfdir/pki/tls/private,g' etc/apache2/vhosts.d/*
sed -i -e 's,/usr/bin/systemd-tmpfiles --create /etc/tmpfiles.d/openqa.conf,/sbin/systemd-tmpfiles --create /lib/tmpfiles.d/openqa.conf,g' systemd/systemd-openqa-generator
#These services and files are not used.
rm -rf systemd/openqa-vde_switch.service
rm -rf systemd/openqa-slirpvde.service
rm -rf script/openqa-slirpvde
rm -rf script/openqa-vde_switch
rm -rf script/openqa-auto-update
rm -rf script/openqa-continuous-update
rm -rf script/openqa-check-devel-repo
rm -rf usr/lib/sysusers.d/geekotest.conf
rm -rf usr/lib/sysusers.d/openQA-worker.conf

%build
%make_build

%install
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
%makeinstall_std

mkdir -p %buildroot%_datadir/openqa/etc/openqa
ln -s %_sysconfdir/openqa/openqa.ini %buildroot%_datadir/openqa/etc/openqa/openqa.ini
ln -s %_sysconfdir/openqa/database.ini %buildroot%_datadir/openqa/etc/openqa/database.ini
mkdir -p %buildroot%_bindir
ln -s %_datadir/openqa/script/client %buildroot%_bindir/openqa-client
ln -s %_datadir/openqa/script/openqa-cli %buildroot%_bindir/openqa-cli
ln -s %_datadir/openqa/script/clone_job.pl %buildroot%_bindir/openqa-clone-job
ln -s %_datadir/openqa/script/dump_templates %buildroot%_bindir/openqa-dump-templates
ln -s %_datadir/openqa/script/load_templates %buildroot%_bindir/openqa-load-templates
ln -s %_datadir/openqa/script/openqa-clone-custom-git-refspec %buildroot%_bindir/openqa-clone-custom-git-refspec
ln -s %_datadir/openqa/script/openqa-validate-yaml %buildroot%_bindir/openqa-validate-yaml
ln -s %_datadir/openqa/script/openqa-label-all %buildroot%_bindir/openqa-label-all
ln -s %_datadir/openqa/script/setup-db %buildroot%_bindir/openqa-setup-db

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
# Skip tests not working currently, or flaky
rm -f t/03-auth.t
rm -f t/05-scheduler-full.t
rm -f t/24-worker-overall.t
rm -f t/25-cache-client.t
rm -f t/25-cache-service.t
rm -f t/09-job_clone.t
rm -f t/40-script_openqa-clone-custom-git-refspec.t
rm -f t/43-scheduling-and-worker-scalability.t
rm -f t/42-screenshots.t
rm -f t/ui/*.t
# we don't really need the tidy test
rm -f t/00-tidy.t

rm -rf %buildroot/DB
export LC_ALL=en_US.UTF-8
sed -i -e 's,unshare -r -n ,,g' t/40-openqa-clone-job.t t/32-openqa_client-script.t
sed -i -e '/fails without network/d' t/32-openqa_client-script.t
export CI=1
export OPENQA_TEST_TIMEOUT_SCALE_CI=10
# Skip container tests that would need additional requirements, e.g.
# docker-compose. Also, these tests are less relevant (or not relevant) for
# packaging
export CONTAINER_TEST=0
export HELM_TEST=0
make test-with-database OGIT_CEILING_DIRECTORIES="/" BS_RUN=1 PROVE_ARGS='-r' CHECKSTYLE=0 TEST_PG_PATH=%buildroot/DB
rm -rf %buildroot/DB

%post
%tmpfiles_create %_tmpfilesdir/openqa-webui.conf

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
#init
%_unitdir/openqa-webui.service
%_unitdir/openqa-livehandler.service
%_unitdir/openqa-gru.service
%_unitdir/openqa-scheduler.service
%_unitdir/openqa-websockets.service
%_unitdir/openqa-enqueue-audit-event-cleanup.service
%_unitdir/openqa-enqueue-audit-event-cleanup.timer
%_unitdir/openqa-enqueue-asset-cleanup.service
%_unitdir/openqa-enqueue-asset-cleanup.timer
%_unitdir/openqa-enqueue-result-cleanup.service
%_unitdir/openqa-enqueue-result-cleanup.timer
%_unitdir/openqa-enqueue-bug-cleanup.service
%_unitdir/openqa-enqueue-bug-cleanup.timer
%_tmpfilesdir/openqa-webui.conf
# web libs
%dir %_datadir/openqa/lib
%dir %_datadir/openqa/lib/OpenQA
%_datadir/openqa/lib/DBIx/
%_datadir/openqa/lib/OpenQA/LiveHandler.pm
%_datadir/openqa/lib/OpenQA/Resource/
%_datadir/openqa/lib/OpenQA/Scheduler/
%_datadir/openqa/lib/OpenQA/Schema/
%_datadir/openqa/lib/OpenQA/WebAPI/
%_datadir/openqa/lib/OpenQA/WebSockets/
%_datadir/openqa/templates
%_datadir/openqa/public
%_datadir/openqa/assets
%_datadir/openqa/dbicdh
%_datadir/openqa/script/configure-web-proxy
%dir %_datadir/openqa/script
%_datadir/openqa/script/create_admin
%_datadir/openqa/script/fetchneedles
%_datadir/openqa/script/initdb
%_datadir/openqa/script/openqa
%_datadir/openqa/script/openqa-scheduler
%_datadir/openqa/script/openqa-scheduler-daemon
%_datadir/openqa/script/openqa-websockets
%_datadir/openqa/script/openqa-websockets-daemon
%_datadir/openqa/script/openqa-livehandler
%_datadir/openqa/script/openqa-livehandler-daemon
%_datadir/openqa/script/openqa-enqueue-asset-cleanup
%_datadir/openqa/script/openqa-enqueue-audit-event-cleanup
%_datadir/openqa/script/openqa-enqueue-bug-cleanup
%_datadir/openqa/script/openqa-enqueue-result-cleanup
%_datadir/openqa/script/openqa-gru
%_datadir/openqa/script/openqa-rollback
%_datadir/openqa/script/openqa-webui-daemon
%_datadir/openqa/script/upgradedb
%_datadir/openqa/script/modify_needle
%dir %_localstatedir/openqa/share
%defattr(-,_geekotest,root)
%dir %_localstatedir/openqa/db
%dir %_localstatedir/openqa/images
%dir %_localstatedir/openqa/webui
%dir %_localstatedir/openqa/webui/cache
%dir %_localstatedir/openqa/share/factory
%dir %_localstatedir/openqa/share/tests
%_localstatedir/openqa/testresults

%files python-scripts
%_datadir/openqa/script/openqa-label-all
%_bindir/openqa-label-all

%files common
%doc COPYING
%dir %_datadir/openqa
%ghost %dir %_datadir/openqa/packed
%_datadir/openqa/lib
%exclude %_datadir/openqa/lib/OpenQA/CacheService/
%exclude %_datadir/openqa/lib/DBIx/
%exclude %_datadir/openqa/lib/OpenQA/Client.pm
%exclude %_datadir/openqa/lib/OpenQA/Client
%exclude %_datadir/openqa/lib/OpenQA/UserAgent.pm
%exclude %_datadir/openqa/lib/OpenQA/LiveHandler.pm
%exclude %_datadir/openqa/lib/OpenQA/Resource/
%exclude %_datadir/openqa/lib/OpenQA/Scheduler/
%exclude %_datadir/openqa/lib/OpenQA/Schema/
%exclude %_datadir/openqa/lib/OpenQA/WebAPI/
%exclude %_datadir/openqa/lib/OpenQA/WebSockets/
%exclude %_datadir/openqa/lib/OpenQA/Worker/
%dir %_localstatedir/openqa
%_localstatedir/openqa/factory
%_localstatedir/openqa/tests
%_localstatedir/openqa/script

%files worker
%dir %_datadir/openqa/lib
%dir %_datadir/openqa/lib/OpenQA
%{_datadir}/openqa/lib/OpenQA/CacheService/
%{_datadir}/openqa/lib/OpenQA/Worker
%config(noreplace) %_sysconfdir/openqa/workers.ini
%config(noreplace) %attr(0400,_openqa-worker,root) %_sysconfdir/openqa/client.conf
%dir %_unitdir
/lib/systemd/system-generators/systemd-openqa-generator
%_unitdir/openqa-worker.target
%_unitdir/openqa-worker@.service
%_unitdir/openqa-worker-plain@.service
%_unitdir/openqa-worker-cacheservice-minion.service
%_unitdir/openqa-worker-cacheservice.service
%_unitdir/openqa-worker-no-cleanup@.service
%_unitdir/openqa-worker-auto-restart@.service
%_unitdir/openqa-reload-worker-auto-restart@.service
%_unitdir/openqa-reload-worker-auto-restart@.path
%_tmpfilesdir/openqa.conf
#worker libs
%dir %{_datadir}/openqa
%dir %{_datadir}/openqa/script
%_datadir/openqa/script/worker
%_datadir/openqa/script/openqa-workercache
%_datadir/openqa/script/openqa-workercache-daemon
%_datadir/openqa/script/openqa-worker-cacheservice-minion
%dir %_localstatedir/openqa/pool
%defattr(-,_openqa-worker,root)
%dir %_localstatedir/openqa/cache

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
%_datadir/openqa/script/openqa-load-templates
%_datadir/openqa/script/openqa-dump-templates
%_datadir/openqa/script/openqa-cli
%_datadir/openqa/script/openqa-clone-job
%_datadir/openqa/script/openqa-clone-custom-git-refspec
%_datadir/openqa/script/openqa-validate-yaml
%_datadir/openqa/lib/OpenQA/Client.pm
%_datadir/openqa/lib/OpenQA/Client
%_datadir/openqa/lib/OpenQA/UserAgent.pm
%_bindir/openqa-client
%_bindir/openqa-cli
%_bindir/openqa-clone-job
%_bindir/openqa-dump-templates
%_bindir/openqa-load-templates
%_bindir/openqa-clone-custom-git-refspec
%_bindir/openqa-validate-yaml

%files doc
%doc docs/*

%files local-db
%_unitdir/openqa-setup-db.service
%_datadir/openqa/script/setup-db
%_bindir/openqa-setup-db

%files single-instance

%changelog
* Thu Feb 09 2023 Alexei Takaseev <taf@altlinux.org> 4.6-alt9.1
- Change BR: postgresql10-server -> postgresql15-server
- Change Requires: postgresql10-server -> postgresql15-server

* Wed Dec 07 2022 Alexandr Antonov <aas@altlinux.org> 4.6-alt9
- update to current version

* Tue Jun 21 2022 Alexandr Antonov <aas@altlinux.org> 4.6-alt8
- update to current version

* Mon Mar 28 2022 Alexandr Antonov <aas@altlinux.org> 4.6-alt7
- update to current version

* Wed Dec 8 2021 Alexandr Antonov <aas@altlinux.org> 4.6-alt6
- update to current version

* Mon Nov 8 2021 Alexandr Antonov <aas@altlinux.org> 4.6-alt5
- update to current version

* Fri Aug 27 2021 Alexandr Antonov <aas@altlinux.org> 4.6-alt4
- update to current version

* Fri Aug 27 2021 Alexandr Antonov <aas@altlinux.org> 4.6-alt3
- update to current version

* Wed May 12 2021 Alexandr Antonov <aas@altlinux.org> 4.6-alt2
- update to current version

* Mon Mar 15 2021 Alexandr Antonov <aas@altlinux.org> 4.6-alt1
- update to current version

* Fri Jan 22 2021 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt18
- update to current version

* Tue Dec 08 2020 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt17
- update to current version

* Thu Oct 08 2020 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt16
- update to current version

* Thu Aug 06 2020 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt15
- update to current version

* Wed Jul 15 2020 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt14
- update to current version

* Wed Jun 10 2020 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt13
- update to current version

* Fri Apr 24 2020 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt12
- update to current version

* Thu Mar 05 2020 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt11
- update to current version

* Wed Feb 26 2020 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt10
- update to current version

* Wed Feb 05 2020 Alexandr Antonov <aas@altlinux.org> 4.5.1528009330.e68ebe2b-alt9
- update to current version

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
