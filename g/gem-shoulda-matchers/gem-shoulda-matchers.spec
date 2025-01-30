%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname shoulda-matchers

Name:          gem-shoulda-matchers
Version:       6.4.0
Release:       alt1
Summary:       Simple one-liner tests for common Rails functionality
License:       MIT
Group:         Development/Ruby
Url:           https://matchers.shoulda.io/
Vcs:           https://github.com/thoughtbot/shoulda-matchers.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activesupport) >= 5.2.0
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(rake) >= 13.0.1
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildRequires: gem(appraisal) >= 2.4.0
BuildRequires: gem(fssm) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(rouge) >= 0
BuildRequires: gem(rspec) >= 3.9
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-packaging) >= 0
BuildRequires: gem(rubocop-rails) >= 0
BuildRequires: gem(warnings_logger) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(zeus) >= 0
BuildConflicts: gem(appraisal) >= 3
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency appraisal >= 2.4.0,appraisal < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Requires:      ruby >= 3.0.5
Requires:      gem(activesupport) >= 5.2.0
Requires:      gem(fssm) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(rouge) >= 0
Requires:      gem(warnings_logger) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(zeus) >= 0
Provides:      shoulda-matchers = %EVR
Provides:      gem(shoulda-matchers) = 6.4.0

%description
Shoulda Matchers provides RSpec- and Minitest-compatible one-liners to test
common Rails functionality that, if written by hand, would be much longer, more
complex, and error-prone.


%if_enabled    doc
%package       -n gem-shoulda-matchers-doc
Version:       6.4.0
Release:       alt1
Summary:       Simple one-liner tests for common Rails functionality documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета shoulda-matchers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(shoulda-matchers) = 6.4.0

%description   -n gem-shoulda-matchers-doc
Simple one-liner tests for common Rails functionality documentation
files.

Shoulda Matchers provides RSpec- and Minitest-compatible one-liners to test
common Rails functionality that, if written by hand, would be much longer, more
complex, and error-prone.

%description   -n gem-shoulda-matchers-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета shoulda-matchers.
%endif


%if_enabled    devel
%package       -n gem-shoulda-matchers-devel
Version:       6.4.0
Release:       alt1
Summary:       Simple one-liner tests for common Rails functionality development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета shoulda-matchers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(shoulda-matchers) = 6.4.0
Requires:      gem(appraisal) >= 2.4.0
Requires:      gem(bundler) >= 2.0
Requires:      gem(rake) >= 13.0.1
Requires:      gem(rspec) >= 3.9
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-packaging) >= 0
Requires:      gem(rubocop-rails) >= 0
Conflicts:     gem(appraisal) >= 3
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-shoulda-matchers-devel
Simple one-liner tests for common Rails functionality development
package.

Shoulda Matchers provides RSpec- and Minitest-compatible one-liners to test
common Rails functionality that, if written by hand, would be much longer, more
complex, and error-prone.

%description   -n gem-shoulda-matchers-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета shoulda-matchers.
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
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-shoulda-matchers-doc
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-shoulda-matchers-devel
%doc LICENSE README.md CHANGELOG.md CONTRIBUTING.md
%endif


%changelog
* Mon Jan 13 2025 Pavel Skrylev <majioa@altlinux.org> 6.4.0-alt1
- ^ 4.5.1 -> 6.4.0

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 4.5.1-alt1
- + packaged gem with Ruby Policy 2.0
