%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname valkey-glide-rb

Name:          gem-valkey-glide-rb
Version:       1.0.0
Release:       alt1
Summary:       A Ruby client library for Valkey
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/valkey-io/valkey-glide-ruby
Vcs:           https://github.com/valkey-io/valkey-glide-ruby.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(ffi) >= 1.17.0
BuildRequires: gem(minitest) >= 5.16
BuildRequires: gem(minitest-reporters) >= 1.4
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildConflicts: gem(minitest-reporters) >= 2
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0
%ruby_use_gem_dependency minitest >= 6.0
%ruby_use_gem_dependency ffi >= 1.17.0
Requires:      ruby >= 3.0.0
Requires:      gem(ffi) >= 1.17.0
Provides:      gem(valkey-glide-rb) = 1.0.0

%description
A Ruby client library for Valkey


%if_enabled    doc
%package       -n gem-valkey-glide-rb-doc
Version:       1.0.0
Release:       alt1
Summary:       A Ruby client library for Valkey documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета valkey-glide-rb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(valkey-glide-rb) = 1.0.0

%description   -n gem-valkey-glide-rb-doc
A Ruby client library for Valkey documentation files.

%description   -n gem-valkey-glide-rb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета valkey-glide-rb.
%endif


%if_enabled    devel
%package       -n gem-valkey-glide-rb-devel
Version:       1.0.0
Release:       alt1
Summary:       A Ruby client library for Valkey development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета valkey-glide-rb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(valkey-glide-rb) = 1.0.0
Requires:      gem(ffi) >= 1.17.0
Requires:      gem(minitest) >= 5.16
Requires:      gem(minitest-reporters) >= 1.4
Requires:      gem(rake) >= 13.0
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(minitest-reporters) >= 2
Conflicts:     gem(rake) >= 14

%description   -n gem-valkey-glide-rb-devel
A Ruby client library for Valkey development package.

%description   -n gem-valkey-glide-rb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета valkey-glide-rb.
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
%doc CHANGELOG.md CONTRIBUTING.md README.md THIRD_PARTY_LICENSES_RUBY
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-valkey-glide-rb-doc
%doc CHANGELOG.md CONTRIBUTING.md README.md THIRD_PARTY_LICENSES_RUBY
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-valkey-glide-rb-devel
%doc CHANGELOG.md CONTRIBUTING.md README.md THIRD_PARTY_LICENSES_RUBY
%endif


%changelog
* Mon Sep 28 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
