# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname amazing-print
%define        gemname amazing_print

Name:          gem-%pkgname
Version:       1.2.2
Release:       alt1
Summary:       Pretty print your Ruby objects with style
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/amazing-print/amazing_print
Vcs:           https://github.com/amazing-print/amazing_print.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Pretty print your Ruby objects with style -- in full color and with proper
indentation.

AmazingPrint is a fork of AwesomePrint which became stale and should be used
in its place to avoid conflicts. It is a Ruby library that pretty prints Ruby
objects in full color exposing their internal structure with proper indentation.
Rails ActiveRecord objects and usage within Rails templates are supported via
included mixins.


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
* Thu Dec 10 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.2-alt1
- + packaged gem with usage Ruby Policy 2.0
