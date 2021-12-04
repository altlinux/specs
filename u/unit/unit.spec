# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%global optflags_lto %optflags_lto -ffat-lto-objects

%def_enable perl
%def_enable python
%def_enable php
%def_enable ruby
%def_disable devel

Name: unit
Version: 1.26.1
Release: alt1

Summary: NGINX Unit - Web Application Server
License: Apache-2.0
Group: System/Servers

Url: https://unit.nginx.org/
Vcs: http://hg.nginx.org/unit/
# Mirror Vcs: https://github.com/nginx/unit

Source: %name-%version.tar

%define restart_flag /var/run/%name.restart

BuildRequires: libssl-devel
BuildRequires: libpcre-devel
%{?_enable_ruby:BuildRequires: ruby libruby-devel}
%{?_enable_perl:BuildRequires: perl-devel perl-base}
%{?_enable_php:BuildRequires: php7 php7-devel php-base}
%{?_enable_python:BuildRequires: python3-devel}

Provides: nginx-unit = %EVR

%description
NGINX Unit is a polyglot app server, a reverse proxy, and a static
file server, available for Unix-like systems. It was built by nginx
team members from scratch to be highly efficient and fully configurable
at runtime.

%package perl
Summary: Perl module for NGINX Unit
Group: System/Servers
Requires: unit = %EVR

%description perl
Perl module for NGINX Unit

%package python3
Summary: Python module for NGINX Unit
Group: System/Servers
Requires: unit = %EVR

%description python3
Python module for NGINX Unit

%package php
Summary: PHP module for NGINX Unit
Group: System/Servers
Requires: unit = %EVR

%description php
PHP module for NGINX Unit

%package ruby
Summary: Ruby module for NGINX Unit
Group: System/Servers
Requires: unit = %EVR

%description ruby
Ruby module for NGINX Unit

%prep
%setup

# "The memfd_create() system call first appeared in Linux 3.17"
sed -i -e 's/NXT_HAVE_MEMFD_CREATE/NO_&/' auto/shmem

%build
%ifarch %e2k
# lcc 1.25.12 found some perl/php interpreter header glitches missed by gcc
%add_optflags -Wno-error=unused-function -Wno-error=ignored-qualifiers
%endif

CONFIGURE_ARGS="
	--prefix=%_prefix
	--state=%_localstatedir/unit
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
%if_enabled python
  ./configure python --config=python3-config
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

sed -i -e 's!Environment=.*!EnvironmentFile=/etc/sysconfig/unit!' pkg/rpm/rpmbuild/SOURCES/unit.service

%install
%makeinstall_std unitd-install libunit-install
%if_enabled perl
  %makeinstall_std perl-install
%endif
%if_enabled python
  %makeinstall_std python3-install
%endif
%if_enabled php
  %makeinstall_std php-install
%endif
%if_enabled ruby
  %makeinstall_std ruby-install
%endif

install -pD -m644 pkg/rpm/rpmbuild/SOURCES/unit.logrotate %buildroot%_sysconfdir/logrotate.d/unit
install -pD -m644 pkg/rpm/rpmbuild/SOURCES/unit.service   %buildroot%systemd_unitdir/unit.service
install -pD -m755 .gear/unit.init    %buildroot%_initdir/unit
install -pD -m755 .gear/unit.sysconf %buildroot%_sysconfdir/sysconfig/unit
mkdir -p %buildroot%_localstatedir/unit
mkdir -p %buildroot%_runtimedir/unit
mkdir -p %buildroot%_logdir/unit

ln NOTICE COPYRIGHT
ln pkg/rpm/rpmbuild/SOURCES/unit.example-ruby-app    ruby-app.ru
ln pkg/rpm/rpmbuild/SOURCES/unit.example-ruby-config ruby-unit.config
ln pkg/rpm/rpmbuild/SOURCES/unit.example-perl-app    perl-app.ru
ln pkg/rpm/rpmbuild/SOURCES/unit.example-perl-config perl-unit.config
ln pkg/rpm/rpmbuild/SOURCES/unit.example-python-app    python-app.ru
ln pkg/rpm/rpmbuild/SOURCES/unit.example-python-config python-unit.config
ln pkg/rpm/rpmbuild/SOURCES/unit.example-php-app     php-app.ru
ln pkg/rpm/rpmbuild/SOURCES/unit.example-php-config  php-unit.config

