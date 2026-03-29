# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname tpm-key_attestation

Name:          gem-tpm-key-attestation
Version:       0.14.1
Release:       alt1
Summary:       TPM Key Attestation validation
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/cedarcode/tpm-key_attestation
Vcs:           https://github.com/cedarcode/tpm-key_attestation.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(appraisal) >= 2.4.0
BuildRequires: gem(bindata) >= 2.4
BuildRequires: gem(byebug) >= 11.0
BuildRequires: gem(openssl) > 2.0
BuildRequires: gem(openssl-signature_algorithm) >= 1.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1
BuildConflicts: gem(appraisal) >= 3
BuildConflicts: gem(bindata) >= 3
BuildConflicts: gem(byebug) >= 13
BuildConflicts: gem(openssl-signature_algorithm) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency appraisal >= 2.4.0,appraisal < 3
%ruby_use_gem_dependency byebug >= 12.0.0,byebug < 13
%ruby_alias_names tpm-key_attestation,tpm-key-attestation
Requires:      ruby >= 2.4.0
Requires:      gem(bindata) >= 2.4
Requires:      gem(openssl) > 2.0
Requires:      gem(openssl-signature_algorithm) >= 1.0
Conflicts:     gem(bindata) >= 3
Conflicts:     gem(openssl-signature_algorithm) >= 2
Provides:      gem(tpm-key_attestation) = 0.14.1

%description
TPM Key Attestation validation.

TPM Key Attestation utitlies


%if_enabled    doc
%package       -n gem-tpm-key-attestation-doc
Version:       0.14.1
Release:       alt1
Summary:       TPM Key Attestation validation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tpm-key_attestation
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(tpm-key_attestation) = 0.14.1

%description   -n gem-tpm-key-attestation-doc
TPM Key Attestation validation documentation files.

%description   -n gem-tpm-key-attestation-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tpm-key_attestation.
%endif


%if_enabled    devel
%package       -n gem-tpm-key-attestation-devel
Version:       0.14.1
Release:       alt1
Summary:       TPM Key Attestation validation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета tpm-key_attestation
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(tpm-key_attestation) = 0.14.1
Requires:      gem(appraisal) >= 2.4.0
Requires:      gem(byebug) >= 11.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1
Conflicts:     gem(appraisal) >= 3
Conflicts:     gem(byebug) >= 13
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
* Sun Mar 29 2026 Pavel Skrylev <majioa@altlinux.org> 0.14.1-alt1
- ^ 0.10.0 -> 0.14.1
- * define explicit dependencies

* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt1
- + packaged gem with usage Ruby Policy 2.0
