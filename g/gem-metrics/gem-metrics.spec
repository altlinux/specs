%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%define        gemname metrics

Name:          gem-metrics
Version:       0.15.0
Release:       alt1
Summary:       Application metrics and instrumentation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/metrics
Vcs:           https://github.com/socketry/metrics.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.2
Provides:      gem(metrics) = 0.15.0

%description
Application metrics and instrumentation.


%if_enabled    doc
%package       -n gem-metrics-doc
Version:       0.15.0
Release:       alt1
Summary:       Application metrics and instrumentation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета metrics
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(metrics) = 0.15.0

%description   -n gem-metrics-doc
Application metrics and instrumentation documentation files.

%description   -n gem-metrics-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета metrics.
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
%doc license.md readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-metrics-doc
%doc license.md readme.md
%ruby_gemdocdir
%endif


%changelog
* Sat Mar 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.15.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
