%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubocop-rake

Name:          gem-rubocop-rake
Version:       0.7.1
Release:       alt1
Summary:       A RuboCop plugin for Rake
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubocop/rubocop-rake
Vcs:           https://github.com/rubocop/rubocop-rake.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(lint_roller) >= 1.1
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-rspec) >= 0
BuildConflicts: gem(lint_roller) >= 2
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      ruby >= 2.7.0
Requires:      gem(lint_roller) >= 1.1
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(lint_roller) >= 2
Provides:      gem(rubocop-rake) = 0.7.1

%description
A RuboCop plugin for Rake.


%if_enabled    doc
%package       -n gem-rubocop-rake-doc
Version:       0.7.1
Release:       alt1
Summary:       A RuboCop plugin for Rake documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-rake
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rubocop-rake) = 0.7.1

%description   -n gem-rubocop-rake-doc
A RuboCop plugin for Rake documentation files.

%description   -n gem-rubocop-rake-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-rake.
%endif


%if_enabled    devel
%package       -n gem-rubocop-rake-devel
Version:       0.7.1
Release:       alt1
Summary:       A RuboCop plugin for Rake development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-rake
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rubocop-rake) = 0.7.1
Requires:      gem(lint_roller) >= 1.1
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-rspec) >= 0
Conflicts:     gem(lint_roller) >= 2
Conflicts:     gem(rake) >= 14

%description   -n gem-rubocop-rake-devel
A RuboCop plugin for Rake development package.

%description   -n gem-rubocop-rake-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-rake.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rubocop-rake-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubocop-rake-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Sun Nov 23 2025 Pavel Skrylev <majioa@altlinux.org> 0.7.1-alt1
- ^ 0.6.0 -> 0.7.1

* Tue Jan 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- + packaged gem with Ruby Policy 2.0
