Name: paris-traceroute
Version: 0.92
Release: alt1

Summary: Paris traceroute is a new version of the well-known network diagnosis and measurement tool
License: GPLv2+
Group: Monitoring

Url: http://www.paris-traceroute.net/
Source: http://www.paris-traceroute.net/downloads/paris-traceroute-%version-dev.tar.gz

# Automatically added by buildreq on Fri Dec 16 2011
BuildRequires: gcc-c++

%description
Paris traceroute is a new version of the well-known network diagnosis
and measurement tool. It addresses problems caused by load balancers
with the initial implementation of traceroute.

%prep
%setup -n %name-current

%build
%configure
%make_build

%install
%makeinstall_std
install -pDm644 man/paris-traceroute.8 %buildroot%_man8dir/paris-traceroute.8

%files
%_bindir/*
%_man8dir/*

%changelog
* Fri Dec 16 2011 Victor Forsiuk <force@altlinux.org> 0.92-alt1
- Initial build.
