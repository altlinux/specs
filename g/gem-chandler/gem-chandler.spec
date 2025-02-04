%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname chandler

Name:          gem-chandler
Version:       0.9.0.5
Release:       alt1
Summary:       Syncs CHANGELOG entries to GitHub's release notes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mattbrictson/chandler
Vcs:           https://github.com/mattbrictson/chandler.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(coveralls) >= 0.8.20
BuildRequires: gem(danger) >= 6.0
BuildRequires: gem(minitest) >= 5.10
BuildRequires: gem(minitest-reporters) >= 1.1
BuildRequires: gem(mocha) >= 1.2
BuildRequires: gem(netrc) >= 0
BuildRequires: gem(octokit) >= 2.2.0
BuildRequires: gem(rake) >= 12.0
BuildRequires: gem(rubocop) >= 0.48.1
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(coveralls) >= 0.9
BuildConflicts: gem(danger) >= 10
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(minitest-reporters) >= 2
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency danger >= 9.5.1,danger < 10
%ruby_use_gem_dependency mocha >= 2.0,mocha < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      ruby >= 2.3.0
Requires:      gem(netrc) >= 0
Requires:      gem(octokit) >= 2.2.0
Provides:      gem(chandler) = 0.9.0.5

%description
chandler syncs your CHANGELOG entries to GitHub's release notes so you don't
have to enter release notes manually. For Ruby projects, you can even add
chandler to your gem's Rakefile to make this an automatic part of your release
process!


%package       -n chandler
Version:       0.9.0.5
Release:       alt1
Summary:       Syncs CHANGELOG entries to GitHub's release notes executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета chandler
Group:         Other
BuildArch:     noarch

Requires:      gem(chandler) = 0.9.0.5

%description   -n chandler
Syncs CHANGELOG entries to GitHub's release notes executable(s).

chandler syncs your CHANGELOG entries to GitHub's release notes so you don't
have to enter release notes manually. For Ruby projects, you can even add
chandler to your gem's Rakefile to make this an automatic part of your release
process!

%description   -n chandler -l ru_RU.UTF-8
Исполнямка для самоцвета chandler.


%if_enabled    doc
%package       -n gem-chandler-doc
Version:       0.9.0.5
Release:       alt1
Summary:       Syncs CHANGELOG entries to GitHub's release notes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chandler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chandler) = 0.9.0.5

%description   -n gem-chandler-doc
Syncs CHANGELOG entries to GitHub's release notes documentation files.

chandler syncs your CHANGELOG entries to GitHub's release notes so you don't
have to enter release notes manually. For Ruby projects, you can even add
chandler to your gem's Rakefile to make this an automatic part of your release
process!

%description   -n gem-chandler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chandler.
%endif


%if_enabled    devel
%package       -n gem-chandler-devel
Version:       0.9.0.5
Release:       alt1
Summary:       Syncs CHANGELOG entries to GitHub's release notes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chandler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chandler) = 0.9.0.5
Requires:      gem(bundler) >= 2.0
Requires:      gem(coveralls) >= 0.8.20
Requires:      gem(danger) >= 6.0
Requires:      gem(minitest) >= 5.10
Requires:      gem(minitest-reporters) >= 1.1
Requires:      gem(mocha) >= 1.2
Requires:      gem(rake) >= 12.0
Requires:      gem(rubocop) >= 0.48.1
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(coveralls) >= 0.9
Conflicts:     gem(danger) >= 10
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(minitest-reporters) >= 2
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop) >= 2

%description   -n gem-chandler-devel
Syncs CHANGELOG entries to GitHub's release notes development package.

chandler syncs your CHANGELOG entries to GitHub's release notes so you don't
have to enter release notes manually. For Ruby projects, you can even add
chandler to your gem's Rakefile to make this an automatic part of your release
process!

%description   -n gem-chandler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chandler.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n chandler
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%_bindir/chandler

%if_enabled    doc
%files         -n gem-chandler-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-chandler-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%endif


%changelog
* Mon Jan 27 2025 Pavel Skrylev <majioa@altlinux.org> 0.9.0.5-alt1
- ^ 0.9.0 -> 0.9.0.5

* Fri Oct 14 2022 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1.1
- ! closes gem build requires into the check condition

* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1
- + packaged gem with Ruby Policy 2.0
