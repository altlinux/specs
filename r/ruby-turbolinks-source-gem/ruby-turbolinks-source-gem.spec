%define        pkgname turbolinks-source
%define        gemname turbolinks-source

Name:          ruby-%pkgname-gem
Version:       5.2.0
Release:       alt2
Summary:       Turbolinks JavaScript assets, packaged as a RubyGem
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/turbolinks/turbolinks-source-gem
%vcs           https://github.com/turbolinks/turbolinks-source-gem.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary

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
%ruby_build --use=%gemname --alias=%gemname-gem

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
* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 5.2.0-alt2
- Use Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version.

* Fri Jul 27 2018 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- Initial build for Sisyphus
