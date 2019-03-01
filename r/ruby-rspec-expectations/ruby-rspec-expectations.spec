%define        pkgname rspec-expectations

Name:          ruby-%pkgname
Version:       3.8.2
Release:       alt2
Summary:       Provides a readable API to express expected outcomes of a code example
License:       MIT
Group:         Development/Ruby
Url:           http://relishapp.com/rspec/rspec-expectations
# VCS:         https://github.com/rspec/rspec-expectations.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
RSpec::Expectations lets you express expected outcomes on an object in
an example.


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

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Fri Mar 1 2019 Pavel Skrylev <majioa@altlinux.org> 3.8.2-alt2
- Use Ruby Policy 2.0.

* Wed Oct 10 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.2-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.1-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Oct 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version

* Tue Aug 22 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version

* Sat Dec 26 2015 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- Initial build for ALT Linux
