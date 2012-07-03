%define pkgname unicorn

Name: %pkgname
Version: 4.3.1
Release: alt1
Summary: Unicorn: Rack HTTP server for fast clients and Unix
License: GPL2
Group: System/Servers
Url: http://unicorn.bogomips.org/

Packager: Anton Gorlov <stalker at altlinux.org>

Source: %pkgname-%version.tar

# Automatically added by buildreq on Tue Aug 09 2011
# optimized out: ruby ruby-stdlibs ruby-tool-rdoc
BuildRequires: libruby-devel ragel rubygems

%description
Unicorn is an HTTP server for Rack applications designed to only serve fast clients on low-latency, high-bandwidth connections
and take advantage of features in Unix/Unix-like kernels. Slow clients should only be served by placing a reverse proxy
capable of fully buffering both the the request and response in between Unicorn and slow clients.

%package doc
Summary: Documentation files for %pkgname
Group: Documentation

%description doc
Documentation files for %pkgname

%prep
%setup -n %pkgname-%version

%build
%make_build ext/unicorn_http/unicorn_http.c
%ruby_config
%ruby_build
#for t in test/*_test.rb; do
#ruby_test_unit -Ilib:test "$t"
#done

%install
%ruby_install
%rdoc lib/

%files
%doc ISSUES README TUNING KNOWN_ISSUES FAQ DESIGN examples*
%ruby_sitelibdir/*
%ruby_sitearchdir/*
%_bindir/*

%files doc
%ruby_ri_sitedir/Unicorn*

%changelog
* Fri May 18 2012 Anton Gorlov <stalker@altlinux.ru> 4.3.1-alt1
- update to  new version 

* Tue Mar 20 2012 Anton Gorlov <stalker@altlinux.ru> 4.2.0-alt1
- update to  new version

* Sat Sep 03 2011 Anton Gorlov <stalker@altlinux.ru> 4.1.1-alt1
- update to  new version

* Wed Aug 17 2011 Anton Gorlov <stalker@altlinux.ru> 4.0.1-alt3
- added examples to main package

* Sat Aug 13 2011 Anton Gorlov <stalker@altlinux.ru> 4.0.1-alt2
- fix conflict with with ruby-parseconfig-doc

* Sat Aug 13 2011 Anton Gorlov <stalker@altlinux.ru> 4.0.1-alt1
- initial build for ALTLinux

