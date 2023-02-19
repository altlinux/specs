%define        gemname ohai

Name:          gem-ohai
Version:       18.0.26
Release:       alt1
Summary:       Ohai profiles your system and emits JSON
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/ohai
Vcs:           https://github.com/chef/ohai.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(chefstyle) = 2.2.2
BuildRequires: gem(ipaddr_extensions) >= 0
BuildRequires: gem(rake) >= 10.1.0
BuildRequires: gem(rspec-collection_matchers) >= 1.0
BuildRequires: gem(rspec-core) >= 3.0
BuildRequires: gem(rspec-expectations) >= 3.0
BuildRequires: gem(rspec-mocks) >= 3.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(pry-stack_explorer) >= 0
BuildRequires: gem(rb-readline) >= 0
BuildRequires: gem(chef-config) >= 14.12
BuildRequires: gem(chef-utils) >= 16.0
BuildRequires: gem(ffi) >= 1.9
BuildRequires: gem(ffi-yajl) >= 2.2
BuildRequires: gem(ipaddress) >= 0
BuildRequires: gem(mixlib-cli) >= 1.7.0
BuildRequires: gem(mixlib-config) >= 2.0
BuildRequires: gem(mixlib-log) >= 2.0.1
BuildRequires: gem(mixlib-shellout) >= 3.2.5
BuildRequires: gem(plist) >= 3.1
BuildRequires: gem(train-core) >= 0
BuildRequires: gem(wmi-lite) >= 1.0
BuildConflicts: gem(rspec-collection_matchers) >= 2
BuildConflicts: gem(rspec-core) >= 4
BuildConflicts: gem(rspec-expectations) >= 4
BuildConflicts: gem(rspec-mocks) >= 4
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(chef-config) >= 19
BuildConflicts: gem(chef-utils) >= 19
BuildConflicts: gem(ffi) >= 2
BuildConflicts: gem(ffi-yajl) >= 3
BuildConflicts: gem(mixlib-config) >= 4.0
BuildConflicts: gem(mixlib-log) >= 4.0
BuildConflicts: gem(mixlib-shellout) >= 4
BuildConflicts: gem(plist) >= 4
BuildConflicts: gem(wmi-lite) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_ignore_names rails
Requires:      gem(chef-config) >= 14.12
Requires:      gem(chef-utils) >= 16.0
Requires:      gem(ffi) >= 1.9
Requires:      gem(ffi-yajl) >= 2.2
Requires:      gem(ipaddress) >= 0
Requires:      gem(mixlib-cli) >= 1.7.0
Requires:      gem(mixlib-config) >= 2.0
Requires:      gem(mixlib-log) >= 2.0.1
Requires:      gem(mixlib-shellout) >= 3.2.5
Requires:      gem(plist) >= 3.1
Requires:      gem(train-core) >= 0
Requires:      gem(wmi-lite) >= 1.0
Conflicts:     gem(chef-config) >= 19
Conflicts:     gem(chef-utils) >= 19
Conflicts:     gem(ffi) >= 2
Conflicts:     gem(ffi-yajl) >= 3
Conflicts:     gem(mixlib-config) >= 4.0
Conflicts:     gem(mixlib-log) >= 4.0
Conflicts:     gem(mixlib-shellout) >= 4
Conflicts:     gem(plist) >= 4
Conflicts:     gem(wmi-lite) >= 2
Obsoletes:     ohai < %EVR
Provides:      ohai = %EVR
Provides:      gem(ohai) = 18.0.26


%description
Ohai is a tool that is used to detect attributes on a node, and then provide
these attributes to the chef-client at the start of every chef-client run. Ohai
is required by the chef-client and must be present on a node.


%package       -n ohai
Version:       18.0.26
Release:       alt1
Summary:       Ohai profiles your system and emits JSON executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ohai
Group:         Development/Other
BuildArch:     noarch

Requires:      gem(ohai) = 18.0.26

%description   -n ohai
Ohai profiles your system and emits JSON executable(s).

Ohai is a tool that is used to detect attributes on a node, and then provide
these attributes to the chef-client at the start of every chef-client run. Ohai
is required by the chef-client and must be present on a node.

%description   -n ohai -l ru_RU.UTF-8
Исполнямка для самоцвета ohai.


%package       -n gem-ohai-doc
Version:       18.0.26
Release:       alt1
Summary:       Ohai profiles your system and emits JSON documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ohai
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ohai) = 18.0.26

%description   -n gem-ohai-doc
Ohai profiles your system and emits JSON documentation files.

Ohai is a tool that is used to detect attributes on a node, and then provide
these attributes to the chef-client at the start of every chef-client run. Ohai
is required by the chef-client and must be present on a node.

%description   -n gem-ohai-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ohai.


%package       -n gem-ohai-devel
Version:       18.0.26
Release:       alt1
Summary:       Ohai profiles your system and emits JSON development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ohai
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ohai) = 18.0.26
Requires:      gem(chefstyle) = 2.2.2
Requires:      gem(ipaddr_extensions) >= 0
Requires:      gem(rake) >= 10.1.0
Requires:      gem(rspec-collection_matchers) >= 1.0
Requires:      gem(rspec-core) >= 3.0
Requires:      gem(rspec-expectations) >= 3.0
Requires:      gem(rspec-mocks) >= 3.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(pry-stack_explorer) >= 0
Requires:      gem(rb-readline) >= 0
Conflicts:     gem(rspec-collection_matchers) >= 2
Conflicts:     gem(rspec-core) >= 4
Conflicts:     gem(rspec-expectations) >= 4
Conflicts:     gem(rspec-mocks) >= 4
Conflicts:     gem(rubocop-performance) >= 2

