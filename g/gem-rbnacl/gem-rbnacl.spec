%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname rbnacl

Name:          gem-rbnacl
Version:       7.1.1
Release:       alt1
Summary:       Ruby binding to the Networking and Cryptography (NaCl) library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cryptosphere/rbnacl
Vcs:           https://github.com/rubycrypto/rbnacl.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 0.70.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(ffi) >= 0
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(ffi) >= 0
Obsoletes:     ruby-rbnacl < %EVR
Provides:      ruby-rbnacl = %EVR
Provides:      gem(rbnacl) = 7.1.1


%description
Ruby binding to the Networking and Cryptography (NaCl) library


%if_enabled    doc
%package       -n gem-rbnacl-doc
Version:       7.1.1
Release:       alt1
Summary:       Ruby binding to the Networking and Cryptography (NaCl) library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rbnacl
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rbnacl) = 7.1.1

%description   -n gem-rbnacl-doc
Ruby binding to the Networking and Cryptography (NaCl) library documentation
files.

%description   -n gem-rbnacl-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rbnacl.
%endif


%if_enabled    devel
%package       -n gem-rbnacl-devel
Version:       7.1.1
Release:       alt1
Summary:       Ruby binding to the Networking and Cryptography (NaCl) library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rbnacl
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rbnacl) = 7.1.1
Requires:      gem(bundler) >= 0
Requires:      gem(guard-rspec) >= 0
Requires:      gem(coveralls) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0.70.0
Requires:      gem(rake) >= 0
Conflicts:     gem(rubocop) >= 2

%description   -n gem-rbnacl-devel
Ruby binding to the Networking and Cryptography (NaCl) library development
package.

%description   -n gem-rbnacl-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rbnacl.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rbnacl-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rbnacl-devel
%doc README.md
%endif


%changelog
* Thu Mar 14 2024 Pavel Skrylev <majioa@altlinux.org> 7.1.1-alt1
- ^ 5.0.0 -> 7.1.1

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Sep 11 2017 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
