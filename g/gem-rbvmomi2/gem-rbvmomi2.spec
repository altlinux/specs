%define        gemname rbvmomi2

Name:          gem-rbvmomi2
Version:       3.5.0
Release:       alt1
Summary:       Ruby interface to the VMware vSphere API
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ManageIQ/rbvmomi2
Vcs:           https://github.com/manageiq/rbvmomi2.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(pry) >= 0.13.1
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rubocop) >= 1.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(soap4r-ng) >= 2.0
BuildRequires: gem(test-unit) >= 3.3
BuildRequires: gem(yard) >= 0.9.25
BuildRequires: gem(builder) >= 3.2
BuildRequires: gem(json) >= 2.3
BuildRequires: gem(nokogiri) >= 1.12.5
BuildRequires: gem(optimist) >= 3.0
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(soap4r-ng) >= 3
BuildConflicts: gem(test-unit) >= 4
BuildConflicts: gem(yard) >= 0.10
BuildConflicts: gem(builder) >= 4
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(optimist) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
Requires:      gem(builder) >= 3.2
Requires:      gem(json) >= 2.3
Requires:      gem(nokogiri) >= 1.12.5
Requires:      gem(optimist) >= 3.0
Conflicts:     gem(builder) >= 4
Conflicts:     gem(json) >= 3
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(optimist) >= 4
Provides:      gem(rbvmomi2) = 3.5.0


%description
Ruby interface to the VMware vSphere API


%package       -n rbvmomish2
Version:       3.5.0
Release:       alt1
Summary:       Ruby interface to the VMware vSphere API executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rbvmomi2
Group:         Other
BuildArch:     noarch

Requires:      gem(rbvmomi2) = 3.5.0
Conflicts:     rbvmomish

%description   -n rbvmomish2
Ruby interface to the VMware vSphere API executable(s).

%description   -n rbvmomish2 -l ru_RU.UTF-8
Исполнямка для самоцвета rbvmomi2.


%package       -n gem-rbvmomi2-doc
Version:       3.5.0
Release:       alt1
Summary:       Ruby interface to the VMware vSphere API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rbvmomi2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rbvmomi2) = 3.5.0

%description   -n gem-rbvmomi2-doc
Ruby interface to the VMware vSphere API documentation files.

%description   -n gem-rbvmomi2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rbvmomi2.


%package       -n gem-rbvmomi2-devel
Version:       3.5.0
Release:       alt1
Summary:       Ruby interface to the VMware vSphere API development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rbvmomi2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rbvmomi2) = 3.5.0
Requires:      gem(activesupport) >= 0
Requires:      gem(pry) >= 0.13.1
Requires:      gem(rake) >= 13.0
Requires:      gem(rubocop) >= 1.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(soap4r-ng) >= 2.0
Requires:      gem(test-unit) >= 3.3
Requires:      gem(yard) >= 0.9.25
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(soap4r-ng) >= 3
Conflicts:     gem(test-unit) >= 4
Conflicts:     gem(yard) >= 0.10

%description   -n gem-rbvmomi2-devel
Ruby interface to the VMware vSphere API development package.

%description   -n gem-rbvmomi2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rbvmomi2.


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

%files         -n rbvmomish2
%doc README.md
%_bindir/rbvmomish

%files         -n gem-rbvmomi2-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rbvmomi2-devel
%doc README.md


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 3.5.0-alt1
- + packaged gem with Ruby Policy 2.0
