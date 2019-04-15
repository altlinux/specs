%define  pkgname hiera-eyaml
 
Name: 	 ruby-%pkgname
Version: 2.1.0 
Release: alt2
 
Summary: A backend for Hiera that provides per-value asymmetric encryption of sensitive data
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/voxpupuli/hiera-eyaml
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch: noarch
 
Source:  %pkgname-%version.tar
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup

%gem_replace_version highline ~> 1.7
 
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
 
%build
%gem_build
 
%install
%gem_install
 
%check
%gem_test
 
%files
%doc README*
%_bindir/eyaml
%ruby_gemspec
%ruby_gemlibdir
 
%files doc
%ruby_gemdocdir
 
%changelog
* Wed Apr 10 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.1.0-alt2
- Use new ruby packaging policy
- Make appropriate require to highline

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Apr 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build in Sisyphus
