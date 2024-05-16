%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname train-kubernetes

Name:          gem-train-kubernetes
Version:       0.1.4
Release:       alt1
Summary:       Train Kubernetes
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/bgeesaman/train-kubernetes
Vcs:           https://github.com/bgeesaman/train-kubernetes.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(inspec) >= 3.7.11
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop) >= 0.59
BuildRequires: gem(k8s-ruby) >= 0.10
BuildRequires: gem(train) >= 3.0
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(k8s-ruby) >= 1
BuildConflicts: gem(train) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(k8s-ruby) >= 0.10
Requires:      gem(train) >= 3.0
Conflicts:     gem(k8s-ruby) >= 1
Conflicts:     gem(train) >= 4
Provides:      gem(train-kubernetes) = 0.1.4


%description
A Train "transport" plugin for Chef Inspec that allows testing of all Kubernetes
API resources


%if_enabled    doc
%package       -n gem-train-kubernetes-doc
Version:       0.1.4
Release:       alt1
Summary:       Train Kubernetes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета train-kubernetes
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(train-kubernetes) = 0.1.4

%description   -n gem-train-kubernetes-doc
Train Kubernetes documentation files.

A Train "transport" plugin for Chef Inspec that allows testing of all Kubernetes
API resources

%description   -n gem-train-kubernetes-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета train-kubernetes.
%endif


%if_enabled    devel
%package       -n gem-train-kubernetes-devel
Version:       0.1.4
Release:       alt1
Summary:       Train Kubernetes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета train-kubernetes
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(train-kubernetes) = 0.1.4
Requires:      gem(bundler) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(inspec) >= 3.7.11
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 0.59
Conflicts:     gem(rubocop) >= 2

%description   -n gem-train-kubernetes-devel
Train Kubernetes development package.

A Train "transport" plugin for Chef Inspec that allows testing of all Kubernetes
API resources

%description   -n gem-train-kubernetes-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета train-kubernetes.
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
%files         -n gem-train-kubernetes-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-train-kubernetes-devel
%doc README.md
%endif


%changelog
* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 0.1.4-alt1
- + packaged gem with Ruby Policy 2.0
