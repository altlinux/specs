%define        gemname cleanroom

Name:          gem-cleanroom
Version:       1.0.0
Release:       alt2
Summary:       (More) safely evaluate Ruby DSLs with cleanroom
License:       Apache 2.0
Group:         Development/Ruby
Url:           https://github.com/sethvargo/cleanroom
Vcs:           https://github.com/sethvargo/cleanroom.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-cleanroom < %EVR
Provides:      ruby-cleanroom = %EVR
Provides:      gem(cleanroom) = 1.0.0


%description
Ruby is an excellent programming language for creating and managing custom DSLs,
but how can you securely evaluate a DSL while explicitly controlling the methods
exposed to the user? Our good friends instance_eval and instance_exec are great,
but they expose all methods - public, protected, and private - to the user. Even
worse, they expose the ability to accidentally or intentionally alter the
behavior of the system! The cleanroom pattern is a safer, more convenient,
Ruby-like approach for limiting the information exposed by a DSL while giving
users the ability to write awesome code!

The cleanroom pattern is a unique way for more safely evaluating Ruby DSLs
without adding additional overhead.


%package       -n gem-cleanroom-doc
Version:       1.0.0
Release:       alt2
Summary:       (More) safely evaluate Ruby DSLs with cleanroom documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cleanroom
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(cleanroom) = 1.0.0

%description   -n gem-cleanroom-doc
(More) safely evaluate Ruby DSLs with cleanroom documentation files.

Ruby is an excellent programming language for creating and managing custom DSLs,
but how can you securely evaluate a DSL while explicitly controlling the methods
exposed to the user? Our good friends instance_eval and instance_exec are great,
but they expose all methods - public, protected, and private - to the user. Even
worse, they expose the ability to accidentally or intentionally alter the
behavior of the system! The cleanroom pattern is a safer, more convenient,
Ruby-like approach for limiting the information exposed by a DSL while giving
users the ability to write awesome code!

The cleanroom pattern is a unique way for more safely evaluating Ruby DSLs
without adding additional overhead.

%description   -n gem-cleanroom-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cleanroom.


%package       -n gem-cleanroom-devel
Version:       1.0.0
Release:       alt2
Summary:       (More) safely evaluate Ruby DSLs with cleanroom development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cleanroom
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(cleanroom) = 1.0.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Conflicts:     gem(rspec) >= 4

%description   -n gem-cleanroom-devel
(More) safely evaluate Ruby DSLs with cleanroom development package.

Ruby is an excellent programming language for creating and managing custom DSLs,
but how can you securely evaluate a DSL while explicitly controlling the methods
exposed to the user? Our good friends instance_eval and instance_exec are great,
but they expose all methods - public, protected, and private - to the user. Even
worse, they expose the ability to accidentally or intentionally alter the
behavior of the system! The cleanroom pattern is a safer, more convenient,
Ruby-like approach for limiting the information exposed by a DSL while giving
users the ability to write awesome code!

The cleanroom pattern is a unique way for more safely evaluating Ruby DSLs
without adding additional overhead.

%description   -n gem-cleanroom-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cleanroom.


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

%files         -n gem-cleanroom-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-cleanroom-devel
%doc README.md


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt2
- > Ruby Policy 2.0

* Mon Aug 27 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.1
- Rebuild for new Ruby autorequirements.

* Thu May 21 2015 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build for ALT Linux
