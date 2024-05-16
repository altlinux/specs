%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname beaneater

Name:          gem-beaneater
Version:       1.1.3
Release:       alt1
Summary:       Simple beanstalkd client for ruby
License:       MIT
Group:         Development/Ruby
Url:           http://beanstalkd.github.com/beaneater
Vcs:           https://github.com/beanstalkd/beaneater.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 4.1.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(term-ansicolor) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(redcarpet) >= 1
BuildRequires: gem(github-markup) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(coveralls) >= 0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(redcarpet) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency redcarpet >= 3.5.1.1,redcarpet < 4
Provides:      gem(beaneater) = 1.1.3


%description
Beaneater is the best way to interact with beanstalkd from within Ruby.
Beanstalkd is a simple, fast work queue. Its interface is generic, but was
originally designed for reducing the latency of page views in high-volume web
applications by running time-consuming tasks asynchronously. Read the yardocs
and/or the beanstalk protocol for more details.


%if_enabled    doc
%package       -n gem-beaneater-doc
Version:       1.1.3
Release:       alt1
Summary:       Simple beanstalkd client for ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета beaneater
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(beaneater) = 1.1.3

%description   -n gem-beaneater-doc
Simple beanstalkd client for ruby documentation files.

Beaneater is the best way to interact with beanstalkd from within Ruby.
Beanstalkd is a simple, fast work queue. Its interface is generic, but was
originally designed for reducing the latency of page views in high-volume web
applications by running time-consuming tasks asynchronously. Read the yardocs
and/or the beanstalk protocol for more details.

%description   -n gem-beaneater-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета beaneater.
%endif


%if_enabled    devel
%package       -n gem-beaneater-devel
Version:       1.1.3
Release:       alt1
Summary:       Simple beanstalkd client for ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета beaneater
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(beaneater) = 1.1.3
Requires:      gem(minitest) >= 4.1.0
Requires:      gem(rake) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(term-ansicolor) >= 0
Requires:      gem(json) >= 0
Requires:      gem(redcarpet) >= 1
Requires:      gem(github-markup) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(coveralls) >= 0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(redcarpet) >= 4

%description   -n gem-beaneater-devel
Simple beanstalkd client for ruby development package.

Beaneater is the best way to interact with beanstalkd from within Ruby.
Beanstalkd is a simple, fast work queue. Its interface is generic, but was
originally designed for reducing the latency of page views in high-volume web
applications by running time-consuming tasks asynchronously. Read the yardocs
and/or the beanstalk protocol for more details.

%description   -n gem-beaneater-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета beaneater.
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
%files         -n gem-beaneater-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-beaneater-devel
%doc README.md
%endif


%changelog
* Wed Apr 24 2024 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1
- + packaged gem with Ruby Policy 2.0
