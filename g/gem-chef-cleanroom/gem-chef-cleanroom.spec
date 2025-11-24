%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname chef-cleanroom

Name:          gem-chef-cleanroom
Version:       1.0.5
Release:       alt1
Summary:       (More) safely evaluate Ruby DSLs with cleanroom
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/cleanroom
Vcs:           https://github.com/chef/cleanroom.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(chefstyle) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 1.9.3
Provides:      gem(chef-cleanroom) = 1.0.5

%description
Ruby is an excellent programming language for creating and managing custom DSLs,
but how can you securely evaluate a DSL while explicitly controlling the methods
exposed to the user? Our good friends instance_eval and instance_exec are great,
but they expose all methods - public, protected, and private - to the user. Even
worse, they expose the ability to accidentally or intentionally alter the
behavior of the system! The cleanroom pattern is a safer, more convenient,
Ruby-like approach for limiting the information exposed by a DSL while giving
users the ability to write awesome code!


%if_enabled    doc
%package       -n gem-chef-cleanroom-doc
Version:       1.0.5
Release:       alt1
Summary:       (More) safely evaluate Ruby DSLs with cleanroom documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-cleanroom
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-cleanroom) = 1.0.5

%description   -n gem-chef-cleanroom-doc
(More) safely evaluate Ruby DSLs with cleanroom documentation files.

Ruby is an excellent programming language for creating and managing custom DSLs,
but how can you securely evaluate a DSL while explicitly controlling the methods
exposed to the user? Our good friends instance_eval and instance_exec are great,
but they expose all methods - public, protected, and private - to the user. Even
worse, they expose the ability to accidentally or intentionally alter the
behavior of the system! The cleanroom pattern is a safer, more convenient,
Ruby-like approach for limiting the information exposed by a DSL while giving
users the ability to write awesome code!

%description   -n gem-chef-cleanroom-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-cleanroom.
%endif


%if_enabled    devel
%package       -n gem-chef-cleanroom-devel
Version:       1.0.5
Release:       alt1
Summary:       (More) safely evaluate Ruby DSLs with cleanroom development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-cleanroom
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-cleanroom) = 1.0.5
Requires:      gem(bundler) >= 0
Requires:      gem(chefstyle) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Conflicts:     gem(rspec) >= 4

%description   -n gem-chef-cleanroom-devel
(More) safely evaluate Ruby DSLs with cleanroom development package.

Ruby is an excellent programming language for creating and managing custom DSLs,
but how can you securely evaluate a DSL while explicitly controlling the methods
exposed to the user? Our good friends instance_eval and instance_exec are great,
but they expose all methods - public, protected, and private - to the user. Even
worse, they expose the ability to accidentally or intentionally alter the
behavior of the system! The cleanroom pattern is a safer, more convenient,
Ruby-like approach for limiting the information exposed by a DSL while giving
users the ability to write awesome code!

%description   -n gem-chef-cleanroom-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-cleanroom.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-chef-cleanroom-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-chef-cleanroom-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Thu Nov 20 2025 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
