%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname warden

Name:          gem-warden
Version:       1.2.9.8
Release:       alt0.1
Summary:       General Rack Authentication Framework
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/wardencommunity/warden
Vcs:           https://github.com/wardencommunity/warden.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rack) >= 2.2.2
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rack) >= 2.2.2
Obsoletes:     ruby-warden < %EVR
Provides:      ruby-warden = %EVR
Provides:      gem(warden) = 1.2.9.8

%ruby_use_gem_version warden:1.2.9.8

%description
Warden is rack based middleware, designed to provide a mechanism for
authentication in Ruby web applications. It is a common mechanism that fits into
the Rack Machinery to offer powerful options for authentication.


%if_enabled    doc
%package       -n gem-warden-doc
Version:       1.2.9.8
Release:       alt0.1
Summary:       General Rack Authentication Framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета warden
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(warden) = 1.2.9.8

%description   -n gem-warden-doc
General Rack Authentication Framework documentation files.

Warden is rack based middleware, designed to provide a mechanism for
authentication in Ruby web applications. It is a common mechanism that fits into
the Rack Machinery to offer powerful options for authentication.

%description   -n gem-warden-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета warden.
%endif


%if_enabled    devel
%package       -n gem-warden-devel
Version:       1.2.9.8
Release:       alt0.1
Summary:       General Rack Authentication Framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета warden
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(warden) = 1.2.9.8
Requires:      gem(rake) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(rspec) >= 3
Requires:      gem(rack-test) >= 0
Conflicts:     gem(rspec) >= 4

%description   -n gem-warden-devel
General Rack Authentication Framework development package.

Warden is rack based middleware, designed to provide a mechanism for
authentication in Ruby web applications. It is a common mechanism that fits into
the Rack Machinery to offer powerful options for authentication.

%description   -n gem-warden-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета warden.
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
%files         -n gem-warden-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-warden-devel
%doc README.md
%endif


%changelog
* Tue Apr 16 2024 Pavel Skrylev <majioa@altlinux.org> 1.2.9.8-alt0.1
- ^ 1.2.9 -> 1.2.9p8

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.2.9-alt1
- ^ 1.2.8 -> 1.2.9

* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.8-alt1
- Bump to 1.2.8
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.4-alt2.2
- Rebuild with new Ruby autorequirements.

* Tue Dec 04 2012 Led <led@altlinux.ru> 0.9.4-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Tue Mar 02 2010 Timur Batyrshin <erthad@altlinux.org> 0.9.4-alt2
- added README.alt

* Wed Feb 24 2010 Timur Batyrshin <erthad@altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus
