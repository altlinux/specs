%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname passenger

Name:          gem-passenger
Version:       6.2.0
Release:       alt1
Summary:       Easy and robust deployment Ruby on Rails applications on Apache and Nginx webservers
Summary(ru_RU.UTF-8): Простой и ясный мост между приложениями на Рельсах и серверами Апач и Нжинкс
License:       MIT
Group:         System/Servers
Url:           https://github.com/phusion/passenger
Vcs:           https://github.com/phusion/passenger.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
Source1:       passenger.load.erb
Source2:       passenger.conf.erb
Source3:       passenger.start
Source4:       locations.ini.erb
Patch:         patch.patch
BuildRequires(pre): rpm-macros-ruby setup-rb rake libruby-devel
BuildRequires(pre): rpm-macros-apache2
BuildRequires(pre): rpm-build-python3
BuildRequires: %(eval echo %apache2_apr_buildreq)
BuildRequires: apache2-devel >= 2.2.5
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(apr-1)
BuildRequires: pkgconfig(apr-util-1)
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libcurl)
BuildRequires: apache2-httpd-worker
BuildRequires: gcc-c++
BuildRequires: gnu-config
%if_enabled check
BuildRequires: gem(gpgme) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(mime-types) >= 3.5.1
BuildRequires: gem(rack) >= 1.6.13
BuildRequires: gem(rackup) >= 1.0.1
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rspec-collection_matchers) >= 0
BuildRequires: gem(webrick) >= 1.8.1
BuildConflicts: gem(mime-types) >= 4
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(webrick) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mime-types >= 3.5.2,mime-types < 4
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency webrick >= 1.8.2,webrick < 2
%ruby_ignore_path_tokens dev,build,agent,cxx_supportlib,schema_printer
Requires(pre): apache2 >= %apache2_version-%apache2_release
Requires:      ruby >= 2.5
Requires:      gem(rack) >= 1.6.13
Requires:      gem(rackup) >= 1.0.1
Requires:      gem(rake) >= 12.3.3
Conflicts:     ruby1.8-%gemname
Provides:      gem(passenger) = 6.2.0

%ruby_on_build_rake_tasks apache2

%description
Phusion Passenger - a.k.a. mod_rails or mod_rack - makes deployment of Ruby web
applications, such as those built on the revolutionary Ruby on Rails web
framework, a breeze. It follows the usual Ruby on Rails conventions, such as
"Don't-Repeat-Yourself".
* Deployment is only a matter of uploading application files. No Ruby (on
  Rails)-specific server configuration required!
* Supports both the industry standard Apache web server and the fast and
  lightweight Nginx web server.
* Allows Ruby on Rails applications to use about 33%% less memory, when used in
  combination with Ruby Enterprise Edition (optional).
* Zero maintenance. No port management, server process monitoring or stale file
  cleanup required. Errors are automatically recovered whenever possible.
* Designed for performance, stability and security. Phusion Passenger should
  never crash Apache even in case of crashing Rails applications
* Well-documented, for both system administrators and developers!

%description         -l ru_RU.UTF-8
Phusion Passenger™ известный как mod_rails или mod_rack


%package       -n passenger
Version:       6.2.0
Release:       alt1
Summary:       Easy and robust deployment Ruby on Rails applications on Apache and Nginx webservers executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета passenger
Group:         Other
BuildArch:     noarch

Requires:      gem(passenger) = 6.2.0

%description   -n passenger
Easy and robust deployment Ruby on Rails applications on Apache and Nginx
webservers executable(s).

Phusion Passenger - a.k.a. mod_rails or mod_rack - makes deployment of Ruby web
applications, such as those built on the revolutionary Ruby on Rails web
framework, a breeze. It follows the usual Ruby on Rails conventions, such as
"Don't-Repeat-Yourself".
* Deployment is only a matter of uploading application files. No Ruby (on
  Rails)-specific server configuration required!
* Supports both the industry standard Apache web server and the fast and
  lightweight Nginx web server.
* Allows Ruby on Rails applications to use about 33%% less memory, when used in
  combination with Ruby Enterprise Edition (optional).
* Zero maintenance. No port management, server process monitoring or stale file
  cleanup required. Errors are automatically recovered whenever possible.
