# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname rack

Name: ruby-%pkgname
Version: 1.2.2
Release: alt1

Summary: Modular Ruby webserver interface
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/rack/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Sat Nov 01 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-tool-rdoc ruby-tool-setup

%description
Rack provides a minimal, modular and adaptable interface for developing
web applications in Ruby.  By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.

You may need to install appropriate %name-handler-XXX.

# Different handler autoload
%add_findreq_skiplist %ruby_sitelibdir/rack/handler.rb
# name Class file
%define ruby_rack_subpackage() \
%package handler-%1 \
Summary: %2 handler for Rack \
Group: Development/Ruby \
PreReq: %name = %version-%release \
\
%description handler-%1 \
%2 handler for Rack. \
\
%files handler-%1 \
%ruby_sitelibdir/rack/handler/%3.rb \
%nil

%ruby_rack_subpackage cgi CGI cgi
%ruby_rack_subpackage fastcgi FastCGI fastcgi
%ruby_rack_subpackage mongrel Mongrel mongrel
%ruby_rack_subpackage webrick WEBrick webrick

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
%rdoc lib/

%files
%doc README KNOWN-ISSUES
%_bindir/rackup
%ruby_sitelibdir/*
%exclude %ruby_sitelibdir/rack/handler/*

%files doc
%doc example
%ruby_ri_sitedir/Rack*

%changelog
* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.2.2-alt1
- [1.2.2]

* Sun Apr 11 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.0-alt2
- Fix package broken by erthad

* Wed Mar 31 2010 Timur Batyrshin <erthad@altlinux.org> 1.1.0-alt1
- [1.1.0]

* Mon Oct 19 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.1-alt1
- [1.0.1]

* Sun Oct 18 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.0-alt3
- Updated to 1.0-16-g99c47b8
- Force all form data to be UTF-8 String's

* Sun Aug 16 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.0-alt2
- Backported Ruby 1.9 encoding-related fixes.

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.0.0-alt1
- [1.0.0]
- Packaged rackup script
- Dropped unused handlers

* Sat Nov 01 2008 Sir Raorn <raorn@altlinux.ru> 0.4.0-alt1
- Built for Sisyphus

