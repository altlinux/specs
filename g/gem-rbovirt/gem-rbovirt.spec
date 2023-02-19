%define        gemname rbovirt

Name:          gem-rbovirt
Version:       0.1.7
Release:       alt1.2
Summary:       a ruby client for ovirt
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/abenari/rbovirt
Vcs:           https://github.com/abenari/rbovirt.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rack) >= 1.6
BuildRequires: gem(shoulda) >= 0
BuildRequires: gem(rspec-rails) >= 2.6
BuildRequires: gem(rake) >= 0
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(rest-client) > 1.7.0
BuildConflicts: gem(rack) >= 3
BuildConflicts: gem(rspec-rails) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 2.2.2,rack < 3
%ruby_use_gem_dependency rspec-rails >= 5.0.1,rspec-rails < 6
Requires:      gem(nokogiri) >= 0
Requires:      gem(rest-client) > 1.7.0
Obsoletes:     ruby-rbovirt < %EVR
Provides:      ruby-rbovirt = %EVR
Provides:      gem(rbovirt) = 0.1.7


%description
A Ruby client for oVirt REST API.


%package       -n gem-rbovirt-doc
Version:       0.1.7
Release:       alt1.2
Summary:       a ruby client for ovirt documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rbovirt
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rbovirt) = 0.1.7

%description   -n gem-rbovirt-doc
a ruby client for ovirt documentation files.

A Ruby client for oVirt REST API.

%description   -n gem-rbovirt-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rbovirt.


%package       -n gem-rbovirt-devel
Version:       0.1.7
Release:       alt1.2
Summary:       a ruby client for ovirt development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rbovirt
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rbovirt) = 0.1.7
Requires:      gem(rack) >= 1.6
Requires:      gem(shoulda) >= 0
Requires:      gem(rspec-rails) >= 2.6
Requires:      gem(rake) >= 0
Conflicts:     gem(rack) >= 3
Conflicts:     gem(rspec-rails) >= 6

%description   -n gem-rbovirt-devel
a ruby client for ovirt development package.

A Ruby client for oVirt REST API.

%description   -n gem-rbovirt-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rbovirt.


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

%files         -n gem-rbovirt-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-rbovirt-devel
%doc README.rdoc


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 0.1.7-alt1.2
- ! closes build deps under check condition

* Wed Jun 30 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.7-alt1.1
- ! spec

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.7-alt1
- New version.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.6-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Jun 19 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.6-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus
