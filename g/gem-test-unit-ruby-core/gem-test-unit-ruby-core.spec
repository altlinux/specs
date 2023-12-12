%define        _unpackaged_files_terminate_build 1
%define        gemname test-unit-ruby-core

Name:          gem-test-unit-ruby-core
Version:       1.0.5
Release:       alt1
Summary:       Additional test assertions for Ruby standard libraries
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/test-unit-ruby-core
Vcs:           https://github.com/ruby/test-unit-ruby-core.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(test-unit-ruby-core) = 1.0.5


%description
Additional test assertions for Ruby standard libraries.


%package       -n gem-test-unit-ruby-core-doc
Version:       1.0.5
Release:       alt1
Summary:       Additional test assertions for Ruby standard libraries documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета test-unit-ruby-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(test-unit-ruby-core) = 1.0.5

%description   -n gem-test-unit-ruby-core-doc
Additional test assertions for Ruby standard libraries documentation files.

%description   -n gem-test-unit-ruby-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета test-unit-ruby-core.


%package       -n gem-test-unit-ruby-core-devel
Version:       1.0.5
Release:       alt1
Summary:       Additional test assertions for Ruby standard libraries development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета test-unit-ruby-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(test-unit-ruby-core) = 1.0.5

%description   -n gem-test-unit-ruby-core-devel
Additional test assertions for Ruby standard libraries development package.

%description   -n gem-test-unit-ruby-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета test-unit-ruby-core.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-test-unit-ruby-core-doc
%ruby_gemdocdir

%files         -n gem-test-unit-ruby-core-devel


%changelog
* Fri Dec 01 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- + packaged gem with Ruby Policy 2.0
