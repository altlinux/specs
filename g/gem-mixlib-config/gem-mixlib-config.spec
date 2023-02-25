%define        gemname mixlib-config

Name:          gem-mixlib-config
Version:       3.0.29
Release:       alt1
Summary:       A simple class based Config mechanism, similar to the one found in Chef
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/mixlib-config
Vcs:           https://github.com/chef/mixlib-config.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(github-markup) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(chefstyle) >= 2.2.2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rb-readline) >= 0
BuildRequires: gem(tomlrb) >= 0
BuildConflicts: gem(chefstyle) >= 3
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency chefstyle >= 2.2.2,chefstyle < 3
Requires:      gem(tomlrb) >= 0
Obsoletes:     ruby-mixlib-config < %EVR
Provides:      ruby-mixlib-config = %EVR
Provides:      gem(mixlib-config) = 3.0.29


%description
Mixlib::Config provides a class-based configuration object, as used in Chef.


%package       -n gem-mixlib-config-doc
Version:       3.0.29
Release:       alt1
Summary:       A simple class based Config mechanism, similar to the one found in Chef documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mixlib-config
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mixlib-config) = 3.0.29

%description   -n gem-mixlib-config-doc
A simple class based Config mechanism, similar to the one found in Chef
documentation files.

Mixlib::Config provides a class-based configuration object, as used in Chef.

%description   -n gem-mixlib-config-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mixlib-config.


%package       -n gem-mixlib-config-devel
Version:       3.0.29
Release:       alt1
Summary:       A simple class based Config mechanism, similar to the one found in Chef development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mixlib-config
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mixlib-config) = 3.0.29
Requires:      gem(github-markup) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(chefstyle) >= 2.2.2
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rb-readline) >= 0
Conflicts:     gem(chefstyle) >= 3
Conflicts:     gem(rspec) >= 4

%description   -n gem-mixlib-config-devel
A simple class based Config mechanism, similar to the one found in Chef
development package.

Mixlib::Config provides a class-based configuration object, as used in Chef.

%description   -n gem-mixlib-config-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mixlib-config.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-mixlib-config-doc
%ruby_gemdocdir

%files         -n gem-mixlib-config-devel


%changelog
* Mon Feb 06 2023 Pavel Skrylev <majioa@altlinux.org> 3.0.29-alt1
- ^ 3.0.6 -> 3.0.29

* Fri Jul 10 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.6-alt1
- > Ruby Policy 2.0
- ^ 2.2.14 -> 3.0.6
- ! spec tags

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.2.14-alt1
- New version.

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.2
- Rebuild for new Ruby autorequirements.

* Mon Aug 27 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.1
- Rebuild for new Ruby autorequirements.

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build for ALT Linux
