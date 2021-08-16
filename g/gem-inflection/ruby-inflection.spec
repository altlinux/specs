%define        gemname inflection

Name:          gem-inflection
Version:       1.0.0
Release:       alt2
Summary:       Provides english inflection
License:       MIT or Ruby
Group:         Development/Ruby
Url:           https://github.com/reactormonk/extlib/tree/inflection
Vcs:           https://github.com/reactormonk/extlib.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-inflection < %EVR
Provides:      ruby-inflection = %EVR
Provides:      gem(inflection) = 1.0.0


%description
Support library for inflections.


%package       -n gem-inflection-doc
Version:       1.0.0
Release:       alt2
Summary:       Provides english inflection documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета inflection
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(inflection) = 1.0.0

%description   -n gem-inflection-doc
Provides english inflection documentation files.

Support library for inflections.

%description   -n gem-inflection-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета inflection.


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

%files         -n gem-inflection-doc
%doc README.rdoc
%ruby_gemdocdir


%changelog
* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt2
- ! spec

* Thu Aug 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build in Sisyphus
