# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname safety_net_attestation

Name:          gem-safety-net-attestation
Version:       0.5.0
Release:       alt1
Summary:       Ruby gem to verify Android SafetyNet attestation statements
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bdewater/safety_net_attestation
Vcs:           https://github.com/bdewater/safety_net_attestation.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(irb) >= 0
BuildRequires: gem(jwt) >= 2.0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rspec) >= 3.8
BuildConflicts: gem(jwt) >= 4.0
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names safety_net_attestation,safety-net-attestation
Requires:      ruby >= 2.3
Requires:      gem(jwt) >= 2.0
Conflicts:     gem(jwt) >= 4.0
Provides:      gem(safety_net_attestation) = 0.5.0

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


%if_enabled    doc
%package       -n gem-safety-net-attestation-doc
Version:       0.5.0
Release:       alt1
Summary:       Ruby gem to verify Android SafetyNet attestation statements documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета safety_net_attestation
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(safety_net_attestation) = 0.5.0

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
%endif


%if_enabled    devel
%package       -n gem-safety-net-attestation-devel
Version:       0.5.0
Release:       alt1
Summary:       Ruby gem to verify Android SafetyNet attestation statements development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета safety_net_attestation
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(safety_net_attestation) = 0.5.0
Requires:      gem(appraisal) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(irb) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rspec) >= 3.8
Conflicts:     gem(rspec) >= 4

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
%doc CHANGELOG.md CODE_OF_CONDUCT.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-safety-net-attestation-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-safety-net-attestation-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md README.md
%endif


%changelog
* Sun Mar 29 2026 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- ^ 0.4.0[1] -> 0.5.0
- * define explicit dependencies

* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 0.4.0.1-alt0.1
- ^ 0.4.0 -> 0.4.0[1]

* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- + packaged gem with usage Ruby Policy 2.0
