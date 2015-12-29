%define  pkgname semantic_puppet
 
Name: 	 ruby-%pkgname
Version: 0.1.1 
Release: alt1
 
Summary: Library of useful tools for working with Semantic Versions and module dependencies
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/puppetlabs/semantic_puppet
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Library of tools used by Puppet to parse, validate, and compare Semantic
Versions and Version Ranges and to query and resolve module
dependencies.

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
* Wed Dec 23 2015 Andrey Cherepanov <cas@altlinux.org> 0.1.1-alt1
- Initial build for ALT Linux
