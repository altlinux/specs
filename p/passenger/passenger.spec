%define        gemname passenger

Name:          passenger
Version:       6.0.11
Release:       alt3
Summary:       Easy and robust deployment Ruby on Rails applications on Apache and Nginx webservers
Summary(ru_RU.UTF-8): Простой и ясный мост между приложениями на Рельсах и серверами Апач и Нжинкс
License:       MIT
Group:         System/Servers
Url:           https://github.com/phusion/passenger
Vcs:           https://github.com/phusion/passenger.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Source1:       passenger.load
Source2:       passenger.conf
Source3:       passenger.start
Source4:       locations.ini
Patch:         patch.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-macros-apache2
BuildRequires(pre): rpm-build-python3
BuildRequires: %(eval echo %apache2_apr_buildreq)
BuildRequires: apache2-devel >= 2.2.5
BuildRequires: zlib-devel
BuildRequires: libapr1-devel
BuildRequires: libaprutil1-devel
BuildRequires: libssl-devel
BuildRequires: libcurl-devel
BuildRequires: apache2-httpd-worker
BuildRequires: gcc-c++
BuildRequires: gem(rake) >= 0.8.1
BuildRequires: gem(rack) >= 0
BuildRequires: gnu-config

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency json >= 1.8.5,json < 3
%ruby_use_gem_dependency mime-types >= 3.3.1,mime-types < 4
%ruby_use_gem_dependency rack >= 2.2.2,rack < 3
%ruby_use_gem_dependency rake >= 13.0.5,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires(pre): apache2 >= %apache2_version-%apache2_release
Provides:      gem(passenger) = 6.0.11
Conflicts:     ruby1.8-passenger

%ruby_on_build_rake_tasks apache2

%description
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

%description         -l ru_RU.UTF-8
Phusion Passenger™ известный как mod_rails или mod_rack


%package       -n gem-passenger
Version:       6.0.11
Release:       alt2
Summary:       Easy and robust deployment Ruby on Rails applications on Apache and Nginx webservers
Group:         Development/Ruby

Requires:      gem(passenger) = 6.0.11
Requires:      gem(rake) >= 0.8.1
Requires:      gem(rack) >= 0

%description   -n gem-passenger
Easy and robust deployment Ruby on Rails applications on Apache and Nginx
webservers executable(s).

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

%description   -n gem-passenger -l ru_RU.UTF-8
Исполнямка для самоцвета passenger.


%package       -n gem-passenger-doc
Version:       6.0.11
Release:       alt2
Summary:       Easy and robust deployment Ruby on Rails applications on Apache and Nginx webservers gem
Summary(ru_RU.UTF-8): Самоцвет простого и ясного моста между приложениями на Рельсах и серверами Апач и Нжинкс
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(passenger) = 6.0.11

%description   -n gem-passenger-doc
Easy and robust deployment Ruby on Rails applications on Apache and Nginx
webservers documentation files.

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

%description   -n gem-passenger-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета passenger.


%package       -n gem-passenger-devel
Version:       6.0.11
Release:       alt2
Summary:       Easy and robust deployment Ruby on Rails applications on Apache and Nginx webservers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета passenger
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(passenger) = 6.0.11

%description   -n gem-passenger-devel
Easy and robust deployment Ruby on Rails applications on Apache and Nginx
webservers development package.

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

%description   -n gem-passenger-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета passenger.


%package       -n apache2-mod-passenger
Version:       6.0.11
Release:       alt2
Summary:       Easy and robust deployment Ruby on Rails applications on Apache and Nginx webservers apache module files
Summary(ru_RU.UTF-8): Модуль passenger для вебсервера apache
Group:         System/Servers

Requires:      passenger = 6.0.11
Requires:      apache2-httpd-worker
Provides:      apache2-mod_passenger = 6.0.11
Provides:      mod_passenger = 6.0.11

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
%ifnarch armh
install -p -D -m 755 -- buildout/apache2/mod_passenger.so %buildroot%apache2_libexecdir/mod_passenger.so
%endif
install -d -m 755 -- %buildroot%apache2_mods_available
install -d -m 755 -- %buildroot%apache2_mods_start
install -p -m 644 -- %SOURCE1 %buildroot%apache2_mods_available/passenger.load
install -p -m 644 -- %SOURCE2 %buildroot%apache2_mods_available/passenger.conf
install -p -m 644 -- %SOURCE3 %buildroot%apache2_mods_start/100-passenger.conf
install -p -D -m 644 -- %SOURCE4 %buildroot/%ruby_gemlibdir/locations.ini
sed 's,@a_libexecdir@,%apache2_libexecdir,g' \
    -i %buildroot%apache2_mods_available/passenger.load
sed -e 's,@passenger_path@,%ruby_gemlibdir/locations.ini,g' -e 's,@ruby_exec@,%__ruby,g' \
    -i %buildroot%apache2_mods_available/passenger.conf
sed -e 's,@rubylibdir@,%ruby_sitearchdir,g' \
    -e 's,@a_libexecdir@,%apache2_libexecdir,g' \
    -e 's,@bindir@,%_bindir,g' \
    -e 's,@libdir@,%_libdir,g' \
    -e 's,@datadir@,%_datadir,g' \
    -e 's,@name@,%name,g' \
    -i %buildroot%ruby_gemlibdir/locations.ini

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
%doc README.md
%_bindir/passenger
%_bindir/passenger-install-apache2-module
%_bindir/passenger-install-nginx-module
%_bindir/passenger-config
%_bindir/passenger-status
%_bindir/passenger-memory-stats
%_mandir/*

%files         -n gem-passenger
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%ifnarch armh
%ruby_gemextdir
%endif

%files         -n gem-passenger-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-passenger-devel
%doc README.md

%files         -n apache2-mod-passenger
%config(noreplace) %apache2_mods_available/passenger.conf
%config            %apache2_mods_available/passenger.load
%config            %apache2_mods_start/100-passenger.conf
%ifnarch armh
%apache2_libexecdir/mod_passenger.so
%endif


%changelog
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
