%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname bcrypt

Name:          gem-bcrypt
Version:       3.1.20
Release:       alt1
Summary:       bcrypt-ruby is a Ruby binding for the OpenBSD bcrypt() password hashing algorithm, allowing you to easily store a secure hash of your users' passwords
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/codahale/bcrypt-ruby
Vcs:           https://github.com/codahale/bcrypt-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake-compiler) >= 1.1.2
BuildRequires: gem(rspec) >= 3
BuildConflicts: gem(rake-compiler) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Obsoletes:     ruby-bcrypt < %EVR
Provides:      ruby-bcrypt = %EVR
Provides:      gem(bcrypt) = 3.1.20


%description
bcrypt() is a sophisticated and secure hash algorithm designed by The OpenBSD
project for hashing passwords. The bcrypt Ruby gem provides a simple wrapper for
safely handling passwords.


%if_enabled    doc
%package       -n gem-bcrypt-doc
Version:       3.1.20
Release:       alt1
Summary:       bcrypt-ruby is a Ruby binding for the OpenBSD bcrypt() password hashing algorithm, allowing you to easily store a secure hash of your users' passwords documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bcrypt
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bcrypt) = 3.1.20

%description   -n gem-bcrypt-doc
bcrypt-ruby is a Ruby binding for the OpenBSD bcrypt() password hashing
algorithm, allowing you to easily store a secure hash of your users' passwords
documentation files.

bcrypt() is a sophisticated and secure hash algorithm designed by The OpenBSD
project for hashing passwords. The bcrypt Ruby gem provides a simple wrapper for
safely handling passwords.

%description   -n gem-bcrypt-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bcrypt.
%endif


%if_enabled    devel
%package       -n gem-bcrypt-devel
Version:       3.1.20
Release:       alt1
Summary:       bcrypt-ruby is a Ruby binding for the OpenBSD bcrypt() password hashing algorithm, allowing you to easily store a secure hash of your users' passwords development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bcrypt
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bcrypt) = 3.1.20
Requires:      gem(rake-compiler) >= 1.1.2
Requires:      gem(rspec) >= 3
Conflicts:     gem(rake-compiler) >= 2

%description   -n gem-bcrypt-devel
bcrypt-ruby is a Ruby binding for the OpenBSD bcrypt() password hashing
algorithm, allowing you to easily store a secure hash of your users' passwords
development package.

bcrypt() is a sophisticated and secure hash algorithm designed by The OpenBSD
project for hashing passwords. The bcrypt Ruby gem provides a simple wrapper for
safely handling passwords.

%description   -n gem-bcrypt-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bcrypt.
%endif


%prep
%setup
%autopatch

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
%files         -n gem-bcrypt-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-bcrypt-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Tue Jul 23 2024 Pavel Skrylev <majioa@altlinux.org> 3.1.20-alt1
- ^ 3.1.17 -> 3.1.20

* Wed Mar 16 2022 Pavel Skrylev <majioa@altlinux.org> 3.1.17-alt1
- ^ 3.1.13 -> 3.1.17

* Tue Apr 07 2020 Pavel Skrylev <majioa@altlinux.org> 3.1.13-alt1.3
- ! spec obsoletes/provides pair

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 3.1.13-alt1.2
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.13-alt1.1
- fixed (!) spec according to changelog rules

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.13-alt1
- fixed (!) spec
- updated (^) 3.1.12 -> 3.1.13

* Thu Apr 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.1.12-alt2
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.12-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.12-alt1
- Initial build for Sisyphus
