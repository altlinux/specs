Name: bgpq3
Version: 0.1.31
Release: alt1

Group: Security/Networking
Summary: Automate BGP filter generation based on routing database information
URL: http://snar.spb.ru/prog/bgpq3/
License: BSD
Source0: %name-%version.tar
Patch0: bgpq3-alt-DESTDIR.patch

%description
You are running BGP in your network and want to automate filter generation for your routers? Well, with BGPQ3 it's easy.

%prep
%setup
%patch0 -p0

%build
%configure --prefix=%_datadir
%make_build

%install
mkdir -p %buildroot%_bindir %buildroot%_man8dir
%makeinstall_std

%files
%_bindir/%name
%_man8dir/%name.8.*
%doc COPYRIGHT CHANGES README.md %name.html

%changelog
* Mon Jul 31 2017 Terechkov Evgenii <evg@altlinux.org> 0.1.31-alt1
- Initial build for ALT Linux Sisyphus
