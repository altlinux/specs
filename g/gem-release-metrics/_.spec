# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname release-metrics

Name:          gem-%pkgname
Version:       1.1.0
Release:       alt1
Summary:       Puppet, Inc. Release Metrics
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://rubygems.org/gems/release-metrics
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
%summary.


%package       -n releases
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n releases
Executable file for %gemname gem.

%description   -n releases -l ru_RU.UTF8
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

%files         -n releases
%doc README*
%_bindir/*

%files         doc
%ruby_gemdocdir


%changelog
* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with usage Ruby Policy 2.0
