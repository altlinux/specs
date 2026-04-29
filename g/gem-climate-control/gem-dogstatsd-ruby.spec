%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname climate_control

Name:          gem-climate-control
Version:       1.2.0
Release:       alt1
Summary:       Modify your ENV easily with ClimateControl
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/thoughtbot/climate_control
Vcs:           https://github.com/thoughtbot/climate_control.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby
BuildRequires(pre): setup-rb
BuildRequires(pre): rake
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(standard) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names climate_control,climate-control
Requires:      ruby >= 2.7.0
Provides:      gem(climate_control) = 1.2.0

%description
Modify your ENV


%if_enabled    doc
%package       -n gem-climate-control-doc
Version:       1.2.0
Release:       alt1
Summary:       Modify your ENV easily with ClimateControl documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета climate_control
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(climate_control) = 1.2.0

%description   -n gem-climate-control-doc
Modify your ENV easily with ClimateControl documentation files.

%description   -n gem-climate-control-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета climate_control.
%endif


%if_enabled    devel
%package       -n gem-climate-control-devel
Version:       1.2.0
Release:       alt1
Summary:       Modify your ENV easily with ClimateControl development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета climate_control
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(climate_control) = 1.2.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(standard) >= 0

%description   -n gem-climate-control-devel
Modify your ENV easily with ClimateControl development package.

%description   -n gem-climate-control-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета climate_control.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-climate-control-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-climate-control-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%endif


%changelog
* Wed Apr 29 2026 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
