Name: spice-html5
Version: 0.1.7
Release: alt1
Summary: Pure Javascript SPICE client
Group: Networking/Remote access

License: LGPLv3
Url: http://www.spice-space.org
Source: %name/%name-%version.tar
Patch1: Spice-devel-Add-Send-Ctrl-Alt-Delete-button-to-spice_auto.html.patch

BuildArch: noarch

%description
%name is a Javascript SPICE client.  This includes a simple HTML
page to initiate a session, and the client itself.  It includes a configuration
file for Apache, but should work with any web server.

%prep
%setup
%patch1 -p1

%build

%install
%makeinstall_std

%files
%_datadir/%name
%doc COPYING COPYING.LESSER README TODO apache.conf.sample

%changelog
* Sun Oct 16 2016 Alexey Shabalin <shaba@altlinux.ru> 0.1.7-alt1
- 0.1.7

* Mon Nov 30 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.6-alt2
- add patch for view Ctrl-Alt-Delete button

* Wed Oct 14 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.6-alt1
- Initial packaging

