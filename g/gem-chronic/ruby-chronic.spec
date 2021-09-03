%define        gemname chronic

Name:          gem-chronic
Version:       0.10.2.1
Release:       alt0.1
Summary:       Chronic is a pure Ruby natural language date parser
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mojombo/chronic
Vcs:           https://github.com/mojombo/chronic.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(numerizer) >= 0.2 gem(numerizer) < 1
BuildRequires: gem(rake) >= 10 gem(rake) < 14
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(activesupport) >= 4 gem(activesupport) < 7

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency activesupport >= 6.1.3.2,activesupport < 7
%ruby_use_gem_version chronic:0.10.2.1
Requires:      gem(numerizer) >= 0.2 gem(numerizer) < 1
Obsoletes:     ruby-chronic < %EVR
Provides:      ruby-chronic = %EVR
Provides:      gem(chronic) = 0.10.2.1


%description
Chronic is a natural language date/time parser written in pure Ruby. See below
for the wide variety of formats Chronic will parse.


%package       -n gem-chronic-doc
Version:       0.10.2.1
Release:       alt0.1
Summary:       Chronic is a pure Ruby natural language date parser documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chronic
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chronic) = 0.10.2.1

%description   -n gem-chronic-doc
Chronic is a pure Ruby natural language date parser documentation
files.

Chronic is a natural language date/time parser written in pure Ruby. See below
for the wide variety of formats Chronic will parse.

%description   -n gem-chronic-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chronic.


%package       -n gem-chronic-devel
Version:       0.10.2.1
Release:       alt0.1
Summary:       Chronic is a pure Ruby natural language date parser development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chronic
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chronic) = 0.10.2.1
Requires:      gem(rake) >= 10 gem(rake) < 14
Requires:      gem(simplecov) >= 0
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(activesupport) >= 4 gem(activesupport) < 7

%description   -n gem-chronic-devel
Chronic is a pure Ruby natural language date parser development
package.

Chronic is a natural language date/time parser written in pure Ruby. See below
for the wide variety of formats Chronic will parse.

%description   -n gem-chronic-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chronic.


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

%files         -n gem-chronic-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-chronic-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.10.2.1-alt0.1
- ^ 0.10.2 -> 0.10.2[.1]

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.10.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Apr 24 2017 Andrey Cherepanov <cas@altlinux.org> 0.10.2-alt1
- Initial build in Sisyphus
