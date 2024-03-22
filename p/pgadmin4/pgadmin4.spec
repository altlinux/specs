%def_without   desktop

Name:          pgadmin4
Version:       8.3
Release:       alt2
Summary:       pgAdmin is the most popular and feature rich Open Source administration and development platform for PostgreSQL
License:       MIT
Group:         Networking/WWW
Url:           https://pgadmin.org
Vcs:           https://github.com/pgadmin-org/pgadmin4.git

Source:        %name-%version.tar
Source1:       pgadmin4.sysconfig
Source2:       pgadmin4.logrotate
Source3:       pgadmin4.service
Source4:       config_local.py
Source5:       pgadmin4.conf
Patch:         %name-%EVR.patch
Autoprov:      yes,nopython
%if_with       desktop
ExclusiveArch: x86_64
%else_without  desktop
BuildArch:     noarch
%endif
%add_debuginfo_skiplist %_libdir/%name-desktop
%add_debuginfo_skiplist %_libexecdir/%name
%add_findreq_skiplist %_libexecdir/**/*
%add_findprov_skiplist %_libexecdir/**/*
%add_findreq_skiplist %_libdir/%name-desktop/**/*
%add_findprov_skiplist %_libdir/%name-desktop/**/*
BuildRequires(pre): rpm-build-python3
# required for python web-server pre start
#
# required for nw.js
BuildRequires: pkgconfig(cups)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(atk)
BuildRequires: pkgconfig(cairo) >= 1.6
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xkbcommon)

Requires:      nginx
Requires:      python3(flask)
Requires:      python3(flask_gravatar)
Requires:      python3(flask_login)
Requires:      python3(flask_mail)
Requires:      python3(flask_migrate)
Requires:      python3(flask_sqlalchemy)
Requires:      python3(flask_wtf)
Requires:      python3(flask_compress)
Requires:      python3(flask_paranoid)
Requires:      python3(flask_babel)
Requires:      python3(flask_security)
Requires:      python3(flask_socketio)
Requires:      python3(wtforms)
Requires:      python3(passlib)
Requires:      python3(pytz)
Requires:      python3(speaklater)
Requires:      python3(sqlparse)
Requires:      python3(psutil)
Requires:      python3(psycopg)
Requires:      python3(dateutil)
Requires:      python3(sqlalchemy)
Requires:      python3(bcrypt)
Requires:      python3(cryptography)
Requires:      python3(sshtunnel)
Requires:      python3(ldap3)
Requires:      python3(gssapi)
Requires:      python3(eventlet)
Requires:      python3(httpagentparser)
Requires:      python3(user_agents)
Requires:      python3(authlib)
Requires:      python3(pyotp)
Requires:      python3(qrcode)
Requires:      python3(PIL)
Requires:      python3(boto3)
Requires:      python3(botocore)
Requires:      python3(urllib3)
Requires:      python3(azure.mgmt.core)
Requires:      python3(azure.mgmt.rdbms)
Requires:      python3(azure.mgmt.resource)
Requires:      python3(azure.common)
Requires:      python3(azure.mgmt.subscription)
Requires:      python3(azure.identity)
Requires:      python3(azure.mgmt.resource)
Requires:      python3(azure.common)
Requires:      python3(azure.mgmt.subscription)
Requires:      python3(googleapiclient)
Requires:      python3(google_auth_oauthlib)
Requires:      python3(werkzeug)
Requires:      python3(keyring)
Requires:      python3(typer)
Requires:      postgresql-common

%description
pgAdmin is the most popular and feature rich Open Source administration and
development platform for PostgreSQL, the most advanced Open Source database in
the world.

