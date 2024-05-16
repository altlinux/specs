%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname w3c_validators

Name:          gem-w3c-validators
Version:       1.3.7
Release:       alt1
Summary:       A Ruby wrapper for the World Wide Web Consortium's online validation services
License:       GPL-1 or Ruby
Group:         Development/Ruby
Url:           https://github.com/w3c-validators/w3c_validators
Vcs:           https://github.com/w3c-validators/w3c_validators.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(vcr) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(nokogiri) >= 1.6
BuildRequires: gem(json) >= 1.8
BuildRequires: gem(rexml) >= 3.2
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(rexml) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names w3c_validators,w3c-validators
Requires:      gem(nokogiri) >= 1.6
Requires:      gem(json) >= 1.8
Requires:      gem(rexml) >= 3.2
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(rexml) >= 4
Obsoletes:     ruby-w3c-validators < %EVR
Provides:      ruby-w3c-validators = %EVR
Provides:      gem(w3c_validators) = 1.3.7


%description
A Ruby wrapper for the World Wide Web Consortium's online validation services.


%if_enabled    doc
%package       -n gem-w3c-validators-doc
Version:       1.3.7
Release:       alt1
Summary:       A Ruby wrapper for the World Wide Web Consortium's online validation services documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета w3c_validators
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(w3c_validators) = 1.3.7

%description   -n gem-w3c-validators-doc
A Ruby wrapper for the World Wide Web Consortium's online validation services
documentation files.

%description   -n gem-w3c-validators-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета w3c_validators.
%endif


%if_enabled    devel
%package       -n gem-w3c-validators-devel
Version:       1.3.7
Release:       alt1
Summary:       A Ruby wrapper for the World Wide Web Consortium's online validation services development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета w3c_validators
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(w3c_validators) = 1.3.7
Requires:      gem(rake) >= 0
Requires:      gem(vcr) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(webrick) >= 0

%description   -n gem-w3c-validators-devel
A Ruby wrapper for the World Wide Web Consortium's online validation services
development package.

%description   -n gem-w3c-validators-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета w3c_validators.
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
%files         -n gem-w3c-validators-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-w3c-validators-devel
%doc README.md
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 1.3.7-alt1
- ^ 1.3.4 -> 1.3.7

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.4-alt1
- New version.

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 1.3.3-alt1
- Initial build for Sisyphus
