%define        gemname chandler

Name:          gem-chandler
Version:       0.9.0
Release:       alt1.1
Summary:       Syncs CHANGELOG entries to GitHub's release notes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mattbrictson/chandler
Vcs:           https://github.com/mattbrictson/chandler.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(netrc) >= 0
BuildRequires: gem(octokit) >= 2.2.0
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(coveralls) >= 0.8.20 gem(coveralls) < 0.9
BuildRequires: gem(danger) >= 5.11 gem(danger) < 10
BuildRequires: gem(rake) >= 12.0 gem(rake) < 14
BuildRequires: gem(minitest) >= 5.10 gem(minitest) < 6
BuildRequires: gem(minitest-reporters) >= 1.1 gem(minitest-reporters) < 2
BuildRequires: gem(mocha) >= 1.2 gem(mocha) < 2
BuildRequires: gem(rubocop) >= 0.48.1 gem(rubocop) < 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency danger >= 8.6.1,danger < 10
Requires:      gem(netrc) >= 0
Requires:      gem(octokit) >= 2.2.0
Provides:      gem(chandler) = 0.9.0

%description
chandler syncs your CHANGELOG entries to GitHub's release notes so you don't
have to enter release notes manually. For Ruby projects, you can even add
chandler to your gem's Rakefile to make this an automatic part of your release
process!


%package       -n chandler
Version:       0.9.0
Release:       alt1.1
Summary:       Syncs CHANGELOG entries to GitHub's release notes executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета chandler
Group:         Other
BuildArch:     noarch

Requires:      gem(chandler) = 0.9.0

%description   -n chandler
Syncs CHANGELOG entries to GitHub's release notes executable(s).

chandler syncs your CHANGELOG entries to GitHub's release notes so you don't
have to enter release notes manually. For Ruby projects, you can even add
chandler to your gem's Rakefile to make this an automatic part of your release
process!

%description   -n chandler -l ru_RU.UTF-8
Исполнямка для самоцвета chandler.


%package       -n gem-chandler-doc
Version:       0.9.0
Release:       alt1.1
Summary:       Syncs CHANGELOG entries to GitHub's release notes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chandler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chandler) = 0.9.0

%description   -n gem-chandler-doc
Syncs CHANGELOG entries to GitHub's release notes documentation files.

chandler syncs your CHANGELOG entries to GitHub's release notes so you don't
have to enter release notes manually. For Ruby projects, you can even add
chandler to your gem's Rakefile to make this an automatic part of your release
process!

%description   -n gem-chandler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chandler.


%package       -n gem-chandler-devel
Version:       0.9.0
Release:       alt1.1
Summary:       Syncs CHANGELOG entries to GitHub's release notes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chandler
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chandler) = 0.9.0
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(coveralls) >= 0.8.20 gem(coveralls) < 0.9
Requires:      gem(danger) >= 5.11 gem(danger) < 10
Requires:      gem(rake) >= 12.0 gem(rake) < 14
Requires:      gem(minitest) >= 5.10 gem(minitest) < 6
Requires:      gem(minitest-reporters) >= 1.1 gem(minitest-reporters) < 2
Requires:      gem(mocha) >= 1.2 gem(mocha) < 2
Requires:      gem(rubocop) >= 0.48.1 gem(rubocop) < 2

%description   -n gem-chandler-devel
Syncs CHANGELOG entries to GitHub's release notes development package.

chandler syncs your CHANGELOG entries to GitHub's release notes so you don't
have to enter release notes manually. For Ruby projects, you can even add
chandler to your gem's Rakefile to make this an automatic part of your release
process!

%description   -n gem-chandler-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chandler.


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

%files         -n chandler
%doc README.md
%_bindir/chandler

%files         -n gem-chandler-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-chandler-devel
%doc README.md


%changelog
* Fri Oct 14 2022 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1.1
- ! closes gem build requires into the check condition

* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1
- + packaged gem with Ruby Policy 2.0
