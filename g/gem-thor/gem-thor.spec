%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname thor

Name:          gem-thor
Version:       1.3.2
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
BuildRequires: gem(bundler) >= 1.0
BuildRequires: gem(childlabor) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0.13
BuildRequires: gem(webmock) >= 3.13.0
BuildConflicts: gem(bundler) >= 3
%if_enabled check
BuildRequires: gem(coveralls_reborn) >= 0.23.1
BuildRequires: gem(rspec) >= 3.2
BuildRequires: gem(rspec-mocks) >= 3
BuildRequires: gem(rubocop) >= 1.15.0
BuildConflicts: gem(coveralls_reborn) >= 1
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency coveralls_reborn >= 0.28,coveralls_reborn < 1
%ruby_ignore_names _names
Requires:      ruby >= 2.6.0
Requires:      rubygems >= 1.3.5
Provides:      gem(thor) = 1.3.2

%description
Thor is a simple and efficient tool for building self-documenting command line
utilities. It removes the pain of parsing command line options, writing "USAGE:"
banners, and can also be used as an alternative to the Rake build tool. The
syntax is Rake-like, so it should be familiar to most Rake users.


%package       -n thor
Version:       1.3.2
Release:       alt1
Summary:       Thor is a toolkit for building powerful command-line interfaces executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета thor
Group:         Other
BuildArch:     noarch

Requires:      gem(thor) = 1.3.2

%description   -n thor
Thor is a toolkit for building powerful command-line interfaces
executable(s).

Thor is a simple and efficient tool for building self-documenting command line
utilities. It removes the pain of parsing command line options, writing "USAGE:"
banners, and can also be used as an alternative to the Rake build tool. The
syntax is Rake-like, so it should be familiar to most Rake users.

%description   -n thor -l ru_RU.UTF-8
Исполнямка для самоцвета thor.


%if_enabled    doc
%package       -n gem-thor-doc
Version:       1.3.2
Release:       alt1
Summary:       Thor is a toolkit for building powerful command-line interfaces documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета thor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(thor) = 1.3.2

%description   -n gem-thor-doc
Thor is a toolkit for building powerful command-line interfaces documentation
files.

Thor is a simple and efficient tool for building self-documenting command line
utilities. It removes the pain of parsing command line options, writing "USAGE:"
banners, and can also be used as an alternative to the Rake build tool. The
syntax is Rake-like, so it should be familiar to most Rake users.

%description   -n gem-thor-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета thor.
%endif


%if_enabled    devel
%package       -n gem-thor-devel
Version:       1.3.2
Release:       alt1
Summary:       Thor is a toolkit for building powerful command-line interfaces development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета thor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(thor) = 1.3.2
Requires:      gem(bundler) >= 1.0
Requires:      gem(coveralls_reborn) >= 0.23.1
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(coveralls_reborn) >= 1
Conflicts:     gem(rubocop) >= 2

%description   -n gem-thor-devel
Thor is a toolkit for building powerful command-line interfaces development
package.

Thor is a simple and efficient tool for building self-documenting command line
utilities. It removes the pain of parsing command line options, writing "USAGE:"
banners, and can also be used as an alternative to the Rake build tool. The
syntax is Rake-like, so it should be familiar to most Rake users.

%description   -n gem-thor-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета thor.
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
%doc CONTRIBUTING.md LICENSE.md README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n thor
%doc CONTRIBUTING.md LICENSE.md README.md
%_bindir/thor

%if_enabled    doc
%files         -n gem-thor-doc
%doc CONTRIBUTING.md LICENSE.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-thor-devel
%doc CONTRIBUTING.md LICENSE.md README.md
%endif


%changelog
* Wed Jan 15 2025 Pavel Skrylev <majioa@altlinux.org> 1.3.2-alt1
- ^ 1.2.1 -> 1.3.2

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
