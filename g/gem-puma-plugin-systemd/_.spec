# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname puma-plugin-systemd

Name:          gem-puma-plugin-systemd
Version:       0.1.5
Release:       alt1
Summary:       Puma integration with systemd: notify, status, watchdog
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sj26/puma-plugin-systemd
Vcs:           https://github.com/sj26/puma-plugin-systemd.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(puma) >= 3.6 gem(puma) < 6
BuildRequires: gem(json) >= 0
BuildRequires: gem(bundler) >= 1.13 gem(bundler) < 3
BuildRequires: gem(rake) >= 12.3.3 gem(rake) < 14
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency puma >= 5.2.2,puma < 6
Requires:      gem(puma) >= 3.6 gem(puma) < 6
Requires:      gem(json) >= 0
Provides:      gem(puma-plugin-systemd) = 0.1.5


%description
Puma integration with systemd for better daemonising under modern Linux
systemds: notify, status, watchdog.

* Notify systemd when puma has booted and is ready to handle requests
* Publish puma stats as systemd service status for a quick overview
* Use the watchdog to make sure your puma processes are healthy and haven't
  locked up or run out of memory


%package       -n gem-puma-plugin-systemd-devel
Version:       0.1.5
Release:       alt1
Summary:       Puma integration with systemd: notify, status, watchdog development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета puma-plugin-systemd
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puma-plugin-systemd) = 0.1.5
Requires:      gem(bundler) >= 1.13 gem(bundler) < 3
Requires:      gem(rake) >= 12.3.3 gem(rake) < 14
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6

%description   -n gem-puma-plugin-systemd-devel
Puma integration with systemd: notify, status, watchdog development package.

%description   -n gem-puma-plugin-systemd-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета puma-plugin-systemd.


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

%files         -n gem-puma-plugin-systemd-devel
%doc README.md


%changelog
* Fri Jul 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.5-alt1
- + packaged gem with Ruby Policy 2.0
