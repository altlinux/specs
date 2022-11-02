%define        gemname kwalify

Name:          gem-kwalify
Version:       0.7.2
Release:       alt1
Summary:       Kwalify is a parser, schema validator, and data binding tool for YAML and JSON
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mgallego/kwalify
Vcs:           https://github.com/mgallego/kwalify.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       kwalify.gemspec
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(kwalify) = 0.7.2


%description
Kwalify is a parser, schema validator, and data bind ing tool for YAML and JSON


%package       -n kwalify
Version:       0.7.2
Release:       alt1
Summary:       Kwalify is a parser, schema validator, and data binding tool for YAML and JSON executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета kwalify
Group:         Other
BuildArch:     noarch

Requires:      gem(kwalify) = 0.7.2

%description   -n kwalify
Kwalify is a parser, schema validator, and data binding tool for YAML and JSON
executable(s).

Kwalify is a parser, schema validator, and data bind ing tool for YAML and JSON

%description   -n kwalify -l ru_RU.UTF-8
Исполнямка для самоцвета kwalify.


%package       -n gem-kwalify-doc
Version:       0.7.2
Release:       alt1
Summary:       Kwalify is a parser, schema validator, and data binding tool for YAML and JSON documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета kwalify
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(kwalify) = 0.7.2

%description   -n gem-kwalify-doc
Kwalify is a parser, schema validator, and data binding tool for YAML and JSON
documentation files.

Kwalify is a parser, schema validator, and data bind ing tool for YAML and JSON

%description   -n gem-kwalify-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета kwalify.


%package       -n gem-kwalify-devel
Version:       0.7.2
Release:       alt1
Summary:       Kwalify is a parser, schema validator, and data binding tool for YAML and JSON development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета kwalify
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(kwalify) = 0.7.2

%description   -n gem-kwalify-devel
Kwalify is a parser, schema validator, and data binding tool for YAML and JSON
development package.

Kwalify is a parser, schema validator, and data bind ing tool for YAML and JSON

%description   -n gem-kwalify-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета kwalify.


%prep
%setup
cp %SOURCE1 ./

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.txt doc-api/files/__/README_txt.html
%ruby_gemspec
%ruby_gemlibdir

%files         -n kwalify
%doc README.txt doc-api/files/__/README_txt.html
%_bindir/kwalify

%files         -n gem-kwalify-doc
%doc README.txt doc-api/files/__/README_txt.html
%ruby_gemdocdir

%files         -n gem-kwalify-devel
%doc README.txt doc-api/files/__/README_txt.html


%changelog
* Tue Nov 01 2022 Pavel Skrylev <majioa@altlinux.org> 0.7.2-alt1
- + packaged gem with Ruby Policy 2.0
