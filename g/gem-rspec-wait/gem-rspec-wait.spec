%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rspec-wait

Name:          gem-rspec-wait
Version:       1.0.2
Release:       alt1
Summary:       Time-resilient expectations in RSpec
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/laserlemon/rspec-wait
Vcs:           https://github.com/laserlemon/rspec-wait.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.4
BuildRequires: gem(rubocop) >= 1.77
BuildRequires: gem(rubocop-md) >= 2.0
BuildRequires: gem(rubocop-performance) >= 1.25
BuildRequires: gem(rubocop-rake) >= 0.7.0
BuildRequires: gem(rubocop-rspec) >= 3.6
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-md) >= 3
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 0.8
BuildConflicts: gem(rubocop-rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.0
Requires:      gem(rspec) >= 3.4
Requires:      gem(rubocop) >= 1.77
Requires:      gem(rubocop-md) >= 2.0
Requires:      gem(rubocop-performance) >= 1.25
Requires:      gem(rubocop-rake) >= 0.7.0
Requires:      gem(rubocop-rspec) >= 3.6
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-md) >= 3
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 0.8
Conflicts:     gem(rubocop-rspec) >= 4
Provides:      gem(rspec-wait) = 1.0.2

%description
RSpec::Wait enables time-resilient expectations in your RSpec test suite.


%if_enabled    doc
%package       -n gem-rspec-wait-doc
Version:       1.0.2
Release:       alt1
Summary:       Time-resilient expectations in RSpec documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-wait
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rspec-wait) = 1.0.2

%description   -n gem-rspec-wait-doc
Time-resilient expectations in RSpec documentation files.

RSpec::Wait enables time-resilient expectations in your RSpec test suite.

%description   -n gem-rspec-wait-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-wait.
%endif


%if_enabled    devel
%package       -n gem-rspec-wait-devel
Version:       1.0.2
Release:       alt1
Summary:       Time-resilient expectations in RSpec development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-wait
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rspec-wait) = 1.0.2
Requires:      gem(bundler) >= 2.0
Requires:      gem(rake) >= 13.0

%description   -n gem-rspec-wait-devel
Time-resilient expectations in RSpec development package.

RSpec::Wait enables time-resilient expectations in your RSpec test suite.

%description   -n gem-rspec-wait-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-wait.
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
%doc LICENSE.txt README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rspec-wait-doc
%doc LICENSE.txt README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rspec-wait-devel
%doc LICENSE.txt README.md CHANGELOG.md CONTRIBUTING.md
%endif


%changelog
* Fri Nov 28 2025 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
