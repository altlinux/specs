%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname majo

Name:          gem-majo
Version:       1.0.1
Release:       alt1
Summary:       A memory profiler focusing on long-lived objects
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/pocke/majo
Vcs:           https://github.com/pocke/majo.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: fakegit
%if_enabled check
BuildRequires: gem(csv) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rbs) >= 0
BuildRequires: gem(rubocop) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.1.0
Provides:      gem(majo) = 1.0.1

%description
A memory profiler focusing on long-lived objects.


%if_enabled    doc
%package       -n gem-majo-doc
Version:       1.0.1
Release:       alt1
Summary:       A memory profiler focusing on long-lived objects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета majo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(majo) = 1.0.1

%description   -n gem-majo-doc
A memory profiler focusing on long-lived objects documentation files.

%description   -n gem-majo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета majo.
%endif


%if_enabled    devel
%package       -n gem-majo-devel
Version:       1.0.1
Release:       alt1
Summary:       A memory profiler focusing on long-lived objects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета majo
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(majo) = 1.0.1
Requires:      gem(csv) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rbs) >= 0
Requires:      gem(rubocop) >= 0

%description   -n gem-majo-devel
A memory profiler focusing on long-lived objects development package.

%description   -n gem-majo-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета majo.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-majo-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-majo-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Thu Oct 23 2025 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
