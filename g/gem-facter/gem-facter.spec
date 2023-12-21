%define        _unpackaged_files_terminate_build 1
%define        gemname facter

Name:          gem-facter
Version:       4.5.1
Release:       alt1
Summary:       Ruby library for retrieving facts from operating systems
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://tickets.puppetlabs.com/browse/FACT
Vcs:           https://github.com/puppetlabs/facter.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         ronn.patch
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 0.81.0
BuildRequires: gem(rubocop-performance) >= 1.5.2
BuildRequires: gem(rubocop-rspec) >= 1.38
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(sys-filesystem) >= 1.4
BuildRequires: gem(webmock) >= 3.12
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(octokit) >= 4.18.0
BuildRequires: gem(packaging) >= 0
BuildRequires: gem(ffi) >= 1.15.5
BuildRequires: gem(ronn-ng) >= 0.7
BuildRequires: gem(hocon) >= 1.3
BuildRequires: gem(thor) >= 1.0.1
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(sys-filesystem) >= 2
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(octokit) >= 6
BuildConflicts: gem(ffi) >= 2
BuildConflicts: gem(ronn-ng) >= 1
BuildConflicts: gem(hocon) >= 2
BuildConflicts: gem(thor) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency ffi >= 1.15.5,ffi < 2
%ruby_use_gem_dependency octokit >= 5.6.1,octokit < 6
Requires:      gem(hocon) >= 1.3
Requires:      gem(thor) >= 1.0.1
Requires:      coreutils
Requires:      dmidecode
Requires:      net-tools
Requires:      pciutils
Requires:      bind-utils
Conflicts:     gem(hocon) >= 2
Conflicts:     gem(thor) >= 2
Obsoletes:     ruby-facter
Provides:      ruby-facter
Provides:      gem(facter) = 4.5.1


%description
A cross-platform Ruby library for retrieving facts from operating systems.
Supports multiple resolution mechanisms, any of which can be restricted to
working only on certain operating systems or environments. Facter is especially
useful for retrieving things like operating system names, IP addresses, MAC
addresses, and SSH keys.

It is easy to extend Facter to include your own custom facts or to include
additional mechanisms for retrieving facts.


%package       -n facter
Version:       4.5.1
Release:       alt1
Summary:       Ruby library for retrieving facts from operating systems executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета facter
Group:         System/Base
BuildArch:     noarch

Requires:      gem(facter) = 4.5.1

%description   -n facter
Ruby library for retrieving facts from operating systems executable(s).

A cross-platform Ruby library for retrieving facts from operating systems.
Supports multiple resolution mechanisms, any of which can be restricted to
working only on certain operating systems or environments. Facter is especially
useful for retrieving things like operating system names, IP addresses, MAC
addresses, and SSH keys.

It is easy to extend Facter to include your own custom facts or to include
additional mechanisms for retrieving facts.

%description   -n facter -l ru_RU.UTF-8
Исполнямка для самоцвета facter.


%package       -n gem-facter-doc
Version:       4.5.1
Release:       alt1
Summary:       Ruby library for retrieving facts from operating systems documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета facter
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(facter) = 4.5.1

%description   -n gem-facter-doc
Ruby library for retrieving facts from operating systems documentation files.

A cross-platform Ruby library for retrieving facts from operating systems.
Supports multiple resolution mechanisms, any of which can be restricted to
working only on certain operating systems or environments. Facter is especially
useful for retrieving things like operating system names, IP addresses, MAC
addresses, and SSH keys.

It is easy to extend Facter to include your own custom facts or to include
additional mechanisms for retrieving facts.

%description   -n gem-facter-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета facter.


%package       -n gem-facter-devel
Version:       4.5.1
Release:       alt1
Summary:       Ruby library for retrieving facts from operating systems development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета facter
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(facter) = 4.5.1
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 0.81.0
Requires:      gem(rubocop-performance) >= 1.5.2
Requires:      gem(rubocop-rspec) >= 1.38
Requires:      gem(simplecov) >= 0.17
Requires:      gem(sys-filesystem) >= 1.4
Requires:      gem(webmock) >= 3.12
Requires:      gem(yard) >= 0.9
Requires:      gem(octokit) >= 4.18.0
Requires:      gem(packaging) >= 0
Requires:      gem(ffi) >= 1.15.5
Requires:      gem(ronn-ng) >= 0.7
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rspec) >= 3
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(sys-filesystem) >= 2
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(yard) >= 1
Conflicts:     gem(octokit) >= 6
Conflicts:     gem(ffi) >= 2
Conflicts:     gem(ronn-ng) >= 1

