%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname recursive-open-struct

Name:          gem-recursive-open-struct
Version:       1.1.3
Release:       alt1
Summary:       OpenStruct subclass that returns nested hash attributes as RecursiveOpenStructs
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/aetherknight/recursive-open-struct
Vcs:           https://github.com/aetherknight/recursive-open-struct.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rspec) >= 3.2
BuildRequires: gem(simplecov) >= 0
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(recursive-open-struct) = 1.1.3


%description
RecursiveOpenStruct is a subclass of OpenStruct. It differs from OpenStruct in
that it allows nested hashes to be treated in a recursive fashion. For
example:

ros = RecursiveOpenStruct.new({ :a => { :b => 'c' } }) ros.a.b # 'c'

Also, nested hashes can still be accessed as hashes:

ros.a_as_a_hash # { :b => 'c' }


%if_enabled    doc
%package       -n gem-recursive-open-struct-doc
Version:       1.1.3
Release:       alt1
Summary:       OpenStruct subclass that returns nested hash attributes as RecursiveOpenStructs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета recursive-open-struct
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(recursive-open-struct) = 1.1.3

%description   -n gem-recursive-open-struct-doc
OpenStruct subclass that returns nested hash attributes as RecursiveOpenStructs
documentation files.

RecursiveOpenStruct is a subclass of OpenStruct. It differs from OpenStruct in
that it allows nested hashes to be treated in a recursive fashion. For
example:

ros = RecursiveOpenStruct.new({ :a => { :b => 'c' } }) ros.a.b # 'c'

Also, nested hashes can still be accessed as hashes:

ros.a_as_a_hash # { :b => 'c' }

%description   -n gem-recursive-open-struct-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета recursive-open-struct.
%endif


%if_enabled    devel
%package       -n gem-recursive-open-struct-devel
Version:       1.1.3
Release:       alt1
Summary:       OpenStruct subclass that returns nested hash attributes as RecursiveOpenStructs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета recursive-open-struct
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(recursive-open-struct) = 1.1.3
Requires:      gem(bundler) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(rspec) >= 3.2
Requires:      gem(simplecov) >= 0
Conflicts:     gem(rspec) >= 4

%description   -n gem-recursive-open-struct-devel
OpenStruct subclass that returns nested hash attributes as RecursiveOpenStructs
development package.

RecursiveOpenStruct is a subclass of OpenStruct. It differs from OpenStruct in
that it allows nested hashes to be treated in a recursive fashion. For
example:

ros = RecursiveOpenStruct.new({ :a => { :b => 'c' } }) ros.a.b # 'c'

Also, nested hashes can still be accessed as hashes:

ros.a_as_a_hash # { :b => 'c' }

%description   -n gem-recursive-open-struct-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета recursive-open-struct.
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
%files         -n gem-recursive-open-struct-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-recursive-open-struct-devel
%doc README.md
%endif


%changelog
* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1
- + packaged gem with Ruby Policy 2.0
