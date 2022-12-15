Name: multiwatch
Version: 1.0.0
Release: alt1
License: MIT
Summary: %{name} is used to fork and watch multiple FastCGI backends
Group: System/Servers

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: libev-devel gcc-c++ glib2-devel

%description
Multiwatch forks multiple instance of one application and keeps them running;
it is made to be used with spawn-fcgi, so all forks share the same fastcgi
socket (no webserver restart needed if you increase/decrease the number of
forks), and it is easier than to setup multiple daemontool supervised
instances.

%prep
%setup

%build
%cmake

%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_man1dir
install -pm644 %name.1 %buildroot%_man1dir/

%files
%doc README COPYING
%_bindir/%name
%_man1dir/%{name}*

%changelog
* Thu Dec 15 2022 L.A. Kostis <lakostis@altlinux.ru> 1.0.0-alt1
- Initial build for ALTLinux.
