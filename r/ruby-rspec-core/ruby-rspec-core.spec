%define        pkgname rspec-core

Name:          ruby-%pkgname
Version:       3.8.0
Release:       alt2
Summary:       RSpec runner and formatters
License:       MIT
Group:         Development/Ruby
Url:           http://relishapp.com/rspec/rspec-core
# VCS:         https://github.com/rspec/rspec-core.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec)

%add_findreq_skiplist *.sh

%description
rspec-core provides the structure for writing executable examples of how
your code should behave, and an rspec command with tools to constrain
which examples get run and tailor the output.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%package       -n rspec
Summary:       Executable file for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n rspec
Executable file for %gemname gem.


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

%files         -n rspec
%_bindir/*

%changelog
* Fri Mar 1 2019 Pavel Skrylev <majioa@altlinux.org> 3.8.0-alt2
- Use Ruby Policy 2.0.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt2.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 15 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt2
- Rebuild with mocha 1.5.0.

* Thu Jan 04 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.1-alt1
- New version.

* Tue Oct 17 2017 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1.1
- Rebuild with Ruby 2.4.1

* Thu Jun 01 2017 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- New version
- Package rspec executable

* Mon Jan 18 2016 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt1
- Initial build for ALT Linux
