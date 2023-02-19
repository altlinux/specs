# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname tpm-key_attestation

Name:          gem-tpm-key-attestation
Version:       0.11.0
Release:       alt1
Summary:       TPM Key Attestation validation
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/cedarcode/tpm-key_attestation
Vcs:           https://github.com/cedarcode/tpm-key_attestation.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(appraisal) >= 2.2.0
BuildRequires: gem(byebug) >= 11.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 0.80.1
BuildRequires: gem(bindata) >= 2.4
BuildRequires: gem(openssl) > 2.0
BuildRequires: gem(openssl-signature_algorithm) >= 1.0
BuildConflicts: gem(appraisal) >= 3
BuildConflicts: gem(byebug) >= 12
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(bindata) >= 3
BuildConflicts: gem(openssl) >= 4
BuildConflicts: gem(openssl-signature_algorithm) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency appraisal >= 2.4.0,appraisal < 3
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency openssl >= 3.0.0,openssl < 4
%ruby_alias_names tpm-key_attestation,tpm-key-attestation
Requires:      gem(bindata) >= 2.4
Requires:      gem(openssl) > 2.0
Requires:      gem(openssl-signature_algorithm) >= 1.0
Conflicts:     gem(bindata) >= 3
Conflicts:     gem(openssl) >= 4
Conflicts:     gem(openssl-signature_algorithm) >= 2
Provides:      gem(tpm-key_attestation) = 0.11.0


%description
TPM Key Attestation validation.

TPM Key Attestation utitlies


%package       -n gem-tpm-key-attestation-doc
Version:       0.11.0
Release:       alt1
Summary:       TPM Key Attestation validation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tpm-key_attestation
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tpm-key_attestation) = 0.11.0

%description   -n gem-tpm-key-attestation-doc
TPM Key Attestation validation documentation files.

%description   -n gem-tpm-key-attestation-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tpm-key_attestation.


%package       -n gem-tpm-key-attestation-devel
Version:       0.11.0
Release:       alt1
Summary:       TPM Key Attestation validation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета tpm-key_attestation
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(tpm-key_attestation) = 0.11.0
Requires:      gem(appraisal) >= 2.2.0
Requires:      gem(byebug) >= 11.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 0.80.1
Conflicts:     gem(appraisal) >= 3
Conflicts:     gem(byebug) >= 12
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2

%description   -n gem-tpm-key-attestation-devel
TPM Key Attestation validation development package.

%description   -n gem-tpm-key-attestation-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета tpm-key_attestation.


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

%files         -n gem-tpm-key-attestation-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-tpm-key-attestation-devel
%doc README.md


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 0.11.0-alt1
- ^ 0.10.0 -> 0.11.0

* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt1
- + packaged gem with usage Ruby Policy 2.0
