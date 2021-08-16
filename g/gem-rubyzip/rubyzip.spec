%define        gemname rubyzip

Name:          gem-rubyzip
Version:       2.3.0
Release:       alt1
Summary:       rubyzip is a ruby module for reading and writing zip files
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/rubyzip/rubyzip
Vcs:           https://github.com/rubyzip/rubyzip.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: zip
BuildRequires: gem(coveralls) >= 0.7 gem(coveralls) < 1
BuildRequires: gem(minitest) >= 5.4 gem(minitest) < 6
BuildRequires: gem(pry) >= 0.10 gem(pry) < 1
BuildRequires: gem(rake) >= 12.3 gem(rake) < 14
BuildRequires: gem(rubocop) >= 0.80.1 gem(rubocop) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.13.0,rubocop < 2
Provides:      gem(rubyzip) = 2.3.0

%description
rubyzip is a ruby module for reading and writing zip files.


%package       -n gem-rubyzip-doc
Version:       2.3.0
Release:       alt1
Summary:       rubyzip is a ruby module for reading and writing zip files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubyzip
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubyzip) = 2.3.0

%description   -n gem-rubyzip-doc
rubyzip is a ruby module for reading and writing zip files documentation
files.

rubyzip is a ruby module for reading and writing zip files.

%description   -n gem-rubyzip-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubyzip.


%package       -n gem-rubyzip-devel
Version:       2.3.0
Release:       alt1
Summary:       rubyzip is a ruby module for reading and writing zip files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubyzip
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubyzip) = 2.3.0
Requires:      gem(coveralls) >= 0.7 gem(coveralls) < 1
Requires:      gem(minitest) >= 5.4 gem(minitest) < 6
Requires:      gem(pry) >= 0.10 gem(pry) < 1
Requires:      gem(rake) >= 12.3 gem(rake) < 14
Requires:      gem(rubocop) >= 0.80.1 gem(rubocop) < 2

%description   -n gem-rubyzip-devel
rubyzip is a ruby module for reading and writing zip files development
package.

rubyzip is a ruby module for reading and writing zip files.

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
