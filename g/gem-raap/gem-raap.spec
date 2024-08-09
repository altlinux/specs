%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname raap

Name:          gem-raap
Version:       0.10.0
Release:       alt1
Summary:       RBS as a Property
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ksss/raap
Vcs:           https://github.com/ksss/raap.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(debug) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rbs) >= 3.0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-on-rbs) >= 0
BuildRequires: gem(steep) >= 0
BuildRequires: gem(timeout) >= 0.4
BuildConflicts: gem(rbs) >= 4
BuildConflicts: gem(timeout) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rbs) >= 3.0
Requires:      gem(timeout) >= 0.4
Conflicts:     gem(rbs) >= 4
Conflicts:     gem(timeout) >= 1
Provides:      gem(raap) = 0.10.0


%description
Property based testing tool with RBS. RaaP is a property based testing tool.
RaaP considers the RBS as a test case. It generates random values for the method
arguments for each type, and then calls the method. The return value of the
method is checked to see if it matches the type, if not, the test fails. If you
write an RBS, it becomes a test case.


%package       -n raap
Version:       0.10.0
Release:       alt1
Summary:       RBS as a Property executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета raap
Group:         Other
BuildArch:     noarch

Requires:      gem(raap) = 0.10.0

%description   -n raap
RBS as a Property executable(s).

Property based testing tool with RBS. RaaP is a property based testing tool.
RaaP considers the RBS as a test case. It generates random values for the method
arguments for each type, and then calls the method. The return value of the
method is checked to see if it matches the type, if not, the test fails. If you
write an RBS, it becomes a test case.


%description   -n raap -l ru_RU.UTF-8
Исполнямка для самоцвета raap.


%if_enabled    doc
%package       -n gem-raap-doc
Version:       0.10.0
Release:       alt1
Summary:       RBS as a Property documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета raap
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(raap) = 0.10.0

%description   -n gem-raap-doc
RBS as a Property documentation files.

Property based testing tool with RBS. RaaP is a property based testing tool.
RaaP considers the RBS as a test case. It generates random values for the method
arguments for each type, and then calls the method. The return value of the
method is checked to see if it matches the type, if not, the test fails. If you
write an RBS, it becomes a test case.

%description   -n gem-raap-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета raap.
%endif


%if_enabled    devel
%package       -n gem-raap-devel
Version:       0.10.0
Release:       alt1
Summary:       RBS as a Property development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета raap
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(raap) = 0.10.0
Requires:      gem(debug) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-on-rbs) >= 0
Requires:      gem(steep) >= 0

%description   -n gem-raap-devel
RBS as a Property development package.

Property based testing tool with RBS. RaaP is a property based testing tool.
RaaP considers the RBS as a test case. It generates random values for the method
arguments for each type, and then calls the method. The return value of the
method is checked to see if it matches the type, if not, the test fails. If you
write an RBS, it becomes a test case.

%description   -n gem-raap-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета raap.
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

%files         -n raap
%doc README.md
%_bindir/raap

%if_enabled    doc
%files         -n gem-raap-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-raap-devel
%doc README.md
%endif


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt1
- + packaged gem with Ruby Policy 2.0
