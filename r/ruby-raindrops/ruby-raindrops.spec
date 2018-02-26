%define pkgname raindrops

Name: ruby-%pkgname 
Version: 0.7.0
Release: alt2

Summary: real-time stats for preforking Rack servers
Group: Development/Ruby 
License: LGPL
Url: http://raindrops.bogomips.org/

Packager: Anton Gorlov <stalker at altlinux.org>


Source: %pkgname-%version.tar.gz

# Automatically added by buildreq on Wed Aug 10 2011
# optimized out: ruby ruby-stdlibs ruby-tool-rdoc
BuildRequires: libruby-devel ruby-tool-setup

%description 
Raindrops is a real time stats package to show statistics for Rack HTTP servers. It is designed for preforking servers such as Rainbows! 
and Unicorn, but should support any Rack HTTP server under Ruby 1.9, 1.8 and possibly Rubinius (untested) on platforms
supporting POSIX shared memory and compiled with GCC (for atomic builtins).
Raindrops includes a Struct-like Raindrops::Struct class that may be used standalone to create atomic counters shared across any number
of forked processes under SMP.

%package doc 
Summary: Documentation files for %name 
Group: Documentation

%description doc 
Documentation files for %name

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
* Mon Aug 15 2011 Anton Gorlov <stalker@altlinux.ru> 0.7.0-alt2
- fix wrong url

* Wed Aug 10 2011 Anton Gorlov <stalker@altlinux.ru> 0.7.0-alt1
- initial build for ALTLinux



