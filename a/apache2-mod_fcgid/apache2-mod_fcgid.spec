Name: apache2-mod_fcgid
Summary: Apache2 module for high-performance server-side scripting 
Version: 2.2
Release: alt2
License: GPL
Group: System/Servers
URL: http://fastcgi.coremail.cn/
Packager: Evgeny Sinelnikov <sin@altlinux.ru>
Source0: http://dl.sf.net/mod-fcgid/mod_fcgid.%{version}.tar.gz
Source1: fcgid.conf
Source2: fcgid.load
Source3: http://fastcgi.coremail.cn/doc.htm
Source4: http://fastcgi.coremail.cn/configuration.htm
Patch0: mod_fcgid.2.1-docurls.patch
BuildPreReq: apache2-devel,libaprutil1-devel,libapr1-devel
Provides: mod_fcgid = %version-%release
PreReq: apache2

%description
mod_fcgid is a binary-compatible alternative to the Apache module mod_fastcgi.
mod_fcgid has a new process management strategy, which concentrates on reducing
the number of fastcgi servers, and kicking out corrupt fastcgi servers as soon
as possible.

%prep
%setup -q -n mod_fcgid.%{version}
%__cp -p %SOURCE3 directives.htm
%__cp -p %SOURCE4 configuration.htm
%patch -p1
%__sed -i -e 's/\r$//' directives.htm configuration.htm

%build
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
install -m 644 %SOURCE1 %buildroot%apache2_confdir/mods-available/
install -m 644 %SOURCE2 %buildroot%apache2_confdir/mods-available/
install -d -m 755 %buildroot%_localstatedir/run/mod_fcgid/fcgid_sock

%files
%doc ChangeLog AUTHOR COPYING configuration.htm directives.htm
%apache2_moduledir/mod_fcgid.so
%dir %attr(0755,%apache2_user,%apache2_group) %_localstatedir/run/mod_fcgid
%dir %attr(0755,%apache2_user,%apache2_group) %_localstatedir/run/mod_fcgid/fcgid_sock
%apache2_confdir/*

%changelog
* Tue Sep 02 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.2-alt2
- Fixed for new macroses from rpm-macros-apache2

* Thu Jan 24 2008 Evgeny Sinelnikov <sin@altlinux.ru> 2.2-alt1
- Initial release