# Install filetrigger.
mkdir -p %buildroot%_rpmlibdir
cat > %buildroot%_rpmlibdir/%name.filetrigger <<'EOF'
#!/bin/sh
LC_ALL=C grep -Fqs %_sbindir/unitd &&
        [ -f %restart_flag ] ||
        exit 0
rm -f %restart_flag
service %name start
exit 0
EOF
chmod 0755 %buildroot%_rpmlibdir/%name.filetrigger

%check
build/tests

%pre
/usr/sbin/groupadd -r -f _unit
/usr/sbin/useradd -r -g _unit -d /var/empty -s /dev/null -N -c "%summary" _unit >/dev/null 2>&1 ||:

rm -f %restart_flag
if [ $1 -gt 1 ]; then
	SYSTEMCTL=systemctl
	if sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
		$SYSTEMCTL is-active %name.service >/dev/null 2>&1 &&
		$SYSTEMCTL stop %name.service &&
		touch %restart_flag ||:
        else
		%_initdir/%name status >/dev/null 2>&1 &&
		%_initdir/%name stop &&
		touch %restart_flag ||:
	fi
fi

%post
if [ $1 -eq 1 ]; then
	chkconfig --add %name
else
	chkconfig %name resetpriorities
	SYSTEMCTL=systemctl
	sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1 &&
	"$SYSTEMCTL" daemon-reload ||:
fi

%preun
%preun_service unit

%files
%doc CHANGES LICENSE README COPYRIGHT
%_man8dir/*.8*
%_sbindir/unitd
%_initdir/unit
%systemd_unitdir/unit.service
%_rpmlibdir/%name.filetrigger
%config(noreplace) %_sysconfdir/sysconfig/unit
%config(noreplace) %_sysconfdir/logrotate.d/unit
%dir %_localstatedir/unit
%dir %_runtimedir/unit
%dir %_logdir/unit
%dir %_libdir/unit
%dir %_libdir/unit/modules
%if_enabled devel
  %_libdir/libunit.a
  %_includedir/nxt_*.h
%else
  %exclude %_libdir/libunit.a
  %exclude %_includedir/nxt_*.h
%endif

%if_enabled perl
%files perl
%doc COPYRIGHT perl-app.ru perl-unit.config
%_libdir/unit/modules/perl.unit.so
%endif

%if_enabled python
%files python3
%doc COPYRIGHT python-app.ru python-unit.config
%_libdir/unit/modules/python3.unit.so
%endif

%if_enabled php
%files php
%doc COPYRIGHT php-app.ru php-unit.config
%_libdir/unit/modules/php.unit.so
%endif

%if_enabled ruby
%files ruby
%doc COPYRIGHT ruby-app.ru ruby-unit.config
%_libdir/unit/modules/ruby.unit.so
%endif

%changelog
* Sat Dec 04 2021 Vitaly Chikunov <vt@altlinux.org> 1.26.1-alt1
- Update to 1.26.1 (2021-12-02).
- Restart unit from filetrigger (closes: #41487).

* Thu Nov 18 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.26.0-alt1
- Update to 1.26.0-1 (2021-11-18).
- Add condstop to unit.init.

* Tue Oct 26 2021 Anton Farygin <rider@altlinux.ru> 1.25.0-alt3
- added python3 module

* Wed Oct 13 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.25.0-alt2
- FTBFS: build with glibc 2.34

* Tue Aug 24 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.25.0-alt1
- Update to 1.25.0 (2021-08-19).

* Mon May 31 2021 Andrew A. Vasilyev <andy@altlinux.org> 1.24.0-alt1
- Update to 1.24.0 (2021-05-27).

* Sat Apr 10 2021 Michael Shigorin <mike@altlinux.org> 1.22.0-alt2
- E2K: workaround interpreter header glitches found by lcc
- Minor spec cleanup

* Sun Feb 07 2021 Vitaly Chikunov <vt@altlinux.org> 1.22.0-alt1
- Update to 1.22.0 (2021-02-04).

* Sun Nov 29 2020 Vitaly Chikunov <vt@altlinux.org> 1.21.0-alt4
- Do not build unit-debug binaries and debug-modules.

* Sun Nov 29 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.21.0-alt3
- Add PHP module.

* Thu Nov 26 2020 Andrew A. Vasilyev <andy@altlinux.org> 1.21.0-alt2
- Add Perl module.

* Tue Nov 24 2020 Vitaly Chikunov <vt@altlinux.org> 1.21.0-alt1
- Initial import of v1.21.0 (2020-11-19).
- Only ruby module is built.
