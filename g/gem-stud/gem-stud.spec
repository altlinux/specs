%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname stud

Name:          gem-stud
Version:       0.0.23
Release:       alt1
Summary:       stud - common code techniques
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/jordansissel/ruby-stud
Vcs:           https://github.com/jordansissel/ruby-stud.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(insist) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(stud) = 0.0.23


%description
small reusable bits of code I'm tired of writing over and over. A library form
of my software-patterns github repo.


%if_enabled    doc
%package       -n gem-stud-doc
Version:       0.0.23
Release:       alt1
Summary:       stud - common code techniques documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета stud
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(stud) = 0.0.23

%description   -n gem-stud-doc
stud - common code techniques documentation files.

small reusable bits of code I'm tired of writing over and over. A library form
of my software-patterns github repo.

%description   -n gem-stud-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета stud.
%endif


%if_enabled    devel
%package       -n gem-stud-devel
Version:       0.0.23
Release:       alt1
Summary:       stud - common code techniques development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета stud
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(stud) = 0.0.23
Requires:      gem(rspec) >= 0
Requires:      gem(insist) >= 0

%description   -n gem-stud-devel
stud - common code techniques development package.

small reusable bits of code I'm tired of writing over and over. A library form
of my software-patterns github repo.

%description   -n gem-stud-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета stud.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-stud-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-stud-devel
%doc README.md
%endif


%changelog
* Tue Aug 20 2024 Pavel Skrylev <majioa@altlinux.org> 0.0.23-alt1
- + packaged gem with Ruby Policy 2.0
