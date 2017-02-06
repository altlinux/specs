%define  pkgname puppet-lint
 
Name: 	 ruby-%pkgname
Version: 3.0.0
Release: alt1
 
Summary: Check that your Puppet manifests conform to the style guide
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/rodjek/puppet-lint/
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
The goal of this project is to implement as many of the recommended
Puppet style guidelines from the Puppet Labs style guide as practical.
It is not meant to validate syntax. Please use "puppet parser validate"
for that.

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
%_bindir/*
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Mon Feb 06 2017 Denis Medvedev <nbr@altlinux.org> 3.0.0-alt1
- bump to version 3.0.0

* Wed Dec 23 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- Initial build for ALT Linux
