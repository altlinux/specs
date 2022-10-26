%define        gemname minitest-retry

Name:          gem-minitest-retry
Version:       0.2.2.1
Release:       alt1
Summary:       re-run the test when the test fails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/y-yagi/minitest-retry
Vcs:           https://github.com/y-yagi/minitest-retry.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version minitest-retry:0.2.2.1
Requires:      gem(minitest) >= 5.0
Provides:      gem(minitest-retry) = 0.2.2.1


%description
re-run the test when the test fails.


%package       -n gem-minitest-retry-doc
Version:       0.2.2.1
Release:       alt1
Summary:       re-run the test when the test fails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-retry
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-retry) = 0.2.2.1

%description   -n gem-minitest-retry-doc
re-run the test when the test fails documentation files.

%description   -n gem-minitest-retry-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-retry.


%package       -n gem-minitest-retry-devel
Version:       0.2.2.1
Release:       alt1
Summary:       re-run the test when the test fails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-retry
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-retry) = 0.2.2.1
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-minitest-retry-devel
re-run the test when the test fails development package.

%description   -n gem-minitest-retry-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-retry.


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

%files         -n gem-minitest-retry-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-minitest-retry-devel
%doc README.md


%changelog
* Sat Oct 08 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.2.1-alt1
- ^ 0.2.2 -> 0.2.2.1

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.2-alt1
- ^ 0.1.9 -> 0.2.2

* Mon Oct 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.9-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
