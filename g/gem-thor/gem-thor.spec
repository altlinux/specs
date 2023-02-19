%define        gemname thor

Name:          gem-thor
Version:       1.2.1
Release:       alt1
Summary:       Thor is a toolkit for building powerful command-line interfaces
License:       MIT
Group:         Development/Ruby
Url:           http://whatisthor.com/
Vcs:           https://github.com/erikhuda/thor.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(childlabor) >= 0
BuildRequires: gem(coveralls) >= 0.8.19
BuildRequires: gem(rspec) >= 3.2
BuildRequires: gem(rspec-mocks) >= 3
BuildRequires: gem(rubocop) >= 0.50.0
BuildRequires: gem(simplecov) >= 0.13
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(bundler) >= 1.0
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(bundler) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_ignore_names rails
Provides:      gem(thor) = 1.2.1


%description
Thor is a simple and efficient tool for building self-documenting command line
utilities. It removes the pain of parsing command line options, writing "USAGE:"
banners, and can also be used as an alternative to the Rake build tool. The
syntax is Rake-like, so it should be familiar to most Rake users.


%package       -n thor
Version:       1.2.1
Release:       alt1
Summary:       Thor is a toolkit for building powerful command-line interfaces executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета thor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(thor) = 1.2.1

%description   -n thor
Thor is a toolkit for building powerful command-line interfaces
executable(s).

Thor is a simple and efficient tool for building self-documenting command line
utilities. It removes the pain of parsing command line options, writing "USAGE:"
banners, and can also be used as an alternative to the Rake build tool. The
syntax is Rake-like, so it should be familiar to most Rake users.

%description   -n thor -l ru_RU.UTF-8
Исполнямка для самоцвета thor.


%package       -n gem-thor-doc
Version:       1.2.1
Release:       alt1
Summary:       Thor is a toolkit for building powerful command-line interfaces documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета thor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(thor) = 1.2.1

%description   -n gem-thor-doc
Thor is a toolkit for building powerful command-line interfaces documentation
files.

Thor is a simple and efficient tool for building self-documenting command line
utilities. It removes the pain of parsing command line options, writing "USAGE:"
banners, and can also be used as an alternative to the Rake build tool. The
syntax is Rake-like, so it should be familiar to most Rake users.

%description   -n gem-thor-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета thor.


%package       -n gem-thor-devel
Version:       1.2.1
Release:       alt1
Summary:       Thor is a toolkit for building powerful command-line interfaces development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета thor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(thor) = 1.2.1
Requires:      gem(rake) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(childlabor) >= 0
Requires:      gem(coveralls) >= 0.8.19
Requires:      gem(rspec) >= 3.2
Requires:      gem(rspec-mocks) >= 3
Requires:      gem(rubocop) >= 0.50.0
Requires:      gem(simplecov) >= 0.13
Requires:      gem(webmock) >= 0
Requires:      gem(bundler) >= 1.0
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(bundler) >= 3

%description   -n gem-thor-devel
Thor is a toolkit for building powerful command-line interfaces development
package.

Thor is a simple and efficient tool for building self-documenting command line
utilities. It removes the pain of parsing command line options, writing "USAGE:"
banners, and can also be used as an alternative to the Rake build tool. The
syntax is Rake-like, so it should be familiar to most Rake users.

%description   -n gem-thor-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета thor.


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

%files         -n thor
%doc README.md
%_bindir/thor

%files         -n gem-thor-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-thor-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt1
- ^ 1.0.1 -> 1.2.1

* Wed Sep 16 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- ^ 0.20.3 -> 1.0.1
- ! spec tags

* Thu Mar 07 2019 Pavel Skrylev <majioa@altlinux.org> 0.20.3-alt2
- > Ruby Policy 2.0.

* Mon Nov 12 2018 Andrey Cherepanov <cas@altlinux.org> 0.20.3-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.20.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Aug 21 2017 Andrey Cherepanov <cas@altlinux.org> 0.20.0-alt1
- New version

* Fri May 22 2015 Andrey Cherepanov <cas@altlinux.org> 0.19.1-alt1
- Initial build for ALT Linux
