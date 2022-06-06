%define        gemname weighted_average

Name:          gem-weighted-average
Version:       2.0.2
Release:       alt1
Summary:       Perform weighted averages. Rails 3 only
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seamusabshere/weighted_average
Vcs:           https://github.com/seamusabshere/weighted_average.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         dep.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activesupport) >= 3 gem(activesupport) < 7
BuildRequires: gem(arel) >= 2
BuildRequires: gem(cohort_analysis) >= 0.2.1
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(mysql2) >= 0
BuildRequires: gem(pg) >= 0
BuildRequires: gem(activerecord) >= 3 gem(activerecord) < 7
BuildRequires: gem(yard) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency activesupport >= 6.1.3.2,activesupport < 7
%ruby_use_gem_dependency activerecord >= 6.1.3.2,activerecord < 7
Requires:      gem(activesupport) >= 3 gem(activesupport) < 7
Requires:      gem(arel) >= 2
Provides:      gem(weighted_average) = 2.0.2


%description
Perform weighted averages, even across associations. Rails 3 only because it
uses ARel.


%package       -n gem-weighted-average-doc
Version:       2.0.2
Release:       alt1
Summary:       Perform weighted averages. Rails 3 only documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета weighted_average
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(weighted_average) = 2.0.2

%description   -n gem-weighted-average-doc
Perform weighted averages. Rails 3 only documentation files.

Perform weighted averages, even across associations. Rails 3 only because it
uses ARel.

%description   -n gem-weighted-average-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета weighted_average.


%package       -n gem-weighted-average-devel
Version:       2.0.2
Release:       alt1
Summary:       Perform weighted averages. Rails 3 only development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета weighted_average
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(weighted_average) = 2.0.2
Requires:      gem(cohort_analysis) >= 0.2.1
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(mysql2) >= 0
Requires:      gem(pg) >= 0
Requires:      gem(activerecord) >= 3 gem(activerecord) < 7
Requires:      gem(yard) >= 0

%description   -n gem-weighted-average-devel
Perform weighted averages. Rails 3 only development package.

Perform weighted averages, even across associations. Rails 3 only because it
uses ARel.

%description   -n gem-weighted-average-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета weighted_average.


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

%files         -n gem-weighted-average-doc
%doc README.markdown
%ruby_gemdocdir

%files         -n gem-weighted-average-devel
%doc README.markdown


%changelog
* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 2.0.2-alt1
- + packaged gem with Ruby Policy 2.0
