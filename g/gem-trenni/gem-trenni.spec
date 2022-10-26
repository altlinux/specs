%define        gemname trenni

Name:          gem-trenni
Version:       3.13.1
Release:       alt1
Summary:       A fast native templating system that compiles directly to Ruby code
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/trenni
Vcs:           https://github.com/ioquatix/trenni.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
%if_with check
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(bake-bundler) >= 0
BuildRequires: gem(bake-modernize) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 3.4 gem(rspec) < 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rake-compiler) >= 0
Provides:      gem(trenni) = 3.13.1


%description
Trenni is a templating system built loosely on top of XHTML markup. It uses
efficient native parsers where possible and compiles templates into efficient
Ruby. It also includes a markup builder to assist with the generation of
pleasantly formatted markup which is compatible with the included parsers.


%package       -n gem-trenni-doc
Version:       3.13.1
Release:       alt1
Summary:       A fast native templating system that compiles directly to Ruby code documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета trenni
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(trenni) = 3.13.1

%description   -n gem-trenni-doc
A fast native templating system that compiles directly to Ruby code
documentation files.

Trenni is a templating system built loosely on top of XHTML markup. It uses
efficient native parsers where possible and compiles templates into efficient
Ruby. It also includes a markup builder to assist with the generation of
pleasantly formatted markup which is compatible with the included parsers.

%description   -n gem-trenni-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета trenni.


%package       -n gem-trenni-devel
Version:       3.13.1
Release:       alt1
Summary:       A fast native templating system that compiles directly to Ruby code development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета trenni
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(trenni) = 3.13.1
Requires:      gem(bake-bundler) >= 0
Requires:      gem(bake-modernize) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(rspec) >= 3.4 gem(rspec) < 4

%description   -n gem-trenni-devel
A fast native templating system that compiles directly to Ruby code development
package.

Trenni is a templating system built loosely on top of XHTML markup. It uses
efficient native parsers where possible and compiles templates into efficient
Ruby. It also includes a markup builder to assist with the generation of
pleasantly formatted markup which is compatible with the included parsers.

%description   -n gem-trenni-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета trenni.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-trenni-doc
%ruby_gemdocdir

%files         -n gem-trenni-devel
%ruby_includedir/*


%changelog
* Mon Oct 17 2022 Pavel Skrylev <majioa@altlinux.org> 3.13.1-alt1
- + packaged gem with Ruby Policy 2.0
