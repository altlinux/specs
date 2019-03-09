%define        pkgname rspec-mocks

Name:          ruby-%pkgname
Version:       3.8.0
Release:       alt2
Summary:       RSpec's 'test double' framework, with support for stubbing and mocking
License:       MIT
Group:         Development/Ruby
Url:           http://relishapp.com/rspec/rspec-mocks
# VCS:         https://github.com/rspec/rspec-mocks.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
rspec-mocks is a test-double framework for rspec with support for method
stubs, fakes, and message expectations on generated test-doubles and
real objects alike.


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
* Fri Mar 1 2019 Pavel Skrylev <majioa@altlinux.org> 3.8.0-alt2
- Use Ruby Policy 2.0.


* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Oct 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version

* Tue Aug 22 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version

* Mon Jan 18 2016 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- Initial build for ALT Linux
