%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fixme

Name:          gem-fixme
Version:       6.1.1
Release:       alt1
Summary:       Comments that raise after a certain point in time
License:       MIT
Group:         Development/Ruby
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(timecop) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(fixme) = 6.1.1

%description
Comments that raise after a certain point in time.


%if_enabled    doc
%package       -n gem-fixme-doc
Version:       6.1.1
Release:       alt1
Summary:       Comments that raise after a certain point in time documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fixme
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(fixme) = 6.1.1

%description   -n gem-fixme-doc
Comments that raise after a certain point in time documentation files.

%description   -n gem-fixme-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fixme.
%endif


%if_enabled    devel
%package       -n gem-fixme-devel
Version:       6.1.1
Release:       alt1
Summary:       Comments that raise after a certain point in time development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fixme
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(fixme) = 6.1.1
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(timecop) >= 0

%description   -n gem-fixme-devel
Comments that raise after a certain point in time development package.

%description   -n gem-fixme-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fixme.
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
%doc CHANGELOG.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-fixme-doc
%doc CHANGELOG.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fixme-devel
%doc CHANGELOG.md README.md
%endif


%changelog
* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 6.1.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
