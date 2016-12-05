Name: nfacct
Version: 1.0.2
Release: alt1
Summary: Command line tool to create/retrieve/delete accounting objects
Group: Networking/Other
License: GPLv2+
Url: http://www.netfilter.org/projects/nfacct/index.html
Source0: %name-%version.tar
BuildRequires: libmnl-devel
BuildRequires: libnetfilter_acct-devel
Requires: iptables >= 1.4.13

%description
Nfacct is the command line tool to create/retrieve/delete accounting objects.

%prep
%setup

%build
autoreconf -fisv
%configure
%make_build

%install
%makeinstall_std

%files
%doc COPYING
%_sbindir/*
%_man8dir/%{name}*

%changelog
* Mon Dec 05 2016 Novikov Sergey <sotor@altlinux.org> 1.0.2-alt1
- initial packaging
