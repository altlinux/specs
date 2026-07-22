%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rspec-its

Name:          gem-rspec-its
Version:       2.0.0
Release:       alt1
Summary:       Provides "its" method formerly part of rspec-core
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rspec/rspec-its
Vcs:           https://github.com/rspec/rspec-its.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(aruba) >= 2.2.0
BuildRequires: gem(bundler) > 2.0.0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(cucumber) >= 1.3.8
BuildRequires: gem(ffi) >= 1.17.0
BuildRequires: gem(matrix) >= 0.4.2
BuildRequires: gem(rake) >= 13.2.0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rspec-core) >= 3.13.0
BuildRequires: gem(rspec-expectations) >= 3.13.0
BuildRequires: gem(rspec-mocks) >= 0
BuildRequires: gem(rspec-support) >= 0
BuildRequires: gem(rubocop) >= 1.68.0
BuildConflicts: gem(aruba) >= 3
BuildConflicts: gem(ffi) >= 2
BuildConflicts: gem(matrix) >= 0.5
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency aruba >= 2.4.1,aruba < 3
%ruby_use_gem_dependency ffi >= 1.17.0,ffi < 2
%ruby_use_gem_dependency rake >= 13.3.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.81.6,rubocop < 2
Requires:      ruby > 3.0.0
Requires:      gem(rspec-core) >= 3.13.0
Requires:      gem(rspec-expectations) >= 3.13.0
Provides:      gem(rspec-its) = 2.0.0

%description
RSpec extension gem for attribute matching.


%if_enabled    doc
%package       -n gem-rspec-its-doc
Version:       2.0.0
Release:       alt1
Summary:       Provides "its" method formerly part of rspec-core documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-its
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rspec-its) = 2.0.0

%description   -n gem-rspec-its-doc
Provides "its" method formerly part of rspec-core documentation files.

RSpec extension gem for attribute matching.

%description   -n gem-rspec-its-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-its.
%endif


%if_enabled    devel
%package       -n gem-rspec-its-devel
Version:       2.0.0
Release:       alt1
Summary:       Provides "its" method formerly part of rspec-core development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-its
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rspec-its) = 2.0.0
Requires:      gem(aruba) >= 2.2.0
Requires:      gem(coveralls) >= 0
Requires:      gem(cucumber) >= 1.3.8
Requires:      gem(ffi) >= 1.17.0
Requires:      gem(matrix) >= 0.4.2
Requires:      gem(rspec) >= 0
Requires:      gem(rspec-mocks) >= 0
Requires:      gem(rspec-support) >= 0
Requires:      gem(rubocop) >= 1.68.0
Conflicts:     gem(aruba) >= 3
Conflicts:     gem(ffi) >= 2
Conflicts:     gem(matrix) >= 0.5
Conflicts:     gem(rubocop) >= 2

%description   -n gem-rspec-its-devel
Provides "its" method formerly part of rspec-core development package.

RSpec extension gem for attribute matching.

%description   -n gem-rspec-its-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-its.
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
%doc Changelog.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rspec-its-doc
%doc Changelog.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rspec-its-devel
%doc Changelog.md LICENSE.txt README.md
%endif


%changelog
* Wed Jul 08 2026 Alexander Burmatov <thatman@altlinux.org> 2.0.0-alt1
- ^ 1.3.0 -> 2.0.0

* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- + packaged gem with Ruby Policy 2.0
