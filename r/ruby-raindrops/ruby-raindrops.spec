%define pkgname raindrops

Name: ruby-%pkgname 
Version: 0.17.0
Release: alt2

Summary: real-time stats for preforking Rack servers
Group: Development/Ruby 
License: LGPL
Url: http://raindrops.bogomips.org/

Source: %pkgname-%version.tar

BuildRequires: libruby-devel ruby-tool-setup

%description 
Raindrops is a real time stats package to show statistics for Rack HTTP
servers.  It is designed for preforking servers such as Rainbows! and
Unicorn, but should support any Rack HTTP server under Ruby and possibly
Rubinius (untested) on platforms supporting POSIX shared memory and
compiled with GCC (for atomic builtins).  Raindrops includes a
Struct-like Raindrops::Struct class that may be used standalone to
create atomic counters shared across any number of forked processes
under SMP.

%package doc 
Summary: Documentation files for %name 
Group: Documentation
BuildArch: noarch

%description doc
Documentation files for %name.

%prep
%setup -q -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build
#for t in test/test_*.rb; do
#ruby_test_unit -Iext/kgio:lib "$t"
#done


%install
%ruby_install
%rdoc lib/

%files
%doc README TODO
%ruby_sitelibdir/*
%ruby_sitearchdir/*

%files doc
%doc COPYING
%ruby_ri_sitedir/Raindrops*

%changelog
* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.17.0-alt2
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.7.0-alt2.2
- Rebuilt with ruby-2.0.0-alt1

* Thu Dec 06 2012 Led <led@altlinux.ru> 0.7.0-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Mon Aug 15 2011 Anton Gorlov <stalker@altlinux.ru> 0.7.0-alt2
- fix wrong url

* Wed Aug 10 2011 Anton Gorlov <stalker@altlinux.ru> 0.7.0-alt1
- initial build for ALTLinux
