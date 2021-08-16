%define        gemname rspec-collection_matchers

Name:          gem-rspec-collection-matchers
Version:       1.2.0
Release:       alt1
Summary:       rspec-collection_matchers-1.2.0
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rspec/rspec-collection_matchers
Vcs:           https://github.com/rspec/rspec-collection_matchers.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec-expectations) >= 2.99.0.beta1
BuildRequires: gem(bundler) >= 1.3 gem(bundler) < 3
BuildRequires: gem(activemodel) >= 3.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Requires:      gem(rspec-expectations) >= 2.99.0.beta1
Provides:      gem(rspec-collection_matchers) = 1.2.0


%description
Collection cardinality matchers, extracted from rspec-expectations


%package       -n gem-rspec-collection-matchers-doc
Version:       1.2.0
Release:       alt1
Summary:       rspec-collection_matchers-1.2.0 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-collection_matchers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec-collection_matchers) = 1.2.0

%description   -n gem-rspec-collection-matchers-doc
rspec-collection_matchers-1.2.0 documentation files.

Collection cardinality matchers, extracted from rspec-expectations

%description   -n gem-rspec-collection-matchers-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-collection_matchers.


%package       -n gem-rspec-collection-matchers-devel
Version:       1.2.0
Release:       alt1
Summary:       rspec-collection_matchers-1.2.0 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-collection_matchers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec-collection_matchers) = 1.2.0
Requires:      gem(bundler) >= 1.3 gem(bundler) < 3
Requires:      gem(activemodel) >= 3.0

%description   -n gem-rspec-collection-matchers-devel
rspec-collection_matchers-1.2.0 development package.

Collection cardinality matchers, extracted from rspec-expectations

%description   -n gem-rspec-collection-matchers-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-collection_matchers.


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

%files         -n gem-rspec-collection-matchers-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rspec-collection-matchers-devel
%doc README.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- + packaged gem with Ruby Policy 2.0
