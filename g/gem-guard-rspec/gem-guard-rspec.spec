%define        _unpackaged_files_terminate_build 1
%def_disable    check
%def_enable    doc
%def_enable    devel
%define        gemname guard-rspec

Name:          gem-guard-rspec
Version:       4.7.3
Release:       alt1
Summary:       Guard gem for RSpec
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/guard/guard-rspec
Vcs:           https://github.com/guard/guard-rspec.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(guard) >= 2.1
BuildRequires: gem(guard-compat) >= 1.1
BuildRequires: gem(guard-rubocop) >= 0
BuildRequires: gem(launchy) >= 2.4
BuildRequires: gem(rake) >= 11.1
BuildRequires: gem(rubocop) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(guard) >= 3
BuildConflicts: gem(guard-compat) >= 2
BuildConflicts: gem(launchy) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.5.9,bundler < 3
%ruby_use_gem_dependency rake >= 13.3.1,rake < 14
Requires:      gem(guard) >= 2.1
Requires:      gem(guard-compat) >= 1.1
Requires:      gem(rspec) >= 3.4
Conflicts:     gem(guard) >= 3
Conflicts:     gem(guard-compat) >= 2
Conflicts:     gem(rspec) >= 4
Provides:      gem(guard-rspec) = 4.7.3

%description
Guard::RSpec automatically run your specs (much like autotest).


%if_enabled    doc
%package       -n gem-guard-rspec-doc
Version:       4.7.3
Release:       alt1
Summary:       Guard gem for RSpec documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета guard-rspec
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(guard-rspec) = 4.7.3

%description   -n gem-guard-rspec-doc
Guard gem for RSpec documentation files.

Guard::RSpec automatically run your specs (much like autotest).

%description   -n gem-guard-rspec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета guard-rspec.
%endif


%if_enabled    devel
%package       -n gem-guard-rspec-devel
Version:       4.7.3
Release:       alt1
Summary:       Guard gem for RSpec development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета guard-rspec
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(guard-rspec) = 4.7.3
Requires:      gem(coveralls) >= 0
Requires:      gem(guard-rubocop) >= 0
Requires:      gem(launchy) >= 2.4
Requires:      gem(rake) >= 11.1
Requires:      gem(rubocop) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(launchy) >= 3
Conflicts:     gem(rake) >= 14

%description   -n gem-guard-rspec-devel
Guard gem for RSpec development package.

Guard::RSpec automatically run your specs (much like autotest).

%description   -n gem-guard-rspec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета guard-rspec.
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
%doc CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-guard-rspec-doc
%doc CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-guard-rspec-devel
%doc CONTRIBUTING.md LICENSE.txt README.md
%endif


%changelog
* Tue Jul 07 2026 Alexander Burmatov <thatman@altlinux.org> 4.7.3-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
