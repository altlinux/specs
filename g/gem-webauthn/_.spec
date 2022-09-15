%define        gemname webauthn

Name:          gem-webauthn
Version:       2.5.1.1
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
BuildRequires: gem(android_key_attestation) >= 0.3.0 gem(android_key_attestation) < 0.4
BuildRequires: gem(awrence) >= 1.1 gem(awrence) < 2
BuildRequires: gem(bindata) >= 2.4 gem(bindata) < 3
BuildRequires: gem(cbor) >= 0.5.9 gem(cbor) < 0.6
BuildRequires: gem(cose) >= 1.1 gem(cose) < 2
BuildRequires: gem(openssl) >= 2.2 gem(openssl) < 4
BuildRequires: gem(safety_net_attestation) >= 0.4.0 gem(safety_net_attestation) < 0.5
BuildRequires: gem(tpm-key_attestation) >= 0.10.0 gem(tpm-key_attestation) < 0.11
BuildRequires: gem(bundler) >= 1.17 gem(bundler) < 3
BuildRequires: gem(byebug) >= 11.0 gem(byebug) < 12
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.8 gem(rspec) < 4
BuildRequires: gem(rubocop) >= 1.9.1 gem(rubocop) < 2
BuildRequires: gem(rubocop-rake) >= 0.5.1 gem(rubocop-rake) < 1
BuildRequires: gem(rubocop-rspec) >= 2.2.0 gem(rubocop-rspec) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency openssl >= 3.0.0,openssl < 4
%ruby_use_gem_dependency rubocop-rake >= 0.6.0,rubocop-rake < 1
Requires:      gem(android_key_attestation) >= 0.3.0 gem(android_key_attestation) < 0.4
Requires:      gem(awrence) >= 1.1 gem(awrence) < 2
Requires:      gem(bindata) >= 2.4 gem(bindata) < 3
Requires:      gem(cbor) >= 0.5.9 gem(cbor) < 0.6
Requires:      gem(cose) >= 1.1 gem(cose) < 2
Requires:      gem(openssl) >= 2.2 gem(openssl) < 4
Requires:      gem(safety_net_attestation) >= 0.4.0 gem(safety_net_attestation) < 0.5
Requires:      gem(tpm-key_attestation) >= 0.10.0 gem(tpm-key_attestation) < 0.11
Provides:      gem(webauthn) = 2.5.1.1

%ruby_use_gem_version webauthn:2.5.1.1

%description
WebAuthn ruby server library - Make your application a W3C Web Authentication
conformant Relying Party and allow your users to authenticate with U2F and FIDO2
authenticators.

Takes care of the server-side operations needed to register or authenticate a
user credential, including the necessary cryptographic checks.


%package       -n gem-webauthn-doc
Version:       2.5.1.1
Release:       alt1
Summary:       WebAuthn ruby server library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета webauthn
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(webauthn) = 2.5.1.1

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
Version:       2.5.1.1
Release:       alt1
Summary:       WebAuthn ruby server library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета webauthn
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(webauthn) = 2.5.1.1
Requires:      gem(bundler) >= 1.17 gem(bundler) < 3
Requires:      gem(byebug) >= 11.0 gem(byebug) < 12
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.8 gem(rspec) < 4
Requires:      gem(rubocop) >= 1.9.1 gem(rubocop) < 2
Requires:      gem(rubocop-rake) >= 0.5.1 gem(rubocop-rake) < 1
Requires:      gem(rubocop-rspec) >= 2.2.0 gem(rubocop-rspec) < 3

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
* Fri Jul 01 2022 Pavel Skrylev <majioa@altlinux.org> 2.5.1.1-alt1
- ^ 2.5.1 -> 2.5.1[1]

* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 2.5.1-alt1
- ^ 2.4.0 -> 2.5.1

* Fri Jul 17 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- + packaged gem with usage Ruby Policy 2.0
