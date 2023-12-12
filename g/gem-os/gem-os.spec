%define        _unpackaged_files_terminate_build 1
%define        gemname os

Name:          gem-os
Version:       1.1.4
Release:       alt1
Summary:       The OS gem allows for some easy telling if you're on windows or not
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rdp/os
Vcs:           https://github.com/rdp/os.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0.8
BuildRequires: gem(test-unit) >= 3
BuildRequires: gem(rspec) >= 2.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(test-unit) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(os) = 1.1.4
Obsoletes:     ruby-os < %EVR
Provides:      ruby-os = %EVR
Provides:      gem(os) = 1.1.4


%description
The OS gem allows for some easy telling if youre on windows or not. OS.windows?
As well as some other helper utilities.


%package       -n gem-os-doc
Version:       1.1.4
Release:       alt1
Summary:       The OS gem allows for some easy telling if you're on windows or not documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета os
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(os) = 1.1.4

%description   -n gem-os-doc
The OS gem allows for some easy telling if you're on windows or not
documentation files.

The OS gem allows for some easy telling if youre on windows or not. OS.windows?
As well as some other helper utilities.

%description   -n gem-os-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета os.


%package       -n gem-os-devel
Version:       1.1.4
Release:       alt1
Summary:       The OS gem allows for some easy telling if you're on windows or not development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета os
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(os) = 1.1.4
Requires:      gem(rake) >= 0.8
Requires:      gem(test-unit) >= 3
Requires:      gem(rspec) >= 2.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(test-unit) >= 4

%description   -n gem-os-devel
The OS gem allows for some easy telling if you're on windows or not development
package.

The OS gem allows for some easy telling if youre on windows or not. OS.windows?
As well as some other helper utilities.

%description   -n gem-os-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета os.


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

%files         -n gem-os-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-os-devel
%doc README.md


%changelog
* Wed Nov 29 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.4-alt1
- ^ 1.0.1 -> 1.1.4

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- updated (^) 1.0.0 -> 1.0.1
- used (>) Ruby Policy 2.0

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
