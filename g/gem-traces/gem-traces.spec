%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%define        gemname traces

Name:          gem-traces
Version:       0.18.2
Release:       alt1
Summary:       Application instrumentation and tracing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/traces
Vcs:           https://github.com/socketry/traces.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.2
Provides:      gem(traces) = 0.18.2

%description
Application instrumentation and tracing.


%if_enabled    doc
%package       -n gem-traces-doc
Version:       0.18.2
Release:       alt1
Summary:       Application instrumentation and tracing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета traces
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(traces) = 0.18.2

%description   -n gem-traces-doc
Application instrumentation and tracing documentation files.

%description   -n gem-traces-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета traces.
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
%files         -n gem-traces-doc
%doc license.md readme.md
%ruby_gemdocdir
%endif


%changelog
* Sat Mar 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.18.2-alt1
- ^ 0.7.0 -> 0.18.2

* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- + packaged gem with Ruby Policy 2.0
