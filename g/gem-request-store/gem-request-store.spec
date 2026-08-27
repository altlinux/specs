%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname request_store

Name:          gem-request-store
Version:       1.7.0
Release:       alt1
Summary:       Per-request global storage for Rack
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/steveklabnik/request_store/
Vcs:           https://github.com/steveklabnik/request_store.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(rack) >= 1.4
BuildRequires: gem(rake) >= 13
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 6.0,minitest < 7
%ruby_alias_names request_store,request-store
Requires:      gem(rack) >= 1.4
Requires:      gem(rake) >= 13
Conflicts:     gem(rake) >= 14
Obsoletes:     ruby-request_store < %EVR
Provides:      ruby-request_store = %EVR
Provides:      gem(request_store) = 1.7.0

%description
Per-request global storage for Rack


%if_enabled    doc
%package       -n gem-request-store-doc
Version:       1.7.0
Release:       alt1
Summary:       Per-request global storage for Rack documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета request_store
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(request_store) = 1.7.0

%description   -n gem-request-store-doc
Per-request global storage for Rack documentation files.

%description   -n gem-request-store-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета request_store.
%endif


%if_enabled    devel
%package       -n gem-request-store-devel
Version:       1.7.0
Release:       alt1
Summary:       Per-request global storage for Rack development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета request_store
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(request_store) = 1.7.0
Requires:      gem(minitest) >= 5.0
Conflicts:     gem(minitest) >= 7

%description   -n gem-request-store-devel
Per-request global storage for Rack development package.

%description   -n gem-request-store-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета request_store.
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
%doc LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-request-store-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-request-store-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Sat Aug 22 2026 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- ^ 1.5.0 -> 1.7.0

* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- ^ 1.4.1 -> 1.5.0

* Tue Oct 02 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus
