%define pkgname proj4rb

Name: ruby-proj4
Version: 0.3.0
Release: alt2

Summary: Proj.4 bindings
License: MIT
Group: Development/Ruby
URL: http://rubyforge.org/projects/%pkgname/

# Automatically added by buildreq on Mon Aug 31 2009
BuildRequires: libruby-devel proj-devel ruby-tool-setup

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-rdoc
Source: %pkgname-%version.tar

%description
This is a Ruby binding for the Proj.4 Carthographic Projection library
(http://trac.osgeo.org/proj/), that supports conversions between a large
number of geographic coordinate systems and datums.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -q -n %pkgname-%version
cp %_datadir/ruby-setup/setup.rb .

%build
%ruby_config
%ruby_build
#ruby setup.rb test

%install
%ruby_install
%rdoc lib/ ext/

%files
%ruby_sitearchdir/*
%ruby_sitelibdir/*
%doc README

%files doc
%ruby_ri_sitedir/Proj4

%changelog
* Tue Sep 08 2009 Grigory Batalov <bga@altlinux.ru> 0.3.0-alt2
- Fix build with ruby-1.9.1 (use RARRAY_LEN).

* Mon Aug 31 2009 Grigory Batalov <bga@altlinux.ru> 0.3.0-alt1
- Initial build for ALT Linux.
