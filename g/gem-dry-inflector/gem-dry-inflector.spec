%define        gemname dry-inflector

Name:          gem-dry-inflector
Version:       0.2.1
Release:       alt1
Summary:       String inflections for dry-rb
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-inflector
Vcs:           https://github.com/dry-rb/dry-inflector.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(dry-inflector) = 0.2.1


%description
dry-inflector is an inflector gem for Ruby, which provides a configurable
inflector object, rather than using a singleton.


%package       -n gem-dry-inflector-doc
Version:       0.2.1
Release:       alt1
Summary:       String inflections for dry-rb documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-inflector
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dry-inflector) = 0.2.1

%description   -n gem-dry-inflector-doc
String inflections for dry-rb documentation files.

dry-inflector is an inflector gem for Ruby, which provides a configurable
inflector object, rather than using a singleton.

%description   -n gem-dry-inflector-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dry-inflector.


%package       -n gem-dry-inflector-devel
Version:       0.2.1
Release:       alt1
Summary:       String inflections for dry-rb development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-inflector
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dry-inflector) = 0.2.1
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(rspec) >= 0 gem(rspec) < 4

%description   -n gem-dry-inflector-devel
String inflections for dry-rb development package.

dry-inflector is an inflector gem for Ruby, which provides a configurable
inflector object, rather than using a singleton.

%description   -n gem-dry-inflector-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dry-inflector.


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

%files         -n gem-dry-inflector-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-dry-inflector-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- ^ 0.1.2 -> 0.2.1

* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
