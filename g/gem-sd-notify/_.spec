# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname sd-notify
%define        gemname sd_notify

Name:          gem-%pkgname
Version:       0.1.0
Release:       alt1
Summary:       A pure-Ruby implementation of systemd's sd_notify(3)
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/agis/ruby-sdnotify
Vcs:           https://github.com/agis/ruby-sdnotify.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
A pure-Ruby implementation of sd_notify(3) that can be used to communicate
state changes of Ruby programs to systemd.


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

%files         doc
%ruby_gemdocdir


%changelog
* Mon Dec 07 2020 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt1
- + packaged gem with usage Ruby Policy 2.0
