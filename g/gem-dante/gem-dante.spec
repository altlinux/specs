%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname dante

Name:          gem-dante
Version:       0.2.0
Release:       alt1
Summary:       Turn any process into a demon
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/bazaarlabs/dante
Vcs:           https://github.com/bazaarlabs/dante.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(mocha) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(dante) = 0.2.0


%description
Dante is the simplest possible thing that will work to turn arbitrary ruby code
into an executable that can be started via command line or start/stop a daemon,
and will store a pid file for you.

If you need to create a ruby executable and you want standard daemon start/stop
with pid files and no hassle, this gem will be a great way to get started.


%if_enabled    doc
%package       -n gem-dante-doc
Version:       0.2.0
Release:       alt1
Summary:       Turn any process into a demon documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dante
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dante) = 0.2.0

%description   -n gem-dante-doc
Turn any process into a demon documentation files.

Dante is the simplest possible thing that will work to turn arbitrary ruby code
into an executable that can be started via command line or start/stop a daemon,
and will store a pid file for you.

If you need to create a ruby executable and you want standard daemon start/stop
with pid files and no hassle, this gem will be a great way to get started.

%description   -n gem-dante-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dante.
%endif


%if_enabled    devel
%package       -n gem-dante-devel
Version:       0.2.0
Release:       alt1
Summary:       Turn any process into a demon development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dante
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dante) = 0.2.0
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(mocha) >= 0

%description   -n gem-dante-devel
Turn any process into a demon development package.

Dante is the simplest possible thing that will work to turn arbitrary ruby code
into an executable that can be started via command line or start/stop a daemon,
and will store a pid file for you.

If you need to create a ruby executable and you want standard daemon start/stop
with pid files and no hassle, this gem will be a great way to get started.

%description   -n gem-dante-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dante.
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
%files         -n gem-dante-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-dante-devel
%doc README.md
%endif


%changelog
* Wed Apr 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with Ruby Policy 2.0
