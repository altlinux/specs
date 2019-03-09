%define        pkgname rspec

Name:          ruby-%pkgname
Version:       3.8.0
Release:       alt3
Summary:       RSpec meta-gem that depends on the other components
License:       MIT
Group:         Development/Ruby
Url:           http://rspec.info/
# VCS:         https://github.com/rspec/rspec.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
rspec is a meta-gem, which depends on the rspec-core, rspec-expectations and
rspec-mocks gems. Each of these can be installed separately and loaded in
isolation using require. Among other benefits, this allows you to use
rspec-expectations, for example, in Test::Unit::TestCase if you happen to
prefer that style.

Conversely, if you like RSpec's approach to declaring example groups and
examples (describe and it) but prefer Test::Unit assertions and mocha, rr or
flexmock for mocking, you'll be able to do that without having to install or
load the components of RSpec that you're not using.

%prep
%setup

%build
%gem_build

%install
%gem_install
rm -rf %buildroot%ruby_gemdocdir

%files
%ruby_gemspec
%ruby_gemlibdir

%changelog
* Tue Feb 26 2019 Pavel Skrylev <majioa@altlinux.org> 3.8.0-alt3
- Use Ruby Policy 2.0.

* Thu Jan 10 2019 Pavel Skrylev <majioa@altlinux.org> 3.8.0-alt2
- Place library into proper ruby gem folder.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus
