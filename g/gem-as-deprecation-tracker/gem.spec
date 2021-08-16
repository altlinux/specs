%define        gemname as_deprecation_tracker

Name:          gem-as-deprecation-tracker
Version:       1.5.0
Release:       alt1
Summary:       Track known ActiveSupport deprecation warnings
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/domcleal/as_deprecation_tracker
Vcs:           https://github.com/domcleal/as_deprecation_tracker.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activesupport) >= 4.2
BuildRequires: gem(railties) >= 4.2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(activesupport) >= 4.2
Requires:      gem(railties) >= 4.2
Provides:      gem(as_deprecation_tracker) = 1.5.0


%description
Tracks known ActiveSupport (Rails) deprecation warnings and catches new issues
when an unknown warning is seen.


%package       -n gem-as-deprecation-tracker-doc
Version:       1.5.0
Release:       alt1
Summary:       Track known ActiveSupport deprecation warnings documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета as_deprecation_tracker
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(as_deprecation_tracker) = 1.5.0

%description   -n gem-as-deprecation-tracker-doc
Track known ActiveSupport deprecation warnings documentation files.

Tracks known ActiveSupport (Rails) deprecation warnings and catches new issues
when an unknown warning is seen.

%description   -n gem-as-deprecation-tracker-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета as_deprecation_tracker.


%package       -n gem-as-deprecation-tracker-devel
Version:       1.5.0
Release:       alt1
Summary:       Track known ActiveSupport deprecation warnings development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета as_deprecation_tracker
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(as_deprecation_tracker) = 1.5.0

%description   -n gem-as-deprecation-tracker-devel
Track known ActiveSupport deprecation warnings development package.

Tracks known ActiveSupport (Rails) deprecation warnings and catches new issues
when an unknown warning is seen.

%description   -n gem-as-deprecation-tracker-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета as_deprecation_tracker.


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

%files         -n gem-as-deprecation-tracker-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-as-deprecation-tracker-devel
%doc README.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- + packaged gem with Ruby Policy 2.0
