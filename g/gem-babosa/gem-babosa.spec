%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname babosa

Name:          gem-babosa
Version:       2.1.0
Release:       alt1
Summary:       A library for creating slugs
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/norman/babosa
Vcs:           https://github.com/norman/babosa.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.7.0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(standard) >= 1.1.7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.6.0
Provides:      gem(babosa) = 2.1.0

%description
A library for creating slugs. Babosa an extraction and improvement of the string
code from FriendlyId, intended to help developers create similar libraries or
plugins.


%if_enabled    doc
%package       -n gem-babosa-doc
Version:       2.1.0
Release:       alt1
Summary:       A library for creating slugs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета babosa
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(babosa) = 2.1.0

%description   -n gem-babosa-doc
A library for creating slugs documentation files.

A library for creating slugs. Babosa an extraction and improvement of the string
code from FriendlyId, intended to help developers create similar libraries or
plugins.

%description   -n gem-babosa-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета babosa.
%endif


%if_enabled    devel
%package       -n gem-babosa-devel
Version:       2.1.0
Release:       alt1
Summary:       A library for creating slugs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета babosa
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(babosa) = 2.1.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.7.0
Requires:      gem(simplecov) >= 0
Requires:      gem(standard) >= 1.1.7

%description   -n gem-babosa-devel
A library for creating slugs development package.

A library for creating slugs. Babosa an extraction and improvement of the string
code from FriendlyId, intended to help developers create similar libraries or
plugins.

%description   -n gem-babosa-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета babosa.
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
%doc Changelog.md MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-babosa-doc
%doc Changelog.md MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-babosa-devel
%doc Changelog.md MIT-LICENSE README.md
%endif


%changelog
* Tue Sep 22 2026 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
