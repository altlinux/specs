Summary:        the fatest network packet injector
Name:           t50
Version:        5.4.1
Release:        alt1
URL:            http://t50.sourceforge.net/
Packager: 	Valentin Rosavitskiy <valintinr@altlinux.org>
License:        GPLv2
Group: 		Security/Networking

#BuildRequires:  
Source0:        %name-%version.tar
Patch0:		t50-5.4.1-alt1-drop_checkroot.patch

%description
T50 (f.k.a. F22 Raptor) is a tool designed to perform "Stress Testing".
The concept started on 2001, right after release 'nb-isakmp.c', and
the main goal was:
  - Having a tool to perform TCP/IP protocol fuzzer,  covering common regular
    protocols, such as: ICMP, TCP and UDP.

%prep
%setup -q
%patch0 -p1

%build
%make_build

%install
%makeinstall_std

%files
%doc CHANGELOG LICENSE README TODO
%_sbindir/%name
%_man8dir/*

%changelog
* Fri Jul 11 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 5.4.1-alt1
- Initial build

