%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname spec

Name:          gem-spec
Version:       5.3.4
Release:       alt1
Summary:       Modified minitest for Appium
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bootstraponline/spec
Vcs:           https://github.com/bootstraponline/spec.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(chronic_duration) >= 0.10.2
BuildRequires: gem(hoe) >= 3.7
BuildRequires: gem(rdoc) >= 4.0
BuildConflicts: gem(chronic_duration) >= 0.11
BuildConflicts: gem(hoe) >= 5
BuildConflicts: gem(rdoc) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency hoe >= 4.2.2,hoe < 5
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_ignore_names minitest
Requires:      ruby >= 1.9.3
Requires:      gem(chronic_duration) >= 0.10.2
Conflicts:     gem(chronic_duration) >= 0.11
Provides:      gem(spec) = 5.3.4

%description
Modified minitest for Appium.


%if_enabled    doc
%package       -n gem-spec-doc
Version:       5.3.4
Release:       alt1
Summary:       Modified minitest for Appium documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета spec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(spec) = 5.3.4

%description   -n gem-spec-doc
Modified minitest for Appium documentation files.

%description   -n gem-spec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета spec.
%endif


%if_enabled    devel
%package       -n gem-spec-devel
Version:       5.3.4
Release:       alt1
Summary:       Modified minitest for Appium development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета spec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(spec) = 5.3.4
Requires:      gem(hoe) >= 3.7
Requires:      gem(rdoc) >= 4.0
Conflicts:     gem(hoe) >= 5
Conflicts:     gem(rdoc) >= 7

%description   -n gem-spec-devel
Modified minitest for Appium development package.

%description   -n gem-spec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета spec.
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
%doc History.txt README.txt readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-spec-doc
%doc History.txt README.txt readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-spec-devel
%doc History.txt README.txt readme.md
%endif


%changelog
* Fri Jan 10 2025 Pavel Skrylev <majioa@altlinux.org> 5.3.4-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
