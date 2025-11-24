%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname test-unit-ruby-core

Name:          gem-test-unit-ruby-core
Version:       1.0.13
Release:       alt1
Summary:       Additional test assertions for Ruby standard libraries
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/test-unit-ruby-core
Vcs:           https://github.com/ruby/test-unit-ruby-core.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.3
Requires:      gem(test-unit) >= 0
Provides:      gem(test-unit-ruby-core) = 1.0.13

%description
Additional test assertions for Ruby standard libraries.


%if_enabled    doc
%package       -n gem-test-unit-ruby-core-doc
Version:       1.0.13
Release:       alt1
Summary:       Additional test assertions for Ruby standard libraries documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета test-unit-ruby-core
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(test-unit-ruby-core) = 1.0.13

%description   -n gem-test-unit-ruby-core-doc
Additional test assertions for Ruby standard libraries documentation files.

%description   -n gem-test-unit-ruby-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета test-unit-ruby-core.
%endif


%if_enabled    devel
%package       -n gem-test-unit-ruby-core-devel
Version:       1.0.13
Release:       alt1
Summary:       Additional test assertions for Ruby standard libraries development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета test-unit-ruby-core
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(test-unit-ruby-core) = 1.0.13
Requires:      gem(rake) >= 0

%description   -n gem-test-unit-ruby-core-devel
Additional test assertions for Ruby standard libraries development package.

%description   -n gem-test-unit-ruby-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета test-unit-ruby-core.
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
%doc COPYING README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-test-unit-ruby-core-doc
%doc COPYING README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-test-unit-ruby-core-devel
%doc COPYING README.md
%endif


%changelog
* Thu Nov 20 2025 Pavel Skrylev <majioa@altlinux.org> 1.0.13-alt1
- ^ 1.0.5 -> 1.0.13

* Fri Dec 01 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- + packaged gem with Ruby Policy 2.0
