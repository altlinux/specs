%define _unpackaged_files_terminate_build 1

Name:    conserver
Version: 8.2.2
Release: alt2

Summary:  Serial console server daemon/client
License: BSD-3-Clause

Group:   System/Servers
URL:     http://www.conserver.com/

Source:  %{name}-%{version}.tar
Source1: conserver.init
Source2: conserver.service

Patch:  certificate-auth.patch
Patch1: conserver-no-exampledir.patch
Patch2: conserver-gssapi.patch

BuildRequires: libssl-devel
BuildRequires: libpam-devel
BuildRequires: libkrb5-devel
BuildRequires: libfreeipmi-devel

%description
Conserver is an application that allows multiple users to watch a
serial console at the same time.  It can log the data, allows users to
take write-access of a console (one at a time), and has a variety of
bells and whistles to accentuate that basic functionality.

%package client
Summary: Serial console client
Group: Communications

%description client
This is the client package needed to interact with a Conserver daemon.

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1

%build

# define the name of the machine on which the main conserver
# daemon will be running if you don't want to use the default
# hostname (console)
%define master console

%autoreconf
%configure \
	--with-master=%{master} \
	--with-ipv6 \
	--with-openssl \
	--with-pam \
	--with-freeipmi \
	--with-gssapi \
	--with-striprealm \
	--with-port=782

%make

%install
%makeinstall_std

# put commented copies of the sample configure files in the
# system configuration directory
install -d -pm 755 %buildroot%_sysconfdir

sed -e 's/^/#/' \
  < conserver.cf/conserver.cf \
  > %buildroot%_sysconfdir/conserver.cf

sed -e 's/^/#/' \
  < conserver.cf/conserver.passwd \
  > %buildroot%_sysconfdir/conserver.passwd

# Init scripts.
install -d -pm 755 %buildroot%_initdir
install -D -pm 755 %SOURCE1 %buildroot%_initdir/conserver

install -d -pm 755 %buildroot%_unitdir
install -D -pm 644 %SOURCE2 %buildroot%_unitdir/converver.service

%post
%post_service conserver

# make sure /etc/services has a conserver entry
if ! egrep conserver /etc/services > /dev/null 2>&1 ; then
  echo "console		782/tcp		conserver" >> /etc/services
fi

%preun
%preun_service conserver

%files
%doc CHANGES FAQ INSTALL README conserver.cf
%config(noreplace) %{_sysconfdir}/conserver.cf
%config(noreplace) %{_sysconfdir}/conserver.passwd
%_initdir/*
%_unitdir/*
%_sbindir/conserver
%_libdir/conserver/convert
%_man5dir/*
%_man8dir/*

%files client
%_bindir/console
%_man1dir/console.1*

%changelog
* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 8.2.2-alt2
- NMU: Fix license.

* Thu Sep 06 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 8.2.2-alt1
- Updated to upstream version 8.2.2.

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 8.1.16-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 8.1.16-alt1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Tue Nov 17 2009 Andriy Stepanov <stanv@altlinux.ru> 8.1.16-alt1
- ALT: initial build
