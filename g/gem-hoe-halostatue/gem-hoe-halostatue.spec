%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hoe-halostatue

Name:          gem-hoe-halostatue
Version:       3.0.0
Release:       alt1
Summary:       Hoe::Halostatue is a [Hoe][hoe] meta-plugin
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/halostatue/hoe-halostatue
Vcs:           https://github.com/halostatue/hoe-halostatue.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(minitest-autotest) >= 1.0
BuildRequires: gem(minitest-focus) >= 1.1
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rdoc) >= 6.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(simplecov-lcov) >= 0.8
BuildRequires: gem(standard) >= 1.50
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(minitest-autotest) >= 2
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rdoc) >= 8
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(simplecov-lcov) >= 1
BuildConflicts: gem(standard) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Provides:      gem(hoe-halostatue) = 3.0.0

%description
Hoe::Halostatue is a [Hoe][hoe] meta-plugin that provides improved support for
Markdown README files, provides features from other plugins, and enables
improved support for [trusted publishing][tp].

Hoe::Halostatue 3.0 incorporates functionality derived from
[`hoe-gemspec2`][hgs2] with more support for [reproducible builds][rb] and
replaces [`hoe-markdown`][hmd] with an internal implementation.


%if_enabled    doc
%package       -n gem-hoe-halostatue-doc
Version:       3.0.0
Release:       alt1
Summary:       Hoe::Halostatue is a [Hoe][hoe] meta-plugin documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-halostatue
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-halostatue) = 3.0.0

%description   -n gem-hoe-halostatue-doc
Hoe::Halostatue is a [Hoe][hoe] meta-plugin that provides improved support for
Markdown README files, provides features from other plugins, and enables
improved support for [trusted publishing][tp] documentation files.

%description   -n gem-hoe-halostatue-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-halostatue.
%endif


%if_enabled    devel
%package       -n gem-hoe-halostatue-devel
Version:       3.0.0
Release:       alt1
Summary:       Hoe::Halostatue is a [Hoe][hoe] meta-plugin development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-halostatue
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-halostatue) = 3.0.0
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(minitest-autotest) >= 1.0
Requires:      gem(minitest-focus) >= 1.1
Requires:      gem(rake) >= 10.0
Requires:      gem(rdoc) >= 6.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(simplecov-lcov) >= 0.8
Requires:      gem(standard) >= 1.50
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(minitest-autotest) >= 2
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rdoc) >= 8
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(simplecov-lcov) >= 1
Conflicts:     gem(standard) >= 2

%description   -n gem-hoe-halostatue-devel
Hoe::Halostatue is a [Hoe][hoe] meta-plugin that provides improved support for
Markdown README files, provides features from other plugins, and enables
improved support for [trusted publishing][tp] development package.

%description   -n gem-hoe-halostatue-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-halostatue.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-hoe-halostatue-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hoe-halostatue-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md
%endif


%changelog
* Thu May 21 2026 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
