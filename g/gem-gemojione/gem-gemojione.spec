%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname gemojione

Name:          gem-gemojione
Version:       4.3.3
Release:       alt1
Summary:       A gem for EmojiOne
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bonusly/gemojione
Vcs:           https://github.com/bonusly/gemojione.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(codeclimate-test-reporter) >= 1.0.0
BuildRequires: gem(json) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rmagick) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(sprite-factory) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency codeclimate-test-reporter >= 1.0.0
Requires:      gem(json) >= 0
Provides:      gem(gemojione) = 4.3.3

%description
A gem for EmojiOne


%if_enabled    doc
%package       -n gem-gemojione-doc
Version:       4.3.3
Release:       alt1
Summary:       A gem for EmojiOne documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gemojione
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gemojione) = 4.3.3

%description   -n gem-gemojione-doc
A gem for EmojiOne documentation files.

%description   -n gem-gemojione-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gemojione.
%endif


%if_enabled    devel
%package       -n gem-gemojione-devel
Version:       4.3.3
Release:       alt1
Summary:       A gem for EmojiOne development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gemojione
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gemojione) = 4.3.3
Requires:      gem(bundler) >= 0
Requires:      gem(codeclimate-test-reporter) >= 1.0.0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rmagick) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(sprite-factory) >= 0

%description   -n gem-gemojione-devel
A gem for EmojiOne development package.

%description   -n gem-gemojione-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gemojione.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-gemojione-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-gemojione-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Tue Sep 22 2026 Pavel Skrylev <majioa@altlinux.org> 4.3.3-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
