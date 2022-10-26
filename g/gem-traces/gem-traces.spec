%define        gemname traces

Name:          gem-traces
Version:       0.7.0
Release:       alt1
Summary:       Application instrumentation and tracing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/traces
Vcs:           https://github.com/socketry/traces.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bake-test) >= 0.2 gem(bake-test) < 1
BuildRequires: gem(bake-test-external) >= 0.2 gem(bake-test-external) < 1
BuildRequires: gem(covered) >= 0.16 gem(covered) < 1
BuildRequires: gem(sus) >= 0.13 gem(sus) < 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(traces) = 0.7.0


%description
Application instrumentation and tracing.


%package       -n gem-traces-doc
Version:       0.7.0
Release:       alt1
Summary:       Application instrumentation and tracing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета traces
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(traces) = 0.7.0

%description   -n gem-traces-doc
Application instrumentation and tracing documentation files.

%description   -n gem-traces-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета traces.


%package       -n gem-traces-devel
Version:       0.7.0
Release:       alt1
Summary:       Application instrumentation and tracing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета traces
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(traces) = 0.7.0
Requires:      gem(bake-test) >= 0.2 gem(bake-test) < 1
Requires:      gem(bake-test-external) >= 0.2 gem(bake-test-external) < 1
Requires:      gem(covered) >= 0.16 gem(covered) < 1
Requires:      gem(sus) >= 0.13 gem(sus) < 1

%description   -n gem-traces-devel
Application instrumentation and tracing development package.

%description   -n gem-traces-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета traces.


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

%files         -n gem-traces-doc
%ruby_gemdocdir

%files         -n gem-traces-devel


%changelog
* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- + packaged gem with Ruby Policy 2.0
