%define        gemname webauthn

Name:          gem-webauthn
Version:       2.5.2
Release:       alt1
Summary:       WebAuthn ruby server library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cedarcode/webauthn-ruby
Vcs:           https://github.com/cedarcode/webauthn-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.17
BuildRequires: gem(byebug) >= 11.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.8
BuildRequires: gem(rubocop) >= 1.9.1
BuildRequires: gem(rubocop-rake) >= 0.5.1
BuildRequires: gem(rubocop-rspec) >= 2.2.0
BuildRequires: gem(android_key_attestation) >= 0.3.0
BuildRequires: gem(awrence) >= 1.1
BuildRequires: gem(bindata) >= 2.4
BuildRequires: gem(cbor) >= 0.5.9
BuildRequires: gem(cose) >= 1.1
BuildRequires: gem(openssl) >= 2.2
BuildRequires: gem(safety_net_attestation) >= 0.4.0
BuildRequires: gem(tpm-key_attestation) >= 0.11.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(byebug) >= 12
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(android_key_attestation) >= 0.4
BuildConflicts: gem(awrence) >= 2
BuildConflicts: gem(bindata) >= 3
BuildConflicts: gem(cbor) >= 0.6
BuildConflicts: gem(cose) >= 2
BuildConflicts: gem(openssl) >= 4
BuildConflicts: gem(safety_net_attestation) >= 0.5
BuildConflicts: gem(tpm-key_attestation) >= 0.12
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency openssl >= 3.0.0,openssl < 4
%ruby_use_gem_dependency rubocop-rake >= 0.6.0,rubocop-rake < 1
Requires:      gem(android_key_attestation) >= 0.3.0
Requires:      gem(awrence) >= 1.1
Requires:      gem(bindata) >= 2.4
Requires:      gem(cbor) >= 0.5.9
Requires:      gem(cose) >= 1.1
Requires:      gem(openssl) >= 2.2
Requires:      gem(safety_net_attestation) >= 0.4.0
Requires:      gem(tpm-key_attestation) >= 0.11.0
Conflicts:     gem(android_key_attestation) >= 0.4
Conflicts:     gem(awrence) >= 2
Conflicts:     gem(bindata) >= 3
Conflicts:     gem(cbor) >= 0.6
Conflicts:     gem(cose) >= 2
Conflicts:     gem(openssl) >= 4
Conflicts:     gem(safety_net_attestation) >= 0.5
Conflicts:     gem(tpm-key_attestation) >= 0.12
Provides:      gem(webauthn) = 2.5.2


%description
WebAuthn ruby server library - Make your application a W3C Web Authentication
conformant Relying Party and allow your users to authenticate with U2F and FIDO2
authenticators.

Takes care of the server-side operations needed to register or authenticate a
user credential, including the necessary cryptographic checks.


%package       -n gem-webauthn-doc
Version:       2.5.2
Release:       alt1
Summary:       WebAuthn ruby server library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета webauthn
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(webauthn) = 2.5.2

%description   -n gem-webauthn-doc
WebAuthn ruby server library documentation files.

WebAuthn ruby server library - Make your application a W3C Web Authentication
conformant Relying Party and allow your users to authenticate with U2F and FIDO2
authenticators.

Takes care of the server-side operations needed to register or authenticate a
user credential, including the necessary cryptographic checks.

%description   -n gem-webauthn-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета webauthn.


%package       -n gem-webauthn-devel
Version:       2.5.2
Release:       alt1
Summary:       WebAuthn ruby server library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета webauthn
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(webauthn) = 2.5.2
Requires:      gem(bundler) >= 1.17
Requires:      gem(byebug) >= 11.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.8
Requires:      gem(rubocop) >= 1.9.1
Requires:      gem(rubocop-rake) >= 0.5.1
Requires:      gem(rubocop-rspec) >= 2.2.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(byebug) >= 12
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 3

%description   -n gem-webauthn-devel
WebAuthn ruby server library development package.

WebAuthn ruby server library - Make your application a W3C Web Authentication
conformant Relying Party and allow your users to authenticate with U2F and FIDO2
authenticators.

Takes care of the server-side operations needed to register or authenticate a
user credential, including the necessary cryptographic checks.

%description   -n gem-webauthn-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета webauthn.


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

%files         -n gem-webauthn-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-webauthn-devel
%doc README.md


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 2.5.2-alt1
- ^ 2.5.1.1 -> 2.5.2

* Fri Jul 01 2022 Pavel Skrylev <majioa@altlinux.org> 2.5.1.1-alt1
- ^ 2.5.1 -> 2.5.1[1]

* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 2.5.1-alt1
- ^ 2.4.0 -> 2.5.1

* Fri Jul 17 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- + packaged gem with usage Ruby Policy 2.0
