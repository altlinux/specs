# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname safety_net_attestation

Name:          gem-safety-net-attestation
Version:       0.4.0.1
Release:       alt0.1
Summary:       Ruby gem to verify Android SafetyNet attestation statements
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bdewater/safety_net_attestation
Vcs:           https://github.com/bdewater/safety_net_attestation.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rspec) >= 3.8
BuildRequires: gem(rubocop) >= 0.75.0
BuildRequires: gem(jwt) >= 2.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(jwt) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_alias_names safety_net_attestation,safety-net-attestation
%ruby_ignore_names rails
Requires:      gem(jwt) >= 2.0
Conflicts:     gem(jwt) >= 3
Provides:      gem(safety_net_attestation) = 0.4.0.1

%ruby_use_gem_version safety_net_attestation:0.4.0.1

%description
A Ruby gem to verify SafetyNet attestation statements from Google Play Services
on your server.

This gem verifies that the statement:

* has a valid signature that is trusted using certificates from
https://pki.goog/
* has the correct nonce
* has been generated recently (default allowed leeway from current time is 60
seconds)
* has a signing certificate with the correct subject

With a valid statement your application can then inspect the information
contained about the device integrity, calling app, and if applicable any
integrity errors and potential solutions (see usage).


%package       -n gem-safety-net-attestation-doc
Version:       0.4.0.1
Release:       alt0.1
Summary:       Ruby gem to verify Android SafetyNet attestation statements documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета safety_net_attestation
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(safety_net_attestation) = 0.4.0.1

%description   -n gem-safety-net-attestation-doc
Ruby gem to verify Android SafetyNet attestation statements documentation
files.

A Ruby gem to verify SafetyNet attestation statements from Google Play Services
on your server.

This gem verifies that the statement:

* has a valid signature that is trusted using certificates from
https://pki.goog/
* has the correct nonce
* has been generated recently (default allowed leeway from current time is 60
seconds)
* has a signing certificate with the correct subject

With a valid statement your application can then inspect the information
contained about the device integrity, calling app, and if applicable any
integrity errors and potential solutions (see usage).

%description   -n gem-safety-net-attestation-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета safety_net_attestation.


%package       -n gem-safety-net-attestation-devel
Version:       0.4.0.1
Release:       alt0.1
Summary:       Ruby gem to verify Android SafetyNet attestation statements development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета safety_net_attestation
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(safety_net_attestation) = 0.4.0.1
Requires:      gem(bundler) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rspec) >= 3.8
Requires:      gem(rubocop) >= 0.75.0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2

%description   -n gem-safety-net-attestation-devel
Ruby gem to verify Android SafetyNet attestation statements development
package.

A Ruby gem to verify SafetyNet attestation statements from Google Play Services
on your server.

This gem verifies that the statement:

* has a valid signature that is trusted using certificates from
https://pki.goog/
* has the correct nonce
* has been generated recently (default allowed leeway from current time is 60
seconds)
* has a signing certificate with the correct subject

With a valid statement your application can then inspect the information
contained about the device integrity, calling app, and if applicable any
integrity errors and potential solutions (see usage).

%description   -n gem-safety-net-attestation-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета safety_net_attestation.


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

%files         -n gem-safety-net-attestation-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-safety-net-attestation-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 0.4.0.1-alt0.1
- ^ 0.4.0 -> 0.4.0[1]

* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt0.1
- + packaged gem with usage Ruby Policy 2.0
