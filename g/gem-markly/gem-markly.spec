%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname markly

Name:          gem-markly
Version:       0.10.0
Release:       alt1
Summary:       CommonMark parser and renderer. Written in C, wrapped in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/markly
Vcs:           https://github.com/ioquatix/markly.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bake) >= 0
BuildRequires: gem(covered) >= 0
BuildRequires: gem(sus) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(markly) = 0.10.0


%description
CommonMark parser and renderer. Written in C, wrapped in Ruby.


%if_enabled    doc
%package       -n gem-markly-doc
Version:       0.10.0
Release:       alt1
Summary:       CommonMark parser and renderer. Written in C, wrapped in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета markly
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(markly) = 0.10.0

%description   -n gem-markly-doc
CommonMark parser and renderer. Written in C, wrapped in Ruby documentation
files.

%description   -n gem-markly-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета markly.
%endif


%if_enabled    devel
%package       -n gem-markly-devel
Version:       0.10.0
Release:       alt1
Summary:       CommonMark parser and renderer. Written in C, wrapped in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета markly
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(markly) = 0.10.0
Requires:      gem(bake) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(sus) >= 0

%description   -n gem-markly-devel
CommonMark parser and renderer. Written in C, wrapped in Ruby development
package.

%description   -n gem-markly-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета markly.
%endif


%package       -n markly
Version:       0.10.0
Release:       alt1
Summary:       CommonMark parser and renderer. Written in C, wrapped in Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета markly
Group:         Other
BuildArch:     noarch

Requires:      gem(markly) = 0.10.0

%description   -n markly
CommonMark parser and renderer. Written in C, wrapped in Ruby.

%description   -n markly -l ru_RU.UTF-8
Исполнямка для самоцвета markly.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc readme.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-markly-doc
%doc readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-markly-devel
%doc readme.md
%ruby_includedir/*
%endif

%files         -n markly
%doc readme.md


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt1
- ^ 0.7.0 -> 0.10.0

* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- ^ 0.6.0 -> 0.7.0

* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- + packaged gem with Ruby Policy 2.0
