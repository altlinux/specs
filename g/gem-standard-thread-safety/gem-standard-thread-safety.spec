%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname standard-thread_safety

Name:          gem-standard-thread-safety
Version:       1.0.0
Release:       alt1
Summary:       A Standard Ruby plugin that configures rubocop-thread_safety
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/kirillplatonov/standard-thread_safety
Vcs:           https://github.com/kirillplatonov/standard-thread_safety.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(lint_roller) >= 1.0
BuildRequires: gem(rubocop-thread_safety) >= 0
BuildConflicts: gem(lint_roller) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(lint_roller) >= 1.0
Requires:      gem(rubocop-thread_safety) >= 0
Conflicts:     gem(lint_roller) >= 2
Provides:      gem(standard-thread_safety) = 1.0.0


%description
A Standard Ruby plugin that configures rubocop-thread_safety


%if_enabled    doc
%package       -n gem-standard-thread-safety-doc
Version:       1.0.0
Release:       alt1
Summary:       A Standard Ruby plugin that configures rubocop-thread_safety documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета standard-thread_safety
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(standard-thread_safety) = 1.0.0

%description   -n gem-standard-thread-safety-doc
A Standard Ruby plugin that configures rubocop-thread_safety documentation
files.

%description   -n gem-standard-thread-safety-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета standard-thread_safety.
%endif


%if_enabled    devel
%package       -n gem-standard-thread-safety-devel
Version:       1.0.0
Release:       alt1
Summary:       A Standard Ruby plugin that configures rubocop-thread_safety development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета standard-thread_safety
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(standard-thread_safety) = 1.0.0

%description   -n gem-standard-thread-safety-devel
A Standard Ruby plugin that configures rubocop-thread_safety development
package.

%description   -n gem-standard-thread-safety-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета standard-thread_safety.
%endif


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
%doc CHANGELOG.md MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-standard-thread-safety-doc
%doc CHANGELOG.md MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-standard-thread-safety-devel
%doc CHANGELOG.md MIT-LICENSE README.md
%endif


%changelog
* Mon Aug 26 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
