# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname bcrypt-pbkdf
%define        gemname bcrypt_pbkdf

Name:          gem-%pkgname
Version:       1.1.0
Release:       alt1.1
Summary:       Ruby gem implementing bcrypt_pbkdf
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mfazekas/bcrypt_pbkdf-ruby
Vcs:           https://github.com/net-ssh/bcrypt_pbkdf-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%ruby_use_gem_dependency rdoc >= 6.3.0,rdoc < 7
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
%ruby_use_gem_dependency rake-compiler-dock >= 1.1.0,rake-compiler-dock < 2
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
bcrypt_pdkfd is a ruby gem implementing bcrypt_pdkfd from OpenBSD. This is
currently used by net-ssh to read password encrypted Ed25519 keys.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       devel
Summary:       Development headers files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   devel
Development headers for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.


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
%ruby_gemextdir
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/*


%changelog
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
