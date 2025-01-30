%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-spec-context

Name:          gem-minitest-spec-context
Version:       0.0.5
Release:       alt1
Summary:       Provides context method to MiniTest::Spec
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ywen/minitest-spec-context
Vcs:           https://github.com/ywen/minitest-spec-context.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(activesupport) >= 6.0
BuildRequires: gem(minitest) >= 0
BuildConflicts: gem(activesupport) >= 8
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency activesupport >= 7.1,activesupport < 8
Provides:      gem(minitest-spec-context) = 0.0.5

%description
This gem provides a context method for MiniTest::Spec.


%if_enabled    doc
%package       -n gem-minitest-spec-context-doc
Version:       0.0.5
Release:       alt1
Summary:       Provides context method to MiniTest::Spec documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-spec-context
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-spec-context) = 0.0.5

%description   -n gem-minitest-spec-context-doc
Provides context method to MiniTest::Spec documentation files.

This gem provides a context method for MiniTest::Spec.

%description   -n gem-minitest-spec-context-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-spec-context.
%endif


%if_enabled    devel
%package       -n gem-minitest-spec-context-devel
Version:       0.0.5
Release:       alt1
Summary:       Provides context method to MiniTest::Spec development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-spec-context
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-spec-context) = 0.0.5
Requires:      gem(activesupport) >= 6.0
Requires:      gem(minitest) >= 0
Conflicts:     gem(activesupport) >= 8

%description   -n gem-minitest-spec-context-devel
Provides context method to MiniTest::Spec development package.

This gem provides a context method for MiniTest::Spec.

%description   -n gem-minitest-spec-context-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-spec-context.
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

%if_enabled    doc
%files         -n gem-minitest-spec-context-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-spec-context-devel
%doc LICENSE README.md
%endif


%changelog
* Mon Jan 27 2025 Pavel Skrylev <majioa@altlinux.org> 0.0.5-alt1
- ^ 0.0.4 -> 0.0.5

* Fri Dec 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.4-alt1
- + packaged gem with Ruby Policy 2.0