* Designed for performance, stability and security. Phusion Passenger should
  never crash Apache even in case of crashing Rails applications
* Well-documented, for both system administrators and developers!

%description   -n passenger -l ru_RU.UTF-8
Исполнямка для самоцвета passenger.


%if_enabled    doc
%package       -n gem-passenger-doc
Version:       6.2.0
Release:       alt1
Summary:       Easy and robust deployment Ruby on Rails applications on Apache and Nginx webservers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета passenger
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(passenger) = 6.2.0

%description   -n gem-passenger-doc
Easy and robust deployment Ruby on Rails applications on Apache and Nginx
webservers documentation files.

Phusion Passenger - a.k.a. mod_rails or mod_rack - makes deployment of Ruby web
applications, such as those built on the revolutionary Ruby on Rails web
framework, a breeze. It follows the usual Ruby on Rails conventions, such as
"Don't-Repeat-Yourself".
* Deployment is only a matter of uploading application files. No Ruby (on
  Rails)-specific server configuration required!
* Supports both the industry standard Apache web server and the fast and
  lightweight Nginx web server.
* Allows Ruby on Rails applications to use about 33%% less memory, when used in
  combination with Ruby Enterprise Edition (optional).
* Zero maintenance. No port management, server process monitoring or stale file
  cleanup required. Errors are automatically recovered whenever possible.
* Designed for performance, stability and security. Phusion Passenger should
  never crash Apache even in case of crashing Rails applications
* Well-documented, for both system administrators and developers!

%description   -n gem-passenger-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета passenger.
%endif


%if_enabled    devel
%package       -n gem-passenger-devel
Version:       6.2.0
Release:       alt1
Summary:       Easy and robust deployment Ruby on Rails applications on Apache and Nginx webservers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета passenger
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(passenger) = 6.2.0
Requires:      %(eval echo %apache2_apr_buildreq)
Requires:      gcc-c++
Requires:      gnu-config
Requires:      apache2-devel >= 2.2.5
Requires:      pkgconfig(zlib)
Requires:      pkgconfig(apr-1)
Requires:      pkgconfig(apr-util-1)
Requires:      pkgconfig(libssl)
Requires:      pkgconfig(libcurl)
Requires:      apache2-httpd-worker
Requires:      gem(gpgme) >= 0
Requires:      gem(json) >= 0
Requires:      gem(mime-types) >= 3.5.1
Requires:      gem(rack) >= 1.6.13
Requires:      gem(rackup) >= 1.0.1
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(rspec-collection_matchers) >= 0
Requires:      gem(webrick) >= 1.8.1
Conflicts:     gem(mime-types) >= 4
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(webrick) >= 2

%description   -n gem-passenger-devel
Easy and robust deployment Ruby on Rails applications on Apache and Nginx
webservers development package.

Phusion Passenger - a.k.a. mod_rails or mod_rack - makes deployment of Ruby web
applications, such as those built on the revolutionary Ruby on Rails web
framework, a breeze. It follows the usual Ruby on Rails conventions, such as
"Don't-Repeat-Yourself".
* Deployment is only a matter of uploading application files. No Ruby (on
  Rails)-specific server configuration required!
* Supports both the industry standard Apache web server and the fast and
  lightweight Nginx web server.
* Allows Ruby on Rails applications to use about 33%% less memory, when used in
  combination with Ruby Enterprise Edition (optional).
* Zero maintenance. No port management, server process monitoring or stale file
  cleanup required. Errors are automatically recovered whenever possible.
* Designed for performance, stability and security. Phusion Passenger should
  never crash Apache even in case of crashing Rails applications
* Well-documented, for both system administrators and developers!

%description   -n gem-passenger-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета passenger.
%endif


%package       -n apache2-mod-passenger
Version:       6.2.0
Release:       alt1
Summary:       Easy and robust deployment Ruby on Rails applications on Apache and Nginx webservers apache module files
Summary(ru_RU.UTF-8): Модуль passenger для вебсервера apache
Group:         System/Servers

Requires:      passenger = %EVR
Requires:      apache2-httpd-worker
Provides:      mod_passenger = 6.2.0
Provides:      apache2-mod_passenger = 6.2.0

