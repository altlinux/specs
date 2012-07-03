Name: stress
Version: 1.0.4
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: A tool which imposes a configurable amount of load on your system
License: GPLv2+
Group: System/Kernel and hardware

URL: http://weather.ou.edu/~apw/projects/stress
Source: %url/stress-%version.tar.gz

%description
stress is a tool which imposes a configurable amount of CPU, I/O, RAM, and
HDD load and report any errors it detects.

stress is not a benchmark. It is a tool used by system administrators to
evaluate how well their systems will scale, by kernel programmers to evaluate
perceived performance characteristics, and by systems programmers to expose the
classes of bugs which only or more frequently manifest themselves when the
system is under heavy load.

%prep
%setup

%build
%configure
# uniprocessor make is just OK as only one source file is compiled :)
%make

%install
%makeinstall_std

%files
%doc doc/stress.html
%_bindir/stress
%_man1dir/stress.*
%_infodir/stress*

%changelog
* Mon Mar 22 2010 Victor Forsiuk <force@altlinux.org> 1.0.4-alt1
- 1.0.4

* Fri Feb 19 2010 Victor Forsiuk <force@altlinux.org> 1.0.3-alt1
- 1.0.3

* Sun Dec 20 2009 Victor Forsyuk <force@altlinux.org> 1.0.2-alt1
- 1.0.2

* Wed Aug 12 2009 Victor Forsyuk <force@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Dec 17 2007 Victor Forsyuk <force@altlinux.org> 1.0.0-alt1
- 1.0.0

* Fri Jan 19 2007 Victor Forsyuk <force@altlinux.org> 0.18.9-alt1
- 0.18.9
- Add project URL.

* Fri Jul 01 2005 Anton Farygin <rider@altlinux.ru> 0.18.6-alt1
- new version

* Wed Oct 29 2003 Rider <rider@altlinux.ru> 0.18.1-alt1
- first build for Sisyphus
