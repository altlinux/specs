%define        gemname bson

Name:          gem-bson
Version:       4.14.1
Release:       alt1
Summary:       Ruby Implementation of the BSON Specification (2.0.0+)
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://bsonspec.org
Vcs:           https://github.com/mongodb/bson-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-bson < %EVR
Provides:      ruby-bson = %EVR
Provides:      gem(bson) = 4.14.1


%description
An implementation of the BSON specification in Ruby.


%package       -n gem-bson-doc
Version:       4.14.1
Release:       alt1
Summary:       Ruby Implementation of the BSON Specification (2.0.0+) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bson
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bson) = 4.14.1

%description   -n gem-bson-doc
Ruby Implementation of the BSON Specification (2.0.0+) documentation
files.

An implementation of the BSON specification in Ruby.

%description   -n gem-bson-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bson.


%package       -n gem-bson-devel
Version:       4.14.1
Release:       alt1
Summary:       Ruby Implementation of the BSON Specification (2.0.0+) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bson
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bson) = 4.14.1

%description   -n gem-bson-devel
Ruby Implementation of the BSON Specification (2.0.0+) development
package.

An implementation of the BSON specification in Ruby.

%description   -n gem-bson-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bson.


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
%ruby_gemextdir

%files         -n gem-bson-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-bson-devel
%doc README.md
%ruby_includedir/*


%changelog
* Wed Mar 16 2022 Pavel Skrylev <majioa@altlinux.org> 4.14.1-alt1
- ^ 4.12.0 -> 4.14.1

* Sat Apr 24 2021 Pavel Skrylev <majioa@altlinux.org> 4.12.0-alt1
- new version 4.12.0

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 4.8.2-alt1
- ^ 4.4.2 -> 4.8.2
- ! spec tags

* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 4.4.2-alt1
- > Ruby Policy 2.0
- ^ 4.3.0 -> 4.4.2

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1.1
- Rebuild with Ruby 2.5.0

* Thu Jan 18 2018 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version.

* Tue Sep 19 2017 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- Initial build for Sisyphus
