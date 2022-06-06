%define        gemname goodcheck

Name:          gem-goodcheck
Version:       3.1.0
Release:       alt1
Summary:       Regexp based customizable linter
License:       MIT
Group:         Development/Ruby
Url:           https://sider.github.io/goodcheck/
Vcs:           https://github.com/sider/goodcheck.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.16
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(marcel) >= 1.0 gem(marcel) < 2.0
BuildRequires: gem(strong_json) >= 1.1 gem(strong_json) < 2.2
BuildRequires: gem(rainbow) >= 3.0 gem(rainbow) < 4.0
BuildRequires: gem(psych) >= 3.1 gem(psych) < 5.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(marcel) >= 1.0 gem(marcel) < 2.0
Requires:      gem(strong_json) >= 1.1 gem(strong_json) < 2.2
Requires:      gem(rainbow) >= 3.0 gem(rainbow) < 4.0
Requires:      gem(psych) >= 3.1 gem(psych) < 5.0
Provides:      gem(goodcheck) = 3.1.0


%description
Goodcheck is a regexp based linter that allows you to define custom rules in a
YAML file.


%package       -n goodcheck
Version:       3.1.0
Release:       alt1
Summary:       Regexp based customizable linter executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета goodcheck
Group:         Other
BuildArch:     noarch

Requires:      gem(goodcheck) = 3.1.0

%description   -n goodcheck
Regexp based customizable linter executable(s).

Goodcheck is a regexp based linter that allows you to define custom rules in a
YAML file.

%description   -n goodcheck -l ru_RU.UTF-8
Исполнямка для самоцвета goodcheck.


%package       -n gem-goodcheck-doc
Version:       3.1.0
Release:       alt1
Summary:       Regexp based customizable linter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета goodcheck
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(goodcheck) = 3.1.0

%description   -n gem-goodcheck-doc
Regexp based customizable linter documentation files.

Goodcheck is a regexp based linter that allows you to define custom rules in a
YAML file.

%description   -n gem-goodcheck-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета goodcheck.


%package       -n gem-goodcheck-devel
Version:       3.1.0
Release:       alt1
Summary:       Regexp based customizable linter development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета goodcheck
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(goodcheck) = 3.1.0
Requires:      gem(bundler) >= 1.16
Requires:      gem(rake) >= 13.0
Requires:      gem(minitest) >= 5.0
Requires:      gem(simplecov) >= 0.17

%description   -n gem-goodcheck-devel
Regexp based customizable linter development package.

Goodcheck is a regexp based linter that allows you to define custom rules in a
YAML file.

%description   -n gem-goodcheck-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета goodcheck.


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

%files         -n goodcheck
%doc README.md
%_bindir/goodcheck

%files         -n gem-goodcheck-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-goodcheck-devel
%doc README.md


%changelog
* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- + packaged gem with Ruby Policy 2.0
