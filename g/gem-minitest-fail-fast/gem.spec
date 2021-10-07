%define        gemname minitest-fail-fast

Name:          gem-minitest-fail-fast
Version:       0.1.0
Release:       alt1
Summary:       Fail and exit as soon as a test fails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/teoljungberg/minitest-fail-fast
Vcs:           https://github.com/teoljungberg/minitest-fail-fast.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5 gem(minitest) < 6
BuildRequires: gem(bundler) >= 1.9 gem(bundler) < 3
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(minitest) >= 5 gem(minitest) < 6
Provides:      gem(minitest-fail-fast) = 0.1.0


%description
Reimplements RSpec's "fail fast" feature for minitest.


%package       -n gem-minitest-fail-fast-doc
Version:       0.1.0
Release:       alt1
Summary:       Fail and exit as soon as a test fails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-fail-fast
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-fail-fast) = 0.1.0

%description   -n gem-minitest-fail-fast-doc
Fail and exit as soon as a test fails documentation files.

Reimplements RSpec's "fail fast" feature for minitest.

%description   -n gem-minitest-fail-fast-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-fail-fast.


%package       -n gem-minitest-fail-fast-devel
Version:       0.1.0
Release:       alt1
Summary:       Fail and exit as soon as a test fails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-fail-fast
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-fail-fast) = 0.1.0
Requires:      gem(bundler) >= 1.9 gem(bundler) < 3
Requires:      gem(rake) >= 10.0 gem(rake) < 14

%description   -n gem-minitest-fail-fast-devel
Fail and exit as soon as a test fails development package.

Reimplements RSpec's "fail fast" feature for minitest.

%description   -n gem-minitest-fail-fast-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-fail-fast.


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

%files         -n gem-minitest-fail-fast-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-minitest-fail-fast-devel
%doc README.md


%changelog
* Fri Sep 10 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt1
- + packaged gem with Ruby Policy 2.0
