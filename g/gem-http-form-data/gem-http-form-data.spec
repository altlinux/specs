%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname http-form_data

Name:          gem-http-form-data
Version:       2.3.0
Release:       alt1
Summary:       http-form_data-2.3.0
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/httprb/form_data.rb
Vcs:           https://github.com/httprb/form_data.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(guard) >= 0
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(rspec) >= 3.1
BuildRequires: gem(rubocop) >= 0.48.1
BuildRequires: gem(simplecov) >= 0.9
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Provides:      gem(http-form_data) = 2.3.0


%description
Utility-belt to build form data request bodies. Provides support for
`application/x-www-form-urlencoded` and `multipart/form-data` types.


%if_enabled    doc
%package       -n gem-http-form-data-doc
Version:       2.3.0
Release:       alt1
Summary:       http-form_data-2.3.0 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета http-form_data
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(http-form_data) = 2.3.0

%description   -n gem-http-form-data-doc
http-form_data-2.3.0 documentation files.

Utility-belt to build form data request bodies. Provides support for
`application/x-www-form-urlencoded` and `multipart/form-data` types.
%description   -n gem-http-form-data-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета http-form_data.
%endif


%if_enabled    devel
%package       -n gem-http-form-data-devel
Version:       2.3.0
Release:       alt1
Summary:       http-form_data-2.3.0 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета http-form_data
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(http-form_data) = 2.3.0
Requires:      gem(rake) >= 0
Requires:      gem(guard) >= 0
Requires:      gem(guard-rspec) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(coveralls) >= 0
Requires:      gem(rspec) >= 3.1
Requires:      gem(rubocop) >= 0.48.1
Requires:      gem(simplecov) >= 0.9
Requires:      gem(redcarpet) >= 0
Requires:      gem(yard) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2

%description   -n gem-http-form-data-devel
http-form_data-2.3.0 development package.

Utility-belt to build form data request bodies. Provides support for
`application/x-www-form-urlencoded` and `multipart/form-data` types.
%description   -n gem-http-form-data-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета http-form_data.
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
%files         -n gem-http-form-data-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-http-form-data-devel
%doc README.md
%endif


%changelog
* Wed Apr 17 2024 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- + packaged gem with Ruby Policy 2.0
