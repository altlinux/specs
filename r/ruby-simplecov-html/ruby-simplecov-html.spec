%define  pkgname simplecov-html
 
Name: 	 ruby-%pkgname
Version: 0.10.0 
Release: alt1
 
Summary: HTML formatter for SimpleCov code coverage tool for Ruby
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/colszowka/simplecov-html
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Generates a nice HTML report of your SimpleCov ruby code coverage
results on Ruby 1.9 using client-side Javascript quite extensively.

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
* Tue Oct 25 2016 Andrey Cherepanov <cas@altlinux.org> 0.10.0-alt1
- Initial build in Sisyphus
