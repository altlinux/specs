%define        gemname facets

Name:          gem-facets
Version:       3.1.0
Release:       alt1.1
Summary:       The orginal well curated collection of extension methods for Ruby
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           http://rubyworks.github.com/facets
Vcs:           https://github.com/rubyworks/facets.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(lemon) >= 0
BuildRequires: gem(qed) >= 0
# BuildRequires: gem(rubytest-cli) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0
# BuildRequires: gem(guard) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names cgi-exception
Provides:      gem(facets) = 3.1.0


%description
Facets is the premier collection of extension methods for the Ruby programming
language. Facets extensions are unique by virtue of thier atomicity. They are
stored in individual files allowing for highly granular control of requirements.
In addition, Facets includes a few additional classes and mixins suitable to
wide variety of applications.


%package       -n gem-facets-doc
Version:       3.1.0
Release:       alt1.1
Summary:       The orginal well curated collection of extension methods for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета facets
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(facets) = 3.1.0

%description   -n gem-facets-doc
The orginal well curated collection of extension methods for Ruby documentation
files.

Facets is the premier collection of extension methods for the Ruby programming
language. Facets extensions are unique by virtue of thier atomicity. They are
stored in individual files allowing for highly granular control of requirements.
In addition, Facets includes a few additional classes and mixins suitable to
wide variety of applications.

%description   -n gem-facets-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета facets.


%package       -n gem-facets-devel
Version:       3.1.0
Release:       alt1.1
Summary:       The orginal well curated collection of extension methods for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета facets
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(facets) = 3.1.0
Requires:      gem(lemon) >= 0
Requires:      gem(qed) >= 0
# Requires:      gem(rubytest-cli) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0
# Requires:      gem(guard) >= 0

%description   -n gem-facets-devel
The orginal well curated collection of extension methods for Ruby development
package.

Facets is the premier collection of extension methods for the Ruby programming
language. Facets extensions are unique by virtue of thier atomicity. They are
stored in individual files allowing for highly granular control of requirements.
In addition, Facets includes a few additional classes and mixins suitable to
wide variety of applications.

%description   -n gem-facets-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета facets.


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

%files         -n gem-facets-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-facets-devel
%doc README.md


%changelog
* Wed Mar 23 2022 Pavel Vasenkov <pav@altlinux.org> 3.1.0-alt1.1
- + disable provides cgi-exception

* Wed Oct 06 2021 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- + packaged gem with Ruby Policy 2.0
