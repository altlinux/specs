%define        gemname hamlit

Name:          gem-hamlit
Version:       3.0.3
Release:       alt1
Summary:       High Performance Haml Implementation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/k0kubun/hamlit
Vcs:           https://github.com/k0kubun/hamlit.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(benchmark_driver) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(erubi) >= 0
BuildRequires: gem(haml) >= 5
BuildRequires: gem(less) >= 0
BuildRequires: gem(minitest-reporters) >= 1.1
BuildRequires: gem(rails) >= 4.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(sass) >= 0
BuildRequires: gem(slim) >= 0
BuildRequires: gem(string_template) >= 0
BuildRequires: gem(unindent) >= 0
BuildRequires: gem(benchmark-ips) >= 2.3.0
BuildRequires: gem(maxitest) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(stackprof) >= 0
BuildRequires: gem(temple) >= 0.8.2
BuildRequires: gem(thor) >= 0
BuildRequires: gem(tilt) >= 0
BuildConflicts: gem(minitest-reporters) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency benchmark-ips >= 2.10.0,benchmark-ips < 3
Requires:      gem(temple) >= 0.8.2
Requires:      gem(thor) >= 0
Requires:      gem(tilt) >= 0
Provides:      gem(hamlit) = 3.0.3


%description
High Performance Haml Implementation


%package       -n hamlit
Version:       3.0.3
Release:       alt1
Summary:       High Performance Haml Implementation executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета hamlit
Group:         Other
BuildArch:     noarch

Requires:      gem(hamlit) = 3.0.3

%description   -n hamlit
High Performance Haml Implementation executable(s).

%description   -n hamlit -l ru_RU.UTF-8
Исполнямка для самоцвета hamlit.


%package       -n gem-hamlit-doc
Version:       3.0.3
Release:       alt1
Summary:       High Performance Haml Implementation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hamlit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hamlit) = 3.0.3

%description   -n gem-hamlit-doc
High Performance Haml Implementation documentation files.

%description   -n gem-hamlit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hamlit.


%package       -n gem-hamlit-devel
Version:       3.0.3
Release:       alt1
Summary:       High Performance Haml Implementation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hamlit
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hamlit) = 3.0.3
Requires:      gem(benchmark_driver) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(erubi) >= 0
Requires:      gem(haml) >= 5
Requires:      gem(less) >= 0
Requires:      gem(minitest-reporters) >= 1.1
Requires:      gem(rails) >= 4.0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(sass) >= 0
Requires:      gem(slim) >= 0
Requires:      gem(string_template) >= 0
Requires:      gem(unindent) >= 0
Requires:      gem(benchmark-ips) >= 2.3.0
Requires:      gem(maxitest) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(stackprof) >= 0
Conflicts:     gem(minitest-reporters) >= 2

%description   -n gem-hamlit-devel
High Performance Haml Implementation development package.

%description   -n gem-hamlit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hamlit.


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
%ruby_gemextdir

%files         -n hamlit
%doc README.md
%_bindir/hamlit

%files         -n gem-hamlit-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hamlit-devel
%doc README.md
%ruby_includedir/*


%changelog
* Fri Apr 14 2023 Pavel Skrylev <majioa@altlinux.org> 3.0.3-alt1
- + packaged gem with Ruby Policy 2.0
