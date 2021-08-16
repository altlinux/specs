%define        gemname rubocop-rails

Name:          gem-rubocop-rails
Version:       2.11.0
Release:       alt1
Summary:       Automatic Rails code style checking tool
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubocop/rubocop-rails
Vcs:           https://github.com/rubocop/rubocop-rails/.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activesupport) >= 4.2.0
BuildRequires: gem(rack) >= 1.1
BuildRequires: gem(rubocop) >= 1.7.0 gem(rubocop) < 2.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(activesupport) >= 4.2.0
Requires:      gem(rack) >= 1.1
Requires:      gem(rubocop) >= 1.7.0 gem(rubocop) < 2.0
Provides:      gem(rubocop-rails) = 2.11.0


%description
Automatic Rails code style checking tool. A RuboCop extension focused on
enforcing Rails best practices and coding conventions.


%package       -n gem-rubocop-rails-doc
Version:       2.11.0
Release:       alt1
Summary:       Automatic Rails code style checking tool documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-rails) = 2.11.0

%description   -n gem-rubocop-rails-doc
Automatic Rails code style checking tool documentation files.

Automatic Rails code style checking tool. A RuboCop extension focused on
enforcing Rails best practices and coding conventions.

%description   -n gem-rubocop-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-rails.


%package       -n gem-rubocop-rails-devel
Version:       2.11.0
Release:       alt1
Summary:       Automatic Rails code style checking tool development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-rails) = 2.11.0

%description   -n gem-rubocop-rails-devel
Automatic Rails code style checking tool development package.

Automatic Rails code style checking tool. A RuboCop extension focused on
enforcing Rails best practices and coding conventions.

%description   -n gem-rubocop-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-rails.


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

%files         -n gem-rubocop-rails-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-rails-devel
%doc README.md


%changelog
* Wed Jun 23 2021 Pavel Skrylev <majioa@altlinux.org> 2.11.0-alt1
- + packaged gem with Ruby Policy 2.0
