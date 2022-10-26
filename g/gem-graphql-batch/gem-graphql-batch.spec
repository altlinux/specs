%define        gemname graphql-batch

Name:          gem-graphql-batch
Version:       0.5.1
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
%if_with check
BuildRequires: gem(graphql) >= 1.9.6 gem(graphql) < 3
BuildRequires: gem(promise.rb) >= 0.7.2 gem(promise.rb) < 0.8
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(minitest) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency graphql >= 1.9.6,graphql < 2
Requires:      gem(graphql) >= 1.9.6 gem(graphql) < 3
Requires:      gem(promise.rb) >= 0.7.2 gem(promise.rb) < 0.8
Provides:      gem(graphql-batch) = 0.5.1


%description
Provides an executor for the graphql gem which allows queries to be batched.


%package       -n gem-graphql-batch-doc
Version:       0.5.1
Release:       alt1
Summary:       A query batching executor for the graphql gem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета graphql-batch
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(graphql-batch) = 0.5.1

%description   -n gem-graphql-batch-doc
A query batching executor for the graphql gem documentation files.

Provides an executor for the graphql gem which allows queries to be batched.

%description   -n gem-graphql-batch-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета graphql-batch.


%package       -n gem-graphql-batch-devel
Version:       0.5.1
Release:       alt1
Summary:       A query batching executor for the graphql gem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета graphql-batch
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(graphql-batch) = 0.5.1
Requires:      gem(byebug) >= 0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(minitest) >= 0

%description   -n gem-graphql-batch-devel
A query batching executor for the graphql gem development package.

Provides an executor for the graphql gem which allows queries to be batched.

%description   -n gem-graphql-batch-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета graphql-batch.


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

%files         -n gem-graphql-batch-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-graphql-batch-devel
%doc README.md


%changelog
* Sat Oct 08 2022 Pavel Skrylev <majioa@altlinux.org> 0.5.1-alt1
- ^ 0.4.3 -> 0.5.1

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.3-alt1
- ^ 0.4.1 -> 0.4.3

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.1-alt1
- updated to (^) v0.4.1
- fix (!) spec

* Wed Jun 05 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- added (+) initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
