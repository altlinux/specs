%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname dry-transformer

Name:          gem-dry-transformer
Version:       1.0.1
Release:       alt1
Summary:       Data transformation toolkit
License:       MIT
Group:         Development/Ruby
Url:           https://dry-rb.org/gems/dry-transformer
Vcs:           https://github.com/dry-rb/dry-transformer.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(warning) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rspec) >= 3.8
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(zeitwerk) >= 2.6
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(zeitwerk) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(zeitwerk) >= 2.6
Conflicts:     gem(zeitwerk) >= 3
Provides:      gem(dry-transformer) = 1.0.1


%description
dry-transformer is a library that allows you to compose procs into a functional
pipeline using left-to-right function composition.

The approach came from Functional Programming, where simple functions are
composed into more complex functions in order to transform some data. It works
like |> in Elixir or >> in F#. dry-transformer provides a mechanism to define
and compose transformations, along with a number of built-in transformations.


%if_enabled    doc
%package       -n gem-dry-transformer-doc
Version:       1.0.1
Release:       alt1
Summary:       Data transformation toolkit documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dry-transformer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dry-transformer) = 1.0.1

%description   -n gem-dry-transformer-doc
Data transformation toolkit documentation files.

dry-transformer is a library that allows you to compose procs into a functional
pipeline using left-to-right function composition.

The approach came from Functional Programming, where simple functions are
composed into more complex functions in order to transform some data. It works
like |> in Elixir or >> in F#. dry-transformer provides a mechanism to define
and compose transformations, along with a number of built-in transformations.

%description   -n gem-dry-transformer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dry-transformer.
%endif


%if_enabled    devel
%package       -n gem-dry-transformer-devel
Version:       1.0.1
Release:       alt1
Summary:       Data transformation toolkit development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dry-transformer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dry-transformer) = 1.0.1
Requires:      gem(rake) >= 12.3.3
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(rexml) >= 0
Requires:      gem(warning) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rspec) >= 3.8
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(pry) >= 0
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rspec) >= 4

%description   -n gem-dry-transformer-devel
Data transformation toolkit development package.

dry-transformer is a library that allows you to compose procs into a functional
pipeline using left-to-right function composition.

The approach came from Functional Programming, where simple functions are
composed into more complex functions in order to transform some data. It works
like |> in Elixir or >> in F#. dry-transformer provides a mechanism to define
and compose transformations, along with a number of built-in transformations.

%description   -n gem-dry-transformer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dry-transformer.
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
%files         -n gem-dry-transformer-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dry-transformer-devel
%doc README.md
%endif


%changelog
* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + packaged gem with Ruby Policy 2.0
