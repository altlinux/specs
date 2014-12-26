Name: capstats
Version: 0.21
Release: alt1
Packager: Andriy Stepanov <stanv@altlinux.ru>
Summary: A command-line tool collecting packet statistics
License: %bsd
Url: https://www.bro.org/sphinx/components/capstats/README.html
Source0: %name-%version.tar
Patch0: capstats-0.21-configure-alt.patch
#Patch1: %name-%version-%release.patch
Source1: cmake.tar
Group: Networking/Other
BuildRequires: cmake
BuildRequires: libpcap-devel
BuildRequires: gcc-c++
BuildRequires: rpm-build-licenses

%description
capstats is a small tool to collect statistics on the current load of a
network interface, using either libpcap or the native interface for Endace.
It reports statistics per time interval and/or for the tool total run-time.

%prep
%setup -a1
%patch0 -p1
#patch1

%build
%configure --disable-rpath
%make_build

%install
# make install DESTDIR=%buildroot INSTALL="install -p"
%makeinstall DESTDIR=%buildroot

%files
%doc CHANGES COPYING README
%_bindir/%name

%changelog
* Fri Dec 26 2014 Andriy Stepanov <stanv@altlinux.ru> 0.21-alt1
- Build for ALTLinux

