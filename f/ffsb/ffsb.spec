%define beta -rc2

Name: ffsb
Version: 6.0
Release: alt0.2

Summary: The Flexible Filesystem Benchmark
License: GPLv2+
Group: Monitoring

Url: http://sourceforge.net/projects/ffsb
Source: http://downloads.sourceforge.net/%name/%name-%version%beta.tar.bz2
Packager: Michael Shigorin <mike@altlinux.org>

%description
The Flexible Filesystem Benchmark (FFSB) is a cross-platform
filesystem performance measurement tool. It uses customizable
profiles to measure of different workloads, and it supports
multiple groups of threads across multiple filesystems.

%prep
%setup -n %name-%version%beta

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS README
%doc examples/
%_bindir/%name

%changelog
* Fri Aug 14 2009 Michael Shigorin <mike@altlinux.org> 6.0-alt0.2
- 6.0-rc2 built for ALT Linux (suggested by led@)
- based on Fedora spec

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 12 2008 Eric Sandeen <sandeen@redhat.com> 5.2.1-1
- Initial build
