%define        gemname json

Name:          gem-json
Version:       2.6.3
Release:       alt1
Summary:       JSON parser and generator
License:       Ruby
Group:         Development/Ruby
Url:           http://flori.github.io/json/
Vcs:           https://github.com/flori/json.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(all_images) >= 0
BuildConflicts: gem(all_images) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-json < %EVR
Obsoletes:     ruby-json-utils < %EVR
Provides:      ruby-json = %EVR
Provides:      ruby-json-utils = %EVR
Provides:      gem(json) = 2.6.3


%description
This library can parse JSON texts and generate them from ruby data structures.


%package       -n gem-json-pure
Version:       2.6.3
Release:       alt1
Summary:       JSON parser and generator
Group:         Development/Ruby
BuildArch:     noarch

Obsoletes:     ruby-json-pure
Provides:      ruby-json-pure
Provides:      gem(json_pure) = 2.6.3

%description   -n gem-json-pure
This library can parse JSON texts and generate them from ruby data
structures.

The package is the compiled-less version of the json gem.


%package       -n gem-json-pure-doc
Version:       2.6.3
Release:       alt1
Summary:       JSON parser and generator documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета json_pure
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(json_pure) = 2.6.3

%description   -n gem-json-pure-doc
JSON parser and generator documentation files.

This library can parse JSON texts and generate them from ruby data
structures.

The package is the compiled-less version of the json gem.

%description   -n gem-json-pure-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета json_pure.


%package       -n gem-json-pure-devel
Version:       2.6.3
Release:       alt1
Summary:       JSON parser and generator development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета json_pure
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(json_pure) = 2.6.3
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(all_images) >= 0
Requires:      gem(json) >= 2.3.0
Conflicts:     gem(all_images) >= 1
Conflicts:     gem(json) >= 3

%description   -n gem-json-pure-devel
JSON parser and generator development package.

This library can parse JSON texts and generate them from ruby data
structures.

The package is the compiled-less version of the json gem.

%description   -n gem-json-pure-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета json_pure.


%package       -n gem-json-doc
Version:       2.6.3
Release:       alt1
Summary:       JSON parser and generator documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета json
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(json) = 2.6.3

%description   -n gem-json-doc
JSON parser and generator documentation files.

This library can parse JSON texts and generate them from ruby data structures.

%description   -n gem-json-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета json.


%package       -n gem-json-devel
Version:       2.6.3
Release:       alt1
Summary:       JSON parser and generator development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета json
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(json) = 2.6.3
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(all_images) >= 0
Conflicts:     gem(all_images) >= 1

%description   -n gem-json-devel
JSON parser and generator development package.

This library can parse JSON texts and generate them from ruby data structures.

%description   -n gem-json-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета json.


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

%files         -n gem-json-pure
%doc README.md
%ruby_gemspecdir/json_pure-2.6.3.gemspec
%ruby_gemslibdir/json_pure-2.6.3

%files         -n gem-json-pure-doc
%doc README.md
%ruby_gemsdocdir/json_pure-2.6.3

%files         -n gem-json-pure-devel
%doc README.md

%files         -n gem-json-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-json-devel
%doc README.md
%ruby_includedir/*


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 2.6.3-alt1
- ^ 2.6.2 -> 2.6.3

* Tue Jul 05 2022 Pavel Skrylev <majioa@altlinux.org> 2.6.2-alt1
- ^ 2.6.1 -> 2.6.2

* Wed Mar 16 2022 Pavel Skrylev <majioa@altlinux.org> 2.6.1-alt1
- ^ 2.5.1 -> 2.6.1

* Thu Jun 24 2021 Pavel Skrylev <majioa@altlinux.org> 2.5.1-alt1
- ^ 2.3.1 -> 2.5.1

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt0.1
- ^ 2.2.0 -> 2.3.1
- ! spec tags and syntax

* Wed Mar 27 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- > Ruby Policy 2.0
- ^ 2.1.0 -> 2.2.0

* Wed Jan 23 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt2
- ! provides and obsoletes.

* Mon Jan 14 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- 1.5.1 -> 2.1.0

* Wed Mar 23 2011 Andriy Stepanov <stanv@altlinux.ru> 1.5.1-alt1
- [1.5.1]

* Sat Sep 25 2010 Alexey I. Froloff <raorn@altlinux.org> 1.1.9-alt1
- [1.1.9]

* Fri Jul 24 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.7-alt1
- Built for Sisyphus
