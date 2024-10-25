%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname danger-rubocop

Name:          gem-danger-rubocop
Version:       0.13.0
Release:       alt1
Summary:       A Danger plugin for running Ruby files through Rubocop
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ashfurrow/danger-rubocop
Vcs:           https://github.com/ashfurrow/danger-rubocop.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(rspec) >= 3.4
BuildRequires: gem(guard) >= 2.14
BuildRequires: gem(guard-rspec) >= 4.7
BuildRequires: gem(listen) = 3.0.7
BuildRequires: gem(pry) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(bacon) >= 0
BuildRequires: gem(mocha-on-bacon) >= 0
BuildRequires: gem(prettybacon) >= 0
BuildRequires: gem(danger) >= 0
BuildRequires: gem(rubocop) >= 1.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(guard) >= 3
BuildConflicts: gem(guard-rspec) >= 5
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Requires:      gem(danger) >= 0
Requires:      gem(rubocop) >= 1.0
Conflicts:     gem(rubocop) >= 2
Provides:      gem(danger-rubocop) = 0.13.0


%description
A Danger plugin for running Ruby files through Rubocop.


%if_enabled    doc
%package       -n gem-danger-rubocop-doc
Version:       0.13.0
Release:       alt1
Summary:       A Danger plugin for running Ruby files through Rubocop documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета danger-rubocop
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(danger-rubocop) = 0.13.0

%description   -n gem-danger-rubocop-doc
A Danger plugin for running Ruby files through Rubocop documentation files.

%description   -n gem-danger-rubocop-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета danger-rubocop.
%endif


%if_enabled    devel
%package       -n gem-danger-rubocop-devel
Version:       0.13.0
Release:       alt1
Summary:       A Danger plugin for running Ruby files through Rubocop development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета danger-rubocop
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(danger-rubocop) = 0.13.0
Requires:      gem(bundler) >= 1.3
Requires:      gem(rake) >= 13.0
Requires:      gem(yard) >= 0
Requires:      gem(rspec) >= 3.4
Requires:      gem(guard) >= 2.14
Requires:      gem(guard-rspec) >= 4.7
Requires:      gem(listen) = 3.0.7
Requires:      gem(pry) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(bacon) >= 0
Requires:      gem(mocha-on-bacon) >= 0
Requires:      gem(prettybacon) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(guard) >= 3
Conflicts:     gem(guard-rspec) >= 5

%description   -n gem-danger-rubocop-devel
A Danger plugin for running Ruby files through Rubocop development package.

%description   -n gem-danger-rubocop-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета danger-rubocop.
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
%files         -n gem-danger-rubocop-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-danger-rubocop-devel
%doc README.md
%endif


%changelog
* Thu Oct 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.13.0-alt1
- + packaged gem with Ruby Policy 2.0
