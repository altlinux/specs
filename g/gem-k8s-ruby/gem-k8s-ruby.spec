%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname k8s-ruby

Name:          gem-k8s-ruby
Version:       0.17.2
Release:       alt1
Summary:       Kubernetes client library for Ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/k8s-ruby/k8s-ruby
Vcs:           https://github.com/k8s-ruby/k8s-ruby.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(base64) >= 0
BuildRequires: gem(bundler) >= 1.17
BuildRequires: gem(byebug) >= 11.1
BuildRequires: gem(dry-configurable) >= 0
BuildRequires: gem(dry-struct) >= 0
BuildRequires: gem(dry-types) >= 0
BuildRequires: gem(excon) >= 0.71
BuildRequires: gem(hashdiff) >= 1.0
BuildRequires: gem(jsonpath) >= 1.1
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(recursive-open-struct) >= 1.1.3
BuildRequires: gem(rspec) >= 3.7
BuildRequires: gem(rubocop) >= 0.82
BuildRequires: gem(webmock) >= 3.6
BuildRequires: gem(yajl-ruby) >= 1.4
BuildRequires: gem(yaml-safe_load_stream3) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(byebug) >= 13
BuildConflicts: gem(excon) >= 1
BuildConflicts: gem(hashdiff) >= 2
BuildConflicts: gem(jsonpath) >= 2
BuildConflicts: gem(recursive-open-struct) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(yajl-ruby) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency byebug >= 12.0,byebug < 13
Requires:      ruby >= 2.4
Requires:      gem(base64) >= 0
Requires:      gem(dry-configurable) >= 0
Requires:      gem(dry-struct) >= 0
Requires:      gem(dry-types) >= 0
Requires:      gem(excon) >= 0.71
Requires:      gem(hashdiff) >= 1.0
Requires:      gem(jsonpath) >= 1.1
Requires:      gem(recursive-open-struct) >= 1.1.3
Requires:      gem(yajl-ruby) >= 1.4
Requires:      gem(yaml-safe_load_stream3) >= 0
Conflicts:     gem(excon) >= 1
Conflicts:     gem(hashdiff) >= 2
Conflicts:     gem(jsonpath) >= 2
Conflicts:     gem(recursive-open-struct) >= 2
Conflicts:     gem(yajl-ruby) >= 2
Provides:      gem(k8s-ruby) = 0.17.2

%description
Kubernetes client library for Ruby


%if_enabled    doc
%package       -n gem-k8s-ruby-doc
Version:       0.17.2
Release:       alt1
Summary:       Kubernetes client library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета k8s-ruby
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(k8s-ruby) = 0.17.2

%description   -n gem-k8s-ruby-doc
Kubernetes client library for Ruby documentation files.

%description   -n gem-k8s-ruby-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета k8s-ruby.
%endif


%if_enabled    devel
%package       -n gem-k8s-ruby-devel
Version:       0.17.2
Release:       alt1
Summary:       Kubernetes client library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета k8s-ruby
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(k8s-ruby) = 0.17.2
Requires:      gem(bundler) >= 1.17
Requires:      gem(byebug) >= 11.1
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rspec) >= 3.7
Requires:      gem(rubocop) >= 0.82
Requires:      gem(webmock) >= 3.6
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(byebug) >= 13
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(webmock) >= 4

%description   -n gem-k8s-ruby-devel
Kubernetes client library for Ruby development package.

%description   -n gem-k8s-ruby-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета k8s-ruby.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-k8s-ruby-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-k8s-ruby-devel
%doc LICENSE README.md
%endif


%changelog
* Fri Nov 28 2025 Pavel Skrylev <majioa@altlinux.org> 0.17.2-alt1
- ^ 0.16.0 -> 0.17.2

* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 0.16.0-alt1
- + packaged gem with Ruby Policy 2.0
