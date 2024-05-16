%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname adal

Name:          gem-adal
Version:       1.0.0
Release:       alt1
Summary:       ADAL for Ruby
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/AzureAD/azure-activedirectory-library-for-ruby
Vcs:           https://github.com/azuread/azure-activedirectory-library-for-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 10.4
BuildRequires: gem(rspec) >= 3.3
BuildRequires: gem(rubocop) >= 0.32
BuildRequires: gem(simplecov) >= 0.10
BuildRequires: gem(sinatra) >= 1.4
BuildRequires: gem(webmock) >= 1.21
BuildRequires: gem(jwt) >= 1.5
BuildRequires: gem(nokogiri) >= 1.6
BuildRequires: gem(uri_template) >= 0.7
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(sinatra) >= 5
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(jwt) >= 3
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(uri_template) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency jwt >= 2.2.1,jwt < 3
%ruby_use_gem_dependency sinatra >= 4.0.0,sinatra < 5
Requires:      gem(jwt) >= 1.5
Requires:      gem(nokogiri) >= 1.6
Requires:      gem(uri_template) >= 0.7
Conflicts:     gem(jwt) >= 3
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(uri_template) >= 1
Provides:      gem(adal) = 1.0.0


%description
Windows Azure Active Directory authentication client library


%if_enabled    doc
%package       -n gem-adal-doc
Version:       1.0.0
Release:       alt1
Summary:       ADAL for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета adal
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(adal) = 1.0.0

%description   -n gem-adal-doc
ADAL for Ruby documentation files.

Windows Azure Active Directory authentication client library

%description   -n gem-adal-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета adal.
%endif


%if_enabled    devel
%package       -n gem-adal-devel
Version:       1.0.0
Release:       alt1
Summary:       ADAL for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета adal
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(adal) = 1.0.0
Requires:      gem(rake) >= 10.4
Requires:      gem(rspec) >= 3.3
Requires:      gem(rubocop) >= 0.32
Requires:      gem(simplecov) >= 0.10
Requires:      gem(sinatra) >= 1.4
Requires:      gem(webmock) >= 1.21
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(sinatra) >= 5
Conflicts:     gem(webmock) >= 4

%description   -n gem-adal-devel
ADAL for Ruby development package.

Windows Azure Active Directory authentication client library

%description   -n gem-adal-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета adal.
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
%files         -n gem-adal-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-adal-devel
%doc README.md
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
