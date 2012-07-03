Summary: DB-Based Kannel Box for message queueing
Name: sqlbox
Version: 0.7.2
Release: alt1.2
License: Kannel
Group: Communications
Url: http://www.kannel.org/~aguerrieri/

Packager: Michael Bochkaryov <misha@altlinux.ru>

Source: sqlbox-%version.tar.bz2

Patch1: alt-asneeded.patch

BuildPreReq: autoconf_2.60 automake_1.9 libssl-devel zlib-devel

# Automatically added by buildreq on Sat Aug 01 2009
BuildRequires: ImageMagick-tools docbook-style-dsssl gcc-c++ gcc-fortran glibc-devel-static jadetex kannel-devel libMySQL-devel libpam-devel libpcre-devel libsqlite3-devel libxml2-devel postgresql-devel transfig

PreReq: kannel

%description
Sqlbox is a special Kannel box that sits between bearerbox and smsbox and uses
a database queue to store and forward messages.

Messages are queued on a configurable table (defaults to send_sms) and moved to
another table (defaults to sent_sms) afterwards.

You can also manually insert messages into the send_sms table and they will be sent
and moved to the sent_sms table as well. This allows for fast and easy injection
of large amounts of messages into Kannel.

%prep

%setup
%patch1

%build
./bootstrap
%configure
%make

%install

%makeinstall
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_var/log/kannel/
mkdir -p %buildroot%_var/spool/kannel/

install -D -m 0640 example/sqlbox.conf.example %buildroot%_sysconfdir/kannel/sqlbox.conf

strip %buildroot%_sbindir/sqlbox


%files
%doc AUTHORS COPYING ChangeLog NEWS README UPGRADE
%attr(0640, kannel, kannel) %config(noreplace) %_sysconfdir/kannel/sqlbox.conf
%_sbindir/*

%changelog
* Thu Apr 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.2
- Fixed build

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt1.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Sat Aug 01 2009 Michael Bochkaryov <misha@altlinux.ru> 0.7.2-alt1
- Initial build for Sisyphus

