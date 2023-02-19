# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname release-metrics

Name:          gem-release-metrics
Version:       1.1.0
Release:       alt1.1
Summary:       Puppet, Inc. Release Metrics
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://rubygems.org/gems/release-metrics
Vcs:           https://git.altlinux.org/gears/g/gem-release-metrics.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(docopt) >= 0
BuildRequires: gem(csv) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(docopt) >= 0
Requires:      gem(csv) >= 0
Provides:      gem(release-metrics) = 1.1.0


%description
Puppet, Inc. Release Metrics.


%package       -n releases
Version:       1.1.0
Release:       alt1.1
Summary:       Puppet, Inc. Release Metrics executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета release-metrics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(release-metrics) = 1.1.0

%description   -n releases
Puppet, Inc. Release Metrics executable(s).

%description   -n releases -l ru_RU.UTF-8
Исполнямка для самоцвета release-metrics.


%package       -n gem-release-metrics-doc
Version:       1.1.0
Release:       alt1.1
Summary:       Puppet, Inc. Release Metrics documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета release-metrics
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(release-metrics) = 1.1.0

%description   -n gem-release-metrics-doc
Puppet, Inc. Release Metrics documentation files.

%description   -n gem-release-metrics-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета release-metrics.


%package       -n gem-release-metrics-devel
Version:       1.1.0
Release:       alt1.1
Summary:       Puppet, Inc. Release Metrics development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета release-metrics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(release-metrics) = 1.1.0

%description   -n gem-release-metrics-devel
Puppet, Inc. Release Metrics development package.

%description   -n gem-release-metrics-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета release-metrics.


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

%files         -n releases
%doc README.md
%_bindir/add-release
%_bindir/releases

%files         -n gem-release-metrics-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-release-metrics-devel
%doc README.md


%changelog
* Sat Feb 11 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1.1
- ! closes build deps under check condition

* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with usage Ruby Policy 2.0
