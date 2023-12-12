%define        _unpackaged_files_terminate_build 1
%define        gemname sparkr

Name:          gem-sparkr
Version:       0.4.1
Release:       alt1
Summary:       ASCII Sparklines in Ruby
License:       MIT
Group:         Development/Ruby
Url:           http://trivelop.de/sparkr/
Vcs:           https://github.com/rrrene/sparkr.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.5
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0
BuildConflicts: gem(bundler) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Provides:      gem(sparkr) = 0.4.1

%ruby_bindir_to %ruby_bindir

%description
Sparkr is a port of spark for Ruby.

It lets you create ASCII sparklines for your Ruby CLIs.


%package       -n sparkr
Version:       0.4.1
Release:       alt1
Summary:       ASCII Sparklines in Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета sparkr
Group:         Other
BuildArch:     noarch

Requires:      gem(sparkr) = 0.4.1

%description   -n sparkr
ASCII Sparklines in Ruby executable(s).

Sparkr is a port of spark for Ruby.

It lets you create ASCII sparklines for your Ruby CLIs.

%description   -n sparkr -l ru_RU.UTF-8
Исполнямка для самоцвета sparkr.


%package       -n gem-sparkr-doc
Version:       0.4.1
Release:       alt1
Summary:       ASCII Sparklines in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sparkr
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sparkr) = 0.4.1

%description   -n gem-sparkr-doc
ASCII Sparklines in Ruby documentation files.

Sparkr is a port of spark for Ruby.

It lets you create ASCII sparklines for your Ruby CLIs.

%description   -n gem-sparkr-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sparkr.


%package       -n gem-sparkr-devel
Version:       0.4.1
Release:       alt1
Summary:       ASCII Sparklines in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sparkr
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sparkr) = 0.4.1
Requires:      gem(bundler) >= 1.5
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0
Conflicts:     gem(bundler) >= 3

%description   -n gem-sparkr-devel
ASCII Sparklines in Ruby development package.

Sparkr is a port of spark for Ruby.

It lets you create ASCII sparklines for your Ruby CLIs.

%description   -n gem-sparkr-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sparkr.


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

%files         -n sparkr
%doc README.md
%ruby_bindir/sparkr

%files         -n gem-sparkr-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sparkr-devel
%doc README.md


%changelog
* Sat Dec 02 2023 Pavel Skrylev <majioa@altlinux.org> 0.4.1-alt1
- + packaged gem with Ruby Policy 2.0
