# vim: set ft=spec: -*- rpm-spec -*-

%define module_name  passenger
%define orig_name    phusion-passenger
%define ruby_name    phusion_passenger
%define real_name    mod_%module_name

%define module_package_name apache2-mod_%module_name

Name: passenger
Version: 4.0.60
Release: alt1

Summary: Easy and robust deployment Ruby on Rails applications on Apache and Nginx webservers
Summary(ru_RU.UTF-8): Простой и ясный мост между приложениями на Рельсах и серверами Апач и Нгинкс
Group: System/Servers
License: other
Url: http://www.modrails.com/

Source: %module_name-%version.tar
Source1: %module_name.load
Source2: %module_name.conf
Source3: %module_name.start
Source4: locations.ini

Patch: %module_name-%version-%release.patch

BuildRequires(pre): apache2-devel >= 2.2.5
BuildRequires(pre): rpm-build-ruby rpm-macros-apache2
BuildRequires: %(eval echo %apache2_apr_buildreq)

# Automatically added by buildreq on Sat Feb 26 2011
BuildRequires: apache2-devel gcc-c++ libcrypto libcurl-devel libruby-devel ruby-rack rubygems

BuildPreReq: ruby-rake apache2-httpd-worker zlib-devel
BuildPreReq: apache2-devel libapr1-devel libaprutil1-devel libssl-devel

Requires: ruby-rails ruby-test-spec ruby-mime-types >= 1.15
Requires(pre): apache2 >= %apache2_version-%apache2_release

Conflicts: ruby1.8-passenger

%description
Phusion Passenger - a.k.a. mod_rails or mod_rack - makes deployment of
Ruby web applications, such as those built on the revolutionary Ruby on
Rails web framework, a breeze. It follows the usual Ruby on Rails
conventions, such as "Don't-Repeat-Yourself".
 * Deployment is only a matter of uploading application files.
   No Ruby (on Rails)-specific server configuration required!
 * Supports both the industry standard Apache web server and the fast
   and lightweight Nginx web server.
 * Allows Ruby on Rails applications to use about 33%% less memory, when
   used in combination with Ruby Enterprise Edition (optional).
 * Zero maintenance. No port management, server process monitoring or
   stale file cleanup required. Errors are automatically recovered
   whenever possible.
 * Designed for performance, stability and security. Phusion Passenger
   should never crash Apache even in case of crashing Rails applications
 * Well-documented, for both system administrators and developers!

%description -l ru_RU.UTF-8
Phusion Passenger™ известный как mod_rails или mod_rack

%package -n %module_package_name

Summary: Easy and robust deployment Ruby on Rails applications on Apache webserver
Summary(ru_RU.UTF-8): Простой и ясный мост между приложениями на Рельсах и сервером Апач
Group: System/Servers
Requires: ruby-rails ruby-test-spec ruby-mime-types >= 1.15 apache2-httpd-worker passenger = %version
Provides: %real_name = %version

%description -n %module_package_name
Documentation files for %name

%prep
%setup -n %module_name-%version
%patch -p1

%build
bin/passenger-install-apache2-module -a --apxs2-path %apache2_apxs --apr-config-path %apache2_apr_config

