%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname insist

Name:          gem-insist
Version:       1.0.0
Release:       alt1
Summary:       A simple block-driven assertion library for both testing and for production code
License:       Apache 2
Group:         Development/Ruby
Url:           https://github.com/jordansissel/ruby-insist
Vcs:           https://github.com/jordansissel/ruby-insist.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 2.8.0
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Provides:      gem(insist) = 1.0.0


%description
A simple block-driven assertion library for both testing and for production code


%if_enabled    doc
%package       -n gem-insist-doc
Version:       1.0.0
Release:       alt1
Summary:       A simple block-driven assertion library for both testing and for production code documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета insist
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(insist) = 1.0.0

%description   -n gem-insist-doc
A simple block-driven assertion library for both testing and for production code
documentation files.

%description   -n gem-insist-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета insist.
%endif


%if_enabled    devel
%package       -n gem-insist-devel
Version:       1.0.0
Release:       alt1
Summary:       A simple block-driven assertion library for both testing and for production code development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета insist
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(insist) = 1.0.0
Requires:      gem(rspec) >= 2.8.0
Conflicts:     gem(rspec) >= 4

%description   -n gem-insist-devel
A simple block-driven assertion library for both testing and for production code
development package.

%description   -n gem-insist-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета insist.
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
%files         -n gem-insist-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-insist-devel
%doc README.md
%endif


%changelog
* Tue Aug 20 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
