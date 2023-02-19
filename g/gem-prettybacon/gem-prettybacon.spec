%define        gemname prettybacon

Name:          gem-prettybacon
Version:       0.0.2
Release:       alt1
Summary:       Prettifies Bacon output
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/irrationalfab/PrettyBacon
Vcs:           https://github.com/irrationalfab/prettybacon.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(bacon) >= 1.2
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(bacon) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Requires:      gem(bacon) >= 1.2
Conflicts:     gem(bacon) >= 2
Provides:      gem(prettybacon) = 0.0.2


%description
Prettifies Bacon output.


%package       -n gem-prettybacon-doc
Version:       0.0.2
Release:       alt1
Summary:       Prettifies Bacon output documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета prettybacon
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(prettybacon) = 0.0.2

%description   -n gem-prettybacon-doc
Prettifies Bacon output documentation files.

%description   -n gem-prettybacon-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета prettybacon.


%package       -n gem-prettybacon-devel
Version:       0.0.2
Release:       alt1
Summary:       Prettifies Bacon output development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета prettybacon
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(prettybacon) = 0.0.2
Requires:      gem(bundler) >= 1.3
Requires:      gem(rake) >= 0
Conflicts:     gem(bundler) >= 3

%description   -n gem-prettybacon-devel
Prettifies Bacon output development package.

%description   -n gem-prettybacon-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета prettybacon.


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

%files         -n gem-prettybacon-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-prettybacon-devel
%doc README.md


%changelog
* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 0.0.2-alt1
- + packaged gem with Ruby Policy 2.0
