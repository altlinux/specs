%define gemname charlock_holmes

Name: gem-charlock-holmes
Version: 0.7.9
Release: alt1
Summary: Character encoding detection, brought to you by ICU
License: MIT
Group: Development/Ruby
Url: https://github.com/brianmario/charlock_holmes
Vcs: https://github.com/brianmario/charlock_holmes.git

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ruby

BuildRequires: gcc-c++ libicu-devel zlib-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

Provides: gem(charlock_holmes) = 0.7.9

%description
charlock_holmes provides binary and text detection as well as text transcoding
using libicu

%package devel
Summary: Headers for gem-charlock-holmes
Group: Development/Ruby

Requires: gem(charlock_holmes) = 0.7.9

%description devel
This package contains development files for gem-charlock-holmes.

%package doc
Summary: Docs for gem-charlock-holmes
Group: Development/Documentation

Requires: gem(charlock_holmes) = 0.7.9

%description doc
This package contains docs for gem-charlock-holmes.

%prep
%setup
%patch -p1

%build
%ruby_build

%install
%ruby_install

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files doc
%ruby_gemdocdir

%files devel
%ruby_includedir/*

%changelog
* Fri Feb 14 2025 Andrey Kovalev <ded@altlinux.org> 0.7.9-alt1
- Initial build for Sisyphus.
