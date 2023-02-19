# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname openssl-signature_algorithm

Name:          gem-openssl-signature-algorithm
Version:       1.2.1
Release:       alt1
Summary:       ECDSA, RSA-PSS and RSA-PKCS#1 algorithms for ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/cedarcode/openssl-signature_algorithm
Vcs:           https://github.com/cedarcode/openssl-signature_algorithm.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(appraisal) >= 2.2
BuildRequires: gem(byebug) >= 11.0
BuildRequires: gem(ed25519) >= 1.2
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 0.80.1
BuildRequires: gem(openssl) > 2.0
BuildConflicts: gem(appraisal) >= 3
BuildConflicts: gem(byebug) >= 12
BuildConflicts: gem(ed25519) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(openssl) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency openssl >= 3.0.0,openssl < 4
%ruby_alias_names openssl-signature_algorithm,openssl-signature-algorithm
Requires:      gem(openssl) > 2.0
Conflicts:     gem(openssl) >= 4
Provides:      gem(openssl-signature_algorithm) = 1.2.1


%description
Sign and verify using signature algorithm wrappers, instead of key
objects.

Provides OpenSSL::SignatureAlgorithm::ECDSA, OpenSSL::SignatureAlgorithm::RSAPSS
and OpenSSL::SignatureAlgorithm::RSAPKCS1 ruby object wrappers on top of
OpenSSL::PKey::EC and OpenSSL::PKey::RSA, so that you can reason in terms of the
algorithms and do less when signing or verifying signatures.

Loosely inspired by rbnacl's Digital Signatures interface.


%package       -n gem-openssl-signature-algorithm-doc
Version:       1.2.1
Release:       alt1
Summary:       ECDSA, RSA-PSS and RSA-PKCS#1 algorithms for ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета openssl-signature_algorithm
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(openssl-signature_algorithm) = 1.2.1

%description   -n gem-openssl-signature-algorithm-doc
ECDSA, RSA-PSS and RSA-PKCS#1 algorithms for ruby documentation files.

Sign and verify using signature algorithm wrappers, instead of key
objects.

Provides OpenSSL::SignatureAlgorithm::ECDSA, OpenSSL::SignatureAlgorithm::RSAPSS
and OpenSSL::SignatureAlgorithm::RSAPKCS1 ruby object wrappers on top of
OpenSSL::PKey::EC and OpenSSL::PKey::RSA, so that you can reason in terms of the
algorithms and do less when signing or verifying signatures.

Loosely inspired by rbnacl's Digital Signatures interface.

%description   -n gem-openssl-signature-algorithm-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета openssl-signature_algorithm.


%package       -n gem-openssl-signature-algorithm-devel
Version:       1.2.1
Release:       alt1
Summary:       ECDSA, RSA-PSS and RSA-PKCS#1 algorithms for ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета openssl-signature_algorithm
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(openssl-signature_algorithm) = 1.2.1
Requires:      gem(appraisal) >= 2.2
Requires:      gem(byebug) >= 11.0
Requires:      gem(ed25519) >= 1.2
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 0.80.1
Conflicts:     gem(appraisal) >= 3
Conflicts:     gem(byebug) >= 12
Conflicts:     gem(ed25519) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2

%description   -n gem-openssl-signature-algorithm-devel
ECDSA, RSA-PSS and RSA-PKCS#1 algorithms for ruby development package.

Sign and verify using signature algorithm wrappers, instead of key
objects.

Provides OpenSSL::SignatureAlgorithm::ECDSA, OpenSSL::SignatureAlgorithm::RSAPSS
and OpenSSL::SignatureAlgorithm::RSAPKCS1 ruby object wrappers on top of
OpenSSL::PKey::EC and OpenSSL::PKey::RSA, so that you can reason in terms of the
algorithms and do less when signing or verifying signatures.

Loosely inspired by rbnacl's Digital Signatures interface.

%description   -n gem-openssl-signature-algorithm-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета openssl-signature_algorithm.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-openssl-signature-algorithm-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-openssl-signature-algorithm-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt1
- ^ 1.0.0 -> 1.2.1

* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with usage Ruby Policy 2.0
