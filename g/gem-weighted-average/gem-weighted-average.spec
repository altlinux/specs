%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname weighted_average

Name:          gem-weighted-average
Version:       2.0.2.4
Release:       alt1
Summary:       Perform weighted averages. Rails 3 only
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seamusabshere/weighted_average
Vcs:           https://github.com/seamusabshere/weighted_average.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(activerecord) >= 6.0
BuildRequires: gem(cohort_analysis) >= 0.2.1
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mysql2) >= 0
BuildRequires: gem(pg) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(activerecord) >= 9.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names weighted_average,weighted-average
Requires:      gem(activerecord) >= 6.0
Conflicts:     gem(activerecord) >= 9.0
Provides:      weighted_average = %EVR
Provides:      gem(weighted_average) = 2.0.2.4

%description
Perform weighted averages, even across associations. Rails 3 only because it
uses ARel.


%if_enabled    doc
%package       -n gem-weighted-average-doc
Version:       2.0.2.4
Release:       alt1
Summary:       Perform weighted averages. Rails 3 only documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета weighted_average
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(weighted_average) = 2.0.2.4

%description   -n gem-weighted-average-doc
Perform weighted averages. Rails 3 only documentation files.

Perform weighted averages, even across associations. Rails 3 only because it
uses ARel.

%description   -n gem-weighted-average-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета weighted_average.
%endif


%if_enabled    devel
%package       -n gem-weighted-average-devel
Version:       2.0.2.4
Release:       alt1
Summary:       Perform weighted averages. Rails 3 only development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета weighted_average
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(weighted_average) = 2.0.2.4
Requires:      gem(cohort_analysis) >= 0.2.1
Requires:      gem(minitest) >= 0
Requires:      gem(mysql2) >= 0
Requires:      gem(pg) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(yard) >= 0

%description   -n gem-weighted-average-devel
Perform weighted averages. Rails 3 only development package.

Perform weighted averages, even across associations. Rails 3 only because it
uses ARel.

%description   -n gem-weighted-average-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета weighted_average.
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
%doc CHANGELOG LICENSE README.markdown
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-weighted-average-doc
%doc CHANGELOG LICENSE README.markdown
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-weighted-average-devel
%doc CHANGELOG LICENSE README.markdown
%endif


%changelog
* Wed Mar 12 2025 Pavel Skrylev <majioa@altlinux.org> 2.0.2.4-alt1
- + explicit require for active_support for suppress undefined methods
  (ALT #53415)

* Mon Jan 27 2025 Pavel Skrylev <majioa@altlinux.org> 2.0.2.3-alt1
- ^ 2.0.2 -> 2.0.2p3

* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 2.0.2-alt1
- + packaged gem with Ruby Policy 2.0
