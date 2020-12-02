# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname openssl-signature-algorithm
%define        gemname openssl-signature_algorithm

Name:          gem-%pkgname
Version:       1.0.0
Release:       alt1
Summary:       ECDSA, RSA-PSS and RSA-PKCS#1 algorithms for ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cedarcode/openssl-signature_algorithm
Vcs:           https://github.com/cedarcode/openssl-signature_algorithm.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
Sign and verify using signature algorithm wrappers, instead of key objects.

Provides OpenSSL::SignatureAlgorithm::ECDSA, OpenSSL::SignatureAlgorithm::RSAPSS
and OpenSSL::SignatureAlgorithm::RSAPKCS1 ruby object wrappers on top of
OpenSSL::PKey::EC and OpenSSL::PKey::RSA, so that you can reason in terms of
the algorithms and do less when signing or verifying signatures.

Loosely inspired by rbnacl's Digital Signatures interface.


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
