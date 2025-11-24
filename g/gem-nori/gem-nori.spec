%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname nori

Name:          gem-nori
Version:       2.7.1
Release:       alt1
Summary:       XML to Hash translator
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/savonrb/nori
Vcs:           https://github.com/savonrb/nori.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bigdecimal) >= 0
BuildRequires: gem(nokogiri) >= 1.4.0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rexml) >= 3.2
BuildRequires: gem(rspec) >= 3.10.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rexml) >= 4
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
Requires:      ruby >= 3.0
Requires:      gem(bigdecimal) >= 0
Requires:      gem(rexml) >= 3.2
Conflicts:     gem(rexml) >= 4
Provides:      gem(nori) = 2.7.1

%description
XML to Hash translator.

Really simple XML parsing ripped from Crack which ripped it from Merb. Nori was
created to bypass the stale development of Crack, improve its XML parse and fix
certain issues.


%if_enabled    doc
%package       -n gem-nori-doc
Version:       2.7.1
Release:       alt1
Summary:       XML to Hash translator documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета nori
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(nori) = 2.7.1

%description   -n gem-nori-doc
XML to Hash translator documentation files.

%description   -n gem-nori-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета nori.
%endif


%if_enabled    devel
%package       -n gem-nori-devel
Version:       2.7.1
Release:       alt1
Summary:       XML to Hash translator development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета nori
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(nori) = 2.7.1
Requires:      gem(nokogiri) >= 1.4.0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rspec) >= 3.10.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-nori-devel
XML to Hash translator development package.

%description   -n gem-nori-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета nori.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-nori-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-nori-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Sat Nov 22 2025 Pavel Skrylev <majioa@altlinux.org> 2.7.1-alt1
- ^ 2.6.0 -> 2.7.1
- * define explicit dependencies

* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 2.6.0-alt1.1
- ! spec syntax

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 2.6.0-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
