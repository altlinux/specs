# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname hammer-cli
%define        gemname hammer_cli

Name:          gem-%pkgname
Version:       2.3.0
Release:       alt1
Summary:       Next-gen CLI tool for foreman
License:       GPLv3
Group:         Development/Ruby
Url:           https://github.com/theforeman/hammer-cli
Vcs:           https://github.com/theforeman/hammer-cli.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%gem_replace_version clamp ~> 1.2

%description
%summary.


%package       -n hammer
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n hammer
Executable file for %gemname gem.

%description   -n hammer -l ru_RU.UTF8
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

%files         -n hammer
%_bindir/hammer*

%files         doc
%ruby_gemdocdir


%changelog
* Thu Dec 10 2020 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- + packaged gem with usage Ruby Policy 2.0
