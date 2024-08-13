%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hotwater

Name:          gem-hotwater
Version:       0.1.2.1
Release:       alt0.1
Summary:       Fast string edit distance
License:       Unlicense
Group:         Development/Ruby
Url:           http://github.com/colinsurprenant/hotwater
Vcs:           https://github.com/colinsurprenant/hotwater.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(ffi) >= 0
BuildRequires: gem(ffi-compiler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rake) >= 0
Requires:      gem(ffi) >= 0
Requires:      gem(ffi-compiler) >= 0
Provides:      gem(hotwater) = 0.1.2.1

%ruby_use_gem_version hotwater:0.1.2.1

%description
Ruby & JRuby gem with fast string edit distance algorithms C implementations
with FFI bindings


%if_enabled    doc
%package       -n gem-hotwater-doc
Version:       0.1.2.1
Release:       alt0.1
Summary:       Fast string edit distance documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hotwater
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hotwater) = 0.1.2.1

%description   -n gem-hotwater-doc
Fast string edit distance documentation files.

Ruby & JRuby gem with fast string edit distance algorithms C implementations
with FFI bindings

%description   -n gem-hotwater-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hotwater.
%endif


%if_enabled    devel
%package       -n gem-hotwater-devel
Version:       0.1.2.1
Release:       alt0.1
Summary:       Fast string edit distance development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hotwater
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hotwater) = 0.1.2.1
Requires:      gem(rspec) >= 0

%description   -n gem-hotwater-devel
Fast string edit distance development package.

Ruby & JRuby gem with fast string edit distance algorithms C implementations
with FFI bindings

%description   -n gem-hotwater-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hotwater.
%endif


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-hotwater-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hotwater-devel
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_includedir/*
%endif


%changelog
* Mon Aug 12 2024 Pavel Skrylev <majioa@altlinux.org> 0.1.2.1-alt0.1
- ^ 0.1.2 -> 0.1.2p1

* Sun May 08 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- + packaged gem with Ruby Policy 2.0
