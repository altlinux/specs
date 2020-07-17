# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname gauntlet

Name:          gem-%pkgname
Version:       2.1.0
Release:       alt1
Summary:       Gauntlet is a pluggable means of running code against all the latest gems and storing off the data
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/gauntlet
Vcs:           https://github.com/seattlerb/gauntlet.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(hoe) >= 3.12
BuildRequires: gem(minitest) >= 5.4
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(net-http-persistent) >= 1.4.1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%gem_replace_version net-http-persistent >= 1.4.1

%description
%summary.

* Downloads all the latest gems and converts them to tarballs for easy access.
* Iterates through all downloaded gems, unpacks them, and then runs your code.
* Automates storage of results to YAML files.
* Easily skips over projects that already have results (overridable).
* gauntlet commandline locates your gauntlet library via rubygems:
  * eg. `gauntlet flog` finds gauntlet_flog.rb in the flog gem.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n %pkgname
%_bindir/%{pkgname}*

%files         doc
%ruby_gemdocdir


%changelog
* Fri Jul 17 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- + packaged gem with usage Ruby Policy 2.0
