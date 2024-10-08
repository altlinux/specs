# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname puma-plugin-systemd

Name:          gem-puma-plugin-systemd
Version:       0.1.5.9
Release:       alt1
Summary:       Puma integration with systemd: notify, status, watchdog
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sj26/puma-plugin-systemd
Vcs:           https://github.com/sj26/puma-plugin-systemd.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.13
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(puma) >= 3.6
BuildRequires: gem(json) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(puma) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(puma) >= 3.6
Requires:      gem(json) >= 0
Conflicts:     gem(puma) >= 7
Provides:      gem(puma-plugin-systemd) = 0.1.5.9


%description
Puma integration with systemd for better daemonising under modern Linux
systemds: notify, status, watchdog.

* Notify systemd when puma has booted and is ready to handle requests
* Publish puma stats as systemd service status for a quick overview
* Use the watchdog to make sure your puma processes are healthy and haven't
locked up or run out of memory


%if_enabled    doc
%package       -n gem-puma-plugin-systemd-doc
Version:       0.1.5.9
Release:       alt1
Summary:       Puma integration with systemd: notify, status, watchdog documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puma-plugin-systemd
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(puma-plugin-systemd) = 0.1.5.9

%description   -n gem-puma-plugin-systemd-doc
Puma integration with systemd: notify, status, watchdog documentation
files.

Puma integration with systemd for better daemonising under modern Linux
systemds: notify, status, watchdog.

* Notify systemd when puma has booted and is ready to handle requests
* Publish puma stats as systemd service status for a quick overview
* Use the watchdog to make sure your puma processes are healthy and haven't
locked up or run out of memory

%description   -n gem-puma-plugin-systemd-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета puma-plugin-systemd.
%endif


%if_enabled    devel
%package       -n gem-puma-plugin-systemd-devel
Version:       0.1.5.9
Release:       alt1
Summary:       Puma integration with systemd: notify, status, watchdog development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета puma-plugin-systemd
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puma-plugin-systemd) = 0.1.5.9
Requires:      gem(bundler) >= 1.13
Requires:      gem(rake) >= 12.3.3
Requires:      gem(minitest) >= 5.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(minitest) >= 6

%description   -n gem-puma-plugin-systemd-devel
Puma integration with systemd: notify, status, watchdog development
package.

Puma integration with systemd for better daemonising under modern Linux
systemds: notify, status, watchdog.

* Notify systemd when puma has booted and is ready to handle requests
* Publish puma stats as systemd service status for a quick overview
* Use the watchdog to make sure your puma processes are healthy and haven't
locked up or run out of memory

%description   -n gem-puma-plugin-systemd-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета puma-plugin-systemd.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-puma-plugin-systemd-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-puma-plugin-systemd-devel
%doc README.md
%endif


%changelog
* Tue Oct 08 2024 Pavel Skrylev <majioa@altlinux.org> 0.1.5.9-alt1
- ^ 0.1.5 -> 0.1.5p9

* Fri Jul 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1
- + packaged gem with Ruby Policy 2.0