pgAdmin 4 is a rewrite of the popular pgAdmin3 management tool for the
PostgreSQL (http://www.postgresql.org) database.

In the following documentation and examples, $PGADMIN4_SRC/ is used to denote
the top-level directory of a copy of the pgAdmin source tree, either from a
tarball or a git checkout.

pgAdmin 4 is written as a web application in Python, using jQuery and Bootstrap
for the client side processing and UI. On the server side, Flask is being
utilised.

Although developed using web technologies, pgAdmin 4 can be deployed either on a
web server using a browser, or standalone on a workstation. The runtime/
subdirectory contains an NWjs based runtime application intended to allow this,
which will execute the Python server and display the UI.


%if_with       desktop
%package       -n pgadmin4-desktop
Summary:       Desktop part of pgAdmin4
Group:         Networking/WWW

Requires:      pgadmin4

%description   -n pgadmin4-desktop
Desktop part of pgAdmin4.
%endif


%prep
%setup
%autopatch -p1

%build
#cd web
#yarn bundle

%install
mkdir -p -- \
	%buildroot/%_libexecdir/%name \
	%buildroot/%_sysconfdir/%name \
	%buildroot/%_bindir/ \
	%buildroot/%_logdir/%name \
	%buildroot/%_localstatedir/%name \
	%buildroot/%_cachedir/%name/azure \
	%buildroot/%_cachedir/%name/kerberos \
	%buildroot/%_cachedir/%name/sessions \
	%buildroot/%_spooldir/%name/storage \
	%buildroot/%_sysconfdir/sysconfig \

cp -rp web/* %buildroot%_libexecdir/%name/
install -Dm0644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/%name
install -Dm0644 %SOURCE2 %buildroot%_logrotatedir/%name
install -Dm0644 %SOURCE3 %buildroot%_unitdir/%name.service
install -Dm0644 %SOURCE4 %buildroot%_sysconfdir/%name/settings.py
install -Dm0644 %SOURCE5 %buildroot%_sysconfdir/nginx/sites-available.d/%name.conf
ln -svr %buildroot%_sysconfdir/%name/settings.py %buildroot%_libexecdir/%name/config_local.py
rm -rf %buildroot%_libexecdir/%name/node_modules

%if_with       desktop
mkdir -p %buildroot/%_libdir/%name-desktop
cp -rp runtime/* %buildroot%_libdir/%name-desktop/
ln -svr %buildroot%_libdir/%name-desktop/node_modules/nw/nwjs/nw %buildroot%_bindir/%name-desktop
%endif

%pre
# Add the "pgadmin" user and group
getent group pgadmin >/dev/null || %_sbindir/groupadd -r pgadmin
getent passwd _pgadmin >/dev/null || \
   %_sbindir/useradd -r -g pgadmin -G pgadmin -M -d %_localstatedir/%name -s /bin/bash -c "PG Admin 4" _pgadmin
usermod -a -G pgadmin _nginx # add _nginx into pgadmin group

%preun
%preun_service %name

%post
%post_service %name

ln -sf %_sysconfdir/nginx/sites-available.d/%name.conf %_sysconfdir/nginx/sites-enabled.d/ 2>/dev/null


%files
%doc README*
%_libexecdir/%name
%_unitdir/%name.service
%config(noreplace) %_sysconfdir/%name
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %_sysconfdir/nginx/sites-available.d/%name.conf
%attr(770,_pgadmin,pgadmin) %_sysconfdir/sysconfig/%name
%dir %attr(770,_pgadmin,pgadmin) %_cachedir/%name
%dir %attr(770,_pgadmin,pgadmin) %_cachedir/%name/azure
%dir %attr(770,_pgadmin,pgadmin) %_cachedir/%name/kerberos
%dir %attr(770,_pgadmin,pgadmin) %_cachedir/%name/sessions
%dir %attr(770,_pgadmin,pgadmin) %_spooldir/%name
%dir %attr(770,_pgadmin,pgadmin) %_spooldir/%name/storage
%dir %attr(770,_pgadmin,pgadmin) %_localstatedir/%name
%dir %attr(770,_pgadmin,pgadmin) %_logdir/%name

%if_with       desktop
%files         -n pgadmin4-desktop
%doc README*
%_libdir/%name-desktop
%_bindir/%name-desktop
%endif


%changelog
* Fri Mar 22 2024 Pavel Vasenkov <pav@altlinux.org> 8.3-alt2
- Fixed packages dependencies (Closes: #49747)

* Fri Mar 01 2024 Pavel Skrylev <majioa@altlinux.org> 8.3-alt1
- First build v8.3 to Sisyphus
