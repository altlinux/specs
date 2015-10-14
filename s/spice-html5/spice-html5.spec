Name: spice-html5
Version: 0.1.6
Release: alt1
Summary: Pure Javascript SPICE client
Group: Networking/Remote access

License: LGPLv3
Url: http://www.spice-space.org
Source: %name/%name-%version.tar

BuildArch: noarch

%description
%name is a Javascript SPICE client.  This includes a simple HTML
page to initiate a session, and the client itself.  It includes a configuration
file for Apache, but should work with any web server.

%prep
%setup

%build

%install
%makeinstall_std

%files
%_datadir/%name
%doc COPYING COPYING.LESSER README TODO apache.conf.sample

%changelog
* Wed Oct 14 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.6-alt1
- Initial packaging

