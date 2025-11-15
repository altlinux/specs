%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname jazz_fingers

Name:          gem-jazz-fingers
Version:       6.3.0
Release:       alt1
Summary:       Exercise those fingers. Pry-based enhancements for the default Ruby console
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/plribeiro3000/jazz_fingers
Vcs:           https://github.com/plribeiro3000/jazz_fingers.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(amazing_print) >= 1.8
BuildRequires: gem(pry) >= 0.13.1
BuildRequires: gem(pry-byebug) >= 3.11
BuildRequires: gem(pry-coolline) >= 0.2
BuildRequires: gem(rubocop) >= 0
BuildConflicts: gem(amazing_print) >= 3
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(pry-byebug) >= 4
BuildConflicts: gem(pry-coolline) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency amazing_print >= 2.0.0,amazing_print < 3
%ruby_alias_names jazz_fingers,jazz-fingers
Requires:      ruby >= 2.0
Provides:      gem(jazz_fingers) = 6.3.0

%description
Spending hours in the ruby console? Spruce it up and show off those hard-working
hands! jazz_fingersreplaces IRB with Pry, improves output through amazing_print,
and has some other goodies up its sleeves.


%if_enabled    doc
%package       -n gem-jazz-fingers-doc
Version:       6.3.0
Release:       alt1
Summary:       Exercise those fingers. Pry-based enhancements for the default Ruby console documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jazz_fingers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jazz_fingers) = 6.3.0

%description   -n gem-jazz-fingers-doc
Exercise those fingers. Pry-based enhancements for the default Ruby console
documentation files.

Spending hours in the ruby console? Spruce it up and show off those hard-working
hands! jazz_fingersreplaces IRB with Pry, improves output through amazing_print,
and has some other goodies up its sleeves.

%description   -n gem-jazz-fingers-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jazz_fingers.
%endif


%if_enabled    devel
%package       -n gem-jazz-fingers-devel
Version:       6.3.0
Release:       alt1
Summary:       Exercise those fingers. Pry-based enhancements for the default Ruby console development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета jazz_fingers
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jazz_fingers) = 6.3.0
Requires:      gem(amazing_print) >= 1.8
Requires:      gem(pry) >= 0.13.1
Requires:      gem(pry-byebug) >= 3.11
Requires:      gem(pry-coolline) >= 0.2
Requires:      gem(rubocop) >= 0
Conflicts:     gem(amazing_print) >= 3
Conflicts:     gem(pry) >= 1
Conflicts:     gem(pry-byebug) >= 4
Conflicts:     gem(pry-coolline) >= 1

%description   -n gem-jazz-fingers-devel
Exercise those fingers. Pry-based enhancements for the default Ruby console
development package.

Spending hours in the ruby console? Spruce it up and show off those hard-working
hands! jazz_fingersreplaces IRB with Pry, improves output through amazing_print,
and has some other goodies up its sleeves.

%description   -n gem-jazz-fingers-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета jazz_fingers.
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
%doc CHANGELOG.md CONTRIBUTING.md CONTRIBUTORS.md LICENSE.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-jazz-fingers-doc
%doc CHANGELOG.md CONTRIBUTING.md CONTRIBUTORS.md LICENSE.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-jazz-fingers-devel
%doc CHANGELOG.md CONTRIBUTING.md CONTRIBUTORS.md LICENSE.md README.md
%endif


%changelog
* Wed Oct 22 2025 Pavel Skrylev <majioa@altlinux.org> 6.3.0-alt1
- ^ 6.2.0 -> 6.3.0

* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 6.2.0-alt1
- + packaged gem with Ruby Policy 2.0
