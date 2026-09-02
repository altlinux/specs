# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname bcrypt_pbkdf

Name:          gem-bcrypt-pbkdf
Version:       1.1.2
Release:       alt1
Summary:       Ruby gem implementing bcrypt_pbkdf
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mfazekas/bcrypt_pbkdf-ruby
Vcs:           https://github.com/net-ssh/bcrypt_pbkdf-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake libruby-devel 
%if_enabled check
BuildRequires: gem(benchmark) >= 0.4.0
BuildRequires: gem(minitest) >= 5
BuildRequires: gem(openssl) >= 3
BuildRequires: gem(rake-compiler) >= 1.1.2
BuildRequires: gem(rake-compiler-dock) >= 1.2.1
BuildRequires: gem(rdoc) >= 6
BuildConflicts: gem(openssl) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5
%ruby_use_gem_dependency rdoc >= 6
%ruby_use_gem_dependency benchmark >= 0.4
%ruby_use_gem_dependency rake-compiler >= 1.1.2
%ruby_use_gem_dependency rake-compiler-dock >= 1.2.1
Provides:      gem(bcrypt_pbkdf) = 1.1.2

%description
bcrypt_pdkfd is a ruby gem implementing bcrypt_pdkfd from OpenBSD. This is
currently used by net-ssh to read password encrypted Ed25519 keys.


%if_enabled    doc
%package       -n gem-bcrypt-pbkdf-doc
Version:       1.1.2
Release:       alt1
Summary:       Ruby gem implementing bcrypt_pbkdf
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bcrypt_pbkdf
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem-bcrypt-pbkdf = 1.1.2-alt1

%description   -n gem-bcrypt-pbkdf-doc
Ruby gem implementing bcrypt_pbkdf documentation files.

bcrypt_pdkfd is a ruby gem implementing bcrypt_pdkfd from OpenBSD. This is
currently used by net-ssh to read password encrypted Ed25519 keys.

%description   -n gem-bcrypt-pbkdf-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bcrypt_pbkdf. %endif
%endif


%if_enabled    devel
%package       -n gem-bcrypt-pbkdf-devel
Version:       1.1.2
Release:       alt1
Summary:       Ruby gem implementing bcrypt_pbkdf
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bcrypt_pbkdf
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bcrypt_pbkdf) = 1.1.2
Requires:      gem(benchmark) >= 0.4.0
Requires:      gem(minitest) >= 5
Requires:      gem(openssl) >= 3
Requires:      gem(rake-compiler) >= 1.1.2
Requires:      gem(rake-compiler-dock) >= 1.2.1
Requires:      gem(rdoc) >= 6
Conflicts:     gem(openssl) >= 4

%description   -n gem-bcrypt-pbkdf-devel
Ruby gem implementing bcrypt_pbkdf development package.

bcrypt_pdkfd is a ruby gem implementing bcrypt_pdkfd from OpenBSD. This is
currently used by net-ssh to read password encrypted Ed25519 keys.

%description   -n gem-bcrypt-pbkdf-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bcrypt_pbkdf. %endif
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
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-bcrypt-pbkdf-doc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-bcrypt-pbkdf-devel
%_includedir/*
%endif


%changelog
* Tue Sep 01 2026 Pavel Skrylev <majioa@altlinux.org> 1.1.2-alt1
- ^ 1.1.1 -> 1.1.2

* Tue Jul 23 2024 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- ^ 1.1.0 -> 1.1.1

* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1.1
- !fix spec for dependencies

* Tue Feb 09 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- ^ 1.1.0.rc1 -> 1.1.0

* Wed Jul 03 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt0.1
- ^ 1.0.1 -> 1.1.0.rc1

* Tue Mar 03 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1.2
- fixed (!) changelog and spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1.1
- fixed (!) spec according to changelog rules

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
