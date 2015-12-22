%define  pkgname puppet-syntax
 
Name: 	 ruby-%pkgname
Version: 2.0.0 
Release: alt1
 
Summary: Syntax checks for Puppet manifests and templates
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/gds-operations/puppet-syntax
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
Syntax checks for Puppet manifests, templates, and Hiera YAML.

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
* Wed Dec 23 2015 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- Initial build for ALT Linux
