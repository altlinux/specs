%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname google-gax

Name:          gem-google-gax
Version:       1.8.2
Release:       alt2
Summary:       Aids the development of APIs for clients and servers based on GRPC and Google APIs conventions
License:       BSD-3-Clause
Group:         Development/Ruby
Url:           https://github.com/googleapis/gax-ruby
Vcs:           https://github.com/googleapis/gax-ruby.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(codecov) >= 0.1
BuildRequires: gem(google-protobuf) >= 3.9
BuildRequires: gem(googleapis-common-protos) >= 1.3.9
BuildRequires: gem(googleapis-common-protos-types) >= 1.0.4
BuildRequires: gem(googleauth) >= 0.9
BuildRequires: gem(grpc) >= 1.24
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rly) >= 0.2.3
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 0.49.0
BuildRequires: gem(simplecov) >= 0.9
BuildConflicts: gem(codecov) >= 1
BuildConflicts: gem(googleapis-common-protos) >= 2.0
BuildConflicts: gem(googleapis-common-protos-types) >= 2.0
BuildConflicts: gem(grpc) >= 2
BuildConflicts: gem(rly) >= 0.3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0
%ruby_use_gem_dependency google-protobuf >= 3.9
%ruby_use_gem_dependency googleauth >= 0.9
Requires:      ruby >= 2.4.0
Requires:      gem(google-protobuf) >= 3.9
Requires:      gem(googleapis-common-protos) >= 1.3.9
Requires:      gem(googleapis-common-protos-types) >= 1.0.4
Requires:      gem(googleauth) >= 0.9
Requires:      gem(grpc) >= 1.24
Requires:      gem(rly) >= 0.2.3
Conflicts:     gem(googleapis-common-protos) >= 2.0
Conflicts:     gem(googleapis-common-protos-types) >= 2.0
Conflicts:     gem(grpc) >= 2
Conflicts:     gem(rly) >= 0.3
Provides:      gem(google-gax) = 1.8.2

%description
Google API Extensions


%if_enabled    doc
%package       -n gem-google-gax-doc
Version:       1.8.2
Release:       alt2
Summary:       Aids the development of APIs for clients and servers based on GRPC and Google APIs conventions documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-gax
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-gax) = 1.8.2

%description   -n gem-google-gax-doc
Aids the development of APIs for clients and servers based on GRPC and Google
APIs conventions documentation files.

Google API Extensions

%description   -n gem-google-gax-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-gax.
%endif


%if_enabled    devel
%package       -n gem-google-gax-devel
Version:       1.8.2
Release:       alt2
Summary:       Aids the development of APIs for clients and servers based on GRPC and Google APIs conventions development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-gax
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-gax) = 1.8.2
Requires:      gem(codecov) >= 0.1
Requires:      gem(rake) >= 10.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 0.49.0
Requires:      gem(simplecov) >= 0.9
Conflicts:     gem(codecov) >= 1
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(simplecov) >= 1

%description   -n gem-google-gax-devel
Aids the development of APIs for clients and servers based on GRPC and Google
APIs conventions development package.

Google API Extensions

%description   -n gem-google-gax-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-gax.
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
%doc README.md CHANGELOG.md CODE_OF_CONDUCT.md LICENSE
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-google-gax-doc
%doc README.md CHANGELOG.md CODE_OF_CONDUCT.md LICENSE
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-google-gax-devel
%doc README.md CHANGELOG.md CODE_OF_CONDUCT.md LICENSE
%endif


%changelog
* Tue Nov 17 2026 Pavel Skrylev <majioa@altlinux.org> 1.8.2-alt2
- * rebased to upstream source
- ! relaxed some deps

* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 1.8.2-alt1.2
- ! closes build reqs under check condition

* Thu Oct 20 2022 Pavel Skrylev <majioa@altlinux.org> 1.8.2-alt1.1
- ! fix gem build requires to novel gems

* Wed Apr 20 2022 Pavel Skrylev <majioa@altlinux.org> 1.8.2-alt1
- ^ 1.8.1 -> 1.8.2

* Thu Jun 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.8.1-alt1
- + packaged gem with Ruby Policy 2.0
