%define  pkgname cheffish

Name:          ruby-%pkgname
Version:       14.0.9
Release:       alt1
Summary:       Resources and tools for testing and interacting with Chef and Chef Server.
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/cheffish
# VCS          https://github.com/chef/cheffish.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary

This library provides a variety of convergent resources for interacting with
the Chef Server; along the way, it happens to provide some very useful and
sophisticated ways of running Chef resources as recipes in RSpec examples.

%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Mon Apr 08 2019 Pavel Skrylev <majioa@altlinux.org> 14.0.9-alt1
- Bump to 14.0.9
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.1-alt1
- Initial build for Sisyphus
