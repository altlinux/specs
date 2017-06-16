Name: tiptop
Version: 2.3
Release: alt1

Summary: Tiptop is a performance monitoring tool for Linux
License: GPLv2
Group: Monitoring

URL: http://tiptop.gforge.inria.fr
Source: %name-%version.tar

Packager: %packager

BuildRequires: libxml2-devel libncurses-devel flex

%description
Tiptop is a performance monitoring tool for Linux.  It provides a
dynamic real-time view of the tasks running in the system. Tiptop is
very similar to the top utility, but most of the information displayed
comes from hardware counters.

%prep
%setup -n %name-%version

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_bindir/p%name
%_man1dir/%name.1.*
%_man1dir/p%name.1.*
%doc README AUTHORS tiptoprc

%changelog
* Fri Jun 16 2017 Terechkov Evgenii <evg@altlinux.org> 2.3-alt1
- Initial build for ALT Linux Sisyphus
