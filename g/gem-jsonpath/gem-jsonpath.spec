%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname jsonpath

Name:          gem-jsonpath
Version:       1.1.5
Release:       alt1
Summary:       Ruby implementation of JsonPath
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/joshbuddy/jsonpath
Vcs:           https://github.com/joshbuddy/jsonpath.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(code_stats) >= 0
BuildRequires: gem(minitest) >= 2.2.0
BuildRequires: gem(phocus) >= 0
BuildRequires: gem(racc) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(multi_json) >= 0
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      gem(multi_json) >= 0
Provides:      gem(jsonpath) = 1.1.5


%description
Ruby implementation of http://goessner.net/articles/JsonPath/.


%package       -n jsonpath
Version:       1.1.5
Release:       alt1
Summary:       Ruby implementation of JsonPath executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета jsonpath
Group:         Other
BuildArch:     noarch

Requires:      gem(jsonpath) = 1.1.5

%description   -n jsonpath
Ruby implementation of http://goessner.net/articles/JsonPath/ executable(s).

%description   -n jsonpath -l ru_RU.UTF-8
Исполнямка для самоцвета jsonpath.


%if_enabled    doc
%package       -n gem-jsonpath-doc
Version:       1.1.5
Release:       alt1
Summary:       Ruby implementation of JsonPath documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jsonpath
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jsonpath) = 1.1.5

%description   -n gem-jsonpath-doc
Ruby implementation of http://goessner.net/articles/JsonPath/ documentation
files.

%description   -n gem-jsonpath-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jsonpath.
%endif


%if_enabled    devel
%package       -n gem-jsonpath-devel
Version:       1.1.5
Release:       alt1
Summary:       Ruby implementation of JsonPath development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета jsonpath
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jsonpath) = 1.1.5
Requires:      gem(bundler) >= 0
Requires:      gem(code_stats) >= 0
Requires:      gem(minitest) >= 2.2.0
Requires:      gem(phocus) >= 0
Requires:      gem(racc) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0
Conflicts:     gem(minitest) >= 6

%description   -n gem-jsonpath-devel
Ruby implementation of http://goessner.net/articles/JsonPath/ development
package.

%description   -n gem-jsonpath-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета jsonpath.
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
%doc README.md test/test_readme.rb
%ruby_gemspec
%ruby_gemlibdir

%files         -n jsonpath
%doc README.md test/test_readme.rb
%_bindir/jsonpath

%if_enabled    doc
%files         -n gem-jsonpath-doc
%doc README.md test/test_readme.rb
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-jsonpath-devel
%doc README.md test/test_readme.rb
%endif


%changelog
* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 1.1.5-alt1
- + packaged gem with Ruby Policy 2.0
