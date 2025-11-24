%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname simplecov-rcov

Name:          gem-simplecov-rcov
Version:       0.3.7
Release:       alt1
Summary:       Rcov style formatter for SimpleCov
License:       Unlicense
Group:         Development/Ruby
Url:           http://github.com/fguillen/simplecov-rcov
Vcs:           https://github.com/fguillen/simplecov-rcov.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.0.0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0.4.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(simplecov) >= 0.4.1
Provides:      gem(simplecov-rcov) = 0.3.7

%description
Rcov style formatter for SimpleCov


%if_enabled    doc
%package       -n gem-simplecov-rcov-doc
Version:       0.3.7
Release:       alt1
Summary:       Rcov style formatter for SimpleCov documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета simplecov-rcov
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(simplecov-rcov) = 0.3.7

%description   -n gem-simplecov-rcov-doc
Rcov style formatter for SimpleCov documentation files.

%description   -n gem-simplecov-rcov-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета simplecov-rcov.
%endif


%if_enabled    devel
%package       -n gem-simplecov-rcov-devel
Version:       0.3.7
Release:       alt1
Summary:       Rcov style formatter for SimpleCov development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета simplecov-rcov
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(simplecov-rcov) = 0.3.7
Requires:      gem(bundler) >= 1.0.0
Requires:      gem(mocha) >= 0
Requires:      gem(rake) >= 0

%description   -n gem-simplecov-rcov-devel
Rcov style formatter for SimpleCov development package.

%description   -n gem-simplecov-rcov-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета simplecov-rcov.
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
%files         -n gem-simplecov-rcov-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-simplecov-rcov-devel
%doc README.md
%endif


%changelog
* Wed Nov 19 2025 Pavel Skrylev <majioa@altlinux.org> 0.3.7-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
