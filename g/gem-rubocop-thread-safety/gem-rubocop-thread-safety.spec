%define        _unpackaged_files_terminate_build 1
%define        gemname rubocop-thread_safety

Name:          gem-rubocop-thread-safety
Version:       0.5.1
Release:       alt1
Summary:       Thread-safety checks via static analysis
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubocop/rubocop-thread_safety
Vcs:           https://github.com/rubocop/rubocop-thread_safety.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(bundler) >= 1.10
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 0.90.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rubocop) >= 0.90.0
Provides:      gem(rubocop-thread_safety) = 0.5.1


%description
Thread-safety checks via static analysis. A plugin for the RuboCop code style
enforcing & linting tool.


%package       -n gem-rubocop-thread-safety-doc
Version:       0.5.1
Release:       alt1
Summary:       Thread-safety checks via static analysis documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-thread_safety
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-thread_safety) = 0.5.1

%description   -n gem-rubocop-thread-safety-doc
Thread-safety checks via static analysis documentation files.

Thread-safety checks via static analysis. A plugin for the RuboCop code style
enforcing & linting tool.

%description   -n gem-rubocop-thread-safety-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-thread_safety.


%package       -n gem-rubocop-thread-safety-devel
Version:       0.5.1
Release:       alt1
Summary:       Thread-safety checks via static analysis development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-thread_safety
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-thread_safety) = 0.5.1
Requires:      gem(appraisal) >= 0
Requires:      gem(bundler) >= 1.10
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 10.0
Requires:      gem(rspec) >= 3.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rspec) >= 4

%description   -n gem-rubocop-thread-safety-devel
Thread-safety checks via static analysis development package.

Thread-safety checks via static analysis. A plugin for the RuboCop code style
enforcing & linting tool.

%description   -n gem-rubocop-thread-safety-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-thread_safety.


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

%files         -n gem-rubocop-thread-safety-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-thread-safety-devel
%doc README.md


%changelog
* Mon Dec 11 2023 Pavel Skrylev <majioa@altlinux.org> 0.5.1-alt1
- + packaged gem with Ruby Policy 2.0
