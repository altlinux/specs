%define        gemname opencensus

Name:          gem-opencensus
Version:       0.5.0
Release:       alt1
Summary:       A stats collection and distributed tracing framework
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/census-instrumentation/opencensus-ruby
Vcs:           https://github.com/census-instrumentation/opencensus-ruby.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.17
BuildRequires: gem(rake) >= 12.0 gem(rake) < 14
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(minitest-focus) >= 1.1 gem(minitest-focus) < 2
BuildRequires: gem(faraday) >= 0.13 gem(faraday) < 3
BuildRequires: gem(rails) >= 5.1.4 gem(rails) < 7
BuildRequires: gem(rubocop) >= 0.59.2 gem(rubocop) < 2
BuildRequires: gem(yard) >= 0.9 gem(yard) < 1
BuildRequires: gem(yard-doctest) >= 0.1.6 gem(yard-doctest) < 0.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rails >= 6.1.3.2,rails < 7
%ruby_use_gem_dependency faraday >= 2.6.0,faraday < 3
Provides:      gem(opencensus) = 0.5.0


%description
A stats collection and distributed tracing framework


%package       -n gem-opencensus-doc
Version:       0.5.0
Release:       alt1
Summary:       A stats collection and distributed tracing framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета opencensus
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(opencensus) = 0.5.0

%description   -n gem-opencensus-doc
A stats collection and distributed tracing framework documentation files.

%description   -n gem-opencensus-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета opencensus.


%package       -n gem-opencensus-devel
Version:       0.5.0
Release:       alt1
Summary:       A stats collection and distributed tracing framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета opencensus
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(opencensus) = 0.5.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0 gem(rake) < 14
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(minitest-focus) >= 1.1 gem(minitest-focus) < 2
Requires:      gem(faraday) >= 0.13 gem(faraday) < 3
Requires:      gem(rails) >= 5.1.4 gem(rails) < 7
Requires:      gem(rubocop) >= 0.59.2 gem(rubocop) < 2
Requires:      gem(yard) >= 0.9 gem(yard) < 1
Requires:      gem(yard-doctest) >= 0.1.6 gem(yard-doctest) < 0.2

%description   -n gem-opencensus-devel
A stats collection and distributed tracing framework development package.

%description   -n gem-opencensus-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета opencensus.


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

%files         -n gem-opencensus-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-opencensus-devel
%doc README.md


%changelog
* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- + packaged gem with Ruby Policy 2.0