%install
#passenger
mkdir -p %buildroot%ruby_sitearchdir/
cp -rp lib/* %buildroot%ruby_sitearchdir/
#mkdir -p %buildroot%ruby_sitearchdir/%orig_name/test/
#cp -rp test/ruby/* %buildroot%ruby_sitearchdir/%orig_name/test/
mkdir -p %buildroot%_bindir/ %buildroot%_man1dir/ %buildroot%_man8dir/
cp -rp bin/* %buildroot%_bindir/
cp -rp man/*.1 %buildroot%_man1dir/
cp -rp man/*.8 %buildroot%_man8dir/
mkdir -p %buildroot%_libdir/%name
cp -rp buildout/agents %buildroot%_libdir/%name/
rm -f %buildroot%_libdir/%name/agents/*.o
cp -rp buildout/common %buildroot%_libdir/%name/
rm -rf %buildroot%_libdir/%name/common/libboost_oxt
rm -rf %buildroot%_libdir/%name/common/libpassenger_common
mkdir -p %buildroot%_datadir/%name
cp -rp $(find -name passenger_native_support.so) %buildroot%ruby_sitearchdir/
cp -rp helper-scripts %buildroot%_datadir/%name/

#extconf.rb
mkdir -p %buildroot%_datadir/%name/source/ext/ruby
cp -rp ext/ruby/extconf.rb %buildroot%_datadir/%name/source/ext/ruby/

#resources
mkdir -p %buildroot%_datadir/%name
cp -rp resources/* %buildroot%_datadir/%name/

#doc
mkdir -p %buildroot%_defaultdocdir/%name
cp -rp doc/* %buildroot%_defaultdocdir/%name/

#mod_passenger
install -p -D -m 755 -- buildout/apache2/%real_name.so %buildroot%apache2_libexecdir/%real_name.so
install -d -m 755 -- %buildroot%apache2_mods_available
install -d -m 755 -- %buildroot%apache2_mods_start
install -p -m 644 -- %SOURCE1 %buildroot%apache2_mods_available/%module_name.load
install -p -m 644 -- %SOURCE2 %buildroot%apache2_mods_available/%module_name.conf
install -p -m 644 -- %SOURCE3 %buildroot%apache2_mods_start/100-%module_name.conf
install -p -m 644 -- %SOURCE4 %buildroot%ruby_sitearchdir/%ruby_name/locations.ini
sed 's,@a_libexecdir@,%apache2_libexecdir,g' \
    -i %buildroot%apache2_mods_available/%module_name.load
sed -e 's,@passenger_path@,%ruby_sitearchdir/%ruby_name/locations.ini,g' -e 's,@ruby_exec@,%__ruby,g' \
    -i %buildroot%apache2_mods_available/%module_name.conf
sed -e 's,@rubylibdir@,%ruby_sitearchdir,g' \
    -e 's,@a_libexecdir@,%apache2_libexecdir,g' \
    -e 's,@bindir@,%_bindir,g' \
    -e 's,@libdir@,%_libdir,g' \
    -e 's,@datadir@,%_datadir,g' \
    -e 's,@name@,%name,g' \
    -i %buildroot%ruby_sitearchdir/%ruby_name/locations.ini

%files
%doc README.md LICENSE CHANGELOG INSTALL.md CONTRIBUTORS CONTRIBUTING.md
%_bindir/*
%_mandir/man?/*
%ruby_sitearchdir/*
%dir %_libdir/%name
%dir %_datadir/%name
%_libdir/%name/*
%_datadir/%name/*
%_defaultdocdir/%name

%post -n %module_package_name
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:

if [ -e %apache2_mods_enabled/%module_name.load ]; then
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
	service %apache2_dname condrestart ||:
    else
	echo "Some errors detected in Apache2 configuration!"
	echo "To use %real_name check configuration and start %apache2_dname service."
	echo
    fi
else
    echo "Apache2 %real_name module had been installed, but does't enabled."
    echo "Check %apache2_mods_start directory for files with '%module_name=no' lines."
    echo
fi

%preun -n %module_package_name
if [ "$1" = "0" ] ; then # last uninstall
    [ -e %apache2_mods_enabled/%module_name.load ] && %apache2_sbindir/a2dismod %module_name 2>&1 >/dev/null ||:
fi

%postun -n %module_package_name
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:
if [ "$1" = "0" ] ; then # last uninstall
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
	service %apache2_dname condrestart ||:
    else
	echo "Some errors detected in Apache2 configuration!"
	echo "To complete %real_name uninstalling check configuration and restart %apache2_dname service."
	echo
    fi
fi

%files -n %module_package_name
%config(noreplace) %apache2_mods_available/%module_name.conf
%config            %apache2_mods_available/%module_name.load
%config            %apache2_mods_start/100-%module_name.conf
%apache2_libexecdir/%real_name.so

%changelog
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

