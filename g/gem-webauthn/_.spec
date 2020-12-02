# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname webauthn

Name:          gem-%pkgname
Version:       2.4.0
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

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
WebAuthn ruby server library - Make your application a W3C Web Authentication
conformant Relying Party and allow your users to authenticate with U2F and
FIDO2 authenticators.

Takes care of the server-side operations needed to register or authenticate
a user credential, including the necessary cryptographic checks.


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
%ruby_build --ignore=conformance

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
* Fri Jul 17 2020 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- + packaged gem with usage Ruby Policy 2.0
