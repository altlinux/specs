# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname cliver

Name:          gem-%pkgname
Version:       0.3.2
Release:       alt1
Summary:       Assertions for command-line dependencies
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/yaauie/cliver
Vcs:           https://github.com/yaauie/cliver.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Sometimes Ruby apps shell out to command-line executables, but there is no
standard way to ensure those underlying dependencies are met. Users usually find
out via a nasty stack-trace and whatever wasn't captured on stderr, or by the
odd behavior exposed by a version mismatch.

Cliver is a simple gem that provides an easy way to detect and use command-line
dependencies. Under the covers, it uses rubygems/requirements so it supports
the version requirements you're used to providing in your gemspec.


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
* Fri Jul 17 2020 Pavel Skrylev <majioa@altlinux.org> 0.3.2-alt1
- + packaged gem with usage Ruby Policy 2.0
