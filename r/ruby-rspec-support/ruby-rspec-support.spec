%define        pkgname rspec-support

Name:          ruby-%pkgname
Version:       3.8.0
Release:       alt2
Summary:       Common code needed by the other RSpec gems
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rspec/rspec-support
# VCS:         https://github.com/rspec/rspec-support.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
RSpec::Support provides common functionality to RSpec::Core,
RSpec::Expectations and RSpec::Mocks. It is considered suitable for
internal use only at this time.


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

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jan 31 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt1
- New version.

* Tue Oct 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version

* Fri May 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version

* Wed Mar 08 2017 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- New version

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 3.2.2-alt1
- Initial build for ALT Linux
