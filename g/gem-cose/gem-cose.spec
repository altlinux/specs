# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname cose

Name:          gem-cose
Version:       1.3.0
Release:       alt1
Summary:       Ruby implementation of RFC 8152 CBOR Object Signing and Encryption (COSE)
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cedarcode/cose-ruby
Vcs:           https://github.com/cedarcode/cose-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(appraisal) >= 2.2.0
BuildRequires: gem(bundler) >= 1.17
BuildRequires: gem(byebug) >= 11.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.8
BuildRequires: gem(rubocop) >= 0.80.1
BuildRequires: gem(rubocop-performance) >= 1.4
BuildRequires: gem(cbor) >= 0.5.9
BuildRequires: gem(openssl-signature_algorithm) >= 1.0
BuildConflicts: gem(appraisal) >= 3
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(byebug) >= 12
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(cbor) >= 0.6
BuildConflicts: gem(openssl-signature_algorithm) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency appraisal >= 2.4.0,appraisal < 3
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(cbor) >= 0.5.9
Requires:      gem(openssl-signature_algorithm) >= 1.0
Conflicts:     gem(cbor) >= 0.6
Conflicts:     gem(openssl-signature_algorithm) >= 2
Provides:      gem(cose) = 1.3.0


%description
Ruby implementation of RFC 8152 CBOR Object Signing and Encryption (COSE).


%package       -n gem-cose-doc
Version:       1.3.0
Release:       alt1
Summary:       Ruby implementation of RFC 8152 CBOR Object Signing and Encryption (COSE) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cose
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(cose) = 1.3.0

%description   -n gem-cose-doc
Ruby implementation of RFC 8152 CBOR Object Signing and Encryption (COSE)
documentation files.

%description   -n gem-cose-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cose.


%package       -n gem-cose-devel
Version:       1.3.0
Release:       alt1
Summary:       Ruby implementation of RFC 8152 CBOR Object Signing and Encryption (COSE) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cose
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(cose) = 1.3.0
Requires:      gem(appraisal) >= 2.2.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(byebug) >= 11.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.8
Requires:      gem(rubocop) >= 0.80.1
Requires:      gem(rubocop-performance) >= 1.4
Conflicts:     gem(appraisal) >= 3
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(byebug) >= 12
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2

%description   -n gem-cose-devel
Ruby implementation of RFC 8152 CBOR Object Signing and Encryption (COSE)
development package.

%description   -n gem-cose-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cose.


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

%files         -n gem-cose-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-cose-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- ^ 1.2.0 -> 1.3.0

* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- + packaged gem with usage Ruby Policy 2.0
