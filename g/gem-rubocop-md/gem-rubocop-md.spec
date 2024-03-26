%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubocop-md

Name:          gem-rubocop-md
Version:       1.2.2
Release:       alt1
Summary:       Run Rubocop against your Markdown files to make sure that code examples follow style guidelines
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubocop-hq/rubocop-md
Vcs:           https://github.com/rubocop-hq/rubocop-md.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.15
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(rubocop) >= 1.0
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rubocop) >= 1.0
Provides:      gem(rubocop-md) = 1.2.2


%description
Run Rubocop against your Markdown files to make sure that code examples follow
style guidelines.


%if_enabled    doc
%package       -n gem-rubocop-md-doc
Version:       1.2.2
Release:       alt1
Summary:       Run Rubocop against your Markdown files to make sure that code examples follow style guidelines documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-md
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-md) = 1.2.2

%description   -n gem-rubocop-md-doc
Run Rubocop against your Markdown files to make sure that code examples follow
style guidelines documentation files.
%description   -n gem-rubocop-md-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-md.
%endif


%if_enabled    devel
%package       -n gem-rubocop-md-devel
Version:       1.2.2
Release:       alt1
Summary:       Run Rubocop against your Markdown files to make sure that code examples follow style guidelines development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-md
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-md) = 1.2.2
Requires:      gem(bundler) >= 1.15
Requires:      gem(rake) >= 13.0
Requires:      gem(minitest) >= 5.0
Conflicts:     gem(minitest) >= 6

%description   -n gem-rubocop-md-devel
Run Rubocop against your Markdown files to make sure that code examples follow
style guidelines development package.
%description   -n gem-rubocop-md-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-md.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rubocop-md-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubocop-md-devel
%doc README.md
%endif


%changelog
* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.2.2-alt1
- + packaged gem with Ruby Policy 2.0
