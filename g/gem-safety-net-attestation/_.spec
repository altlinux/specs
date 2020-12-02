# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname safety-net-attestation
%define        gemname safety_net_attestation

Name:          gem-%pkgname
Version:       0.4.0
Release:       alt1
Summary:       Ruby gem to verify Android SafetyNet attestation statements
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bdewater/safety_net_attestation
Vcs:           https://github.com/bdewater/safety_net_attestation.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
A Ruby gem to verify SafetyNet attestation statements from Google Play Services
on your server.

This gem verifies that the statement:

* has a valid signature that is trusted using certificates from https://pki.goog/
* has the correct nonce
* has been generated recently (default allowed leeway from current time is 60
  seconds)
* has a signing certificate with the correct subject

With a valid statement your application can then inspect the information
contained about the device integrity, calling app, and if applicable any
integrity errors and potential solutions (see usage).


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
* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- + packaged gem with usage Ruby Policy 2.0
