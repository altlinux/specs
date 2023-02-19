%define        gemname test-unit-notify

Name:          gem-test-unit-notify
Version:       1.0.4
Release:       alt1
Summary:       A test result notify extension for test-unit
License:       LGPLv2.1 or later
Group:         Development/Ruby
Url:           https://github.com/test-unit/test-unit-notify
Vcs:           https://github.com/test-unit/test-unit-notify.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(packnga) >= 0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(test-unit) >= 2.4.9
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(test-unit) >= 2.4.9
Provides:      gem(test-unit-notify) = 1.0.4


%description
A test result notify extension for test-unit. This provides test result
notification support.


%package       -n gem-test-unit-notify-doc
Version:       1.0.4
Release:       alt1
Summary:       A test result notify extension for test-unit documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета test-unit-notify
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(test-unit-notify) = 1.0.4

%description   -n gem-test-unit-notify-doc
A test result notify extension for test-unit documentation files.

A test result notify extension for test-unit. This provides test result
notification support.

%description   -n gem-test-unit-notify-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета test-unit-notify.


%package       -n gem-test-unit-notify-devel
Version:       1.0.4
Release:       alt1
Summary:       A test result notify extension for test-unit development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета test-unit-notify
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(test-unit-notify) = 1.0.4
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(packnga) >= 0
Requires:      gem(kramdown) >= 0

%description   -n gem-test-unit-notify-devel
A test result notify extension for test-unit development package.

A test result notify extension for test-unit. This provides test result
notification support.

%description   -n gem-test-unit-notify-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета test-unit-notify.


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

%files         -n gem-test-unit-notify-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-test-unit-notify-devel
%doc README.md


%changelog
* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.4-alt1
- + packaged gem with Ruby Policy 2.0
