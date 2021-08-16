%define        gemname uber

Name:          gem-uber
Version:       0.1.0
Release:       alt2
Summary:       Gem-authoring extensions for classes and modules
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/apotonick/uber
Vcs:           https://github.com/apotonick/uber.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(minitest) >= 0 gem(minitest) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-uber < %EVR
Provides:      ruby-uber = %EVR
Provides:      gem(uber) = 0.1.0


%description
Gem-authoring tools like class method inheritance in modules, dynamic options
and more.


%package       -n gem-uber-doc
Version:       0.1.0
Release:       alt2
Summary:       Gem-authoring extensions for classes and modules documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета uber
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(uber) = 0.1.0

%description   -n gem-uber-doc
Gem-authoring extensions for classes and modules documentation files.

Gem-authoring tools like class method inheritance in modules, dynamic options
and more.

%description   -n gem-uber-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета uber.


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

%files         -n gem-uber-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt2
- > Ruby Policy 2.0
- ! spec

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Sun May 27 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
