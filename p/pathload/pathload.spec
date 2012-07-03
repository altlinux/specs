Summary:	Pathload is a tool for estimating the available bandwidth of an end-to-end path
Name:		pathload
Version:	1.3.2
Release:	alt1
License:	GPLv2
Group:		System/Servers
Source:		http://www-static.cc.gatech.edu/fac/Constantinos.Dovrolis/%name.tar.gz
URL:		http://www.pathrate.org

%description
Pathload is a tool for estimating the available bandwidth
of an end-to-end path from a host S (sender) to a host R (receiver).
The available bandwidth is the maximum IP-layer
throughput that a flow can get in the path from S to R,
without reducing the rate of the rest of the traffic in the path.

%prep
%setup -q -n %{name}_%version

%build
%configure
%make

%install
%__mkdir_p %buildroot/%_sbindir
%__install %{name}_rcv %buildroot/%_sbindir/
%__install %{name}_snd %buildroot/%_sbindir/

%files
%doc README COPYING CHANGES
%_sbindir/%{name}_rcv
%_sbindir/%{name}_snd

%changelog
* Sat Mar 15 2008 Serhii Hlodin <hlodin@altlinux.ru> 1.3.2-alt1
- Initial build from source

