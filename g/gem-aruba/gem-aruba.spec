%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname aruba

Name:          gem-aruba
Version:       2.4.1
Release:       alt1
Summary:       Test command line applications with Cucumber, RSpec or Minitest
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cucumber/aruba
Vcs:           https://github.com/cucumber/aruba.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(appraisal) >= 2.4
BuildRequires: gem(bundler) >= 1.17
BuildRequires: gem(contracts) >= 0.16.0
BuildRequires: gem(cucumber) >= 8.0
BuildRequires: gem(diff-lcs) >= 1.6
BuildRequires: gem(irb) >= 1.16
BuildRequires: gem(json) >= 2.1
BuildRequires: gem(kramdown) >= 2.1
BuildRequires: gem(minitest) >= 5.26.0
BuildRequires: gem(rake) >= 12.0
BuildRequires: gem(rake-manifest) >= 0.2.0
BuildRequires: gem(rspec) >= 3.11
BuildRequires: gem(rspec-expectations) >= 3.4
BuildRequires: gem(rubocop) >= 1.80
BuildRequires: gem(rubocop-packaging) >= 0.5.2
BuildRequires: gem(rubocop-performance) >= 1.26
BuildRequires: gem(rubocop-rspec) >= 3.7
BuildRequires: gem(simplecov) >= 0.18.0
BuildRequires: gem(thor) >= 1.0
BuildConflicts: gem(appraisal) >= 3
BuildConflicts: gem(contracts) >= 0.18.0
BuildConflicts: gem(cucumber) >= 12.0
BuildConflicts: gem(diff-lcs) >= 3
BuildConflicts: gem(irb) >= 2
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(kramdown) >= 3
BuildConflicts: gem(minitest) >= 7.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-manifest) >= 1
BuildConflicts: gem(rspec) >= 5.0
BuildConflicts: gem(rspec-expectations) >= 5.0
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(thor) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency diff-lcs >= 2.0.0,diff-lcs < 3
%ruby_use_gem_dependency rake-manifest >= 0.2.3,rake-manifest < 1
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
%ruby_use_gem_dependency simplecov >= 0.22.0,simplecov < 1
Requires:      ruby >= 3.0.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(contracts) >= 0.16.0
Requires:      gem(cucumber) >= 8.0
Requires:      gem(irb) >= 1.16
Requires:      gem(rspec-expectations) >= 3.4
Requires:      gem(thor) >= 1.0
Conflicts:     gem(contracts) >= 0.18.0
Conflicts:     gem(cucumber) >= 12.0
Conflicts:     gem(irb) >= 2
Conflicts:     gem(rspec-expectations) >= 5.0
Conflicts:     gem(thor) >= 2
Provides:      gem(aruba) = 2.4.1

%description
Extension for popular TDD and BDD frameworks like "Cucumber", "RSpec" and
"Minitest", to make testing command line applications meaningful, easy and fun.


%package       -n aruba
Version:       2.4.1
Release:       alt1
Summary:       Test command line applications with Cucumber, RSpec or Minitest executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета aruba
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(aruba) = 2.4.1

%description   -n aruba
Test command line applications with Cucumber, RSpec or Minitest
executable(s).

Extension for popular TDD and BDD frameworks like "Cucumber", "RSpec" and
"Minitest", to make testing command line applications meaningful, easy and fun.

%description   -n aruba -l ru_RU.UTF-8
Исполнямка для самоцвета aruba.


%if_enabled    doc
%package       -n gem-aruba-doc
Version:       2.4.1
Release:       alt1
Summary:       Test command line applications with Cucumber, RSpec or Minitest documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета aruba
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(aruba) = 2.4.1

%description   -n gem-aruba-doc
Test command line applications with Cucumber, RSpec or Minitest documentation
files.

Extension for popular TDD and BDD frameworks like "Cucumber", "RSpec" and
"Minitest", to make testing command line applications meaningful, easy and fun.

%description   -n gem-aruba-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета aruba.
%endif


%if_enabled    devel
%package       -n gem-aruba-devel
Version:       2.4.1
Release:       alt1
Summary:       Test command line applications with Cucumber, RSpec or Minitest development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета aruba
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(aruba) = 2.4.1
Requires:      gem(appraisal) >= 2.4
Requires:      gem(diff-lcs) >= 1.6
Requires:      gem(json) >= 2.1
Requires:      gem(kramdown) >= 2.1
Requires:      gem(minitest) >= 5.26.0
Requires:      gem(rake) >= 12.0
Requires:      gem(rake-manifest) >= 0.2.0
Requires:      gem(rspec) >= 3.11
Requires:      gem(rubocop) >= 1.80
Requires:      gem(rubocop-packaging) >= 0.5.2
Requires:      gem(rubocop-performance) >= 1.26
Requires:      gem(rubocop-rspec) >= 3.7
Requires:      gem(simplecov) >= 0.18.0
Conflicts:     gem(appraisal) >= 3
Conflicts:     gem(diff-lcs) >= 3
Conflicts:     gem(json) >= 3
Conflicts:     gem(kramdown) >= 3
Conflicts:     gem(minitest) >= 7.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-manifest) >= 1
Conflicts:     gem(rspec) >= 5.0
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rspec) >= 4
Conflicts:     gem(simplecov) >= 1

%description   -n gem-aruba-devel
Test command line applications with Cucumber, RSpec or Minitest development
package.

Extension for popular TDD and BDD frameworks like "Cucumber", "RSpec" and
"Minitest", to make testing command line applications meaningful, easy and fun.

%description   -n gem-aruba-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета aruba.
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
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n aruba
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md
%_bindir/aruba

%if_enabled    doc
%files         -n gem-aruba-doc
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-aruba-devel
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md
%endif


%changelog
* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 2.4.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
