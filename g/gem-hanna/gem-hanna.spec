%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hanna

Name:          gem-hanna
Version:       1.5.0
Release:       alt1
Summary:       RDoc generator designed with simplicity, beauty and ease of browsing in mind
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jeremyevans/hanna
Vcs:           https://github.com/jeremyevans/hanna.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rdoc) >= 4
BuildRequires: gem(minitest-hooks) >= 0
BuildRequires: gem(minitest-global_expectations) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rdoc) >= 4
Provides:      gem(hanna) = 1.5.0


%description
RDoc generator designed with simplicity, beauty and ease of browsing in mind


%if_enabled    doc
%package       -n gem-hanna-doc
Version:       1.5.0
Release:       alt1
Summary:       RDoc generator designed with simplicity, beauty and ease of browsing in mind documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hanna
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hanna) = 1.5.0

%description   -n gem-hanna-doc
RDoc generator designed with simplicity, beauty and ease of browsing in mind
documentation files.

%description   -n gem-hanna-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hanna.
%endif


%if_enabled    devel
%package       -n gem-hanna-devel
Version:       1.5.0
Release:       alt1
Summary:       RDoc generator designed with simplicity, beauty and ease of browsing in mind development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hanna
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hanna) = 1.5.0
Requires:      gem(minitest-hooks) >= 0
Requires:      gem(minitest-global_expectations) >= 0

%description   -n gem-hanna-devel
RDoc generator designed with simplicity, beauty and ease of browsing in mind
development package.

%description   -n gem-hanna-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hanna.
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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-hanna-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hanna-devel
%doc README.rdoc
%endif


%changelog
* Tue May 14 2024 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- + packaged gem with Ruby Policy 2.0
