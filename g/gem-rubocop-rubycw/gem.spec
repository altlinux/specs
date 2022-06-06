%define        gemname rubocop-rubycw

Name:          gem-rubocop-rubycw
Version:       0.1.6
Release:       alt1
Summary:       Integrate RuboCop and ruby -cw
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubocop/rubocop-rubycw
Vcs:           https://github.com/rubocop/rubocop-rubycw.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rubocop) >= 1.0 gem(rubocop) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rubocop) >= 1.0 gem(rubocop) < 2
Provides:      gem(rubocop-rubycw) = 0.1.6


%description
Integrate RuboCop and ruby -cw.


%package       -n gem-rubocop-rubycw-doc
Version:       0.1.6
Release:       alt1
Summary:       Integrate RuboCop and ruby -cw documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-rubycw
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-rubycw) = 0.1.6

%description   -n gem-rubocop-rubycw-doc
Integrate RuboCop and ruby -cw documentation files.

%description   -n gem-rubocop-rubycw-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-rubycw.


%package       -n gem-rubocop-rubycw-devel
Version:       0.1.6
Release:       alt1
Summary:       Integrate RuboCop and ruby -cw development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-rubycw
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-rubycw) = 0.1.6

%description   -n gem-rubocop-rubycw-devel
Integrate RuboCop and ruby -cw development package.

%description   -n gem-rubocop-rubycw-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-rubycw.


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

%files         -n gem-rubocop-rubycw-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-rubycw-devel
%doc README.md


%changelog
* Tue May 17 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.6-alt1
- + packaged gem with Ruby Policy 2.0
