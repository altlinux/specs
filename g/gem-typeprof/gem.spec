%define        gemname typeprof

Name:          gem-typeprof
Version:       0.21.2
Release:       alt1
Summary:       TypeProf is a type analysis tool for Ruby code based on abstract interpretation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby/typeprof
Vcs:           https://github.com/ruby/typeprof.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rbs) >= 1.8.1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rbs) >= 1.8.1
Provides:      gem(typeprof) = 0.21.2


%description
TypeProf performs a type analysis of non-annotated Ruby code.

It abstractly executes input Ruby code in a level of types instead of values,
gathers what types are passed to and returned by methods, and prints the
analysis result in RBS format, a standard type description format for Ruby
3.0.

This tool is planned to be bundled with Ruby 3.0.


%package       -n typeprof
Version:       0.21.2
Release:       alt1
Summary:       TypeProf is a type analysis tool for Ruby code based on abstract interpretation executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета typeprof
Group:         Other
BuildArch:     noarch

Requires:      gem(typeprof) = 0.21.2

%description   -n typeprof
TypeProf is a type analysis tool for Ruby code based on abstract interpretation
executable(s).

TypeProf performs a type analysis of non-annotated Ruby code.

It abstractly executes input Ruby code in a level of types instead of values,
gathers what types are passed to and returned by methods, and prints the
analysis result in RBS format, a standard type description format for Ruby
3.0.

This tool is planned to be bundled with Ruby 3.0.

%description   -n typeprof -l ru_RU.UTF-8
Исполнямка для самоцвета typeprof.


%package       -n gem-typeprof-doc
Version:       0.21.2
Release:       alt1
Summary:       TypeProf is a type analysis tool for Ruby code based on abstract interpretation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета typeprof
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(typeprof) = 0.21.2

%description   -n gem-typeprof-doc
TypeProf is a type analysis tool for Ruby code based on abstract interpretation
documentation files.

TypeProf performs a type analysis of non-annotated Ruby code.

It abstractly executes input Ruby code in a level of types instead of values,
gathers what types are passed to and returned by methods, and prints the
analysis result in RBS format, a standard type description format for Ruby
3.0.

This tool is planned to be bundled with Ruby 3.0.

%description   -n gem-typeprof-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета typeprof.


%package       -n gem-typeprof-devel
Version:       0.21.2
Release:       alt1
Summary:       TypeProf is a type analysis tool for Ruby code based on abstract interpretation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета typeprof
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(typeprof) = 0.21.2

%description   -n gem-typeprof-devel
TypeProf is a type analysis tool for Ruby code based on abstract interpretation
development package.

TypeProf performs a type analysis of non-annotated Ruby code.

It abstractly executes input Ruby code in a level of types instead of values,
gathers what types are passed to and returned by methods, and prints the
analysis result in RBS format, a standard type description format for Ruby
3.0.

This tool is planned to be bundled with Ruby 3.0.

%description   -n gem-typeprof-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета typeprof.


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

%files         -n typeprof
%doc README.md
%_bindir/typeprof

%files         -n gem-typeprof-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-typeprof-devel
%doc README.md


%changelog
* Sun Apr 03 2022 Pavel Skrylev <majioa@altlinux.org> 0.21.2-alt1
- + packaged gem with Ruby Policy 2.0
