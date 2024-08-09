%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ovirt-engine-sdk

Name:          gem-ovirt-engine-sdk
Version:       4.6.0
Release:       alt1
Summary:       The oVirt Ruby SDK is a Ruby gem that simplyfies access to the oVirt Engine API
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/oVirt/ovirt-engine-sdk-ruby
Vcs:           https://github.com/ovirt/ovirt-engine-sdk-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: xmllint
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel
%if_enabled check
BuildRequires: gem(rake) >= 12.3
BuildRequires: gem(rake-compiler) >= 1.0
BuildRequires: gem(rspec) >= 3.7
BuildRequires: gem(rubocop) >= 0.79.0
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(json) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(json) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Requires:      gem(json) >= 1
Conflicts:     gem(json) >= 3
Obsoletes:     ruby-ovirt-engine-sdk < %EVR
Provides:      ruby-ovirt-engine-sdk = %EVR
Provides:      gem(ovirt-engine-sdk) = 4.6.0


%description
This project contains the Ruby SDK for the oVirt Engine API.

Note that most of the code of this SDK is automatically generated. If you just
installed the gem then you will have everything already, but if you downloaded
the source then you will need to generate it, follow the instructions in the
README.adoc file of the parent directory.

This is a mirror from gerrit.ovirt.org http://www.ovirt.org, for issues use
http://bugzilla.redhat.com


%if_enabled    doc
%package       -n gem-ovirt-engine-sdk-doc
Version:       4.6.0
Release:       alt1
Summary:       The oVirt Ruby SDK is a Ruby gem that simplyfies access to the oVirt Engine API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ovirt-engine-sdk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ovirt-engine-sdk) = 4.6.0

%description   -n gem-ovirt-engine-sdk-doc
The oVirt Ruby SDK is a Ruby gem that simplyfies access to the oVirt Engine API
documentation files.

This project contains the Ruby SDK for the oVirt Engine API.

Note that most of the code of this SDK is automatically generated. If you just
installed the gem then you will have everything already, but if you downloaded
the source then you will need to generate it, follow the instructions in the
README.adoc file of the parent directory.

This is a mirror from gerrit.ovirt.org http://www.ovirt.org, for issues use
http://bugzilla.redhat.com

%description   -n gem-ovirt-engine-sdk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ovirt-engine-sdk.
%endif


%if_enabled    devel
%package       -n gem-ovirt-engine-sdk-devel
Version:       4.6.0
Release:       alt1
Summary:       The oVirt Ruby SDK is a Ruby gem that simplyfies access to the oVirt Engine API development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ovirt-engine-sdk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ovirt-engine-sdk) = 4.6.0
Requires:      gem(rake) >= 12.3
Requires:      gem(rake-compiler) >= 1.0
Requires:      gem(rspec) >= 3.7
Requires:      gem(rubocop) >= 0.79.0
Requires:      gem(yard) >= 0.9
Requires:      xmllint
Requires:      libcurl-devel
Requires:      libxml2-devel
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2

%description   -n gem-ovirt-engine-sdk-devel
The oVirt Ruby SDK is a Ruby gem that simplyfies access to the oVirt Engine API
development package.

This project contains the Ruby SDK for the oVirt Engine API.

Note that most of the code of this SDK is automatically generated. If you just
installed the gem then you will have everything already, but if you downloaded
the source then you will need to generate it, follow the instructions in the
README.adoc file of the parent directory.

This is a mirror from gerrit.ovirt.org http://www.ovirt.org, for issues use
http://bugzilla.redhat.com

%description   -n gem-ovirt-engine-sdk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ovirt-engine-sdk.
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
%doc README.adoc
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-ovirt-engine-sdk-doc
%doc README.adoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ovirt-engine-sdk-devel
%doc README.adoc
%ruby_includedir/*
%endif


%changelog
* Fri Jul 26 2024 Pavel Skrylev <majioa@altlinux.org> 4.6.0-alt1
- ^ 4.4.1 -> 4.6.0

* Thu Jun 24 2021 Pavel Skrylev <majioa@altlinux.org> 4.4.1-alt1
- ^ 4.3.0 -> 4.4.1

* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 4.3.0-alt2
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 4.3.0-alt1
- > Ruby Policy 2.0
- ^ 4.2.5 -> 4.3.0

* Mon Oct 08 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.5-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.4-alt1.2
- Rebuild with new Ruby autorequirements.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.4-alt1.1
- Rebuild for aarch64.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.4-alt1
- Initial build for Sisyphus
