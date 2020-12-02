# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname android-key-attestation
%define        gemname android_key_attestation

Name:          gem-%pkgname
Version:       0.3.0
Release:       alt1
Summary:       Ruby gem to verify Android key attestation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bdewater/android_key_attestation
Vcs:           https://github.com/bdewater/android_key_attestation.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
A Ruby gem to verify Android Key attestation statements on your server. Key
attestation allows you to verify that the cryptographic keys you use in apps
are stored the a hardware keystore of an Android device.


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
* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with usage Ruby Policy 2.0
