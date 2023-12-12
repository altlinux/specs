%define        _unpackaged_files_terminate_build 1
%define        gemname rubyzip

Name:          gem-rubyzip
Version:       2.3.2
Release:       alt1
Summary:       rubyzip is a ruby module for reading and writing zip files
License:       BSD 2-Clause
Group:         Development/Ruby
Url:           https://github.com/rubyzip/rubyzip
Vcs:           https://github.com/rubyzip/rubyzip.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: zip
%if_with check
BuildRequires: gem(coveralls) >= 0.7
BuildRequires: gem(minitest) >= 5.4
BuildRequires: gem(pry) >= 0.10
BuildRequires: gem(rake) >= 12.3
BuildRequires: gem(rubocop) >= 0.79
BuildConflicts: gem(coveralls) >= 1
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Provides:      gem(rubyzip) = 2.3.2


%description
rubyzip is a ruby module for reading and writing zip files.


%package       -n gem-rubyzip-doc
Version:       2.3.2
Release:       alt1
Summary:       rubyzip is a ruby module for reading and writing zip files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubyzip
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubyzip) = 2.3.2

%description   -n gem-rubyzip-doc
rubyzip is a ruby module for reading and writing zip files documentation files.

%description   -n gem-rubyzip-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubyzip.


%package       -n gem-rubyzip-devel
Version:       2.3.2
Release:       alt1
Summary:       rubyzip is a ruby module for reading and writing zip files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubyzip
Group:         Development/Ruby
BuildArch:     noarch

Requires:      zip
Requires:      gem(rubyzip) = 2.3.2
Requires:      gem(coveralls) >= 0.7
Requires:      gem(minitest) >= 5.4
Requires:      gem(pry) >= 0.10
Requires:      gem(rake) >= 12.3
Requires:      gem(rubocop) >= 0.79
Conflicts:     gem(coveralls) >= 1
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rubocop) >= 2

%description   -n gem-rubyzip-devel
rubyzip is a ruby module for reading and writing zip files development package.

%description   -n gem-rubyzip-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubyzip.


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

%files         -n gem-rubyzip-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubyzip-devel
%doc README.md


%changelog
* Fri Dec 01 2023 Pavel Skrylev <majioa@altlinux.org> 2.3.2-alt1
- ^ 2.3.0 -> 2.3.2

* Thu May 27 2021 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- ^ 1.2.4 -> 2.3.0

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.4-alt1
- update (^) 1.2.3 -> 1.2.4
- update to (^) Ruby Policy 2.0

* Sat May 25 2019 Andrey Cherepanov <cas@altlinux.org> 1.2.3-alt1
- New version.

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.2-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.7-alt2.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 25 2018 Dmitry Terekhin <jqt4@altlinux.org> 1.1.7-alt2
- Filter the "ruby(jruby)" dependency for mipsel build

* Tue Feb 17 2015 Andrey Cherepanov <cas@altlinux.org> 1.1.7-alt1
- Initial build for ALT Linux
