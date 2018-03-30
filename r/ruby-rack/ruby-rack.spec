# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname rack

Name: ruby-%pkgname
Version: 1.6.8
Release: alt2.2
Epoch:   1

Summary: Modular Ruby webserver interface
Group: Development/Ruby
License: MIT/Ruby
Url: http://rubyforge.org/projects/rack/

BuildArch: noarch

Source: %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

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
#ruby_rack_subpackage mongrel Mongrel mongrel
%ruby_rack_subpackage webrick WEBrick webrick

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
%ruby_install
# Install gemspec
export rbVersion=`ruby -e "puts RbConfig::CONFIG[\"ruby_version\"]"`
install -Dm 0644 %pkgname.gemspec %buildroot%ruby_libdir/gems/$rbVersion/specifications/%pkgname.gemspec
%rdoc lib/

%files
%doc README* KNOWN-ISSUES
%_bindir/rackup
%ruby_sitelibdir/*
%exclude %ruby_sitelibdir/rack/handler/*
%ruby_libdir/gems/*/specifications/*.gemspec

%files doc
%doc example
%ruby_ri_sitedir/Rack*

%changelog
* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt2.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt2.1
- Rebuild with Ruby 2.5.0

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Jun 16 2017 Andrey Cherepanov <cas@altlinux.org> 1:1.6.8-alt1
- Decrease version for pcs-pcsd
- Package gemspec
- Spec cleanup

* Tue May 16 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.3-alt1
- New version

* Mon May 08 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.2-alt1
- New version

* Sat Apr 08 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- new version 2.0.1

* Sat Dec 01 2012 Led <led@altlinux.ru> 1.2.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

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

