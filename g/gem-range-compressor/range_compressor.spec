%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname range_compressor

Name:          gem-range-compressor
Version:       1.2.0
Release:       alt1
Summary:       Compresses Arrays of Objects to Arrays of Ranges
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jaynetics/range_compressor
Vcs:           https://github.com/jaynetics/range_compressor.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.8
BuildRequires: gem(sorted_set) >= 1.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(sorted_set) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names range_compressor,range-compressor
Requires:      ruby >= 1.9.3
Provides:      gem(range_compressor) = 1.2.0

%description
Compresses Arrays of Objects to Arrays of Ranges.


%if_enabled    doc
%package       -n gem-range-compressor-doc
Version:       1.2.0
Release:       alt1
Summary:       Compresses Arrays of Objects to Arrays of Ranges documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета range_compressor
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(range_compressor) = 1.2.0

%description   -n gem-range-compressor-doc
Compresses Arrays of Objects to Arrays of Ranges documentation files.

%description   -n gem-range-compressor-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета range_compressor.
%endif


%if_enabled    devel
%package       -n gem-range-compressor-devel
Version:       1.2.0
Release:       alt1
Summary:       Compresses Arrays of Objects to Arrays of Ranges development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета range_compressor
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(range_compressor) = 1.2.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.8
Requires:      gem(sorted_set) >= 1.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(sorted_set) >= 2

%description   -n gem-range-compressor-devel
Compresses Arrays of Objects to Arrays of Ranges development package.

%description   -n gem-range-compressor-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета range_compressor.
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
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-range-compressor-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-range-compressor-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Thu Oct 30 2025 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
