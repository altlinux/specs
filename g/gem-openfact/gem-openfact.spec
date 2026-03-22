%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname openfact

Name:          gem-openfact
Version:       5.5.0
Release:       alt1
Summary:       OpenFact, a system inventory tool
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/OpenVoxProject/openfact/
Vcs:           https://github.com/openvoxproject/openfact.git
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         bin.patch
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
BuildRequires: erb
%if_enabled check
BuildRequires: gem(base64) >= 0.1
BuildRequires: gem(ffi) >= 1.16.2
BuildRequires: gem(hocon) >= 1.3
BuildRequires: gem(logger) >= 1.5
BuildRequires: gem(packaging) >= 0
BuildRequires: gem(rake) >= 13.0.6
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 1.5
BuildRequires: gem(rubocop-rspec) >= 2.10
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(sys-filesystem) >= 1.4
BuildRequires: gem(thor) >= 1.0.1
BuildRequires: gem(webmock) >= 3.12
BuildRequires: gem(yard) >= 0.9
BuildConflicts: gem(base64) >= 0.4
BuildConflicts: gem(benchmark) >= 0.6
BuildConflicts: gem(ffi) >= 2
BuildConflicts: gem(hocon) >= 2
BuildConflicts: gem(logger) >= 2
BuildConflicts: gem(ostruct) >= 0.7
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(sys-filesystem) >= 2
BuildConflicts: gem(thor) >= 2
BuildConflicts: gem(tsort) >= 0.3
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency ffi >= 1.17.0,ffi < 2
Requires:      ruby >= 2.5
Requires:      gem(base64) >= 0.1
Requires:      gem(hocon) >= 1.3
Requires:      gem(logger) >= 1.5
Requires:      gem(packaging) >= 0
Requires:      gem(thor) >= 1.0.1
Conflicts:     ruby >= 5.0
Conflicts:     gem(base64) >= 0.4
Conflicts:     gem(benchmark) >= 0.6
Conflicts:     gem(hocon) >= 2
Conflicts:     gem(logger) >= 2
Conflicts:     gem(ostruct) >= 0.7
Conflicts:     gem(thor) >= 2
Conflicts:     gem(tsort) >= 0.3
Provides:      gem(openfact) = 5.5.0

%description
You can prove anything with facts!


%package       -n openfact
Version:       5.5.0
Release:       alt1
Summary:       OpenFact, a system inventory tool executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета openfact
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires(pre): alternatives >= 0:0.2.0-alt0.12
Requires:      gem(openfact) = 5.5.0
Requires:      gem(packaging) >= 0

%description   -n openfact
OpenFact, a system inventory tool executable(s).

You can prove anything with facts!

%description   -n openfact -l ru_RU.UTF-8
Исполнямка для самоцвета openfact.


%if_enabled    doc
%package       -n gem-openfact-doc
Version:       5.5.0
Release:       alt1
Summary:       OpenFact, a system inventory tool documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета openfact
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(openfact) = 5.5.0

%description   -n gem-openfact-doc
OpenFact, a system inventory tool documentation files.

You can prove anything with facts!

%description   -n gem-openfact-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета openfact.
%endif


%if_enabled    devel
%package       -n gem-openfact-devel
Version:       5.5.0
Release:       alt1
Summary:       OpenFact, a system inventory tool development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета openfact
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(openfact) = 5.5.0
Requires:      gem(ffi) >= 1.16.2
Requires:      gem(rake) >= 13.0.6
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-performance) >= 1.5
Requires:      gem(rubocop-rspec) >= 2.10
Requires:      gem(simplecov) >= 0.17
Requires:      gem(sys-filesystem) >= 1.4
Requires:      gem(webmock) >= 3.12
Requires:      gem(yard) >= 0.9
Conflicts:     gem(ffi) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 4
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(sys-filesystem) >= 2
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(yard) >= 1

%description   -n gem-openfact-devel
OpenFact, a system inventory tool development package.

You can prove anything with facts!

%description   -n gem-openfact-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета openfact.
%endif


%prep
%setup
%autopatch -p1

%build
%ruby_build

%install
%ruby_install
mkdir -p %buildroot%_altdir
rm -rf %buildroot%_bindir/openfact
echo "%_bindir/facter /usr/lib/ruby/gemie/gems/%gemname-%version/bin/openfact 50" > %buildroot%_altdir/openfact

%check
%ruby_test

%files
%doc LICENSE CHANGELOG.md CONTRIBUTING.md HISTORY.md README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n openfact
%doc LICENSE CHANGELOG.md CONTRIBUTING.md HISTORY.md README.md
%_altdir/openfact
%_man1dir/openfact.1.xz

%if_enabled    doc
%files         -n gem-openfact-doc
%doc LICENSE CHANGELOG.md CONTRIBUTING.md HISTORY.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-openfact-devel
%doc LICENSE CHANGELOG.md CONTRIBUTING.md HISTORY.md README.md
%endif


%changelog
* Sat Mar 21 2026 Pavel Skrylev <majioa@altlinux.org> 5.5.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
