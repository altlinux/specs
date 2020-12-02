# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname tpm-key-attestation
%define        gemname tpm-key_attestation

Name:          gem-%pkgname
Version:       0.10.0
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

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.

TPM Key Attestation utitlies


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
* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt1
- + packaged gem with usage Ruby Policy 2.0