%description   -n gem-ohai-devel
Ohai profiles your system and emits JSON development package.

Ohai is a tool that is used to detect attributes on a node, and then provide
these attributes to the chef-client at the start of every chef-client run. Ohai
is required by the chef-client and must be present on a node.

%description   -n gem-ohai-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ohai.


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

%files         -n ohai
%_bindir/ohai

%files         -n gem-ohai-doc
%ruby_gemdocdir

%files         -n gem-ohai-devel


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 18.0.26-alt1
- ^ 18.0.10 -> 18.0.26

* Thu Apr 21 2022 Pavel Skrylev <majioa@altlinux.org> 18.0.10-alt1
- ^ 16.13.2 -> 18.0.10

* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 16.13.2-alt1
- ^ 16.2.4 -> 16.13.2

* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 16.2.4-alt1
- ^ 15.0.30 -> 16.2.4

* Mon Mar 25 2019 Pavel Skrylev <majioa@altlinux.org> 15.0.30-alt1
- > Ruby Policy 2.0
- ^ 15.0.25 -> 15.0.30

* Mon Dec 10 2018 Andrey Cherepanov <cas@altlinux.org> 15.0.25-alt1
- New version.

* Wed Dec 05 2018 Andrey Cherepanov <cas@altlinux.org> 15.0.20-alt1
- New version.

* Wed Nov 21 2018 Andrey Cherepanov <cas@altlinux.org> 15.0.7-alt1
- New version.

* Fri Oct 12 2018 Andrey Cherepanov <cas@altlinux.org> 14.6.2-alt1
- New version.

* Fri Oct 05 2018 Andrey Cherepanov <cas@altlinux.org> 14.5.9-alt1
- New version.

* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 14.5.7-alt1
- New version.

* Fri Sep 28 2018 Andrey Cherepanov <cas@altlinux.org> 14.5.6-alt1
- New version.

* Thu Sep 20 2018 Andrey Cherepanov <cas@altlinux.org> 14.5.5-alt1
- New version.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 14.5.4-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 14.5.1-alt1
- New version.

* Mon Aug 27 2018 Andrey Cherepanov <cas@altlinux.org> 14.2.4-alt1.1
- Rebuild for new Ruby autorequirements.

* Sat Jul 07 2018 Andrey Cherepanov <cas@altlinux.org> 14.2.4-alt1
- New version.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 14.2.1-alt1
- New version.
- Package as gem.

* Thu Jun 14 2018 Dmitry Terekhin <jqt4@altlinux.org> 14.2.0-alt2
- Delete dependency "ruby-net-dhcp" for rebuild to mipsel.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 14.2.0-alt1
- New version.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.7-alt1
- New version.

* Tue May 22 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.6-alt1
- New version.

* Sun May 20 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.5-alt1
- New version.

* Sat May 19 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.4-alt1
- New version.

* Wed May 16 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.3-alt1
- New version.

* Tue May 15 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.2-alt1
- New version.

* Fri May 11 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.1-alt1
- New version.

* Sat May 05 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.0-alt1
- New version.

* Thu May 03 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.34-alt1
- New version.

* Wed May 02 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.32-alt1
- New version.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.31-alt1
- New version.

* Wed Mar 28 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.30-alt1
- New version.

* Tue Mar 20 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.29-alt1
- New version.

* Sat Mar 17 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.28-alt1
- New version.

* Fri Mar 16 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.26-alt1
- New version.

* Sat Mar 10 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.25-alt1
- New version.

* Thu Mar 08 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.23-alt1
- New version.

* Wed Mar 07 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.22-alt1
- New version.

* Sat Mar 03 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.21-alt1
- New version.

* Fri Mar 02 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.20-alt1
- New version.

* Tue Feb 27 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.15-alt1
- New version.

* Sat Feb 24 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.13-alt1
- New version.

* Mon Feb 19 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.12-alt1
- New version.

* Tue Feb 13 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.2-alt1
- New version.

* Wed Jan 31 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.1-alt1
- New version.

* Thu Jan 11 2018 Andrey Cherepanov <cas@altlinux.org> 13.7.1-alt1
- New version.

* Wed Dec 06 2017 Andrey Cherepanov <cas@altlinux.org> 13.7.0-alt1
- New version.

* Wed Oct 25 2017 Andrey Cherepanov <cas@altlinux.org> 13.6.0-alt1
- New version

* Fri Sep 29 2017 Andrey Cherepanov <cas@altlinux.org> 13.5.0-alt1
- New version

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 13.4.0-alt1
- New version

* Mon Aug 14 2017 Andrey Cherepanov <cas@altlinux.org> 13.3.0-alt1
- New version

* Sat Jul 01 2017 Andrey Cherepanov <cas@altlinux.org> 13.2.0-alt1
- New version

* Sat May 13 2017 Andrey Cherepanov <cas@altlinux.org> 13.1.0-alt1
- New version

* Thu Apr 13 2017 Andrey Cherepanov <cas@altlinux.org> 13.0.1-alt1
- New version

* Fri Apr 07 2017 Andrey Cherepanov <cas@altlinux.org> 13.0.0-alt1
- New version

* Wed Mar 08 2017 Andrey Cherepanov <cas@altlinux.org> 8.23.0-alt1
- new version 8.23.0

* Wed Oct 05 2016 Andrey Cherepanov <cas@altlinux.org> 8.20.0-alt1
- new version 8.20.0

* Mon Oct 19 2015 Andrey Cherepanov <cas@altlinux.org> 8.7.0-alt1
- New version

* Fri Jan 30 2015 Andrey Cherepanov <cas@altlinux.org> 8.0.1-alt1
- Initial build for ALT Linux
