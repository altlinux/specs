%define        _unpackaged_files_terminate_build 1
%define        gemname baltix

Name:          gem-baltix
Version:       0.2
Release:       alt1
Summary:       Baltix is setup replacement and spec control utility for RPM/local packages
License:       MIT
Group:         Development/Ruby
Url:           https://github.org/majioa/baltix
Vcs:           https://github.org/majioa/baltix.git
Packager:      Baltix Development Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar

BuildRequires(pre): rpm-build-baltix
%baltix_with_parts doc,exec
BuildRequires: ruby >= 3.0.0
%if_enabled check
BuildRequires: rubocop
BuildRequires: libruby-devel
%endif
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(rake) >= 13.0.6
BuildConflicts: gem(bundler) >= 3
%if_enabled check
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(cucumber) >= 5.2
BuildRequires: gem(digest) >= 0
BuildRequires: gem(erb) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(open3) >= 0
BuildRequires: gem(optparse) >= 0
BuildRequires: gem(ostruct) >= 0
BuildRequires: gem(pathname) >= 0
BuildRequires: gem(pry) >= 0.13
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rubocop) >= 1.81.7
BuildRequires: gem(rubocop-md) >= 3.0.0
BuildRequires: gem(rubocop-performance) >= 1.26.1
BuildRequires: gem(rubocop-rspec) >= 3.9.0
BuildRequires: gem(shellwords) >= 0
BuildRequires: gem(shoulda-matchers-cucumber) >= 1.0.1
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-lcov) >= 0
BuildRequires: gem(stringio) >= 0
BuildRequires: gem(tempfile) >= 0
BuildRequires: gem(time) >= 0
BuildRequires: gem(timecop) >= 0
BuildRequires: gem(tmpdir) >= 0
BuildRequires: gem(yaml) >= 0
BuildConflicts: gem(cucumber) >= 6
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 1.82
BuildConflicts: gem(rubocop-md) >= 3.1
BuildConflicts: gem(rubocop-performance) >= 1.27
BuildConflicts: gem(rubocop-rspec) >= 3.10
BuildConflicts: gem(shoulda-matchers-cucumber) >= 2
%endif

%add_findreq_skiplist %baltix_ruby_gemslibdir/**/*
%add_findprov_skiplist %baltix_ruby_gemslibdir/**/*
Requires:      xz
Requires:      ruby >= 3.0.0
Requires:      gem(bundler) >= 2.0
Requires:      gem(digest) >= 0
Requires:      gem(erb) >= 0
Requires:      gem(json) >= 0
Requires:      gem(open3) >= 0
Requires:      gem(optparse) >= 0
Requires:      gem(ostruct) >= 0
Requires:      gem(pathname) >= 0
Requires:      gem(rake) >= 13.0.6
Requires:      gem(rdoc) >= 0
Requires:      gem(shellwords) >= 0
Requires:      gem(stringio) >= 0
Requires:      gem(tempfile) >= 0
Requires:      gem(time) >= 0
Requires:      gem(tmpdir) >= 0
Requires:      gem(yaml) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14
Provides:      gem(baltix) = 0.2

%description
Baltix is setup replacement and spec control utility for RPM/local packages


%if_enabled    exec
%package       -n baltix
Version:       0.2
Release:       alt1
Summary:       Baltix is setup replacement and spec control utility for RPM/local packages executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета baltix
Group:         Other
BuildArch:     noarch

Requires:      gem(baltix) = 0.2

%description   -n baltix
Baltix is setup replacement and spec control utility for RPM/local packages
executable(s).

%description   -n baltix -l ru_RU.UTF-8
Исполнямка для самоцвета baltix.
%endif


%if_enabled    doc
%package       -n gem-baltix-doc
Version:       0.2
Release:       alt1
Summary:       Baltix is setup replacement and spec control utility for RPM/local packages documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета baltix
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(baltix) = 0.2

%description   -n gem-baltix-doc
Baltix is setup replacement and spec control utility for RPM/local packages
documentation files.

%description   -n gem-baltix-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета baltix.
%endif


%if_enabled    devel
%package       -n gem-baltix-devel
Version:       0.2
Release:       alt1
Summary:       Baltix is setup replacement and spec control utility for RPM/local packages development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета baltix
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(baltix) = 0.2
Requires:      gem(activesupport) >= 0
Requires:      gem(cucumber) >= 5.2
Requires:      gem(pry) >= 0.13
Requires:      gem(rubocop) >= 1.81.7
Requires:      gem(rubocop-md) >= 3.0.0
Requires:      gem(rubocop-performance) >= 1.26.1
Requires:      gem(rubocop-rspec) >= 3.9.0
Requires:      gem(shoulda-matchers-cucumber) >= 1.0.1
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-lcov) >= 0
Requires:      gem(timecop) >= 0
Conflicts:     gem(cucumber) >= 6
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rubocop) >= 1.82
Conflicts:     gem(rubocop-md) >= 3.1
Conflicts:     gem(rubocop-performance) >= 1.27
Conflicts:     gem(rubocop-rspec) >= 3.10
Conflicts:     gem(shoulda-matchers-cucumber) >= 2

%description   -n gem-baltix-devel
Baltix is setup replacement and spec control utility for RPM/local packages
development package.

%description   -n gem-baltix-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета baltix.
%endif


%prep
%setup

%build
%baltix_make

%install
%baltix_install

%check
%baltix_test


%files
%doc LICENSE README.md
%b_ruby_gemspec
%b_ruby_gemlibdir

%if_enabled    exec
%files         -n baltix
%doc LICENSE README.md
%_bindir/baltix
%endif

%if_enabled    doc
%files         -n gem-baltix-doc
%doc LICENSE README.md
%b_ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-baltix-devel
%doc LICENSE README.md
%endif


%changelog
* Thu Nov 19 2026 Pavel Skrylev <majioa@altlinux.org> 0.2-alt1
- ^ 0.1.2 -> 0.2
- * built Baltix RPMs with the source CLI
- * switched Baltix to the packaged RPM build macros

* Wed Jul 22 2026 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
