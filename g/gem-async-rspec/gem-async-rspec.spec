%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname async-rspec

Name:          gem-async-rspec
Version:       1.17.0
Release:       alt1
Summary:       Helpers for writing specs against the async gem
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/async-rspec
Vcs:           https://github.com/socketry/async-rspec.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(async) >= 0
BuildRequires: gem(async-io) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rspec-files) >= 1.0
BuildRequires: gem(rspec-memory) >= 1.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-files) >= 2
BuildConflicts: gem(rspec-memory) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rspec) >= 3.0
Requires:      gem(rspec-files) >= 1.0
Requires:      gem(rspec-memory) >= 1.0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-files) >= 2
Conflicts:     gem(rspec-memory) >= 2
Provides:      gem(async-rspec) = 1.17.0


%description
Provides useful RSpec.shared_contexts for testing code that builds on top of
async.


%if_enabled    doc
%package       -n gem-async-rspec-doc
Version:       1.17.0
Release:       alt1
Summary:       Helpers for writing specs against the async gem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета async-rspec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(async-rspec) = 1.17.0

%description   -n gem-async-rspec-doc
Helpers for writing specs against the async gem documentation files.

Provides useful RSpec.shared_contexts for testing code that builds on top of
async.

%description   -n gem-async-rspec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета async-rspec.
%endif


%if_enabled    devel
%package       -n gem-async-rspec-devel
Version:       1.17.0
Release:       alt1
Summary:       Helpers for writing specs against the async gem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета async-rspec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(async-rspec) = 1.17.0
Requires:      gem(async) >= 0
Requires:      gem(async-io) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0

%description   -n gem-async-rspec-devel
Helpers for writing specs against the async gem development package.

Provides useful RSpec.shared_contexts for testing code that builds on top of
async.

%description   -n gem-async-rspec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета async-rspec.
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
%doc license.md readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-async-rspec-doc
%doc license.md readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-async-rspec-devel
%doc license.md readme.md
%endif


%changelog
* Wed Mar 27 2024 Pavel Skrylev <majioa@altlinux.org> 1.17.0-alt1
- ^ 1.16.1 -> 1.17.0

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.16.1-alt1
- + packaged gem with Ruby Policy 2.0