%description   -n gem-facter-devel
Ruby library for retrieving facts from operating systems development package.

A cross-platform Ruby library for retrieving facts from operating systems.
Supports multiple resolution mechanisms, any of which can be restricted to
working only on certain operating systems or environments. Facter is especially
useful for retrieving things like operating system names, IP addresses, MAC
addresses, and SSH keys.

It is easy to extend Facter to include your own custom facts or to include
additional mechanisms for retrieving facts.

%description   -n gem-facter-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета facter.


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n facter
%_bindir/facter
%_man8dir/facter.*xz

%files         -n gem-facter-doc
%ruby_gemdocdir

%files         -n gem-facter-devel


%changelog
* Tue Dec 19 2023 Pavel Skrylev <majioa@altlinux.org> 4.5.1-alt1
- ^ 4.3.1 -> 4.5.1

* Thu Apr 13 2023 Pavel Skrylev <majioa@altlinux.org> 4.3.1-alt1
- ^ 4.2.13 -> 4.3.1

* Fri Oct 07 2022 Pavel Skrylev <majioa@altlinux.org> 4.2.13-alt1
- ^ 4.2.9 -> 4.2.13

* Sun Apr 17 2022 Pavel Skrylev <majioa@altlinux.org> 4.2.9-alt1
- ^ 4.2.7 -> 4.2.9

* Thu Jan 13 2022 Andrey Cherepanov <cas@altlinux.org> 4.2.7-alt1
- New version.

* Fri Dec 10 2021 Andrey Cherepanov <cas@altlinux.org> 4.2.6-alt1
- New version.

* Wed Sep 29 2021 Andrey Cherepanov <cas@altlinux.org> 4.2.5-alt1
- New version.

* Tue Sep 14 2021 Andrey Cherepanov <cas@altlinux.org> 4.2.4-alt1
- New version.

* Mon Aug 16 2021 Andrey Cherepanov <cas@altlinux.org> 4.2.3-alt1
- New version.

* Wed Jul 07 2021 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- New version.

* Thu Jun 17 2021 Andrey Cherepanov <cas@altlinux.org> 4.2.1-alt1
- New version.

* Mon Jan 25 2021 Andrey Cherepanov <cas@altlinux.org> 4.0.49-alt1
- New version.

* Thu Apr 16 2020 Pavel Skrylev <majioa@altlinux.org> 2.5.7.1-alt1
- ! renaming ALT Linux to ALT (closes #38358)
- ^ 2.5.7 -> 2.5.7.1pre

* Tue Mar 10 2020 Pavel Skrylev <majioa@altlinux.org> 2.5.7-alt1
- ^ 2.5.5 -> 2.5.7
- + timeout patch
- ! spec tags

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.5-alt1
- update (^) 2.5.2 -> 2.5.5
- fix (!) spec

* Wed Jul 03 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.2-alt1
- update (^) 2.5.1 -> 2.5.2 with ALT support
- fix (!) spec

* Fri Feb 22 2019 Pavel Skrylev <majioa@altlinux.org> 2.5.1-alt3
- update to (^) Ruby Policy 2.0

* Thu Dec 20 2018 Pavel Skrylev <majioa@altlinux.org> 2.5.1-alt2
- remove (-) bug in ALT Release detection.
- downgrade (v) timeout when accessing to EC2 from virtual env.
- added (+) facter executable rpm.
- remove (-) bug (Closes #35801)

* Tue Dec 18 2018 Pavel Skrylev <majioa@altlinux.org> 2.5.1-alt1
- update to (^) 2.0.1 -> 2.5.1

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt2.2
- Rebuild with new Ruby autorequirements.

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt2.1
- Rebuild with Ruby 2.4.1

* Wed Jan 18 2017 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt2
- Add ALT Linux operating system support
- Add bind-utils for IP address get

* Mon Apr 28 2014 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version

* Fri Nov 30 2012 Led <led@altlinux.ru> 1.6.8-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Fri Apr 27 2012 Sergey Alembekov <rt@altlinux.ru> 1.6.8-alt1
- [1.6.8]

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 1.5.6-alt1
- [1.5.6]

* Fri Oct 31 2008 Sir Raorn <raorn@altlinux.ru> 1.5.2-alt1
- [1.5.2]

* Wed Sep 03 2008 Sir Raorn <raorn@altlinux.ru> 1.5.1-alt1
- Built for Sisyphus
