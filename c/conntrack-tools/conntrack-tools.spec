Name:           conntrack-tools
Version:        0.9.15
Release: 	alt1
Summary:        Tool to manipulate netfilter connection tracking table

Group:          System/Kernel and hardware
License:        GPL
URL:            http://netfilter.org
Source0:        http://netfilter.org/projects/conntrack-tools/files/%name-%version.tar

# Automatically added by buildreq on Sat Oct 30 2010
BuildRequires: flex libnetfilter_conntrack-devel

%description
%name  is  used to search, list, inspect and maintain the netfilter
connection tracking subsystem of the Linux kernel.
Using conntrack , you can dump a list of all (or a filtered selection  of)
currently  tracked  connections, delete connections from the state table, 
and even add new ones.
In  addition,  you  can  also  monitor connection tracking events, e.g. 
show an event message (one line) per newly established connection.

%prep
%setup

%build
%autoreconf -fisv
%configure
%make_build

%install
make install DESTDIR=%buildroot

%files
%doc COPYING AUTHORS
%_sbindir/conntrack
%_sbindir/conntrackd
%_man8dir/*

%changelog
* Sat Oct 30 2010 Anton Farygin <rider@altlinux.ru> 0.9.15-alt1
- New version

* Mon May 05 2008 Avramenko Andrew <liks@altlinux.ru> 0.9.6-alt1
- NMU: New version (Fix build with a new libnetfilter_conntrack)

* Mon Jun 18 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.9.3-alt0.1
- first build

