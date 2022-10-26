%define        gemname bullet

Name:          gem-bullet
Version:       6.1.5
Release:       alt1
Summary:       help to kill N+1 queries and unused eager loading
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/flyerhzm/bullet
Vcs:           https://github.com/flyerhzm/bullet.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(activesupport) >= 3.0.0
BuildRequires: gem(uniform_notifier) >= 1.11 gem(uniform_notifier) < 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(activesupport) >= 3.0.0
Requires:      gem(uniform_notifier) >= 1.11 gem(uniform_notifier) < 2
Provides:      gem(bullet) = 6.1.5


%description
help to kill N+1 queries and unused eager loading.


%package       -n gem-bullet-doc
Version:       6.1.5
Release:       alt1
Summary:       help to kill N+1 queries and unused eager loading documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bullet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bullet) = 6.1.5

%description   -n gem-bullet-doc
help to kill N+1 queries and unused eager loading documentation files.

%description   -n gem-bullet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bullet.


%package       -n gem-bullet-devel
Version:       6.1.5
Release:       alt1
Summary:       help to kill N+1 queries and unused eager loading development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bullet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bullet) = 6.1.5

%description   -n gem-bullet-devel
help to kill N+1 queries and unused eager loading development package.

%description   -n gem-bullet-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bullet.


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

%files         -n gem-bullet-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-bullet-devel
%doc README.md


%changelog
* Fri Oct 07 2022 Pavel Skrylev <majioa@altlinux.org> 6.1.5-alt1
- ^ 6.1.4 -> 6.1.5

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 6.1.4-alt1
- + packaged gem with Ruby Policy 2.0