%description   -n apache2-mod-passenger
Easy and robust deployment Ruby on Rails applications on Apache and Nginx
webservers apache module files.

Phusion Passenger - a.k.a. mod_rails or mod_rack - makes deployment of Ruby web
applications, such as those built on the revolutionary Ruby on Rails web
framework, a breeze. It follows the usual Ruby on Rails conventions, such as
"Don't-Repeat-Yourself".
* Deployment is only a matter of uploading application files. No Ruby
  (on Rails)-specific server configuration required!
* Supports both the industry standard Apache web server and the fast and
  lightweight Nginx web server.
* Allows Ruby on Rails applications to use about 33%% less memory, when used in
  combination with Ruby Enterprise Edition (optional).
* Zero maintenance. No port management, server process monitoring or stale file
  cleanup required. Errors are automatically recovered whenever possible.
* Designed for performance, stability and security. Phusion Passenger should
  never crash Apache even in case of crashing Rails applications
* Well-documented, for both system administrators and developers!

%description   -n apache2-mod-passenger -l ru_RU.UTF-8
Файлы для разработки самоцвета passenger.


%prep
%setup
%autopatch
# Set correct python3 executable in shebang
subst 's|#!.*python$|#!%__python3|' $(grep -Rl '#!.*python$' *)
subst '1i #!%__python3' test/stub/wsgi/passenger_wsgi.py
cp -a -t src/cxx_supportlib/vendor-modified/libev /usr/share/gnu-config/config.{guess,sub}
cp -a -t src/cxx_supportlib/vendor-copy/libuv /usr/share/gnu-config/config.{guess,sub}

%build
%ruby_build

%install
%ruby_install
%ifnarch armh
mkdir -p %buildroot%ruby_gemextdir/
mv -f $(find buildout/ -name passenger_native_support.so) %buildroot%ruby_gemextdir/
%endif

#mod_passenger
install -p -D -m 755 -- buildout/apache2/mod_passenger.so %buildroot%apache2_libexecdir/mod_passenger.so
install -p -D -m 755 -- buildout/support-binaries/PassengerAgent %buildroot%ruby_gemlibdir/src/support-binaries/PassengerAgent

install -d -m 755 -- %buildroot%apache2_mods_available
install -d -m 755 -- %buildroot%apache2_mods_start
%ruby_erb_eval %SOURCE1 %buildroot%apache2_mods_available/passenger.load
%ruby_erb_eval %SOURCE2 %buildroot%apache2_mods_available/passenger.conf
install -p -m 644 -- %SOURCE3 %buildroot%apache2_mods_start/100-passenger.conf
%ruby_erb_eval %SOURCE4 %buildroot/%ruby_gemlibdir/src/ruby_supportlib/locations.ini

%check
%ruby_test

%post          -n apache2-mod-passenger
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:

if [ -e %apache2_mods_enabled/passenger.load ]; then
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
	service %apache2_dname condrestart ||:
    else
	echo "Some errors detected in Apache2 configuration!"
	echo "To use mod_passenger check configuration and start %apache2_dname service."
	echo
    fi
else
    echo "Apache2 mod_passenger module had been installed, but does't enabled."
    echo "Check %apache2_mods_start directory for files with 'passenger=no' lines."
    echo
fi

%preun         -n apache2-mod-passenger
if [ "$1" = "0" ] ; then # last uninstall
    [ -e %apache2_mods_enabled/passenger.load ] && %apache2_sbindir/a2dismod passenger 2>&1 >/dev/null ||:
fi

%postun        -n apache2-mod-passenger
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:
if [ "$1" = "0" ] ; then # last uninstall
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
	service %apache2_dname condrestart ||:
    else
	echo "Some errors detected in Apache2 configuration!"
	echo "To complete mod_passenger uninstalling check configuration and restart %apache2_dname service."
	echo
    fi
fi

