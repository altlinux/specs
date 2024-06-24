%define rcver rc21

Name: boa
Version: 0.94.14
Release: alt0.%rcver.2

Summary: Small and fast web server
License: GPL-1.0+
Group: System/Servers

Url: http://www.boa.org/
Source0: http://www.boa.org/%name-%version%rcver.tar.gz
Source1: boa.init
Source2: boa.sysconfig

BuildRequires: rpm-macros-webserver-common
BuildRequires: flex
BuildRequires: bison

Requires: webserver-common
Provides: webserver

%define boa_user  _boa
%define boa_group _boa
%define boa_home  %_localstatedir/boa

%description
A high speed, lightweight web server (HTTP protocol).
Based on direct use of the select(2) system call, it
internally multiplexes all connections without forking,
for maximum speed and minimum system resource use.

%prep
%setup -n %name-%version%rcver

%build
%configure
%make_build CFLAGS="%optflags"

# tune up the defaults for unprivileged-by-default setup
sed -i -r \
	-e 's,/usr/local/boa,%_sysconfdir/boa,' \
	-e 's,^(Port) 80$,\1 8080,' \
	-e 's,^(User) nobody$,\1 %boa_user,' \
	-e 's,^(Group) nogroup$,\1 %boa_group,' \
	-e 's,^#(ServerAdmin) ,\1 ,' \
	-e 's,^# (PidFile) /var/run/boa.pid,\1 %_runtimedir/boa.pid,' \
	-e 's,^#(VerboseCGILogs)$,\1,' \
	-e 's,^(#VHostRoot) .*$,\1 %webserver_vhostdir,' \
	-e 's,^(DocumentRoot) .*$,\1 %webserver_htdocsdir,' \
	-e 's,^(DirectoryMaker) /usr/lib/,\1 %_libdir/,' \
	-e 's,^# (DirectoryCache) /var/spool/boa,#\1 %_spooldir/boa,' \
	-e 's,^#AddType .* cgi$,& pl,' \
	-e 's,^(Alias /doc) /usr/doc$,#\1 %_defaultdocdir,' \
	-e 's,^(ScriptAlias /cgi-bin/) .*$,#\1 %webserver_cgibindir/,' \
	-e 's,(nothing for) user,\1 the rest,' \
	examples/boa.conf

%install
install -pDm755 {src,%buildroot%_sbindir}/boa
install -pDm755 {src,%buildroot%_libdir/boa}/boa_indexer

install -pDm644 docs/boa.8 %buildroot%_man8dir/boa.8

install -pDm644 examples/boa.conf %buildroot%_sysconfdir/boa/boa.conf
install -pDm644 contrib/rpm/boa.logrotate %buildroot%_logrotatedir/boa

install -pDm755 %SOURCE1 %buildroot%_initdir/boa
install -pDm644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/boa

sed -i 's,/var/spool/boa,%_spooldir/boa,' %buildroot%_sysconfdir/sysconfig/boa

mkdir -p %buildroot{%_logdir/boa,%_spooldir/boa}
mkdir -p %buildroot{%webserver_htdocsdir,%webserver_cgibindir}

%pre
groupadd -r -f %boa_group ||:
useradd -g %boa_group -c 'boa webserver' \
        -d %boa_home -s /dev/null -r %boa_user >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc docs/*.{texi,png} contrib/*
%_man8dir/*
%_sbindir/boa
%_libdir/boa/boa_indexer
%dir %_libdir/boa
%dir %_sysconfdir/boa
%config(noreplace) %_initdir/boa
%config(noreplace) %_sysconfdir/boa/boa.conf
%config(noreplace) %_sysconfdir/sysconfig/boa
%config(noreplace) %_logrotatedir/boa
%dir %attr(0770,root,%boa_group) %_spooldir/boa
# see also Secure Packaging Policy, no easy way for webmaster group
%dir %attr(0770,root,%boa_group) %_logdir/boa

%changelog
* Tue Jun 25 2024 Michael Shigorin <mike@altlinux.org> 0.94.14-alt0.rc21.2
- privsep out-of-box (_boa user/group according to Pseudo User Policy)
- proper default config (with proper DirectoryMaker while at that)
- move to webserver-common infrastructure
- proper service handling
- disable CGI by default

* Mon Jun 24 2024 Michael Shigorin <mike@altlinux.org> 0.94.14-alt0.rc21.1
- initial build for ALT Sisyphus (based on Rosa/Cooker package)
  + major spec cleanup (starting with rpmcs)
  + clarified License:
  + proper initscript

