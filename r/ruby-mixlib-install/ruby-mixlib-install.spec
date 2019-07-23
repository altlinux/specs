%define        pkgname mixlib-install

Name:          ruby-%pkgname
Version:       3.11.20
Release:       alt1
Summary:       A library for interacting with Chef Software Inc's software distribution systems
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/mixlib-install
%vcs           https://github.com/chef/mixlib-install.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemlibdir/*

%description
%summary.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --ignore=acceptance

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemlibdir
%ruby_gemspec

%files         doc
%ruby_gemdocdir

%files         -n %pkgname
%_bindir/%pkgname

%changelog
* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 3.11.20-alt1
- Fix spec
- Bump to 3.11.20

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 3.11.11-alt1
- Bump to 3.11.11
- Use Ruby Policy 2.0

* Tue Nov 20 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.7-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.6-alt1
- New version.

* Sun Jul 08 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.1-alt1
- New version.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.0-alt1
- New version.
- Package as gem.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 3.10.0-alt1
- Initial build for Sisyphus
