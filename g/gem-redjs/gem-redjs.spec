%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname redjs

Name:          gem-redjs
Version:       0.6.2
Release:       alt1
Summary:       JavaScript compatibility specs for Ruby
License:       Unlicense
Group:         Development/Ruby
Url:           http://github.com/cowboyd/redjs
Vcs:           https://github.com/cowboyd/redjs.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 2.7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(redjs) = 0.6.2

%description
An interface compatibility suite for Ruby embeddings of Javascript.


%if_enabled    doc
%package       -n gem-redjs-doc
Version:       0.6.2
Release:       alt1
Summary:       JavaScript compatibility specs for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета redjs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(redjs) = 0.6.2

%description   -n gem-redjs-doc
JavaScript compatibility specs for Ruby documentation files.

An interface compatibility suite for Ruby embeddings of Javascript.

%description   -n gem-redjs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета redjs.
%endif


%if_enabled    devel
%package       -n gem-redjs-devel
Version:       0.6.2
Release:       alt1
Summary:       JavaScript compatibility specs for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета redjs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(redjs) = 0.6.2
Requires:      gem(rspec) >= 2.7

%description   -n gem-redjs-devel
JavaScript compatibility specs for Ruby development package.

An interface compatibility suite for Ruby embeddings of Javascript.

%description   -n gem-redjs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета redjs.
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
%files         -n gem-redjs-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-redjs-devel
%doc README.md
%endif


%changelog
* Fri Dec 13 2024 Pavel Skrylev <majioa@altlinux.org> 0.6.2-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
