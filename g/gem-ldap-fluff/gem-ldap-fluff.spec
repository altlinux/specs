%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ldap_fluff

Name:          gem-ldap-fluff
Version:       0.8.0
Release:       alt1
Summary:       LDAP querying tools for Active Directory, FreeIPA and POSIX-style
License:       GPL-2.0-only
Group:         Other
Url:           https://github.com/theforeman/ldap_fluff
Vcs:           https://github.com/theforeman/ldap_fluff.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 13.1.0
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildRequires: gem(activesupport) >= 5
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(net-ldap) >= 0.11
BuildRequires: gem(theforeman-rubocop) >= 0.0.6
BuildConflicts: gem(activesupport) >= 8
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(net-ldap) >= 1
BuildConflicts: gem(theforeman-rubocop) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency theforeman-rubocop >= 0.1.2,theforeman-rubocop < 1
%ruby_alias_names ldap_fluff,ldap-fluff
Requires:      ruby >= 2.7
Requires:      gem(activesupport) >= 5
Requires:      gem(net-ldap) >= 0.11
Conflicts:     ruby >= 4
Conflicts:     gem(activesupport) >= 8
Conflicts:     gem(net-ldap) >= 1
Provides:      gem(ldap_fluff) = 0.8.0

%description
Simple library for binding & group querying on top of various LDAP
implementations


%if_enabled    doc
%package       -n gem-ldap-fluff-doc
Version:       0.8.0
Release:       alt1
Summary:       LDAP querying tools for Active Directory, FreeIPA and POSIX-style documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ldap_fluff
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ldap_fluff) = 0.8.0

%description   -n gem-ldap-fluff-doc
LDAP querying tools for Active Directory, FreeIPA and POSIX-style documentation
files.

Simple library for binding & group querying on top of various LDAP
implementations

%description   -n gem-ldap-fluff-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ldap_fluff.
%endif


%if_enabled    devel
%package       -n gem-ldap-fluff-devel
Version:       0.8.0
Release:       alt1
Summary:       LDAP querying tools for Active Directory, FreeIPA and POSIX-style development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ldap_fluff
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ldap_fluff) = 0.8.0
Requires:      gem(minitest) >= 5.0
Requires:      gem(rake) >= 13.1.0
Requires:      gem(theforeman-rubocop) >= 0.0.6
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rake) >= 14
Conflicts:     gem(theforeman-rubocop) >= 1

%description   -n gem-ldap-fluff-devel
LDAP querying tools for Active Directory, FreeIPA and POSIX-style development
package.

Simple library for binding & group querying on top of various LDAP
implementations

%description   -n gem-ldap-fluff-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ldap_fluff.
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
%doc LICENSE README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-ldap-fluff-doc
%doc LICENSE README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ldap-fluff-devel
%doc LICENSE README.rdoc
%endif


%changelog
* Mon Dec 09 2024 Pavel Skrylev <majioa@altlinux.org> 0.8.0-alt1
- ^ 0.6.0 -> 0.8.0
- * define explicit dependencies

* Tue Oct 11 2022 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt1
- ^ 0.5.0 -> 0.6.0

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- ^ 0.4.7 -> 0.5.0

* Wed May 13 2020 Pavel Skrylev <majioa@altlinux.org> 0.4.7-alt2
- > Ruby Policy 2.0
- ! spec tags

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.7-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.7-alt1
- New version.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.7-alt1
- Initial build for Sisyphus
