%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hoe

Name:          gem-hoe
Version:       4.2.2
Release:       alt1
Summary:       Hoe is a rake/rubygems helper for project Rakefiles
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/hoe
Vcs:           https://github.com/seattlerb/hoe.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0.8
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(simplecov) >= 0.17
BuildConflicts: gem(rake) >= 15.0
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(rake) >= 0.8
Conflicts:     gem(rake) >= 15.0
Obsoletes:     ruby-hoe < %EVR
Provides:      ruby-hoe = %EVR
Provides:      gem(hoe) = 4.2.2


%description
Hoe is a rake/rubygems helper for project Rakefiles. It helps you manage,
maintain, and release your project and includes a dynamic plug-in system
allowing for easy extensibility. Hoe ships with plug-ins for all your usual
project tasks including rdoc generation, testing, packaging, deployment, and
announcement.


%package       -n sow
Version:       4.2.2
Release:       alt1
Summary:       Hoe is a rake/rubygems helper for project Rakefiles executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета hoe
Group:         Other
BuildArch:     noarch

Requires:      gem(hoe) = 4.2.2

%description   -n sow
Hoe is a rake/rubygems helper for project Rakefiles executable(s).

Hoe is a rake/rubygems helper for project Rakefiles. It helps you manage,
maintain, and release your project and includes a dynamic plug-in system
allowing for easy extensibility. Hoe ships with plug-ins for all your usual
project tasks including rdoc generation, testing, packaging, deployment, and
announcement.

%description   -n sow -l ru_RU.UTF-8
Исполнямка для самоцвета hoe.


%if_enabled    doc
%package       -n gem-hoe-doc
Version:       4.2.2
Release:       alt1
Summary:       Hoe is a rake/rubygems helper for project Rakefiles documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe) = 4.2.2

%description   -n gem-hoe-doc
Hoe is a rake/rubygems helper for project Rakefiles documentation files.

Hoe is a rake/rubygems helper for project Rakefiles. It helps you manage,
maintain, and release your project and includes a dynamic plug-in system
allowing for easy extensibility. Hoe ships with plug-ins for all your usual
project tasks including rdoc generation, testing, packaging, deployment, and
announcement.

%description   -n gem-hoe-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe.
%endif


%if_enabled    devel
%package       -n gem-hoe-devel
Version:       4.2.2
Release:       alt1
Summary:       Hoe is a rake/rubygems helper for project Rakefiles development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe) = 4.2.2
Requires:      gem(rdoc) >= 4.0
Requires:      gem(simplecov) >= 0.17
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(simplecov) >= 1

%description   -n gem-hoe-devel
Hoe is a rake/rubygems helper for project Rakefiles development package.

Hoe is a rake/rubygems helper for project Rakefiles. It helps you manage,
maintain, and release your project and includes a dynamic plug-in system
allowing for easy extensibility. Hoe ships with plug-ins for all your usual
project tasks including rdoc generation, testing, packaging, deployment, and
announcement.

%description   -n gem-hoe-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe.
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
%doc README.rdoc template/README.txt.erb
%ruby_gemspec
%ruby_gemlibdir

%files         -n sow
%doc README.rdoc template/README.txt.erb
%_bindir/sow

%if_enabled    doc
%files         -n gem-hoe-doc
%doc README.rdoc template/README.txt.erb
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hoe-devel
%doc README.rdoc template/README.txt.erb
%endif


%changelog
* Sat Aug 24 2024 Pavel Skrylev <majioa@altlinux.org> 4.2.2-alt1
- ^ 4.1.0 -> 4.2.2

* Sat Dec 02 2023 Pavel Skrylev <majioa@altlinux.org> 4.1.0-alt1
- ^ 3.23.1 -> 4.1.0

* Fri Mar 18 2022 Pavel Skrylev <majioa@altlinux.org> 3.23.1-alt1
- ^ 3.22.1 -> 3.23.1

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 3.22.1-alt1
- updated (^) 3.18.0 -> 3.22.1
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.18.0-alt1.1
- fixed (!) spec according to changelog rules

* Mon Jul 29 2019 Pavel Skrylev <majioa@altlinux.org> 3.18.0-alt1
- updated (^) 3.17.2 -> 3.18.0
- fixed (!) spec

* Thu Apr 25 2019 Pavel Skrylev <majioa@altlinux.org> 3.17.2-alt1
- Bump to 3.17.2
- Use Ruby Policy 2.0

* Mon Oct 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.17.1-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.17.0-alt2.1
- Rebuild with new Ruby autorequirements.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 3.17.0-alt2
- Clarify ignored modules.
- Package as gem.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.17.0-alt1
- Initial build for Sisyphus
