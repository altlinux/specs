%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname k8s-ruby

Name:          gem-k8s-ruby
Version:       0.16.0
Release:       alt1
Summary:       Kubernetes client library for Ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/k8s-ruby/k8s-ruby
Vcs:           https://github.com/k8s-ruby/k8s-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(yaml-safe_load_stream3) >= 0
BuildRequires: gem(bundler) >= 1.17
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rspec) >= 3.7
BuildRequires: gem(webmock) >= 3.6.2
BuildRequires: gem(rubocop) >= 0.82
BuildRequires: gem(byebug) >= 11.1
BuildRequires: gem(excon) >= 0.71
BuildRequires: gem(dry-struct) >= 0
BuildRequires: gem(dry-types) >= 0
BuildRequires: gem(dry-configurable) >= 0
BuildRequires: gem(recursive-open-struct) >= 1.1.3
BuildRequires: gem(hashdiff) >= 1.0.0
BuildRequires: gem(jsonpath) >= 1.1
BuildRequires: gem(yajl-ruby) >= 1.4.0
BuildConflicts: gem(yaml-safe_load_stream3) > 0.1.2
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(byebug) >= 12
BuildConflicts: gem(excon) >= 1
BuildConflicts: gem(recursive-open-struct) >= 1.2
BuildConflicts: gem(hashdiff) >= 1.1
BuildConflicts: gem(jsonpath) >= 2
BuildConflicts: gem(yajl-ruby) >= 1.5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(yaml-safe_load_stream3) >= 0
Requires:      gem(excon) >= 0.71
Requires:      gem(dry-struct) >= 0
Requires:      gem(dry-types) >= 0
Requires:      gem(dry-configurable) >= 0
Requires:      gem(recursive-open-struct) >= 1.1.3
Requires:      gem(hashdiff) >= 1.0.0
Requires:      gem(jsonpath) >= 1.1
Requires:      gem(yajl-ruby) >= 1.4.0
Conflicts:     gem(yaml-safe_load_stream3) > 0.1.2
Conflicts:     gem(excon) >= 1
Conflicts:     gem(recursive-open-struct) >= 1.2
Conflicts:     gem(hashdiff) >= 1.1
Conflicts:     gem(jsonpath) >= 2
Conflicts:     gem(yajl-ruby) >= 1.5
Provides:      gem(k8s-ruby) = 0.16.0


%description
Kubernetes client library for Ruby


%if_enabled    doc
%package       -n gem-k8s-ruby-doc
Version:       0.16.0
Release:       alt1
Summary:       Kubernetes client library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета k8s-ruby
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(k8s-ruby) = 0.16.0

%description   -n gem-k8s-ruby-doc
Kubernetes client library for Ruby documentation files.

%description   -n gem-k8s-ruby-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета k8s-ruby.
%endif


%if_enabled    devel
%package       -n gem-k8s-ruby-devel
Version:       0.16.0
Release:       alt1
Summary:       Kubernetes client library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета k8s-ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(k8s-ruby) = 0.16.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rspec) >= 3.7
Requires:      gem(webmock) >= 3.6.2
Requires:      gem(rubocop) >= 0.82
Requires:      gem(byebug) >= 11.1
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(byebug) >= 12

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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-k8s-ruby-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-k8s-ruby-devel
%doc README.md
%endif


%changelog
* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 0.16.0-alt1
- + packaged gem with Ruby Policy 2.0
