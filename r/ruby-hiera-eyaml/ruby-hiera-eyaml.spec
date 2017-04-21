%define  pkgname hiera-eyaml
 
Name: 	 ruby-%pkgname
Version: 2.1.0 
Release: alt1
 
Summary: A backend for Hiera that provides per-value asymmetric encryption of sensitive data
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/voxpupuli/hiera-eyaml
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
 
%description
hiera-eyaml is a backend for Hiera that provides per-value encryption of
sensitive data within yaml files to be used by Puppet.

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
%_bindir/eyaml
%ruby_sitelibdir/*
 
%files doc
%ruby_ri_sitedir/*
 
%changelog
* Fri Apr 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build in Sisyphus
