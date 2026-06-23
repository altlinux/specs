%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname chef-zero

Name:          gem-chef-zero
Version:       15.1.11
Release:       alt1
Summary:       Self-contained, easy-setup, fast-start in-memory Chef server for testing and solo setup purposes
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://www.opscode.com/
Vcs:           https://github.com/chef/chef-zero.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby rake setup-rb
%if_enabled check
BuildRequires: gem(chef) >= 18.7
BuildRequires: gem(ffi) >= 1.15.5
BuildRequires: gem(ffi-yajl) >= 2.2
BuildRequires: gem(hashie) >= 2.0
BuildRequires: gem(mixlib-log) >= 2.0
BuildRequires: gem(ohai) >= 18.1
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(pry-stack_explorer) >= 0
BuildRequires: gem(rack) >= 3.1.7
BuildRequires: gem(rackup) >= 2.3.1
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(uuidtools) >= 2.1
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(chef) >= 20
BuildConflicts: gem(ffi-yajl) >= 4.0
BuildConflicts: gem(hashie) >= 6.0
BuildConflicts: gem(mixlib-log) >= 4.0
BuildConflicts: gem(ohai) >= 20
BuildConflicts: gem(rackup) >= 3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(uuidtools) >= 4.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 3.1.7,rack < 4
%ruby_use_gem_dependency chef >= 19.1.116,chef < 20
%ruby_use_gem_dependency ohai >= 19.1.15,ohai < 20
Requires:      ruby >= 3.0
Requires:      gem(ffi-yajl) >= 2.2
Requires:      gem(hashie) >= 2.0
Requires:      gem(mixlib-log) >= 2.0
Requires:      gem(rack) >= 3.1.7
Requires:      gem(rackup) >= 2.3.1
Requires:      gem(uuidtools) >= 2.1
Requires:      gem(webrick) >= 0
Conflicts:     gem(ffi-yajl) >= 4.0
Conflicts:     gem(hashie) >= 6.0
Conflicts:     gem(mixlib-log) >= 4.0
Conflicts:     gem(rackup) >= 3
Conflicts:     gem(uuidtools) >= 4.0
Provides:      gem(chef-zero) = 15.1.11

%description
Chef Zero is a simple, easy-install, in-memory Chef server that can be useful
for Chef Client testing and chef-solo-like tasks that require a full Chef
Server. It IS intended to be simple, Chef 11+ compliant, easy to run and fast to
start. It is NOT intended to be secure, scalable, performant or persistent. It
does NO input validation, authentication or authorization (it will not throw a
400, 401 or 403). It does not save data, and will start up empty each time you
start it.

Because Chef Zero runs in memory, it's super fast and lightweight. This makes it
perfect for testing against a "real" Chef Server without mocking the entire
Internet.


%package       -n chef-zero
Version:       15.1.11
Release:       alt1
Summary:       Self-contained, easy-setup, fast-start in-memory Chef server for testing and solo setup purposes executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета chef-zero
Group:         Other
BuildArch:     noarch

Requires:      gem(chef-zero) = 15.1.11

%description   -n chef-zero
Self-contained, easy-setup, fast-start in-memory Chef server for testing and
solo setup purposes executable(s).

Chef Zero is a simple, easy-install, in-memory Chef server that can be useful
for Chef Client testing and chef-solo-like tasks that require a full Chef
Server. It IS intended to be simple, Chef 11+ compliant, easy to run and fast to
start. It is NOT intended to be secure, scalable, performant or persistent. It
does NO input validation, authentication or authorization (it will not throw a
400, 401 or 403). It does not save data, and will start up empty each time you
start it.

Because Chef Zero runs in memory, it's super fast and lightweight. This makes it
perfect for testing against a "real" Chef Server without mocking the entire
Internet.

%description   -n chef-zero -l ru_RU.UTF-8
Исполнямка для самоцвета chef-zero.


%if_enabled    doc
%package       -n gem-chef-zero-doc
Version:       15.1.11
Release:       alt1
Summary:       Self-contained, easy-setup, fast-start in-memory Chef server for testing and solo setup purposes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-zero
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-zero) = 15.1.11
Obsoletes:     chef-zero-doc < %EVR
Provides:      chef-zero-doc = %EVR

%description   -n gem-chef-zero-doc
Self-contained, easy-setup, fast-start in-memory Chef server for testing and
solo setup purposes documentation files.

Chef Zero is a simple, easy-install, in-memory Chef server that can be useful
for Chef Client testing and chef-solo-like tasks that require a full Chef
Server. It IS intended to be simple, Chef 11+ compliant, easy to run and fast to
start. It is NOT intended to be secure, scalable, performant or persistent. It
does NO input validation, authentication or authorization (it will not throw a
400, 401 or 403). It does not save data, and will start up empty each time you
start it.

Because Chef Zero runs in memory, it's super fast and lightweight. This makes it
perfect for testing against a "real" Chef Server without mocking the entire
Internet.

%description   -n gem-chef-zero-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-zero.
%endif


