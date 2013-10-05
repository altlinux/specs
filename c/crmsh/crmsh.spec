%global gname haclient
%global uname hacluster

Name: crmsh
Summary: Pacemaker command line interface
Version: 1.2.6
Release: alt1
License: GPL-2.0+
Url: http://savannah.nongnu.org/projects/crmsh
Group: System/Configuration/Other
Source0: %name-%version.tar


# Automatically added by buildreq on Wed Aug 14 2013
# optimized out: asciidoc docbook-dtds docbook-style-xsl libgpg-error openssh-clients openssh-common pkg-config python-base python-devel python-modules python-modules-compiler python-modules-encodings xml-common xml-utils xsltproc
BuildRequires: asciidoc-a2x libcluster-glue-devel libpacemaker-devel time

Requires: pacemaker-cli

%description
crm shell, a Pacemaker command line interface.

Pacemaker is an advanced, scalable High-Availability cluster resource
manager for Heartbeat and/or Corosync.

%prep
%setup

%build
./autogen.sh
%configure \
	--localstatedir=%_var \
	--with-package-name=%name \
	--with-version=%version-%release \
	--docdir=%_defaultdocdir/%version-%release

%make_build

%install
%makeinstall_std


%files
%_datadir/crmsh
%_sbindir/crm
%python_sitelibdir/crmsh

%_man8dir/*
%_defaultdocdir/%version-%release
%dir %attr (770, %uname, %gname) %_var/cache/crm

%exclude %_datadir/crmsh/tests

%changelog
* Sat Oct 05 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.6-alt1
- New version

* Tue Aug 13 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.5-alt1
- Build for ALT
