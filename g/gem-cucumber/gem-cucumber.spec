%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname cucumber

Name:          gem-cucumber
Version:       11.1.1
Release:       alt1
Summary:       cucumber-11.1.1
License:       MIT
Group:         Development/Ruby
Url:           https://cucumber.io/
Vcs:           https://github.com/cucumber/cucumber-ruby.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(base64) >= 0.2
BuildRequires: gem(builder) >= 3.2
BuildRequires: gem(cucumber-ci-environment) > 9
BuildRequires: gem(cucumber-compatibility-kit) >= 24.0
BuildRequires: gem(cucumber-core) >= 16.2.0
BuildRequires: gem(cucumber-cucumber-expressions) > 17
BuildRequires: gem(cucumber-html-formatter) > 21
BuildRequires: gem(diff-lcs) >= 1.5
BuildRequires: gem(logger) >= 1.6
BuildRequires: gem(mini_mime) >= 1.1
BuildRequires: gem(multi_test) >= 1.1
BuildRequires: gem(nokogiri) >= 1.15
BuildRequires: gem(rake) >= 13.2
BuildRequires: gem(rspec) >= 3.13
BuildRequires: gem(rubocop) >= 1.81.6
BuildRequires: gem(rubocop-packaging) >= 0.5.2
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-rspec) >= 3.7.0
BuildRequires: gem(simplecov) >= 0.22.0
BuildRequires: gem(sys-uname) >= 1.5
BuildRequires: gem(webrick) >= 1.8
BuildConflicts: gem(base64) >= 1
BuildConflicts: gem(builder) >= 4
BuildConflicts: gem(cucumber-ci-environment) >= 15
BuildConflicts: gem(cucumber-compatibility-kit) >= 30
BuildConflicts: gem(cucumber-core) >= 18
BuildConflicts: gem(cucumber-cucumber-expressions) >= 21
BuildConflicts: gem(cucumber-html-formatter) >= 25
BuildConflicts: gem(diff-lcs) >= 3
BuildConflicts: gem(logger) >= 2
BuildConflicts: gem(mini_mime) >= 2
BuildConflicts: gem(multi_test) >= 2
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(sys-uname) >= 2
BuildConflicts: gem(webrick) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency cucumber-ci-environment >= 14.0.0,cucumber-ci-environment < 15
%ruby_use_gem_dependency cucumber-compatibility-kit >= 29.2.2,cucumber-compatibility-kit < 30
%ruby_use_gem_dependency cucumber-core >= 17.0.0,cucumber-core < 18
%ruby_use_gem_dependency cucumber-cucumber-expressions >= 20.0.0,cucumber-cucumber-expressions < 21
%ruby_use_gem_dependency cucumber-html-formatter >= 24.0.0,cucumber-html-formatter < 25
%ruby_use_gem_dependency diff-lcs >= 2.0.0,diff-lcs < 3
%ruby_use_gem_dependency rubocop >= 1.81.6,rubocop < 2
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
%ruby_use_gem_dependency rubocop-rake >= 0.7.1,rubocop-rake < 1
%ruby_use_gem_dependency rubocop-rspec >= 3.7.0,rubocop-rspec < 4
%ruby_use_gem_dependency simplecov >= 0.22.0,simplecov < 1
Requires:      ruby >= 3.2
Requires:      rubygems >= 3.2.8
Requires:      gem(base64) >= 0.2
Requires:      gem(builder) >= 3.2
Requires:      gem(cucumber-ci-environment) > 9
Requires:      gem(cucumber-core) >= 16.2.0
Requires:      gem(cucumber-cucumber-expressions) > 17
Requires:      gem(cucumber-html-formatter) > 21
Requires:      gem(diff-lcs) >= 1.5
Requires:      gem(logger) >= 1.6
Requires:      gem(mini_mime) >= 1.1
Requires:      gem(multi_test) >= 1.1
Requires:      gem(sys-uname) >= 1.5
Conflicts:     gem(base64) >= 1
Conflicts:     gem(builder) >= 4
Conflicts:     gem(cucumber-ci-environment) >= 15
Conflicts:     gem(cucumber-core) >= 18
Conflicts:     gem(cucumber-cucumber-expressions) >= 21
Conflicts:     gem(cucumber-html-formatter) >= 25
Conflicts:     gem(diff-lcs) >= 3
Conflicts:     gem(logger) >= 2
Conflicts:     gem(mini_mime) >= 2
Conflicts:     gem(multi_test) >= 2
Conflicts:     gem(sys-uname) >= 2
Provides:      gem(cucumber) = 11.1.1

%description
Behaviour Driven Development with elegance and joy


%package       -n cucumber
Version:       11.1.1
Release:       alt1
Summary:       cucumber-11.1.1 executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета cucumber
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber) = 11.1.1

%description   -n cucumber
cucumber-11.1.1 executable(s).

Behaviour Driven Development with elegance and joy

%description   -n cucumber -l ru_RU.UTF-8
Исполнямка для самоцвета cucumber.


%if_enabled    doc
%package       -n gem-cucumber-doc
Version:       11.1.1
Release:       alt1
Summary:       cucumber-11.1.1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cucumber
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber) = 11.1.1

%description   -n gem-cucumber-doc
cucumber-11.1.1 documentation files.

Behaviour Driven Development with elegance and joy

%description   -n gem-cucumber-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cucumber.
%endif


%if_enabled    devel
%package       -n gem-cucumber-devel
Version:       11.1.1
Release:       alt1
Summary:       cucumber-11.1.1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cucumber
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cucumber) = 11.1.1
Requires:      gem(cucumber-compatibility-kit) >= 24.0
Requires:      gem(nokogiri) >= 1.15
Requires:      gem(rake) >= 13.2
Requires:      gem(rspec) >= 3.13
Requires:      gem(rubocop) >= 1.81.6
Requires:      gem(rubocop-packaging) >= 0.5.2
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-rspec) >= 3.7.0
Requires:      gem(simplecov) >= 0.22.0
Requires:      gem(webrick) >= 1.8
Conflicts:     gem(cucumber-compatibility-kit) >= 30
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 4
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(webrick) >= 2

%description   -n gem-cucumber-devel
cucumber-11.1.1 development package.

Behaviour Driven Development with elegance and joy

%description   -n gem-cucumber-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cucumber.
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
%doc LICENSE README.md CHANGELOG.md CHANGELOG.old.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n cucumber
%doc LICENSE README.md CHANGELOG.md CHANGELOG.old.md CONTRIBUTING.md
%_bindir/cucumber

%if_enabled    doc
%files         -n gem-cucumber-doc
%doc LICENSE README.md CHANGELOG.md CHANGELOG.old.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-cucumber-devel
%doc LICENSE README.md CHANGELOG.md CHANGELOG.old.md CONTRIBUTING.md
%endif


%changelog
* Mon Jul 06 2026 Alexander Burmatov <thatman@altlinux.org> 11.1.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
