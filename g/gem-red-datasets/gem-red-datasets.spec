%define        gemname red-datasets

Name:          gem-red-datasets
Version:       0.1.5
Release:       alt1
Summary:       Red Datasets provides classes that provide common datasets such as iris dataset
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/red-data-tools/red-datasets
Vcs:           https://github.com/red-data-tools/red-datasets.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(csv) >= 3.2.4
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(rubyzip) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(csv) >= 3.2.4
Requires:      gem(rexml) >= 0
Requires:      gem(rubyzip) >= 0
Provides:      gem(red-datasets) = 0.1.5


%description
You can use datasets easily because you can access each dataset with multiple
ways such as `#each` and Apache Arrow Record Batch.


%package       -n gem-red-datasets-doc
Version:       0.1.5
Release:       alt1
Summary:       Red Datasets provides classes that provide common datasets such as iris dataset documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета red-datasets
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(red-datasets) = 0.1.5

%description   -n gem-red-datasets-doc
Red Datasets provides classes that provide common datasets such as iris dataset
documentation files.

You can use datasets easily because you can access each dataset with multiple
ways such as `#each` and Apache Arrow Record Batch.

%description   -n gem-red-datasets-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета red-datasets.


%package       -n gem-red-datasets-devel
Version:       0.1.5
Release:       alt1
Summary:       Red Datasets provides classes that provide common datasets such as iris dataset development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета red-datasets
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(red-datasets) = 0.1.5
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(kramdown) >= 0

%description   -n gem-red-datasets-devel
Red Datasets provides classes that provide common datasets such as iris dataset
development package.

You can use datasets easily because you can access each dataset with multiple
ways such as `#each` and Apache Arrow Record Batch.

%description   -n gem-red-datasets-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета red-datasets.


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

%files         -n gem-red-datasets-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-red-datasets-devel
%doc README.md


%changelog
* Fri Apr 14 2023 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1
- + packaged gem with Ruby Policy 2.0
