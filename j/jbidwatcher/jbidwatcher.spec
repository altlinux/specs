Name: jbidwatcher
Version: 2.1.6
Release: alt1

Summary: Free eBay sniping, bidding & monitoring
License: Based on Creative Commons BY-NC-SA license
Group: Networking/Other
Url: http://www.jbidwatcher.com/

Source: %name-%version.tar

Source1: %name.sh

BuildArch: noarch

BuildRequires(pre): /proc rpm-build-java
BuildRequires: ant git

%description
JBidWatcher is a Java-based application allowing you to monitor auctions you're
not part of, submit bids, snipe (bid at the last moment), and otherwise track
your auction-site experience

%prep
%setup

%build
%ant jar

%install
install -d -m 755 %buildroot%_javadir
install -m 644 JBidwatcher-%version.jar %buildroot%_javadir/
ln -s JBidwatcher-%version.jar %buildroot%_javadir/JBidwatcher.jar
install -d -m 755 %buildroot%_bindir
install -m 755 %SOURCE1 %buildroot%_bindir/%name

%files
%doc COPYING.html
%_bindir/*
%_javadir/*

%changelog
* Wed Dec 28 2011 Timur Aitov <timonbl4@altlinux.org> 2.1.6-alt1
- New version

* Tue Apr 26 2011 Timur Aitov <timonbl4@altlinux.org> 2.1.5-alt1
- New version

* Wed Mar 02 2011 Timur Aitov <timonbl4@altlinux.org> 2.1.4-alt1
- New version

* Fri Feb 04 2011 Timur Aitov <timonbl4@altlinux.org> 2.1.3-alt3
- Mod spec file

* Fri Feb 04 2011 Timur Aitov <timonbl4@altlinux.org> 2.1.3-alt2
- Remove Requires: java-1.6.0-sun

* Thu Feb 03 2011 Timur Aitov <timonbl4@altlinux.org> 2.1.3-alt1
- initial build for ALT

