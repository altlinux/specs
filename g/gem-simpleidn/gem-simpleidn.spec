%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname simpleidn

Name:          gem-simpleidn
Version:       0.2.3
Release:       alt1
Summary:       Punycode ACE to unicode UTF-8 (and vice-versa) string conversion
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mmriis/simpleidn
Vcs:           https://github.com/mmriis/simpleidn.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(codecov) >= 0
BuildRequires: gem(rake) >= 13.0.3
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(simplecov) >= 0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Requires:      ruby >= 2.2
Provides:      gem(simpleidn) = 0.2.3

%description
This gem allows easy conversion from punycode ACE strings to unicode UTF-8
strings and vice-versa.


%if_enabled    doc
%package       -n gem-simpleidn-doc
Version:       0.2.3
Release:       alt1
Summary:       Punycode ACE to unicode UTF-8 (and vice-versa) string conversion documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета simpleidn
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(simpleidn) = 0.2.3

%description   -n gem-simpleidn-doc
Punycode ACE to unicode UTF-8 (and vice-versa) string conversion documentation
files.

This gem allows easy conversion from punycode ACE strings to unicode UTF-8
strings and vice-versa.

%description   -n gem-simpleidn-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета simpleidn.
%endif


%if_enabled    devel
%package       -n gem-simpleidn-devel
Version:       0.2.3
Release:       alt1
Summary:       Punycode ACE to unicode UTF-8 (and vice-versa) string conversion development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета simpleidn
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(simpleidn) = 0.2.3
Requires:      gem(codecov) >= 0
Requires:      gem(rake) >= 13.0.3
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(simplecov) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-simpleidn-devel
Punycode ACE to unicode UTF-8 (and vice-versa) string conversion development
package.

This gem allows easy conversion from punycode ACE strings to unicode UTF-8
strings and vice-versa.

%description   -n gem-simpleidn-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета simpleidn.
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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-simpleidn-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-simpleidn-devel
%doc README.rdoc
%endif


%changelog
* Fri Aug 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.2.3-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
