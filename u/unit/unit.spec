# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,unresolved=normal
%global optflags_lto %optflags_lto -ffat-lto-objects

%def_enable perl
%def_enable python
%def_enable php
%def_enable ruby
%def_disable devel

Name: unit
Version: 1.29.0
Release: alt1

Summary: NGINX Unit - Web Application Server
License: Apache-2.0
Group: System/Servers

Url: https://unit.nginx.org/
Vcs: https://github.com/nginx/unit

Source: %name-%version.tar

BuildRequires: libssl-devel
BuildRequires: libpcre-devel
%{?_enable_ruby:BuildRequires: ruby libruby-devel}
%{?_enable_perl:BuildRequires: perl-devel perl-base}
%{?_enable_php:BuildRequires: php8.1 php8.1-devel php-base}
%{?_enable_python:BuildRequires: python3-devel}

Provides: nginx-unit = %EVR
Requires(post): service >= 0.5.33

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

%package checkinstall
Summary: Checkinstall test for %name
Group: Development/Other
Requires: %name = %EVR
Requires: logrotate
Requires: man-db
Requires: systemd-analyze

%description checkinstall
%summary.

%prep
%setup

# "The memfd_create() system call first appeared in Linux 3.17"
sed -i -e 's/NXT_HAVE_MEMFD_CREATE/NO_&/' auto/shmem

sed -i 's!/var/run/!/run/!' pkg/rpm/rpmbuild/SOURCES/unit.logrotate

%build
%add_optflags $(getconf LFS_CFLAGS)
# Test compilation passes with the following options:
#   %%define optflags_lto %nil
#   %%add_optflags -fanalyzer -Wno-analyzer-null-argument -Wno-analyzer-null-dereference -Wno-analyzer-malloc-leak -Wno-analyzer-use-of-uninitialized-value
# Last one is certainly worrisome.

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
	--control=unix:/run/unit/control.sock
	--pid=/run/unit/unit.pid
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
  ./configure php --config=/usr/bin/php-config8.1
%endif
%if_enabled ruby
  ./configure ruby
%endif
%make_build
%if_enabled devel
  %make_build build/libunit.a
%endif
%make_build tests

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

install -pD tools/unitc %buildroot%_bindir/unitc
install -pD -m644 pkg/rpm/rpmbuild/SOURCES/unit.logrotate %buildroot%_sysconfdir/logrotate.d/unit
install -pD -m644 .gear/unit.service %buildroot%systemd_unitdir/unit.service
install -pD -m755 .gear/unit.init    %buildroot%_initdir/unit
mkdir -p %buildroot%_localstatedir/unit
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

%check
# unitc does not pass shellcheck
bash -n %buildroot%_bindir/unitc
bash -n %buildroot%_initdir/unit
build/tests

%pre checkinstall
set -ex
# systemd-analyze better works in non-'/'.
cd
systemd-analyze verify unit.service
logrotate %_sysconfdir/logrotate.d/unit

%pre
/usr/sbin/groupadd -r -f _unit
/usr/sbin/useradd -r -g _unit -d /var/empty -s /dev/null -N -c "%summary" _unit >/dev/null 2>&1 ||:

%post
%post_service_posttrans_restart unit

%preun
%preun_service unit

%files
%doc CHANGES LICENSE README.md COPYRIGHT SECURITY.txt
%_man8dir/*.8*
%_sbindir/unitd
%_bindir/unitc
%_initdir/unit
%systemd_unitdir/unit.service
%config(noreplace) %_sysconfdir/logrotate.d/unit
%dir %_localstatedir/unit
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

%files checkinstall

%changelog
* Sat Dec 17 2022 Vitaly Chikunov <vt@altlinux.org> 1.29.0-alt1
- Update to 1.29.0 (2022-12-15), enable cgroup2 support, install unitc.

* Tue Oct 04 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.28.0-alt2
- Switch to PHP 8.1

* Tue Sep 13 2022 Vitaly Chikunov <vt@altlinux.org> 1.28.0-alt1
- Update to 1.28.0 (2022-09-13).

* Fri Jul 29 2022 Vitaly Chikunov <vt@altlinux.org> 1.27.0-alt2
- Move /var/run -> /run for control.sock and unit.pid (ALT#43362).
- /etc/sysconfig/unit is not installed but read, because there are no
  options by default anymore (they are compiled in).

* Fri Jun 03 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.27.0-alt1
- Update to 1.27.0 (2022-06-02).

* Mon Dec 20 2021 Vitaly Chikunov <vt@altlinux.org> 1.26.1-alt3
- Restore user/group creation that accidentally removed on previous release.

* Sun Dec 19 2021 Vitaly Chikunov <vt@altlinux.org> 1.26.1-alt2
- Restart in posttrans using new service-0.5.33 features.

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
