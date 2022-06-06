%define        gemname hotwater

Name:          gem-hotwater
Version:       0.1.2
Release:       alt1
Summary:       Fast string edit distance
License:       Unlicense
Group:         Development/Ruby
Url:           http://github.com/colinsurprenant/hotwater
Vcs:           https://github.com/colinsurprenant/hotwater.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
BuildRequires: gem(ffi) >= 0
BuildRequires: gem(ffi-compiler) >= 0
BuildRequires: gem(rspec) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rake) >= 0
Requires:      gem(ffi) >= 0
Requires:      gem(ffi-compiler) >= 0
Provides:      gem(hotwater) = 0.1.2

%description
Ruby & JRuby gem with fast string edit distance algorithms C implementations
with FFI bindings


%package       -n gem-hotwater-doc
Version:       0.1.2
Release:       alt1
Summary:       Fast string edit distance documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hotwater
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hotwater) = 0.1.2

%description   -n gem-hotwater-doc
Fast string edit distance documentation files.

Ruby & JRuby gem with fast string edit distance algorithms C implementations
with FFI bindings

%description   -n gem-hotwater-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hotwater.


%package       -n gem-hotwater-devel
Version:       0.1.2
Release:       alt1
Summary:       Fast string edit distance development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hotwater
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hotwater) = 0.1.2
Requires:      gem(rspec) >= 0

%description   -n gem-hotwater-devel
Fast string edit distance development package.

Ruby & JRuby gem with fast string edit distance algorithms C implementations
with FFI bindings

%description   -n gem-hotwater-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hotwater.


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

%files         -n gem-hotwater-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-hotwater-devel
%doc README.md
%ruby_includedir/*


%changelog
* Sun May 08 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- + packaged gem with Ruby Policy 2.0
