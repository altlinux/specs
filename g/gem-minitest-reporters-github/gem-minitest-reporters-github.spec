%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest_reporters_github

Name:          gem-minitest-reporters-github
Version:       1.0.1
Release:       alt1
Summary:       The GitHub Actions reporter for minitest-reporters
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ekohl/minitest_reporters_github
Vcs:           https://github.com/ekohl/minitest_reporters_github.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 13.0
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildRequires: gem(minitest-reporters) >= 1.6.0
BuildConflicts: gem(minitest-reporters) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest-reporters >= 1.6.1,minitest-reporters < 2
%ruby_alias_names minitest_reporters_github,minitest-reporters-github
Requires:      ruby >= 2.7
Requires:      gem(minitest-reporters) >= 1.6.0
Conflicts:     ruby >= 4
Conflicts:     gem(minitest-reporters) >= 2
Provides:      gem(minitest_reporters_github) = 1.0.1

%description
A separate gem until
https://github.com/minitest-reporters/minitest-reporters/pull/332 is merged


%if_enabled    doc
%package       -n gem-minitest-reporters-github-doc
Version:       1.0.1
Release:       alt1
Summary:       The GitHub Actions reporter for minitest-reporters documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest_reporters_github
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest_reporters_github) = 1.0.1

%description   -n gem-minitest-reporters-github-doc
The GitHub Actions reporter for minitest-reporters documentation files.

A separate gem until
https://github.com/minitest-reporters/minitest-reporters/pull/332 is merged

%description   -n gem-minitest-reporters-github-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest_reporters_github.
%endif


%if_enabled    devel
%package       -n gem-minitest-reporters-github-devel
Version:       1.0.1
Release:       alt1
Summary:       The GitHub Actions reporter for minitest-reporters development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest_reporters_github
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest_reporters_github) = 1.0.1
Requires:      gem(rake) >= 13.0
Conflicts:     gem(rake) >= 14

%description   -n gem-minitest-reporters-github-devel
The GitHub Actions reporter for minitest-reporters development package.

A separate gem until
https://github.com/minitest-reporters/minitest-reporters/pull/332 is merged

%description   -n gem-minitest-reporters-github-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest_reporters_github.
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
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-minitest-reporters-github-doc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-reporters-github-devel
%endif


%changelog
* Mon Jan 13 2025 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
