# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname scanf

Name:          gem-%pkgname
Version:       1.0.0.1
Release:       alt0.1
Summary:       scanf is an implementation of the C function scanf(3)
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby/scanf
Vcs:           https://github.com/ruby/scanf.git
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
%ruby_build --use=%gemname --version-replace=%version

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
* Mon Dec 14 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.0.1-alt0.1
- + packaged pre gem with usage Ruby Policy 2.0
