%define        gemname standardrb

Name:          gem-standardrb
Version:       1.0.1
Release:       alt1
Summary:       Alias for the standard gem, which has a standardrb binary
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/testdouble/standardrb
Vcs:           https://github.com/testdouble/standardrb.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(standard) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(standard) >= 0
Provides:      gem(standardrb) = 1.0.1

%description
You're probably in the wrong place. This is an alias for the gem standard,
whose binary is standardrb.


%package       -n gem-standardrb-doc
Version:       1.0.1
Release:       alt1
Summary:       Alias for the standard gem, which has a standardrb binary documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета standardrb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(standardrb) = 1.0.1

%description   -n gem-standardrb-doc
Alias for the standard gem, which has a standardrb binary documentation files.

You're probably in the wrong place. This is an alias for the gem standard,
whose binary is standardrb.

%description   -n gem-standardrb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета standardrb.


%package       -n gem-standardrb-devel
Version:       1.0.1
Release:       alt1
Summary:       Alias for the standard gem, which has a standardrb binary development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета standardrb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(standardrb) = 1.0.1
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-standardrb-devel
Alias for the standard gem, which has a standardrb binary development package.

You're probably in the wrong place. This is an alias for the gem standard,
whose binary is standardrb.

%description   -n gem-standardrb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета standardrb.


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

%files         -n gem-standardrb-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-standardrb-devel
%doc README.md


%changelog
* Thu Jun 30 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + packaged gem with Ruby Policy 2.0
