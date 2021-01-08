# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname webrick

Name:          gem-%pkgname
Version:       1.7.0
Release:       alt1
Summary:       WEBrick is an HTTP server toolkit that can be configured as an HTTPS server
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby/webrick
Vcs:           https://github.com/ruby/webrick.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.


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
* Fri Jan 08 2021 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- + packaged gem with usage Ruby Policy 2.0
