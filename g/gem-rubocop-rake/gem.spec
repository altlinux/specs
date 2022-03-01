%define        gemname rubocop-rake

Name:          gem-rubocop-rake
Version:       0.6.0
Release:       alt1
Summary:       A RuboCop plugin for Rake
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubocop/rubocop-rake
Vcs:           https://github.com/rubocop/rubocop-rake.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rubocop) >= 1.0 gem(rubocop) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rubocop) >= 1.0 gem(rubocop) < 2
Provides:      gem(rubocop-rake) = 0.6.0


%description
A RuboCop plugin for Rake.


%package       -n gem-rubocop-rake-doc
Version:       0.6.0
Release:       alt1
Summary:       A RuboCop plugin for Rake documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-rake
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-rake) = 0.6.0

%description   -n gem-rubocop-rake-doc
A RuboCop plugin for Rake documentation files.

%description   -n gem-rubocop-rake-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-rake.


%package       -n gem-rubocop-rake-devel
Version:       0.6.0
Release:       alt1
Summary:       A RuboCop plugin for Rake development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-rake
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-rake) = 0.6.0

%description   -n gem-rubocop-rake-devel
A RuboCop plugin for Rake development package.

%description   -n gem-rubocop-rake-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-rake.


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

%files         -n gem-rubocop-rake-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-rake-devel
%doc README.md


%changelog
* Tue Jan 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- + packaged gem with Ruby Policy 2.0