%if_enabled    devel
%package       -n gem-chef-zero-devel
Version:       15.1.11
Release:       alt1
Summary:       Self-contained, easy-setup, fast-start in-memory Chef server for testing and solo setup purposes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-zero
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-zero) = 15.1.11
Requires:      gem(chef) >= 18.7
Requires:      gem(ffi) >= 1.15.5
Requires:      gem(ffi-yajl) >= 2.2
Requires:      gem(hashie) >= 2.0
Requires:      gem(mixlib-log) >= 2.0
Requires:      gem(ohai) >= 18.1
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(pry-stack_explorer) >= 0
Requires:      gem(rack) >= 3.1.7
Requires:      gem(rackup) >= 2.3.1
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(uuidtools) >= 2.1
Requires:      gem(webrick) >= 0
Requires:      gem(yard) >= 0
Conflicts:     gem(chef) >= 20
Conflicts:     gem(ffi-yajl) >= 4.0
Conflicts:     gem(hashie) >= 6.0
Conflicts:     gem(mixlib-log) >= 4.0
Conflicts:     gem(ohai) >= 20
Conflicts:     gem(rackup) >= 3
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(uuidtools) >= 3

%description   -n gem-chef-zero-devel
Self-contained, easy-setup, fast-start in-memory Chef server for testing and
solo setup purposes development package.

Chef Zero is a simple, easy-install, in-memory Chef server that can be useful
for Chef Client testing and chef-solo-like tasks that require a full Chef
Server. It IS intended to be simple, Chef 11+ compliant, easy to run and fast to
start. It is NOT intended to be secure, scalable, performant or persistent. It
does NO input validation, authentication or authorization (it will not throw a
400, 401 or 403). It does not save data, and will start up empty each time you
start it.

Because Chef Zero runs in memory, it's super fast and lightweight. This makes it
perfect for testing against a "real" Chef Server without mocking the entire
Internet.

%description   -n gem-chef-zero-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-zero.
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
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n chef-zero
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%_bindir/chef-zero

%if_enabled    doc
%files         -n gem-chef-zero-doc
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-chef-zero-devel
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%endif


%changelog
* Sat May 30 2026 Pavel Skrylev <majioa@altlinux.org> 15.1.11-alt1
- ^ 15.1.6 -> 15.1.11

* Mon Mar 30 2026 Pavel Skrylev <majioa@altlinux.org> 15.1.6-alt1
- ^ 15.0.28 -> 15.1.6

* Thu Nov 20 2025 Pavel Skrylev <majioa@altlinux.org> 15.0.28-alt1
- ^ 15.0.16 -> 15.0.28

* Thu Feb 06 2025 Pavel Skrylev <majioa@altlinux.org> 15.0.16-alt1
- ^ 15.0.12p3 -> 15.0.16

* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 15.0.12.3-alt0.1
- ^ 15.0.0 -> 15.0.12p3

* Sat Mar 19 2022 Andrey Cherepanov <cas@altlinux.org> 15.0.12-alt1
- New version.

* Mon Oct 18 2021 Andrey Cherepanov <cas@altlinux.org> 15.0.11-alt1
- New version.

* Thu Oct 07 2021 Andrey Cherepanov <cas@altlinux.org> 15.0.10-alt1
- New version.

* Thu Sep 09 2021 Andrey Cherepanov <cas@altlinux.org> 15.0.9-alt1
- New version.

* Wed Jun 23 2021 Andrey Cherepanov <cas@altlinux.org> 15.0.8-alt1
- New version.

* Fri May 28 2021 Andrey Cherepanov <cas@altlinux.org> 15.0.6-alt1
- New version.

* Fri Feb 26 2021 Andrey Cherepanov <cas@altlinux.org> 15.0.5-alt1
- New version.

* Thu Jan 07 2021 Andrey Cherepanov <cas@altlinux.org> 15.0.4-alt1
- New version.

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 15.0.3-alt1
- New version.

* Mon Jul 13 2020 Pavel Skrylev <majioa@altlinux.org> 15.0.0-alt1
- ^ 14.0.12 -> 15.0.0
- ! spec tags and license

* Mon Apr 08 2019 Pavel Skrylev <majioa@altlinux.org> 14.0.12-alt1
- ^ 14.0.11 -> 14.0.12
- ! spec

* Thu Mar 07 2019 Pavel Skrylev <majioa@altlinux.org> 14.0.11-alt2
- > Ruby Policy 2.0.

* Tue Nov 20 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.11-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.8-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.6-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Apr 25 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.6-alt1
- New version.

* Sun Apr 22 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.5-alt1
- New version.

* Fri Mar 16 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.2-alt1
- New version.

* Mon Feb 19 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.1-alt1
- New version.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 13.1.0-alt1.1
- Rebuild with Ruby 2.4.1

* Tue Jul 18 2017 Andrey Cherepanov <cas@altlinux.org> 13.1.0-alt1
- New version

* Tue Apr 04 2017 Andrey Cherepanov <cas@altlinux.org> 13.0.0-alt1
- New version

* Wed Mar 29 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.2-alt1
- New version

* Tue Mar 21 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.1-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- new version 5.2.0

* Wed Oct 05 2016 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- new version 5.1.0

* Fri Aug 21 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.3-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- New version

* Tue Feb 17 2015 Andrey Cherepanov <cas@altlinux.org> 4.0-alt1
- Initial build for ALT Linux
