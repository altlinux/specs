%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname warnings_logger

Name:          gem-warnings-logger
Version:       0.1.1
Release:       alt1
Summary:       Easily log warnings in your gems
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/mcmire/warnings_logger
Vcs:           https://github.com/mcmire/warnings_logger.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(snowglobe) >= 0
BuildRequires: gem(super_diff) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names warnings_logger,warnings-logger
Provides:      gem(warnings_logger) = 0.1.1

%description
Easily log warnings in your gems


%if_enabled    doc
%package       -n gem-warnings-logger-doc
Version:       0.1.1
Release:       alt1
Summary:       Easily log warnings in your gems documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета warnings_logger
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(warnings_logger) = 0.1.1

%description   -n gem-warnings-logger-doc
Easily log warnings in your gems documentation files.

%description   -n gem-warnings-logger-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета warnings_logger.
%endif


%if_enabled    devel
%package       -n gem-warnings-logger-devel
Version:       0.1.1
Release:       alt1
Summary:       Easily log warnings in your gems development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета warnings_logger
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(warnings_logger) = 0.1.1
Requires:      gem(bundler) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(snowglobe) >= 0
Requires:      gem(super_diff) >= 0

%description   -n gem-warnings-logger-devel
Easily log warnings in your gems development package.

%description   -n gem-warnings-logger-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета warnings_logger.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-warnings-logger-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-warnings-logger-devel
%doc LICENSE README.md
%endif


%changelog
* Mon Jan 13 2025 Pavel Skrylev <majioa@altlinux.org> 0.1.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
