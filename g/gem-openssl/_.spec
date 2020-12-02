# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname openssl

Name:          gem-%pkgname
Version:       2.2.0
Release:       alt1
Summary:       It wraps the OpenSSL library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby/openssl
Vcs:           https://github.com/ruby/openssl.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: openssl-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
OpenSSL provides SSL, TLS and general purpose cryptography.
It wraps the OpenSSL library.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       devel
Summary:       Development files for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

Requires:      openssl-devel

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.


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
%ruby_gemextdir
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/*


%changelog
* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- + packaged gem with usage Ruby Policy 2.0
