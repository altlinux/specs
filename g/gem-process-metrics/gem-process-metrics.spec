%define        gemname process-metrics

Name:          gem-process-metrics
Version:       0.2.1
Release:       alt1
Summary:       Provide detailed OS-specific process metrics
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/process-metrics
Vcs:           https://github.com/socketry/process-metrics.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(covered) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 12.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.8 gem(rspec) < 4
BuildRequires: gem(console) >= 1.8 gem(console) < 2
BuildRequires: gem(samovar) >= 2.1 gem(samovar) < 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(console) >= 1.8 gem(console) < 2
Requires:      gem(samovar) >= 2.1 gem(samovar) < 3
Provides:      gem(process-metrics) = 0.2.1

%description
Provide detailed OS-specific process metrics.


%package       -n process-metrics
Version:       0.2.1
Release:       alt1
Summary:       Provide detailed OS-specific process metrics executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета process-metrics
Group:         Other
BuildArch:     noarch

Requires:      gem(process-metrics) = 0.2.1

%description   -n process-metrics
Provide detailed OS-specific process metrics executable(s).

%description   -n process-metrics -l ru_RU.UTF-8
Исполнямка для самоцвета process-metrics.


%package       -n gem-process-metrics-doc
Version:       0.2.1
Release:       alt1
Summary:       Provide detailed OS-specific process metrics documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета process-metrics
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(process-metrics) = 0.2.1

%description   -n gem-process-metrics-doc
Provide detailed OS-specific process metrics documentation files.

%description   -n gem-process-metrics-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета process-metrics.


%package       -n gem-process-metrics-devel
Version:       0.2.1
Release:       alt1
Summary:       Provide detailed OS-specific process metrics development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета process-metrics
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(process-metrics) = 0.2.1
Requires:      gem(covered) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 12.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.8 gem(rspec) < 4

%description   -n gem-process-metrics-devel
Provide detailed OS-specific process metrics development package.

%description   -n gem-process-metrics-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета process-metrics.


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

%files         -n process-metrics
%doc README.md
%_bindir/process-metrics

%files         -n gem-process-metrics-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-process-metrics-devel
%doc README.md


%changelog
* Mon Oct 17 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- + packaged gem with Ruby Policy 2.0
