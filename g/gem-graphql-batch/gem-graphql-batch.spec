%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname graphql-batch

Name:          gem-graphql-batch
Version:       0.6.0
Release:       alt1
Summary:       A query batching executor for the graphql gem
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Shopify/graphql-batch
Vcs:           https://github.com/shopify/graphql-batch.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-shopify) >= 1.0.7
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(graphql) >= 1.9.6
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(promise.rb) >= 0.7.2
BuildRequires: gem(rake) >= 12.3.3
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-shopify) >= 3
BuildConflicts: gem(graphql) >= 3
BuildConflicts: gem(promise.rb) >= 0.8
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency graphql >= 1.9.6,graphql < 2
%ruby_use_gem_dependency rubocop-shopify >= 2.14.0,rubocop-shopify < 3
Requires:      ruby >= 2.7
Requires:      gem(graphql) >= 1.9.6
Requires:      gem(promise.rb) >= 0.7.2
Conflicts:     gem(graphql) >= 3
Conflicts:     gem(promise.rb) >= 0.8
Provides:      graphql-batch = %EVR
Provides:      gem(graphql-batch) = 0.6.0

%ruby_use_gem_version graphql-batch:0.6.0

%description
Provides an executor for the graphql gem which allows queries to be batched.


%if_enabled    doc
%package       -n gem-graphql-batch-doc
Version:       0.6.0
Release:       alt1
Summary:       A query batching executor for the graphql gem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета graphql-batch
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(graphql-batch) = 0.6.0

%description   -n gem-graphql-batch-doc
A query batching executor for the graphql gem documentation files.

Provides an executor for the graphql gem which allows queries to be batched.

%description   -n gem-graphql-batch-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета graphql-batch.
%endif


%if_enabled    devel
%package       -n gem-graphql-batch-devel
Version:       0.6.0
Release:       alt1
Summary:       A query batching executor for the graphql gem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета graphql-batch
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(graphql-batch) = 0.6.0
Requires:      gem(byebug) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-shopify) >= 1.0.7
Requires:      gem(rake) >= 12.3.3
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-shopify) >= 3

%description   -n gem-graphql-batch-devel
A query batching executor for the graphql gem development package.

Provides an executor for the graphql gem which allows queries to be batched.

%description   -n gem-graphql-batch-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета graphql-batch.
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
%doc CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-graphql-batch-doc
%doc CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-graphql-batch-devel
%doc CONTRIBUTING.md LICENSE.txt README.md
%endif


%changelog
* Mon Jan 20 2025 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- ^ 0.5.1 -> 0.6.0

* Sat Oct 08 2022 Pavel Skrylev <majioa@altlinux.org> 0.5.1-alt1
- ^ 0.4.3 -> 0.5.1

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.3-alt1
- ^ 0.4.1 -> 0.4.3

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.1-alt1
- updated to (^) v0.4.1
- fix (!) spec

* Wed Jun 05 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- added (+) initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
