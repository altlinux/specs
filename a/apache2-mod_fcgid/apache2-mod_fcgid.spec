Name: apache2-mod_fcgid
Summary: Apache2 module for high-performance server-side scripting 

Version: 2.3.9
Release: alt2
License: %asl
Group: System/Servers
URL: https://httpd.apache.org/mod_fcgid/

Source0: mod_fcgid-%{version}.tar.gz
Source1: %name-fcgid.conf
Source2: %name-fcgid.load
Source3: %name.init

Provides: mod_fcgid = %version-%release
PreReq: apache2

BuildRequires: rpm-build-licenses

BuildPreReq: apache2-devel libaprutil1-devel libapr1-devel

%description
mod_fcgid is a binary-compatible alternative to the Apache module mod_fastcgi.
mod_fcgid has a new process management strategy, which concentrates on reducing
the number of fastcgi servers, and kicking out corrupt fastcgi servers as soon
as possible.

%prep
%setup -q -n mod_fcgid-%{version}

%build
APXS="/usr/bin/apxs2" ./configure.apxs
%__make top_dir=%apache2_libdir

%install
%__make \
  top_dir=%apache2_libdir \
  DESTDIR=%buildroot \
  MKINSTALLDIRS="%__mkdir_p" \
  install

# we don't really want to install this in the system Apache modules dir
%__mkdir_p %buildroot/%apache2_moduledir
%__mkdir_p %buildroot%apache2_confdir/mods-available/

%__mkdir_p %buildroot%_initdir
%__sed -e 's|@apache2_user@|%apache2_user|' -e 's|@apache2_group@|%apache2_group|' < %SOURCE3 > %buildroot%_initdir/mod_fcgid

install -m 644 %SOURCE1 %buildroot%apache2_confdir/mods-available/fcgid.conf
install -m 644 %SOURCE2 %buildroot%apache2_confdir/mods-available/fcgid.load

#install -d -m 755 %buildroot%_localstatedir/run/mod_fcgid/fcgid_sock
install -d -m 755 %buildroot%_runtimedir/mod_fcgid/fcgid_sock

rm -rf %buildroot%webserver_datadir/apache2

%post
%post_service mod_fcgid

%preun
%preun_service mod_fcgid

%files
%doc docs/manual/mod/*
%doc CHANGES-FCGID LICENSE-FCGID NOTICE-FCGID README-FCGID STATUS-FCGID

%apache2_moduledir/mod_fcgid.so
%dir %attr(0755,%apache2_user,%apache2_group) %_runtimedir/mod_fcgid
%dir %attr(0755,%apache2_user,%apache2_group) %_runtimedir/mod_fcgid/fcgid_sock
%apache2_confdir/mods-available/*

%attr(0755,root,root) %_initdir/mod_fcgid

%changelog
* Mon Oct 24 2016 Sergey Y. Afonin <asy@altlinux.ru> 2.3.9-alt2
- Added init script for check subdirectories in %%_runtimedir
- Changed configuration for new directives (from git of misha@altlinux)
- Added some files to %%doc

* Mon Oct 24 2016 Sergey Y. Afonin <asy@altlinux.ru> 2.3.9-alt1
- New version (built for Apache 2.4)
- Changed "mod_fcgid.c" to "mod_fastcgi" in fcgid.conf (ALT #27554)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.2-alt2.qa1
- NMU: rebuilt for debuginfo.

* Tue Sep 02 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.2-alt2
- Fixed for new macroses from rpm-macros-apache2

* Thu Jan 24 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.2-alt1
- Initial release

