%define        gemname ohai

Name:          gem-ohai
Version:       16.13.2
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
BuildRequires: gem(chef-config) >= 14.12 gem(chef-config) < 17
BuildRequires: gem(chef-utils) >= 16.0 gem(chef-utils) < 17
BuildRequires: gem(ffi) >= 1.9 gem(ffi) < 2
BuildRequires: gem(ffi-yajl) >= 2.2 gem(ffi-yajl) < 3
BuildRequires: gem(ipaddress) >= 0
BuildRequires: gem(mixlib-cli) >= 1.7.0
BuildRequires: gem(mixlib-config) >= 2.0 gem(mixlib-config) < 4.0
BuildRequires: gem(mixlib-log) >= 2.0.1 gem(mixlib-log) < 4.0
BuildRequires: gem(mixlib-shellout) >= 3.2.5 gem(mixlib-shellout) < 4
BuildRequires: gem(plist) >= 3.1 gem(plist) < 4
BuildRequires: gem(train-core) >= 0
BuildRequires: gem(wmi-lite) >= 1.0 gem(wmi-lite) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(chef-config) >= 14.12 gem(chef-config) < 17
Requires:      gem(chef-utils) >= 16.0 gem(chef-utils) < 17
Requires:      gem(ffi) >= 1.9 gem(ffi) < 2
Requires:      gem(ffi-yajl) >= 2.2 gem(ffi-yajl) < 3
Requires:      gem(ipaddress) >= 0
Requires:      gem(mixlib-cli) >= 1.7.0
Requires:      gem(mixlib-config) >= 2.0 gem(mixlib-config) < 4.0
Requires:      gem(mixlib-log) >= 2.0.1 gem(mixlib-log) < 4.0
Requires:      gem(mixlib-shellout) >= 3.2.5 gem(mixlib-shellout) < 4
Requires:      gem(plist) >= 3.1 gem(plist) < 4
Requires:      gem(train-core) >= 0
Requires:      gem(wmi-lite) >= 1.0 gem(wmi-lite) < 2
Obsoletes:     ohai < %EVR
Provides:      ohai = %EVR
Provides:      gem(ohai) = 16.13.2


%description
Ohai is a tool that is used to detect attributes on a node, and then provide
these attributes to the chef-client at the start of every chef-client run. Ohai
is required by the chef-client and must be present on a node.


%package       -n ohai
Version:       16.13.2
Release:       alt1
Summary:       Ohai profiles your system and emits JSON executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ohai
Group:         Development/Other
BuildArch:     noarch

Requires:      gem(ohai) = 16.13.2

%description   -n ohai
Ohai profiles your system and emits JSON executable(s).

Ohai is a tool that is used to detect attributes on a node, and then provide
these attributes to the chef-client at the start of every chef-client run. Ohai
is required by the chef-client and must be present on a node.

%description   -n ohai -l ru_RU.UTF-8
Исполнямка для самоцвета ohai.


%package       -n gem-ohai-doc
Version:       16.13.2
Release:       alt1
Summary:       Ohai profiles your system and emits JSON documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ohai
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ohai) = 16.13.2

%description   -n gem-ohai-doc
Ohai profiles your system and emits JSON documentation files.

Ohai is a tool that is used to detect attributes on a node, and then provide
these attributes to the chef-client at the start of every chef-client run. Ohai
is required by the chef-client and must be present on a node.

%description   -n gem-ohai-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ohai.


%package       -n gem-ohai-devel
Version:       16.13.2
Release:       alt1
Summary:       Ohai profiles your system and emits JSON development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ohai
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ohai) = 16.13.2

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
