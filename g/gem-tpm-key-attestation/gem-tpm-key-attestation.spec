# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname tpm-key_attestation

Name:          gem-tpm-key-attestation
Version:       0.14.2
Release:       alt1
Summary:       TPM Key Attestation validation
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/cedarcode/tpm-key_attestation
Vcs:           https://github.com/cedarcode/tpm-key_attestation.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(appraisal) >= 2.4.0
BuildRequires: gem(bindata) >= 2.4
BuildRequires: gem(byebug) >= 11.0
BuildRequires: gem(openssl) > 2.0
BuildRequires: gem(openssl-signature_algorithm) >= 1.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1
BuildConflicts: gem(bindata) >= 3
BuildConflicts: gem(openssl-signature_algorithm) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency appraisal >= 2.4.0
%ruby_use_gem_dependency byebug >= 11.0
%ruby_alias_names tpm-key_attestation,tpm-key-attestation
Requires:      ruby >= 2.4.0
Requires:      gem(bindata) >= 2.4
Requires:      gem(openssl) > 2.0
Requires:      gem(openssl-signature_algorithm) >= 1.0
Conflicts:     gem(bindata) >= 3
Conflicts:     gem(openssl-signature_algorithm) >= 2
Provides:      tpm-key_attestation = %EVR
Provides:      gem(tpm-key_attestation) = 0.14.2

%description
TPM Key Attestation validation.

TPM Key Attestation utitlies


%if_enabled    doc
%package       -n gem-tpm-key-attestation-doc
Version:       0.14.2
Release:       alt1
Summary:       TPM Key Attestation validation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tpm-key_attestation
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tpm-key_attestation) = 0.14.2

%description   -n gem-tpm-key-attestation-doc
TPM Key Attestation validation documentation files.

%description   -n gem-tpm-key-attestation-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tpm-key_attestation.
%endif


%if_enabled    devel
%package       -n gem-tpm-key-attestation-devel
Version:       0.14.2
Release:       alt1
Summary:       TPM Key Attestation validation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета tpm-key_attestation
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(tpm-key_attestation) = 0.14.2
Requires:      gem(appraisal) >= 2.4.0
Requires:      gem(bindata) >= 2.4
Requires:      gem(byebug) >= 11.0
Requires:      gem(openssl) > 2.0
Requires:      gem(openssl-signature_algorithm) >= 1.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1
Conflicts:     gem(bindata) >= 3
Conflicts:     gem(openssl-signature_algorithm) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2

%description   -n gem-tpm-key-attestation-devel
TPM Key Attestation validation development package.

%description   -n gem-tpm-key-attestation-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета tpm-key_attestation.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-tpm-key-attestation-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-tpm-key-attestation-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Tue Sep 29 2026 Pavel Skrylev <majioa@altlinux.org> 0.14.2-alt1
- ^ 0.14.1 -> 0.14.2

* Sun Mar 29 2026 Pavel Skrylev <majioa@altlinux.org> 0.14.1-alt1
- ^ 0.10.0 -> 0.14.1
- * define explicit dependencies

* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt1
- + packaged gem with usage Ruby Policy 2.0
