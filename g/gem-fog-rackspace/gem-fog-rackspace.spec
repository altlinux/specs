%define        gemname fog-rackspace

Name:          gem-fog-rackspace
Version:       0.1.6.6
Release:       alt0.1
Summary:       Rackspace provider gem for Fog ecosystem
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fog/fog-rackspace
Vcs:           https://github.com/fog/fog-rackspace.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(shindo) >= 0.3
BuildRequires: gem(rspec) >= 3.4
BuildRequires: gem(rubyzip) >= 1.3.0
BuildRequires: gem(pry) >= 0.10.3
BuildRequires: gem(vcr) >= 3.0.1
BuildRequires: gem(webmock) >= 1.24.2
BuildRequires: gem(mime-types) >= 0
BuildRequires: gem(mime-types-data) >= 0
BuildRequires: gem(fog-core) >= 1.35
BuildRequires: gem(fog-json) >= 1.0
BuildRequires: gem(fog-xml) >= 0.1
BuildRequires: gem(ipaddress) >= 0.8
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(shindo) >= 1
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubyzip) >= 3
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(vcr) >= 7
BuildConflicts: gem(webmock) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency rubyzip >= 2.3.0,rubyzip < 3
%ruby_use_gem_dependency vcr >= 6.0.0,vcr < 7
Requires:      gem(fog-core) >= 1.35
Requires:      gem(fog-json) >= 1.0
Requires:      gem(fog-xml) >= 0.1
Requires:      gem(ipaddress) >= 0.8
Obsoletes:     ruby-fog-rackspace
Provides:      ruby-fog-rackspace
Provides:      gem(fog-rackspace) = 0.1.6.6

%ruby_use_gem_version fog-rackspace:0.1.6.6

%description
Rackspace provider gem for Fog ecosystem.


%package       -n gem-fog-rackspace-doc
Version:       0.1.6.6
Release:       alt0.1
Summary:       Rackspace provider gem for Fog ecosystem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fog-rackspace
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fog-rackspace) = 0.1.6.6

%description   -n gem-fog-rackspace-doc
Rackspace provider gem for Fog ecosystem documentation files.

%description   -n gem-fog-rackspace-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fog-rackspace.


%package       -n gem-fog-rackspace-devel
Version:       0.1.6.6
Release:       alt0.1
Summary:       Rackspace provider gem for Fog ecosystem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fog-rackspace
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fog-rackspace) = 0.1.6.6
Requires:      gem(bundler) >= 2.0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(shindo) >= 0.3
Requires:      gem(rspec) >= 3.4
Requires:      gem(rubyzip) >= 1.3.0
Requires:      gem(pry) >= 0.10.3
Requires:      gem(vcr) >= 3.0.1
Requires:      gem(webmock) >= 1.24.2
Requires:      gem(mime-types) >= 0
Requires:      gem(mime-types-data) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(shindo) >= 1
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubyzip) >= 3
Conflicts:     gem(pry) >= 1
Conflicts:     gem(vcr) >= 7
Conflicts:     gem(webmock) >= 4

%description   -n gem-fog-rackspace-devel
Rackspace provider gem for Fog ecosystem development package.

%description   -n gem-fog-rackspace-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fog-rackspace.


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

%files         -n gem-fog-rackspace-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fog-rackspace-devel
%doc README.md


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 0.1.6.6-alt0.1
- ^ 0.1.6 -> 0.1.6p6

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.1.6-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.6-alt1
- used (>) Ruby Policy 2.0
- updated (^) 0.1.5 -> 0.1.6

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu May 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus
