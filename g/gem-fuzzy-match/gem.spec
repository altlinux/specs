%define        gemname fuzzy_match

Name:          gem-fuzzy-match
Version:       2.1.0
Release:       alt1
Summary:       Find a needle in a haystack using string similarity and (optionally) regexp rules. Replaces loose_tight_dictionary
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seamusabshere/fuzzy_match
Vcs:           https://github.com/seamusabshere/fuzzy_match.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(active_record_inline_schema) >= 0.4.0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rspec-core) >= 0
BuildRequires: gem(rspec-expectations) >= 0
BuildRequires: gem(rspec-mocks) >= 0
BuildRequires: gem(activerecord) >= 3
BuildRequires: gem(mysql2) >= 0
BuildRequires: gem(cohort_analysis) >= 0
BuildRequires: gem(weighted_average) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(amatch) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(fuzzy_match) = 2.1.0


%description
Find a needle in a haystack using string similarity and (optionally) regexp
rules. Replaces loose_tight_dictionary.


%package       -n fuzzy-match
Version:       2.1.0
Release:       alt1
Summary:       Find a needle in a haystack using string similarity and (optionally) regexp rules. Replaces loose_tight_dictionary executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета fuzzy_match
Group:         Other
BuildArch:     noarch

Requires:      gem(fuzzy_match) = 2.1.0

%description   -n fuzzy-match
Find a needle in a haystack using string similarity and (optionally) regexp
rules. Replaces loose_tight_dictionary executable(s).

%description   -n fuzzy-match -l ru_RU.UTF-8
Исполнямка для самоцвета fuzzy_match.


%package       -n gem-fuzzy-match-doc
Version:       2.1.0
Release:       alt1
Summary:       Find a needle in a haystack using string similarity and (optionally) regexp rules. Replaces loose_tight_dictionary documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fuzzy_match
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fuzzy_match) = 2.1.0

%description   -n gem-fuzzy-match-doc
Find a needle in a haystack using string similarity and (optionally) regexp
rules. Replaces loose_tight_dictionary documentation files.

%description   -n gem-fuzzy-match-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fuzzy_match.


%package       -n gem-fuzzy-match-devel
Version:       2.1.0
Release:       alt1
Summary:       Find a needle in a haystack using string similarity and (optionally) regexp rules. Replaces loose_tight_dictionary development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fuzzy_match
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fuzzy_match) = 2.1.0
Requires:      gem(active_record_inline_schema) >= 0.4.0
Requires:      gem(pry) >= 0
Requires:      gem(rspec-core) >= 0
Requires:      gem(rspec-expectations) >= 0
Requires:      gem(rspec-mocks) >= 0
Requires:      gem(activerecord) >= 3
Requires:      gem(mysql2) >= 0
Requires:      gem(cohort_analysis) >= 0
Requires:      gem(weighted_average) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(amatch) >= 0

%description   -n gem-fuzzy-match-devel
Find a needle in a haystack using string similarity and (optionally) regexp
rules. Replaces loose_tight_dictionary development package.

%description   -n gem-fuzzy-match-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fuzzy_match.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n fuzzy-match
%doc README.markdown
%_bindir/fuzzy_match

%files         -n gem-fuzzy-match-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-fuzzy-match-devel
%doc README.markdown


%changelog
* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- + packaged gem with Ruby Policy 2.0
