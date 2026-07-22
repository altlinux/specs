%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname appraisal

Name:          gem-appraisal
Version:       2.5.0
Release:       alt1
Summary:       Find out what your Ruby gems are worth
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/thoughtbot/appraisal
Vcs:           https://github.com/thoughtbot/appraisal.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(activesupport) >= 3.2.21
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(thor) >= 0.14.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(thor) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency thor >= 1.3.2,thor < 2
Requires:      ruby >= 2.3.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(thor) >= 0.14.0
Conflicts:     gem(thor) >= 2
Provides:      gem(appraisal) = 2.5.0

%description
Appraisal integrates with bundler and rake to test your library against
different versions of dependencies in repeatable scenarios called "appraisals."


%package       -n appraisal
Version:       2.5.0
Release:       alt1
Summary:       Find out what your Ruby gems are worth executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета appraisal
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(appraisal) = 2.5.0
Requires:      gem(thor) >= 0.14.0
Conflicts:     gem(thor) >= 2

%description   -n appraisal
Find out what your Ruby gems are worth executable(s).

Appraisal integrates with bundler and rake to test your library against
different versions of dependencies in repeatable scenarios called "appraisals."

%description   -n appraisal -l ru_RU.UTF-8
Исполнямка для самоцвета appraisal.


%if_enabled    doc
%package       -n gem-appraisal-doc
Version:       2.5.0
Release:       alt1
Summary:       Find out what your Ruby gems are worth documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета appraisal
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(appraisal) = 2.5.0

%description   -n gem-appraisal-doc
Find out what your Ruby gems are worth documentation files.

Appraisal integrates with bundler and rake to test your library against
different versions of dependencies in repeatable scenarios called "appraisals."

%description   -n gem-appraisal-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета appraisal.
%endif


%if_enabled    devel
%package       -n gem-appraisal-devel
Version:       2.5.0
Release:       alt1
Summary:       Find out what your Ruby gems are worth development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета appraisal
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(appraisal) = 2.5.0
Requires:      gem(activesupport) >= 3.2.21
Requires:      gem(rspec) >= 3.0
Conflicts:     gem(rspec) >= 4

%description   -n gem-appraisal-devel
Find out what your Ruby gems are worth development package.

Appraisal integrates with bundler and rake to test your library against
different versions of dependencies in repeatable scenarios called "appraisals."

%description   -n gem-appraisal-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета appraisal.
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
%doc CONTRIBUTING.md MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n appraisal
%doc CONTRIBUTING.md MIT-LICENSE README.md
%_bindir/appraisal

%if_enabled    doc
%files         -n gem-appraisal-doc
%doc CONTRIBUTING.md MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-appraisal-devel
%doc CONTRIBUTING.md MIT-LICENSE README.md
%endif


%changelog
* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 2.5.0-alt1
- ^ 2.4.1 -> 2.5.0

* Mon Oct 10 2022 Pavel Skrylev <majioa@altlinux.org> 2.4.1-alt1
- ^ 2.4.0 -> 2.4.1

* Mon Jun 21 2021 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- + packaged gem with Ruby Policy 2.0
