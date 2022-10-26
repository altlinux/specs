%define        gemname ldap_fluff

Name:          gem-ldap-fluff
Version:       0.6.0
Release:       alt1
Summary:       An LDAP gem for querying LDAP in various styles: Active Directory, FreeIPA & POSIX
License:       GPLv2
Group:         Development/Ruby
Url:           https://github.com/theforeman/ldap_fluff
Vcs:           https://github.com/theforeman/ldap_fluff.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(theforeman-rubocop) >= 0.0.6 gem(theforeman-rubocop) < 0.1
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(net-ldap) >= 0.11
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names ldap_fluff,ldap-fluff
Requires:      gem(activesupport) >= 0
Requires:      gem(net-ldap) >= 0.11
Obsoletes:     ruby-ldap-fluff < %EVR
Provides:      ruby-ldap-fluff = %EVR
Provides:      gem(ldap_fluff) = 0.6.0


%description
Provides multiple implementations of LDAP queries for various backends. Supports
Active Directory, FreeIPA and posix-style LDAP.


%package       -n gem-ldap-fluff-doc
Version:       0.6.0
Release:       alt1
Summary:       An LDAP gem for querying LDAP in various styles: Active Directory, FreeIPA & POSIX documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ldap_fluff
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ldap_fluff) = 0.6.0

%description   -n gem-ldap-fluff-doc
An LDAP gem for querying LDAP in various styles: Active Directory, FreeIPA &
POSIX documentation files.

Provides multiple implementations of LDAP queries for various backends. Supports
Active Directory, FreeIPA and posix-style LDAP.

%description   -n gem-ldap-fluff-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ldap_fluff.


%package       -n gem-ldap-fluff-devel
Version:       0.6.0
Release:       alt1
Summary:       An LDAP gem for querying LDAP in various styles: Active Directory, FreeIPA & POSIX development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ldap_fluff
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ldap_fluff) = 0.6.0
Requires:      gem(minitest) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(theforeman-rubocop) >= 0.0.6 gem(theforeman-rubocop) < 0.1

%description   -n gem-ldap-fluff-devel
An LDAP gem for querying LDAP in various styles: Active Directory, FreeIPA &
POSIX development package.

Provides multiple implementations of LDAP queries for various backends. Supports
Active Directory, FreeIPA and posix-style LDAP.

%description   -n gem-ldap-fluff-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ldap_fluff.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-ldap-fluff-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-ldap-fluff-devel
%doc README.rdoc


%changelog
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
