%define        gemname bump

Name:          gem-bump
Version:       0.10.0
Release:       alt1
Summary:       Bump is a gem that will simplify the way you build gems
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/gregorym/bump
Vcs:           https://github.com/gregorym/bump.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(bump) = 0.10.0


%description
Bump is a gem that will simplify the way you build gems and chef-cookbooks.

%description         -l ru_RU.UTF-8
Бамп есть бисер, который позволяет упростить путь в построении бисеров и
поваренных книг.


%package       -n bump
Version:       0.10.0
Release:       alt1
Summary:       Bump is a gem that will simplify the way you build gems executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета bump
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bump) = 0.10.0
Conflicts:     mesa-demos
Conflicts:     bumper

%description   -n bump
Bump is a gem that will simplify the way you build gems executable(s).

Bump is a gem that will simplify the way you build gems and chef-cookbooks.

%description   -n bump -l ru_RU.UTF-8
Исполнямка для самоцвета bump.


%package       -n gem-bump-doc
Version:       0.10.0
Release:       alt1
Summary:       Bump is a gem that will simplify the way you build gems documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bump
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bump) = 0.10.0

%description   -n gem-bump-doc
Bump is a gem that will simplify the way you build gems documentation
files.

Bump is a gem that will simplify the way you build gems and chef-cookbooks.

%description   -n gem-bump-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bump.


%package       -n gem-bump-devel
Version:       0.10.0
Release:       alt1
Summary:       Bump is a gem that will simplify the way you build gems development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bump
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bump) = 0.10.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0

%description   -n gem-bump-devel
Bump is a gem that will simplify the way you build gems development
package.

Bump is a gem that will simplify the way you build gems and chef-cookbooks.

%description   -n gem-bump-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bump.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n bump
%doc README.md
%_bindir/bump

%files         -n gem-bump-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-bump-devel
%doc README.md


%changelog
* Thu Apr 21 2022 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt1
- ^ 0.8.0 -> 0.10.0

* Thu Jun 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt3.1
- + conflict dep to bumper

* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt3
- ! spec by adding explicit conflict for bump to mesa-demos

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt2
- fix spec

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
