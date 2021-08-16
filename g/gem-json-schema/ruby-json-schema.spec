%define        pkgname json-schema

Name:          gem-%pkgname
Version:       2.8.1
Release:       alt1
Summary:       Ruby JSON Schema Validator
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-json-schema/json-schema
Vcs:           https://github.com/ruby-json-schema/json-schema.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
This library is intended to provide Ruby with an interface for validating JSON
objects against a JSON schema conforming to JSON Schema Draft 4. Legacy support
for JSON Schema Draft 3, JSON Schema Draft 2, and JSON Schema Draft 1 is also
included.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Wed Dec 16 2020 Pavel Skrylev <majioa@altlinux.org> 2.8.1-alt1
- > Ruby Policy 2.0
- ^ 2.8.0 -> 2.8.1

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 07 2018 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- Initial build for Sisyphus
