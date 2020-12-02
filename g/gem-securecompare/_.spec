# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname securecompare

Name:          gem-%pkgname
Version:       1.0.0
Release:       alt1
Summary:       securecompare is a gem that implements a constant time string comparison method safe for use in cryptographic functions
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/samuelkadolph/securecompare
Vcs:           https://github.com/samuelkadolph/securecompare.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.

securecompare borrows the secure_compare private method from
ActiveSupport::MessageVerifier which lets you do safely compare strings without
being vulnerable to timing attacks. Useful for Basic HTTP Authentication in
your rack/rails application.


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
* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with usage Ruby Policy 2.0
