%define  pkgname dispatcher
 
Name: 	 ruby-%pkgname
Version: 0.0.1 
Release: alt1
 
Summary: A lightweight HTTP dispatch interface between Ruby and most webserver configurations
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://rubygems.org/gems/dispatcher/versions/0.0.1
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
The Dispatcher module defines a simple and consistent interface between
Ruby and most webserver configurations. This library provides a very
restrictive set of features, and as such is generally not meant to be
directly used by web-application authors, but instead targets
implementors of frameworks and web-libraries.

%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
%update_setup_rb
 
%build
%ruby_config
%ruby_build
 
%install
%ruby_install
%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
 
%check
%ruby_test_unit -Ilib:test test
 
%files
%doc README*
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Tue Feb 07 2017 Andrey Cherepanov <cas@altlinux.org> 0.0.1-alt1
- Initial build in Sisyphus
