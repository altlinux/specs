%define        gemname retryable

Name:          gem-retryable
Version:       3.0.5
Release:       alt1
Summary:       Kernel#retryable, by Cheah Chu Yeow (http://is.gd/faW9), slightly enhanced and rebuilt as gem as a little Munich Hackday project
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/nfedyashev/retryable
Vcs:           https://github.com/nfedyashev/retryable/tree/master.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 10.4
BuildRequires: gem(yard) >= 0
BuildRequires: gem(fasterer) >= 0
BuildRequires: gem(overcommit) >= 0
BuildRequires: gem(pry) >= 0.9.12.6
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(codeclimate-test-reporter) >= 0
BuildRequires: gem(rspec) >= 3.1
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(bundler) >= 0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
Obsoletes:     ruby-retryable < %EVR
Provides:      ruby-retryable = %EVR
Provides:      gem(retryable) = 3.0.5


%description
Kernel#retryable, by Cheah Chu Yeow (http://is.gd/faW9), slightly enhanced and
rebuilt as gem as a little Munich Hackday project.


%package       -n gem-retryable-doc
Version:       3.0.5
Release:       alt1
Summary:       Kernel#retryable, by Cheah Chu Yeow (http://is.gd/faW9), slightly enhanced and rebuilt as gem as a little Munich Hackday project documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета retryable
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(retryable) = 3.0.5

%description   -n gem-retryable-doc
Kernel#retryable, by Cheah Chu Yeow (http://is.gd/faW9), slightly enhanced and
rebuilt as gem as a little Munich Hackday project documentation files.

%description   -n gem-retryable-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета retryable.


%package       -n gem-retryable-devel
Version:       3.0.5
Release:       alt1
Summary:       Kernel#retryable, by Cheah Chu Yeow (http://is.gd/faW9), slightly enhanced and rebuilt as gem as a little Munich Hackday project development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета retryable
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(retryable) = 3.0.5
Requires:      gem(rake) >= 10.4
Requires:      gem(yard) >= 0
Requires:      gem(fasterer) >= 0
Requires:      gem(overcommit) >= 0
Requires:      gem(pry) >= 0.9.12.6
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(codeclimate-test-reporter) >= 0
Requires:      gem(rspec) >= 3.1
Requires:      gem(simplecov) >= 0
Requires:      gem(bundler) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rspec) >= 4

%description   -n gem-retryable-devel
Kernel#retryable, by Cheah Chu Yeow (http://is.gd/faW9), slightly enhanced and
rebuilt as gem as a little Munich Hackday project development package.

%description   -n gem-retryable-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета retryable.


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

%files         -n gem-retryable-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-retryable-devel
%doc README.md


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 3.0.5-alt1
- ^ 3.0.2 -> 3.0.5

* Tue Sep 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.2-alt1
- New version.

* Mon May 28 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus
