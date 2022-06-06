%define        gemname cohort_analysis

Name:          gem-cohort-analysis
Version:       1.0.3
Release:       alt1
Summary:       Lets you do cohort analysis based on two strategies: "big", which discards characteristics for the maximum cohort result, and "strict", which discards characteristics in order until a minimum cohort size is reached
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seamusabshere/cohort_analysis
Vcs:           https://github.com/seamusabshere/cohort_analysis.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         bot.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activesupport) >= 3
BuildRequires: gem(arel) >= 3
BuildRequires: gem(activerecord) >= 3
BuildRequires: gem(active_record_inline_schema) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-reporters) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(factory_bot) >= 0
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(mysql2) >= 0
BuildRequires: gem(pg) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(activesupport) >= 3
Requires:      gem(arel) >= 3
Provides:      gem(cohort_analysis) = 1.0.3


%description
Lets you do cohort analysis based on two strategies: "big", which discards
characteristics for the maximum cohort result, and "strict", which discards
characteristics in order until a minimum cohort size is reached.


%package       -n gem-cohort-analysis-doc
Version:       1.0.3
Release:       alt1
Summary:       Lets you do cohort analysis based on two strategies: "big", which discards characteristics for the maximum cohort result, and "strict", which discards characteristics in order until a minimum cohort size is reached documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cohort_analysis
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(cohort_analysis) = 1.0.3

%description   -n gem-cohort-analysis-doc
Lets you do cohort analysis based on two strategies: "big", which discards
characteristics for the maximum cohort result, and "strict", which discards
characteristics in order until a minimum cohort size is reached documentation
files.

%description   -n gem-cohort-analysis-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cohort_analysis.


%package       -n gem-cohort-analysis-devel
Version:       1.0.3
Release:       alt1
Summary:       Lets you do cohort analysis based on two strategies: "big", which discards characteristics for the maximum cohort result, and "strict", which discards characteristics in order until a minimum cohort size is reached development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cohort_analysis
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(cohort_analysis) = 1.0.3
Requires:      gem(activerecord) >= 3
Requires:      gem(active_record_inline_schema) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(minitest-reporters) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(factory_bot) >= 0
Requires:      gem(sqlite3) >= 0
Requires:      gem(mysql2) >= 0
Requires:      gem(pg) >= 0

%description   -n gem-cohort-analysis-devel
Lets you do cohort analysis based on two strategies: "big", which discards
characteristics for the maximum cohort result, and "strict", which discards
characteristics in order until a minimum cohort size is reached development
package.

%description   -n gem-cohort-analysis-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cohort_analysis.


%prep
%setup
%autopatch

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

%files         -n gem-cohort-analysis-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-cohort-analysis-devel
%doc README.markdown


%changelog
* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.3-alt1
- + packaged gem with Ruby Policy 2.0
