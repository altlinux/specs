%define        pkgname capybara

Name:          ruby-%pkgname
Version:       3.29.0
Release:       alt1
Summary:       Acceptance test framework for web applications
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/teamcapybara/capybara
%vcs           https://github.com/teamcapybara/capybara.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary

%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.29.0-alt1
- ^ v3.29.0

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 3.16.1-alt1
- ^ v3.16.1
- ^ Ruby Policy 2.0

* Mon Oct 29 2018 Pavel Skrylev <majioa@altlinux.org> 3.10.0-alt1
- new version 3.10.0

* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 3.9.0-alt1
- New version.

* Thu Sep 27 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.2-alt1
- New version.

* Tue Sep 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.1-alt1
- New version.

* Fri Sep 21 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.2-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- Initial build for Sisyphus
