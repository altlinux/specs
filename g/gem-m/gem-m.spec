%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname m

Name:          gem-m
Version:       1.6.2
Release:       alt1
Summary:       A Test::Unit runner that can run tests by line number
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/qrush/m
Vcs:           https://github.com/qrush/m.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0.9.2.2
%if_enabled check
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(method_source) >= 0.6.7
BuildRequires: gem(allocation_stats) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(standard) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names bare
Requires:      ruby >= 2.7
Requires:      gem(method_source) >= 0.6.7
Requires:      gem(rake) >= 0.9.2.2
Provides:      gem(m) = 1.6.2

%description
m stands for metal, a better test/unit and minitest test runner that can run
tests by line number.


%package       -n m
Version:       1.6.2
Release:       alt1
Summary:       A Test::Unit runner that can run tests by line number executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета m
Group:         Other
BuildArch:     noarch

Requires:      gem(m) = 1.6.2

%description   -n m
A Test::Unit runner that can run tests by line number executable(s).

%description   -n m -l ru_RU.UTF-8
Исполнямка для самоцвета m.


%if_enabled    doc
%package       -n gem-m-doc
Version:       1.6.2
Release:       alt1
Summary:       A Test::Unit runner that can run tests by line number documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета m
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(m) = 1.6.2

%description   -n gem-m-doc
A Test::Unit runner that can run tests by line number documentation files.

%description   -n gem-m-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета m.
%endif


%if_enabled    devel
%package       -n gem-m-devel
Version:       1.6.2
Release:       alt1
Summary:       A Test::Unit runner that can run tests by line number development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета m
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(m) = 1.6.2
Requires:      gem(activesupport) >= 0
Requires:      gem(standard) >= 0
Requires:      gem(allocation_stats) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(coveralls) >= 0

%description   -n gem-m-devel
A Test::Unit runner that can run tests by line number development package.

%description   -n gem-m-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета m.
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

%files         -n m
%doc LICENSE README.md
%_bindir/m

%if_enabled    doc
%files         -n gem-m-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-m-devel
%doc LICENSE README.md
%endif


%changelog
* Sun Jan 26 2025 Pavel Skrylev <majioa@altlinux.org> 1.6.2-alt1
- ^ 1.5.1[1] -> 1.6.2

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.5.1.1-alt0.1
- ^ 1.5.1 -> 1.5.1[1]

* Tue Oct 22 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.1-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
