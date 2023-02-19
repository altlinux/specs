%define        gemname licensee

Name:          gem-licensee
Version:       9.16.0
Release:       alt1
Summary:       A Ruby Gem to detect open source project licenses
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/benbalter/licensee
Vcs:           https://github.com/benbalter/licensee.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(faraday) >= 2.0
BuildRequires: gem(faraday-retry) >= 0
BuildRequires: gem(gem-release) >= 2.0
BuildRequires: gem(mustache) >= 0.9
BuildRequires: gem(pry) >= 0.9
BuildRequires: gem(rspec) >= 3.5
BuildRequires: gem(rubocop) >= 1.0
BuildRequires: gem(rubocop-performance) >= 1.5
BuildRequires: gem(rubocop-rspec) >= 2.0
BuildRequires: gem(simplecov) >= 0.16
BuildRequires: gem(webmock) >= 3.1
BuildRequires: gem(dotenv) >= 2.0
BuildRequires: gem(octokit) >= 4.20
BuildRequires: gem(reverse_markdown) >= 1
BuildRequires: gem(rugged) >= 0.24
BuildRequires: gem(thor) >= 0.19
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(gem-release) >= 3
BuildConflicts: gem(mustache) >= 2.0
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(dotenv) >= 3
BuildConflicts: gem(octokit) >= 7.0
BuildConflicts: gem(reverse_markdown) >= 3
BuildConflicts: gem(rugged) >= 2.0
BuildConflicts: gem(thor) >= 2.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency reverse_markdown >= 2.1.1,reverse_markdown < 3
%ruby_use_gem_dependency octokit >= 5.0,octokit < 7
Requires:      gem(dotenv) >= 2.0
Requires:      gem(octokit) >= 4.20
Requires:      gem(reverse_markdown) >= 1
Requires:      gem(rugged) >= 0.24
Requires:      gem(thor) >= 0.19
Conflicts:     gem(dotenv) >= 3
Conflicts:     gem(octokit) >= 7.0
Conflicts:     gem(reverse_markdown) >= 3
Conflicts:     gem(rugged) >= 2.0
Conflicts:     gem(thor) >= 2.0
Provides:      gem(licensee) = 9.16.0


%description
Licensee automates the process of reading LICENSE files and compares their
contents to known licenses using a fancy maths.


%package       -n licensee
Version:       9.16.0
Release:       alt1
Summary:       A Ruby Gem to detect open source project licenses executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета licensee
Group:         Other
BuildArch:     noarch

Requires:      gem(licensee) = 9.16.0

%description   -n licensee
A Ruby Gem to detect open source project licenses executable(s).

Licensee automates the process of reading LICENSE files and compares their
contents to known licenses using a fancy maths.

%description   -n licensee -l ru_RU.UTF-8
Исполнямка для самоцвета licensee.


%package       -n gem-licensee-doc
Version:       9.16.0
Release:       alt1
Summary:       A Ruby Gem to detect open source project licenses documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета licensee
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(licensee) = 9.16.0

%description   -n gem-licensee-doc
A Ruby Gem to detect open source project licenses documentation files.

Licensee automates the process of reading LICENSE files and compares their
contents to known licenses using a fancy maths.

%description   -n gem-licensee-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета licensee.


%package       -n gem-licensee-devel
Version:       9.16.0
Release:       alt1
Summary:       A Ruby Gem to detect open source project licenses development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета licensee
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(licensee) = 9.16.0
Requires:      gem(faraday) >= 2.0
Requires:      gem(faraday-retry) >= 0
Requires:      gem(gem-release) >= 2.0
Requires:      gem(mustache) >= 0.9
Requires:      gem(pry) >= 0.9
Requires:      gem(rspec) >= 3.5
Requires:      gem(rubocop) >= 1.0
Requires:      gem(rubocop-performance) >= 1.5
Requires:      gem(rubocop-rspec) >= 2.0
Requires:      gem(simplecov) >= 0.16
Requires:      gem(webmock) >= 3.1
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(gem-release) >= 3
Conflicts:     gem(mustache) >= 2.0
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rspec) >= 3
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(webmock) >= 4

%description   -n gem-licensee-devel
A Ruby Gem to detect open source project licenses development package.

Licensee automates the process of reading LICENSE files and compares their
contents to known licenses using a fancy maths.

%description   -n gem-licensee-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета licensee.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n licensee
%_bindir/licensee

%files         -n gem-licensee-doc
%ruby_gemdocdir

%files         -n gem-licensee-devel


%changelog
* Sun Feb 19 2023 Pavel Skrylev <majioa@altlinux.org> 9.16.0-alt1
- ^ 9.15.2 -> 9.16.0

* Wed Oct 19 2022 Pavel Skrylev <majioa@altlinux.org> 9.15.2-alt1.1
- !deps to novel

* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 9.15.2-alt1
- + packaged gem with Ruby Policy 2.0