%files
%doc CHANGELOG CONTRIBUTING.md CONTRIBUTORS LICENSE README.md CODE_OF_CONDUCT.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n passenger
%doc CHANGELOG CONTRIBUTING.md CONTRIBUTORS LICENSE README.md CODE_OF_CONDUCT.md
%_bindir/passenger
%_bindir/passenger-install-apache2-module
%_bindir/passenger-install-nginx-module
%_bindir/passenger-config
%_bindir/passenger-status
%_bindir/passenger-memory-stats
%_mandir/*

%if_enabled    doc
%files         -n gem-passenger-doc
%doc CHANGELOG CONTRIBUTING.md CONTRIBUTORS LICENSE README.md CODE_OF_CONDUCT.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-passenger-devel
%doc CHANGELOG CONTRIBUTING.md CONTRIBUTORS LICENSE README.md CODE_OF_CONDUCT.md
%endif

%files         -n apache2-mod-passenger
%config(noreplace) %apache2_mods_available/passenger.conf
%config            %apache2_mods_available/passenger.load
%config            %apache2_mods_start/100-passenger.conf
%ifnarch armh
%apache2_libexecdir/mod_passenger.so
%endif


%changelog
* Tue Sep 01 2026 Pavel Skrylev <majioa@altlinux.org> 6.2.0-alt1
- ^ 6.1.0 -> 6.2.0

* Thu Oct 02 2025 Pavel Skrylev <majioa@altlinux.org> 6.1.0-alt1
- ^ 6.0.23 -> 6.1.0 (closes ALT#39147)
- * rebase to upstream

* Wed Jul 31 2024 Pavel Skrylev <majioa@altlinux.org> 6.0.23-alt1
- ^ 6.0.11 -> 6.0.23

* Thu Nov 16 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 6.0.11-alt3
- NMU: fixed FTBFS on LoongArch (use fresh config.{guess,sub})

* Mon Mar 14 2022 Pavel Skrylev <majioa@altlinux.org> 6.0.11-alt2
- !fix build for new setup

* Thu Oct 14 2021 Pavel Skrylev <majioa@altlinux.org> 6.0.11-alt1
- ^ 6.0.4 -> 6.0.11

* Mon Jun 21 2021 Andrey Cherepanov <cas@altlinux.org> 6.0.4-alt1.1
- FTBFS: use autoreq with python3.
- Exclude build on armh.

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 6.0.4-alt1
- ^ 6.0.2 -> 6.0.4
- ! spec tags

* Fri Jun 28 2019 Pavel Skrylev <majioa@altlinux.org> 6.0.2-alt1
- > Ruby Policy 2.0
- ^ 4.0.60 -> 6.0.2

* Sun Jul 17 2016 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.60-alt1
- Update to last 4.0.x release

* Wed Mar 19 2014 Led <led@altlinux.ru> 4.0.10-alt1.1
- Rebuilt with ruby-2.0.0-alt1

* Wed Aug 14 2013 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.10-alt1
- Update to new 4.0.x release
- Rename library and data directories from phusion-passenger to passenger
- Install locations.ini for packaged directories to file:
  RUBY_SITEARCHDIR/phusion_passenger/locations.ini

* Tue Aug 13 2013 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.21-alt1
- Update to last 3.0.x release

* Thu Apr 18 2013 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.19-alt1
- Update to release

* Fri Nov 30 2012 Led <led@altlinux.ru> 3.0.17-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Thu Aug 30 2012 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.17-alt1
- Update to release

* Sun Nov 27 2011 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.10-alt1
- Update to release
- Start build with new scheme based on upstream git repository:
  https://github.com/FooBarWidget/passenger.git

* Sun Nov 27 2011 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.9-alt3
- Build new release to Sisyphus with Python-2.7

* Fri Nov 18 2011 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.9-alt2
- Add unowned packaged directories
- Fix passenger_native_support.so installation path
- Update spec-file for common way

* Fri Nov 18 2011 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.9-alt1
- Update to release
- Add conflict to ruby1.8-passenger

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.5-alt1.1
- Rebuild with Python-2.7

* Sun Jun 19 2011 Evgeny Sinelnikov <sin@altlinux.ru> 3.0.5-alt1
- Update to release

* Fri Apr 15 2011 Malo Skryleve <malo@altlinux.org> 3.0.2-alt2
- Fixed some errors

* Sat Feb 26 2011 Malo Skryleve <malo@altlinux.org> 3.0.2-alt1
- initial build for ALT Linux Sisyphus
