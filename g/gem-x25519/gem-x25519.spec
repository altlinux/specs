%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname x25519

Name:          gem-x25519
Version:       1.0.10
Release:       alt3
Summary:       Public key cryptography library providing the X25519 Elliptic Curve Diffie-Hellman function
License:       BSD-3-Clause
Group:         Development/Ruby
Url:           https://cr.yp.to/ecdh.html
Vcs:           https://github.com/rubycrypto/x25519.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         fix-arches.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2.1
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 1.0
BuildRequires: gem(rspec) >= 3.10
BuildRequires: gem(rubocop) >= 1.15.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Provides:      gem(x25519) = 1.0.10


%description
An efficient public key cryptography library for Ruby providing key
exchange/agreement via the X25519 (a.k.a. Curve25519) Elliptic Curve
Diffie-Hellman function as described in RFC 7748.


%if_enabled    doc
%package       -n gem-x25519-doc
Version:       1.0.10
Release:       alt1
Summary:       Public key cryptography library providing the X25519 Elliptic Curve Diffie-Hellman function documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета x25519
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(x25519) = 1.0.10

%description   -n gem-x25519-doc
Public key cryptography library providing the X25519 Elliptic Curve
Diffie-Hellman function documentation files.

An efficient public key cryptography library for Ruby providing key
exchange/agreement via the X25519 (a.k.a. Curve25519) Elliptic Curve
Diffie-Hellman function as described in RFC 7748.

%description   -n gem-x25519-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета x25519.
%endif


%if_enabled    devel
%package       -n gem-x25519-devel
Version:       1.0.10
Release:       alt1
Summary:       Public key cryptography library providing the X25519 Elliptic Curve Diffie-Hellman function development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета x25519
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(x25519) = 1.0.10
Requires:      gem(bundler) >= 2.1
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 1.0
Requires:      gem(rspec) >= 3.10
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2

%description   -n gem-x25519-devel
Public key cryptography library providing the X25519 Elliptic Curve
Diffie-Hellman function development package.

An efficient public key cryptography library for Ruby providing key
exchange/agreement via the X25519 (a.k.a. Curve25519) Elliptic Curve
Diffie-Hellman function as described in RFC 7748.

%description   -n gem-x25519-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета x25519.
%endif


%prep
%setup
%autopatch -p1

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
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-x25519-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-x25519-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Sat May 18 2024 Michael Shigorin <mike@altlinux.org> 1.0.10-alt3
- NMU: fixed FTBFS on e2k too

* Mon Apr 29 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.0.10-alt2
- NMU: fixed FTBFS on LoongArch (and possibly riscv64)

* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.10-alt1
- + packaged gem with Ruby Policy 2.0
