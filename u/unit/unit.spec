# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_enable debug
%def_enable perl
%def_enable php
%def_enable ruby
%def_disable devel

Name: unit
Summary: NGINX Unit - Web Application Server
Version: 1.21.0
Release: alt3
License: Apache-2.0
Group: System/Servers
Url: https://unit.nginx.org/
Vcs: http://hg.nginx.org/unit/
# Mirror Vcs: https://github.com/nginx/unit

Source: %name-%version.tar

BuildRequires: libssl-devel
BuildRequires: libpcre-devel
%{?_enable_ruby:BuildRequires: ruby libruby-devel}
%{?_enable_perl:BuildRequires: perl-devel perl-base}
%{?_enable_php:BuildRequires: php7 php7-devel php-base}

Provides: nginx-unit

%description
NGINX Unit is a polyglot app server, a reverse proxy, and a static
file server, available for Unix-like systems. It was built by nginx
team members from scratch to be highly efficient and fully configurable
at runtime.

%package perl
Summary: Perl module for NGINX Unit
Group: System/Servers
Requires: unit

%description perl
Perl module for NGINX Unit

%package php
Summary: PHP module for NGINX Unit
Group: System/Servers
Requires: unit

%description php
PHP module for NGINX Unit

%package ruby
Summary: Ruby module for NGINX Unit
Group: System/Servers
Requires: unit

%description ruby
Ruby module for NGINX Unit

%prep
%setup

# "The memfd_create() system call first appeared in Linux 3.17"
sed -i -e 's/NXT_HAVE_MEMFD_CREATE/NO_&/' auto/shmem

%build
CONFIGURE_ARGS="
	--prefix=%_prefix
	--state=%_sharedstatedir/unit
	--libdir=%_libdir
	--user=_unit
	--group=_unit
	--control=unix:/var/run/unit/control.sock
	--pid=/var/run/unit/unit.pid
	--log=/var/log/unit/unit.log
	--tmp=/var/tmp
	--tests
	--openssl"

CFLAGS="%optflags" \
./configure $CONFIGURE_ARGS \
	--modules=%_libdir/unit/modules
%if_enabled perl
  ./configure perl
%endif
%if_enabled php
  ./configure php
%endif
%if_enabled ruby
  ./configure ruby
%endif
%make_build -s
%if_enabled devel
  %make_build -s build/libunit.a
%endif
%make_build -s tests
mv build build-nodebug

%if_enabled debug
  ./configure $CONFIGURE_ARGS \
	--modules=%_libdir/unit/debug-modules \
	--debug
  %if_enabled perl
    ./configure perl
  %endif
  %if_enabled php
    ./configure php
  %endif
  %if_enabled ruby
    ./configure ruby
  %endif
  %make_build -s
  %if_enabled devel
    %make_build -s build/libunit.a
  %endif
  mv build build-debug
%endif

sed -i -e s/daemon/start_daemon/ \
       -e s/killproc/stop_daemon/ \
	  pkg/rpm/rpmbuild/SOURCES/unit.init

sed -i -e 's!Environment=.*!EnvironmentFile=/etc/sysconfig/unit!' pkg/rpm/rpmbuild/SOURCES/unit.service

%install
ln -sf build-nodebug build
%makeinstall_std unitd-install libunit-install
%if_enabled perl
  %makeinstall_std perl-install
%endif
%if_enabled php
  %makeinstall_std php-install
%endif
%if_enabled ruby
  %makeinstall_std ruby-install
%endif
%if_enabled debug
  # Manual install to not overwrite nodebug files.
  install -m755 build-debug/unitd %buildroot%_sbindir/unitd-debug
  %if_enabled devel
    install -m755 build-debug/libunit.a %buildroot%_libdir/libunit-debug.a
  %endif
  mkdir -p %buildroot%_libdir/unit/debug-modules/
  %if_enabled perl
    install -m755 build-debug/perl.unit.so %buildroot%_libdir/unit/debug-modules/perl.unit.so
  %endif
  %if_enabled php
      install -m755 build-debug/php.unit.so %buildroot%_libdir/unit/debug-modules/php.unit.so
  %endif
  %if_enabled ruby
    install -m755 build-debug/ruby.unit.so %buildroot%_libdir/unit/debug-modules/ruby.unit.so
  %endif
%endif

install -pD -m644 pkg/rpm/rpmbuild/SOURCES/unit.logrotate %buildroot%_sysconfdir/logrotate.d/unit
install -pD -m644 pkg/rpm/rpmbuild/SOURCES/unit.service   %buildroot%systemd_unitdir/unit.service
install -pD -m755 pkg/rpm/rpmbuild/SOURCES/unit.init      %buildroot%_initdir/unit
install -pD -m755 pkg/rpm/rpmbuild/SOURCES/unit.sysconf   %buildroot%_sysconfdir/sysconfig/unit
mkdir -p %buildroot%_localstatedir/unit
mkdir -p %buildroot%_runtimedir/unit
mkdir -p %buildroot%_logdir/unit

ln NOTICE COPYRIGHT
ln pkg/rpm/rpmbuild/SOURCES/unit.example-ruby-app    ruby-app.ru
ln pkg/rpm/rpmbuild/SOURCES/unit.example-ruby-config ruby-unit.config
ln pkg/rpm/rpmbuild/SOURCES/unit.example-perl-app    perl-app.ru
ln pkg/rpm/rpmbuild/SOURCES/unit.example-perl-config perl-unit.config
ln pkg/rpm/rpmbuild/SOURCES/unit.example-php-app     php-app.ru
ln pkg/rpm/rpmbuild/SOURCES/unit.example-php-config  php-unit.config

%check
build/tests

%pre
/usr/sbin/groupadd -r -f _unit
/usr/sbin/useradd -r -g _unit -d /var/empty -s /dev/null -n -c "%summary" _unit >/dev/null 2>&1 ||:

%post
%post_service unit

%preun
%preun_service unit

%files
%doc CHANGES LICENSE README COPYRIGHT
%_sbindir/unitd*
%_initdir/unit
%_sysconfdir/sysconfig/unit
%systemd_unitdir/unit.service
%_sysconfdir/logrotate.d/unit
%_localstatedir/unit
%_runtimedir/unit
%_logdir/unit
%dir %_libdir/%name
%dir %_libdir/%name/*modules
%if_enabled devel
  %_libdir/libunit*.a
  %_includedir/nxt_*.h
%else
  %exclude %_libdir/libunit*.a
  %exclude %_includedir/nxt_*.h
%endif

%if_enabled perl
%files perl
%doc COPYRIGHT perl-app.ru perl-unit.config
%_libdir/unit/*modules/perl.unit.so
%endif
%if_enabled php
%files php
%doc COPYRIGHT php-app.ru php-unit.config
%_libdir/unit/*modules/php.unit.so
%endif
%if_enabled ruby
%files ruby
%doc COPYRIGHT ruby-app.ru ruby-unit.config
%_libdir/unit/*modules/ruby.unit.so
%endif

%changelog
* Sun Nov 29 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.21.0-alt3
- Add PHP module.

* Thu Nov 26 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.21.0-alt2
- Add Perl module.

* Tue Nov 24 2020 Vitaly Chikunov <vt@altlinux.org> 1.21.0-alt1
- Initial import of v1.21.0 (2020-11-19).
- Only ruby module is built.
