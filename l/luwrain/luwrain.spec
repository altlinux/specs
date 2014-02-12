%define _luwraindir /usr/lib/luwrain

Name: luwrain
Version: 0.2.2
Release: alt1
Summary: The accessible environment for blind persons
Url: http://luwrain.org/
Group: Accessibility
License: GPL v.3
Packager: Michael Pozhidaev <msp@altlinux.ru>
BuildArch: noarch

Requires: java-openjdk
BuildRequires: java-1.7.0-openjdk-devel ant 
BuildRequires: dbus-java javamail rome apache-poi jdom mysql-connector-java
BuildRequires: rpm-build-java

Source: %name-%version.tar.gz
Source1: %name-data-%version.tar.gz

%description
With Luwrain blind and visual impaired persons get one more way to be
involved in the incredible world of information technologies.  Luwrain
doesn't take a lot of time to study and aims to be useful on laptops
as well as on usual desktop computers.  You can treat this project as
one more solution for everybody who needs reliable and accessible
companion for various types of work.  The product is designed as new
platform for creating speech-enabled applications with set of standard
tools for easy web access, mail and news reading , etc.

%prep
%setup -q
%build
%__mkdir lib

%__cp %_javadir/rome.jar ./lib
%__cp -r %_javadir/dbus-java/. lib
%__cp -r %_javadir/javamail/. lib
%__cp -r %_javadir/poi/. lib
%__cp -r %_javadir/jdom.jar lib
%__cp %_javadir/mysql-connector* lib

LANG=ru_RU.UTF-8 ant

%install
%__mkdir -p %buildroot%_sysconfdir/profile.d
echo '#!/bin/sh' > %buildroot%_sysconfdir/profile.d/%name.sh
echo 'export LUWRAIN_DIR='%_luwraindir > %buildroot%_sysconfdir/profile.d/%name.sh
%__chmod 755 %buildroot%_sysconfdir/profile.d/%name.sh 
%__install -d -m 755 %buildroot%_luwraindir
%__cp -r conf conf-local-default jar lib sql %buildroot%_luwraindir
%__install -pD -m 755 ./scripts/%name %buildroot%_bindir/%name
%__cp %SOURCE1 luwrain-data.tar.gz
tar xf luwrain-data.tar.gz
%__cp -r luwrain-data-%version %buildroot%_luwraindir/data

%files
%_sysconfdir/profile.d/*
%_bindir/%name
%doc AUTHOR LICENSE README
%_luwraindir

%changelog
* Wed Feb 12 2014 Michael Pozhidaev <msp@altlinux.ru> 0.2.2-alt1
- New version: 0.2.2

* Tue Oct 29 2013 Michael Pozhidaev <msp@altlinux.ru> 0.2.1-alt1
- Initial package

